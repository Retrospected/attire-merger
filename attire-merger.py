#!/usr/bin/python3
#

import json
import os

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
    
    with open('./output/output.json', 'w') as f:
        json.dump(base, f, indent=4)
