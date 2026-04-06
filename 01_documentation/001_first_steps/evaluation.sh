#!/bin/bash
set -e 1

# Create hidden test directory (not visible to student)
mkdir -p /home/damner/code/.labtests

# Move the test file injected by Fermion into the test directory
mv $TEST_FILE_NAME /home/damner/code/.labtests/test_main.py

# Install dependencies quietly
pip3 install fastapi uvicorn pytest pytest-json-report httpx --quiet

# Run pytest with JSON report output
cd /home/damner/code/.labtests
pytest --json-report --json-report-file=.report.json test_main.py || true

# Parse pytest JSON report → boolean array for Fermion UI
cat > /home/damner/code/.labtests/processResults.js << 'EOF'
const report = require('./.report.json')
const results = report.tests.map(t => t.outcome === 'passed')
require('fs').writeFileSync(process.env.UNIT_TEST_OUTPUT_FILE, JSON.stringify(results))
EOF

node /home/damner/code/.labtests/processResults.js
