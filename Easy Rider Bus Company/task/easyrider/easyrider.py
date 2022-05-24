import itertools
import json
import re
from collections import defaultdict

buses = defaultdict(list)


def main():
    errors = {'stop_name': 0, 'stop_type': 0, 'a_time': 0}
    json_str = input()
    json_obj = json.loads(json_str)
    error_sum = 0

    for o in json_obj:

        if not (o.get("bus_id") is not None and type(o["bus_id"]) is int):
            errors["bus_id"] += 1
            error_sum += 1

        if not (o.get("stop_name") is not None and type(o["stop_name"]) is str and o["stop_name"].strip() != '') \
                or re.match(r'[A-Z]\w+.+?(Road|Avenue|Boulevard|Street)$', o["stop_name"]) is None:
            errors["stop_name"] += 1
            error_sum += 1

        if not (o.get("stop_type") is not None
                and type(o["stop_type"]) is str
                and len(o["stop_type"]) <= 1
                and o["stop_type"] in ['S', 'O', 'F', '']):
            errors["stop_type"] += 1
            error_sum += 1

        if not (o.get("a_time") is not None and type(o["a_time"]) is str and o["a_time"].strip() != '') \
                or re.match(r'([01]\d|2[0-3]):([0-5]\d)$', o["a_time"]) is None:
            errors["a_time"] += 1
            error_sum += 1
        else:
            buses[o["bus_id"]].append((o["stop_name"], o["stop_type"], o["a_time"]))

    names = set()
    for k, v in buses.items():
        names.update(v)

    transfer = set()
    for first, second in itertools.combinations(buses.items(), 2):
        first = {f[0] for f in first[1]}
        second = {f[0] for f in second[1]}
        transfer.update(first.intersection(second))

    on_demand = set()

    for k, v in buses.items():
        if v[0][1] == 'O':
            on_demand.add(v[0][0])

        if v[-1][1] == 'O':
            on_demand.add(v[-1][0])

        for s in v:
            if s[1] == 'O' and s[0] in transfer:
                on_demand.add(s[0])

    print("On demand stops test:")
    if len(on_demand) == 0:
        print("OK")
    else:
        print(f"Wrong stop type: {sorted(list(on_demand))}")


main()
