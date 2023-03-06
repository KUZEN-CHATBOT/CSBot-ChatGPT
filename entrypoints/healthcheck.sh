#!/bin/bash

ps -elf | grep amazon-ssm-agent | grep -v grep 2>&1 > /dev/null || exit 1 

ps -elf | grep flask | grep -v grep 2>&1 > /dev/null || exit 5
curl -sf http://localhost:${FLASK_PORT}/ 2>&1 > /dev/null || exit 6