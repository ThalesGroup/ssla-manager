import logging
from typing import Any, List

import sqlalchemy as sa
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Engine, exists
from sqlalchemy.orm import declarative_base, Session

from sslamanager.exceptions import SSLAAlreadyExistsException, SSLANotFound

Base = declarative_base()

logger = logging.getLogger("uvicorn.default")


class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    metadata: dict[str, str] = Field(alias='metadata_')


class SSLATable(Base):
    # table
    __tablename__ = 'ssla'
    # columns
    service = sa.Column('service', sa.String, primary_key=True)
    # data is the ssla content data
    data = sa.Column('data', sa.LargeBinary)
    # 'metadata' is reserved by SQLAlchemy, hence the '_'
    metadata_ = sa.Column('metadata', sa.JSON)

    @staticmethod
    def init_table(engine: "Engine"):
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_ssla(ssla: bytes, service_name: str, database_engine: "Engine"):
        ssla = SSLATable(data=ssla, service=service_name)
        # before insert, verify checksums
        with Session(database_engine) as session:
            # check if already exists
            if session.query(exists().where(SSLATable.service == service_name)).scalar():
                raise SSLAAlreadyExistsException(f"SSLA already exists for service {service_name}")
            else:
                session.add(ssla)
                session.commit()

    @staticmethod
    def find_ssla(service_name: str, database_engine: "Engine") -> Any:
        with Session(database_engine) as session:
            return session.query(SSLATable).filter_by(service=service_name).first()

    @staticmethod
    def update_ssla(ssla: bytes, service_name: str, database_engine: "Engine") -> Any:
        with Session(database_engine) as session:
            sql_object = session.query(SSLATable).filter_by(service=service_name).first()
            if sql_object is None:
                raise SSLANotFound("SSLA not found and cannot be updated")
            elif sql_object.data == ssla:
                logger.info(f"SSLA unmodified for service {service_name}")
            else:
                sql_object.data = ssla
                session.commit()

    @staticmethod
    def delete_ssla(service_name: str, database_engine: "Engine"):
        with Session(database_engine) as session:
            sql_object = session.query(SSLATable).filter_by(service=service_name).first()
            session.delete(sql_object)
            session.commit()

    @staticmethod
    def get_services(database_engine: "Engine") -> List[str]:
        with Session(database_engine) as session:
            services = session.query(SSLATable.service).all()
            return [str(s[0]) for s in services]
