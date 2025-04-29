import os.path
import sqlite3
from pathlib import Path

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import declarative_base

from sslamanager.database.ssla_table import SSLATable

TEST_DATABASE = "/tmp/ssla.db"
SERVICE_NAME_1 = "myservice1"
SERVICE_NAME_2 = "myservice2"
SERVICE_NAME_3 = "myservice3"
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

Base = declarative_base()


def read_file_bytes(path: Path) -> bytes:
    with open(path, 'rb') as f:
        return f.read()


def test_ssla_table():
    db_path = os.path.abspath(TEST_DATABASE)
    if os.path.exists(db_path):
        os.remove(db_path)
    sqlite3.connect(db_path)

    # init ssla table
    db_url = f"sqlite:///{db_path}"
    engine = create_engine(db_url)
    SSLATable.init_table(engine)
    assert Path(TEST_DATABASE).exists()

    # read sslas
    ssla_test_path_1 = os.path.join(CURRENT_DIR, "../static/ssla_tls_server_valid.xml")
    ssla_data_1 = read_file_bytes(ssla_test_path_1)
    ssla_test_path_1_modified = os.path.join(CURRENT_DIR, "../static/ssla_tls_server_valid_modified.xml")
    ssla_data_1_modified = read_file_bytes(ssla_test_path_1_modified)
    ssla_test_path_2 = os.path.join(CURRENT_DIR, "../static/ssla_tls_server_valid_2.xml")
    ssla_data_2 = read_file_bytes(ssla_test_path_2)

    # insert test
    insert_test(ssla_data_1, ssla_data_2, engine)

    # # find test
    find_test(ssla_data_1, ssla_data_2, engine)

    # update ssla
    ssla_test_path_3 = os.path.join(CURRENT_DIR, "../static/ssla_tls_server_valid_3.xml")
    ssla_data_3 = read_file_bytes(ssla_test_path_3)
    update_test(ssla_data_1, ssla_data_1_modified, ssla_data_3, engine)

    # List services
    get_services_test(engine)

    # delete ssla

    delete_test(engine)


def insert_test(ssla_data_1: bytes, ssla_data_2: bytes, engine: "Engine"):
    SSLATable.insert_ssla(ssla_data_1, SERVICE_NAME_1, engine)
    SSLATable.insert_ssla(ssla_data_2, SERVICE_NAME_2, engine)
    # handle case where double insert returns an explicit error
    try:
        SSLATable.insert_ssla(ssla_data_2, SERVICE_NAME_2, engine)
    except Exception as e:
        assert e is not None


def find_test(ssla_data_1: bytes, ssla_data_2: bytes, engine: "Engine"):
    ssla_sql_handler_1 = SSLATable.find_ssla(SERVICE_NAME_1, engine)
    assert ssla_sql_handler_1 is not None
    ssla_data_1_found = ssla_sql_handler_1.data
    assert len(ssla_data_1_found) > 0
    assert ssla_data_1_found == ssla_data_1
    # SSLA 2
    ssla_sql_handler_2 = SSLATable.find_ssla(SERVICE_NAME_2, engine)
    assert ssla_sql_handler_2 is not None
    ssla_data_2_found = ssla_sql_handler_2.data
    assert len(ssla_data_2_found) > 0
    assert ssla_data_2_found == ssla_data_2
    # non existing handling
    ssla_sql_handler_none = SSLATable.find_ssla("dumb", engine)
    assert ssla_sql_handler_none is None


def update_test(ssla_data: bytes, ssla_data_updated: bytes, ssla_data_absent: bytes, engine: "Engine"):
    # update existing
    SSLATable.update_ssla(ssla_data_updated, SERVICE_NAME_1, engine)
    ssla_sql_handler_1_modified = SSLATable.find_ssla(SERVICE_NAME_1, engine)
    assert ssla_sql_handler_1_modified is not None
    ssla_data_1_modified_found = ssla_sql_handler_1_modified.data
    assert len(ssla_data_1_modified_found) > 0
    assert ssla_data_1_modified_found != ssla_data

    # update non existing
    try:
        SSLATable.update_ssla(ssla_data_absent, SERVICE_NAME_3, engine)
    except Exception as e:
        assert e is not None
        assert "not found" in str(e)


def get_services_test(engine: "Engine"):
    services = SSLATable.get_services(engine)
    assert services is not None
    assert len(services) == 2
    assert SERVICE_NAME_1 in services
    assert SERVICE_NAME_2 in services


def delete_test(engine: "Engine"):
    SSLATable.delete_ssla(SERVICE_NAME_1, engine)
    ssla_sql_handler_1 = SSLATable.find_ssla(SERVICE_NAME_1, engine)
    assert ssla_sql_handler_1 is None
