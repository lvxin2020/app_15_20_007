import yaml
data_list = []
with open("./search.yaml","r",encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print(data.values())
    for i in data.values():

        data_list.append((i.get("input"),i.get("exp")))
        print("*" * 10)
print(data_list)