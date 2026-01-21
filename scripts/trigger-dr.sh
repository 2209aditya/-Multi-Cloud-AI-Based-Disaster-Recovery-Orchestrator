#!/bin/bash
echo "🚨 Triggering Disaster Recovery..."

kubectl scale deployment sample-app --replicas=0

echo "✅ Primary scaled down. Restore will start on DR cluster."
