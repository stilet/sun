#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A sun.taskapp beat -l INFO
