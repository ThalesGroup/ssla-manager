#!/usr/bin/env bash

#
# CONSTANTS
#

SCRIPT_PATH="$(realpath "$0")"
PROJECT_DIR="$(dirname "${SCRIPT_PATH:?}")"
SSLA_XSD_FILE="${PROJECT_DIR:?}/sslamanager/parser/templates/ssla/ssla_schema.xsd"
SSLA_MODELS_PACKAGE="sslamanager.parser.build"
SSLA_MODELS_DESTINATION="${PROJECT_DIR:?}/sslamanager/parser/build"

#
# FUNCTIONS
#

function check_requirement(){
    if ! eval "$@" >> /dev/null 2>&1 ; then
        echo "! Fatal : missing requirement"
        if [ -n "${*: -1}" ]; then echo "${@: -1}"; fi
        exit 1
    fi
}

function init_build(){
    cd "${PROJECT_DIR}" || exit
    echo ". Build environment :"
    poetry env info
    poetry check
    echo ". Install dependencies"
    poetry run python -m pip install --upgrade pip
    poetry update
}

function xsdata_generation(){
    echo ". Generate SSLA models"
    cd "${PROJECT_DIR}" || exit
    rm -rf "${SSLA_MODELS_DESTINATION:?}"
    # mandatory to have xsdata[cli] installed
    poetry run python -m pip install --upgrade xsdata[cli]
    poetry run python -m xsdata "${SSLA_XSD_FILE}" --package "${SSLA_MODELS_PACKAGE}"
}

function build(){
    echo ". Build module"
    cd "${PROJECT_DIR}" || exit
    rm -rf "${PROJECT_DIR}/dist"
    poetry build

    echo ". Built in dist/:"
    ls "./dist/"
}

#
# MAIN
#

check_requirement poetry --version "! Install poetry first"

init_build
xsdata_generation
build

echo ". OK"
exit 0


