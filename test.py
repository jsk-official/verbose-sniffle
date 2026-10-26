import os
import json

events = open(os.environ["GITHUB_EVENT_PATH"], "r")
meta = open("src/replicated_storage/meta.toml", "a+")
parsed_events = json.loads(events.read())

commit_id = parsed_events["after"][0:7]
branch = parsed_events["ref"].replace("refs/heads/", "")

meta.write(f"\ncommit = \"{commit_id}\"\nbranch = \"{branch}\"")
print(meta.read())
meta.close()
