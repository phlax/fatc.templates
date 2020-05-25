#!/usr/bin/env python

import json
import os
import sys
import yaml


name = os.environ["TPLS_TEST_NAME"]
parsed = yaml.load(sys.stdin.read(), Loader=yaml.Loader)

# print(parsed)

with open("nginx-example/tpls.json") as f:
    defaults = json.load(f)

render_vars = defaults["defaults"]

with open("example/config.json") as f:
    config = json.load(f)

render_vars.update(config["render"][name]["vars"])

service = render_vars["service"]
version = float(render_vars["compose.version"])
image = render_vars["image"]
restart = render_vars["restart"]
networks = {
    render_vars["network"]: {"ipv4_address": render_vars["ip"]}}
labels = {
    "custom_label": render_vars["label"]}
healthcheck = {
    "interval": "10s",
    "retries": 20,
    "test": render_vars["healthcheck.command"]}
volumes =  [
    "%s:/etc/nginx/conf.d" % render_vars["config"],
    "%s:%s" % (render_vars["assets"], render_vars["assets.mount"])]

# print(render_vars)
# print(parsed)

assert parsed["version"] == version
assert parsed["services"][service]["image"] == image
assert parsed["services"][service]["restart"] == restart
assert parsed["services"][service]["networks"] == networks
assert parsed["services"][service]["volumes"] == volumes
assert parsed["services"][service]["labels"] == labels
assert parsed["services"][service]["healthcheck"] == healthcheck
