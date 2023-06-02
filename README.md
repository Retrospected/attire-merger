# ATTiRe merger
Simple script to merge ATTiRe logs that have been created when running Atomic Red Team (ART) using Invoke-AtomicRedTeam and the Attire-ExecutionLogger module.
This will merge multiple indiviually performed simulated procedures into 1 file to make it uploadable to VECTR.

More information about the ATTiRe logging format can be found here: https://github.com/SecurityRiskAdvisors/ATTiRe

This has been created to cover the missing feature to upload multiple test cases to VECTR as described in this issue: https://github.com/SecurityRiskAdvisors/VECTR/issues/235.

## Usage

Obviously first run your Atomic test procedures to generate multiple JSON files that require merging, then:

1. Place your ATTiRe formatted JSON files in the `./input/` folder.
2. Modify `attire-merger.py` with your execution data to your only liking. This execution data will be used for all tested procedures
3. Run `./attire-merger.py`
4. Take the output from `./output/output.json` and upload it to VECTR via the UI.

## Credits

https://github.com/SecurityRiskAdvisors/invoke-atomic-attire-logger
https://github.com/SecurityRiskAdvisors/VECTR
https://github.com/redcanaryco/atomic-red-team/tree/master/atomics
https://github.com/redcanaryco/invoke-atomicredteam/