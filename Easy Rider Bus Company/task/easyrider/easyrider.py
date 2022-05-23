import json
import re
from collections import defaultdict
buses = defaultdict(set)
def main():
    errors = {'stop_name': 0, 'stop_type': 0, 'a_time': 0}  # 'bus_id': 0, 'stop_id': 0,'next_stop': 0,
    json_str = input()
    json_obj = json.loads(json_str)
    error_sum = 0
    for o in json_obj:
        # print(o)
        if not (o.get("bus_id") is not None and type(o["bus_id"]) is int):
            # errors.setdefault("bus_id", 0)
            errors["bus_id"] += 1
            error_sum += 1

        # if not (o.get("stop_id") is not None and type(o["stop_id"]) is int):
        #     # errors.setdefault("stop_id", 0)
        #     errors["stop_id"] += 1
        #     error_sum += 1

        if not (o.get("stop_name") is not None and type(o["stop_name"]) is str and o["stop_name"].strip() != '') \
                or re.match(r'[A-Z]\w+.+?(Road|Avenue|Boulevard|Street)$', o["stop_name"]) is None:
            # errors.setdefault("stop_name", 0)
            errors["stop_name"] += 1
            error_sum += 1
        else:
            buses[o["bus_id"]].add(o["stop_name"])
        # if not (o.get("next_stop") is not None and type(o["next_stop"]) is int):
        #     # errors.setdefault("next_stop", 0)
        #     errors["next_stop"] += 1
        #     error_sum += 1
        #     # print("next stop=", o["next_stop"], type(o["next_stop"]))

        if not (o.get("stop_type") is not None
                and type(o["stop_type"]) is str
                and len(o["stop_type"]) <= 1
                and o["stop_type"] in ['S', 'O', 'F', '']):
            # errors.setdefault("stop_type", 0)
            errors["stop_type"] += 1
            error_sum += 1

        if not (o.get("a_time") is not None and type(o["a_time"]) is str and o["a_time"].strip() != '') \
                or re.match(r'([01]\d|2[0-3]):([0-5]\d)$', o["a_time"]) is None:
            # errors.setdefault("a_time", 0)
            errors["a_time"] += 1
            error_sum += 1

    # print(f"Type and required field validation: {error_sum} errors")
    # for k, v in errors.items():
    #     print(f"{k}: {v}")
    for k,v in buses.items():
        print(f"bus_id: {k}, stops: {len(v)}")

# print(type(0))
main()
