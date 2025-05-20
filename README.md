# SSLA Manager

Python module to parse and manage Security Service Level Agreement (SSLA) files with a REST API and SQL.

## Usage

Examples :

```python
from pathlib import Path
from typing import List

from sslamanager.api import SecurityPolicyManager
from sslamanager.parser.build.specs.security_metric import MetricType
from sslamanager.parser.build.specs.slo import Slotype
from sslamanager.parser.ssla_parser import SSLA, Metric

if __name__ == "__main__":
    # init the manager with your database
    manager = SecurityPolicyManager(Path("/tmp/ssla.db"))

    # SSLA creation
    # the SSLA is uploaded to your database
    # the SSLA service is used as the id of your SSLA
    ssla_content: bytes = Path("/tmp/ssla.xml").read_bytes()
    ssla_model: SSLA = manager.create_ssla(ssla_content)
    
    # SSLA service listing
    # retrieve all the service names related to the submitted SSLA in your database
    services: List[str] = manager.get_services()
    print(services)

    # SSLA parsing model
    # manipulate the model to retrieve information
    metrics: List[MetricType] = ssla_model.get_metrics("my_ssla_service_name")
    SLOs: List[Slotype] = ssla_model.get_slos()

    # more formats useful to parse using pydantic models
    metrics_jsonable: List[Metric] = ssla_model.get_metrics_json("my_ssla_service_name")
    print(metrics_jsonable.model_dump_json())
    
    # SSLA update
    new_ssla_content: bytes = Path("/tmp/ssla_v2.xml").read_bytes()
    new_ssla_model: SSLA = manager.update_ssla(new_ssla_content)

    # SSLA retrieve content
    ssla_content = manager.get_ssla_content("my_ssla_service_name")

    # SSLA deletion in database
    manager.delete_ssla("my_ssla_service_name")
```

## Build

You need [Poetry](https://python-poetry.org/) to build this module.

First, update this module's version in `./poetry.toml`.

Then build it

```sh
./build.sh
```

## Test

**You need to build the project first to generate the class models**

```sh
# run tests
poetry run coverage run -m pytest
# get the report
poetry run coverage report
```

## Coverage

```
Name                                                              Stmts   Miss  Cover
-------------------------------------------------------------------------------------
sslamanager/__init__.py                                               0      0   100%
sslamanager/database/__init__.py                                      0      0   100%
sslamanager/database/ssla_table.py                                   53      1    98%
sslamanager/exceptions.py                                            22      0   100%
sslamanager/parser/__init__.py                                        0      0   100%
sslamanager/parser/build/__init__.py                                  5      0   100%
sslamanager/parser/build/bf_2.py                                     30      0   100%
sslamanager/parser/build/pkg_2001/__init__.py                         2      0   100%
sslamanager/parser/build/pkg_2001/xmlschema.py                      694      0   100%
sslamanager/parser/build/pkg_2005/__init__.py                         0      0   100%
sslamanager/parser/build/pkg_2005/pkg_08/__init__.py                  0      0   100%
sslamanager/parser/build/pkg_2005/pkg_08/addressing/__init__.py       2      0   100%
sslamanager/parser/build/pkg_2005/pkg_08/addressing/ws_addr.py      111      0   100%
sslamanager/parser/build/sla.py                                      21      0   100%
sslamanager/parser/build/specs/__init__.py                            5      0   100%
sslamanager/parser/build/specs/capability.py                         20      0   100%
sslamanager/parser/build/specs/controls/__init__.py                   3      0   100%
sslamanager/parser/build/specs/controls/ccm.py                       17      0   100%
sslamanager/parser/build/specs/controls/nist.py                      19      0   100%
sslamanager/parser/build/specs/sdt.py                                36      0   100%
sslamanager/parser/build/specs/security_metric.py                   127      0   100%
sslamanager/parser/build/specs/slo.py                                40      0   100%
sslamanager/parser/build/wsag.py                                    211      0   100%
sslamanager/parser/build/xml.py                                       4      0   100%
sslamanager/parser/ssla_parser.py                                   210     14    93%
sslamanager/test/__init__.py                                          0      0   100%
sslamanager/test/database/__init__.py                                 0      0   100%
sslamanager/test/database/ssla_table_test.py                         79      0   100%
sslamanager/test/parser/__init__.py                                   0      0   100%
sslamanager/test/parser/ssla_parser_test.py                         168      0   100%
-------------------------------------------------------------------------------------
TOTAL                                                              1879     15    99%
```
