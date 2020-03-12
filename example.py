from pyaz import az


def az_demo(args_str):
    print("calling: az", args_str)
    result = az(args_str)
    print("exit code:", result.exit_code)
    print("out:", result.out)
    print("log:", result.log)


def main():
    # exit code 0: succeed
    az_demo("account list-locations --query \"[?name=='westus'] | [0]\"")

    # exit code 1: request error
    az_demo("group create -l eastus4 -n foo")

    # exit code 2: command parsing error
    az_demo("group not-exist")

    # exit code 3: resource doesn't exist
    az_demo("group show -g not-exist")

    # Happy scripting with Python!
    import json
    accounts = json.loads(az('account list').out)
    print("My subscriptions:")
    for a in accounts:
        selected = "*" if a["isDefault"] else " "
        print("{} {} {}".format(selected, a["id"], a["name"]))


if __name__ == "__main__":
    main()
