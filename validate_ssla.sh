#!/usr/bin/env bash
#
# Validate an SSLA file and print what a human has to fix in it.
#
# Usage: ./validate_ssla.sh /path/to/ssla.xml
#
# Exit code is 0 when the SSLA is valid, 1 otherwise.

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "usage: $0 <ssla.xml>" >&2
    exit 2
fi

SSLA_FILE="$1"

if [ ! -r "$SSLA_FILE" ]; then
    echo "error: cannot read '$SSLA_FILE'" >&2
    exit 2
fi

uv run --quiet python - "$SSLA_FILE" <<'PY'
import sys
from pathlib import Path

from sslamanager.exceptions import SSLAException
from sslamanager.parser.ssla_parser import SSLAParser

ssla_path = Path(sys.argv[1])
parser = SSLAParser()

try:
    # format validation: well-formed XML + compliance with the SSLA XML Schema
    ssla = parser.parse_from_content(ssla_path.read_bytes())

    # content validation: read the parts a consumer of the SSLA needs
    services = ssla.get_services_names()
    slos = ssla.get_slos_json()
    metrics = {name: ssla.get_metrics_json(name) for name in services}
    properties = {name: ssla.get_service_properties_json(name) for name in services}
except SSLAException as e:
    print(f"INVALID  {ssla_path}")
    print(f"  problem : {type(e).__name__}")
    print(f"  details : {e}")
    sys.exit(1)

# the schema cannot check that an SLO points at a metric that exists
declared = {metric.id for service_metrics in metrics.values() for metric in service_metrics}
errors = []
for slo in slos:
    if slo.metricREF not in declared:
        errors.append(f"SLO '{slo.id}' references the unknown metric '{slo.metricREF}' "
                      f"(declared metrics: {', '.join(sorted(declared))})")

if errors:
    print(f"INVALID  {ssla_path}")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)

print(f"VALID    {ssla_path}")
for name in services:
    print(f"  service '{name}': {len(metrics[name])} metric(s), "
          f"{len(properties[name])} property set(s)")
print(f"  {len(slos)} SLO(s)")
PY
