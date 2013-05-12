#!/bin/bash

PACKAGES="packages"

while read AGENT_PACKAGES; do
  echo enqueue_package "${AGENT_PACKAGES}"
done < "${PACKAGES}/rpm_agent.txt"

