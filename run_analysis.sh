#!/bin/bash

# run_analysis.sh

echo "Exporting data from MongoDB..."
mongoexport --host mongo-db --db analytics --collection entries --out data.json

echo "Analyzing data using JQ..."
total_sum=$(jq '.[].value' data.json | paste -sd+ | bc)
total_count=$(jq '. | length' data.json)

if [ "$total_count" -eq 0 ]; then
    echo "No data found to analyze."
    exit 1
fi

average_value=$(echo "scale=2; $total_sum / $total_count" | bc)

echo "Saving analysis results to analysis_result.txt"
echo "Total entries: $total_count" > analysis_result.txt
echo "Total sum of values: $total_sum" >> analysis_result.txt
echo "Average value: $average_value" >> analysis_result.txt

echo "Analysis complete. Results are in analysis_result.txt"
