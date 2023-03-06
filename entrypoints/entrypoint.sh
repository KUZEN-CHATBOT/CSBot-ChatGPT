#!/bin/bash
set -e
export AWS_REGION=${AWS_REGION:-"ap-northeast-1"}

amazon-ssm-agent -register -code "${SSM_AGENT_CODE}" -id "${SSM_AGENT_ID}" -region "${AWS_REGION}"
amazon-ssm-agent &

flask run --host=0.0.0.0 --port=${FLASK_PORT} &

 # MUST run the process in foreground.
sleep infinity