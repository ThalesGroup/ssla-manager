from pathlib import Path
from typing import List

from sqlalchemy import create_engine, Engine

from sslamanager.database.ssla_table import SSLATable
from sslamanager.exceptions import SSLANotFound
from sslamanager.parser.build import ServicePropertiesType
from sslamanager.parser.build.specs import MetricType
from sslamanager.parser.build.specs.slo import Slotype
from sslamanager.parser.ssla_parser import SSLA, SSLAParser, SLO, Metric, ServiceProperties


class SecurityPolicyManager(object):
    engine: "Engine"
    ssla_parser: SSLAParser

    def __init__(self, database_path: Path):
        db_url = f"sqlite:///{database_path}"
        self.engine = create_engine(db_url)
        SSLATable.init_table(self.engine)
        self.ssla_parser = SSLAParser()

    def create_ssla(self, ssla_content: bytes) -> "SSLA":
        # load ssla model from input
        ssla_model = self.ssla_parser.parse_from_content(ssla_content)
        service_name = ssla_model.get_first_service().service_name
        # insert in database
        SSLATable.insert_ssla(ssla_content, service_name, self.engine)
        return ssla_model

    def get_ssla_content(self, service_name: str) -> bytes:
        ssla_entry = SSLATable.find_ssla(service_name, self.engine)
        if ssla_entry is not None:
            return ssla_entry.data
        else:
            raise SSLANotFound(f"SSLA not found for service '{service_name}'")

    def get_ssla_model(self, service_name: str) -> "SSLA":
        content = self.get_ssla_content(service_name)
        return self.ssla_parser.parse_from_content(content)

    def update_ssla(self, ssla_content: bytes) -> "SSLA":
        # load ssla model from input
        ssla_model = self.ssla_parser.parse_from_content(ssla_content)
        service_name = ssla_model.get_first_service().service_name
        # insert in database
        SSLATable.update_ssla(ssla_content, service_name, self.engine)
        return ssla_model

    def delete_ssla(self, service_name: str):
        SSLATable.delete_ssla(service_name, self.engine)

    def get_services(self) -> List[str]:
        return SSLATable.get_services(self.engine)

    def get_slos(self, service_name: str) -> List["Slotype"]:
        ssla = self.get_ssla_model(service_name=service_name)
        return ssla.get_slos()

    def get_slos_jsonable(self, service_name: str) -> List["SLO"]:
        ssla = self.get_ssla_model(service_name=service_name)
        return ssla.get_slos_json()

    def get_metrics(self, service_name: str) -> List["MetricType"]:
        ssla = self.get_ssla_model(service_name=service_name)
        return ssla.get_metrics(service_name)

    def get_metric(self, service_name: str, metric_id: str) -> "MetricType":
        ssla = self.get_ssla_model(service_name=service_name)
        return ssla.get_metric(service_name, metric_id)

    def get_metrics_jsonable(self, service_name: str) -> List["Metric"]:
        ssla = self.get_ssla_model(service_name=service_name)
        return ssla.get_metrics_json(service_name)

    def get_metric_jsonable(self, service_name: str, metric_id: str) -> "Metric":
        ssla = self.get_ssla_model(service_name=service_name)
        return ssla.get_metric_json(service_name, metric_id)

    def get_service_properties(self, service_name: str) -> List["ServicePropertiesType"]:
        ssla = self.get_ssla_model(service_name=service_name)
        return ssla.get_service_properties(service_name)

    def get_service_properties_jsonable(self, service_name: str) -> List["ServiceProperties"]:
        ssla = self.get_ssla_model(service_name=service_name)
        return ssla.get_service_properties_json(service_name)
