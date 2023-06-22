#!/usr/bin/python3
#

import json
import os
import sys
import csv

base = {
    "attire-version":  "1.1",
    "execution-data":  {
                           "execution-source":  "<PLACEHOLDER>",
                           "execution-id":  "<PLACEHOLDER>",
                           "execution-category":  {
                                                      "name":  "Atomic Red Team",
                                                      "abbreviation":  "ART"
                                                  },
                           "execution-command":  "<PLACEHOLDER>",
                           "target":  {
                                          "user":  "<PLACEHOLDER>",
                                          "host":  "<PLACEHOLDER>",
                                          "ip":  "<PLACEHOLDER>",
                                          "path":  "<PLACEHOLDER>"
                                      },
                           "time-generated":  "<PLACEHOLDER>"
                       },
    "procedures":  []
}

if __name__ == "__main__":

    arguments = sys.argv

    print("ATTiRE merger - converting Atomic CSV files or merging Atomic ATTiRe files into a single ATTiRe file.")
    if len(arguments) != 2:
        print("I will be taking files from ./input/. But specify if you want to use the *.csv files or *.json files in this dir by using the -csv or -json flag.")
        exit()

    if arguments[1] == "-json":
        print("Processing ./input/*json files.")
        # Iterate through each file in the current directory
        for filename in os.listdir("./input/"):

            # Check if the file has a .json extension
            if filename.endswith('.json'):
                with open("./input/"+filename, 'r') as f:
                    file_contents = f.read()
                
                json_obj = json.loads(file_contents)

                if len(json_obj["procedures"])>1:
                    print(f"Skipping file: {filename} because it has more than 1 procedure(?)")

                base["procedures"].append(json_obj["procedures"][0])
    elif arguments[1] == "-csv":
        print("Processing ./input/*csv files.")
        for filename in os.listdir("./input/"):
            # Check if the file has a .csv extension
            if filename.endswith('.csv'):
                with open("./input/"+filename, 'r') as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        time_start = row[0]
                        technique = row[2]
                        procedure_name = row[4]
                        guid = row[7]

                        procedure = {
                            "procedure-name": procedure_name,
                            "procedure-description": "",
                            "procedure-id": {
                                "type": "guid",
                                "id": guid
                            },
                            "mitre-technique-id": technique,
                            "order": 1,
                            "steps": [
                                {
                                    "command": "",
                                    "executor": "",
                                    "order": 1,
                                    "output": [
                                        {
                                            "content": "",
                                            "level": "",
                                            "type": ""
                                        }
                                    ],
                                    "time-start": time_start[:-1]+".000Z",
                                    "time-stop": time_start[:-1]+".000Z"
                                }
                            ]
                        }

                        base["procedures"].append(procedure)
    
    with open('./output/output.json', 'w') as f:
        json.dump(base, f, indent=4)
