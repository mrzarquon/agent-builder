#!/bin/bash

while read AGENT_PACKAGES; do
  echo enqueue_package "${AGENT_PACKAGES}"
done < "rpm_agent.txt"

