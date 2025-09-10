#!/bin/bash
# Script to create required Kafka topics for PostHog

echo "Waiting for Kafka to be ready..."
sleep 10

# Create the required topics
docker exec -it posthog-kafka-1 kafka-topics --create --if-not-exists --topic clickhouse_events_json --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 2>/dev/null || true
docker exec -it posthog-kafka-1 kafka-topics --create --if-not-exists --topic events_plugin_ingestion --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 2>/dev/null || true
docker exec -it posthog-kafka-1 kafka-topics --create --if-not-exists --topic conversion_events --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 2>/dev/null || true
docker exec -it posthog-kafka-1 kafka-topics --create --if-not-exists --topic session_recording_events --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 2>/dev/null || true

echo "Kafka topics created successfully!"
