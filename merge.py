enum_size = open("enum_size.csv").read().splitlines()[1:]
one_item = open("1_item_ans.csv").read().splitlines()[1:]
crazy = open("crazy.csv").read().splitlines()[1:]


ans = {}

for l in crazy:
    oid, bnum = l.split(",")
    ans[oid] = bnum

for l in enum_size:
    oid, bnum = l.split(",")
    ans[oid] = bnum

for l in one_item:
    oid, bnum = l.split(",")
    ans[oid] = bnum

open("merge_ans.csv", "w").write("order_number,box_number\n" + "\n".join(o + "," + b for o, b in ans.items()) + "\n")
