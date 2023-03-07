#!/bin/bash

ps -elf | grep amazon-ssm-agent | grep -v grep 2>&1 > /dev/null || exit 1 

curl -sf http://localhost:${FLASK_PORT}/healthcheck 2>&1 > /dev/null || exit 6