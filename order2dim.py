order_data = open("order_sku.csv").read().splitlines()[1:]
sku_data = open("sku_dimenssion.csv").read().splitlines()[1:]
box_data = open("box_dimension.csv").read().splitlines()[1:]

sku = {}
for s in sku_data:
    sku_id,length,width,height = s.split(",")
    sku[sku_id] = (float(length),float(width),float(height))

boxes = {}
for b in box_data:
    _id,box_number,length,width,height = b.split(",")
    boxes[box_number] = (float(length),float(width),float(height))

orders = {}

for o in order_data:
    order_number, sku_id, quantity = o.split(",")
    if order_number not in orders:
        orders[order_number] = []
    
    for _ in range(int(quantity)):
        orders[order_number].append(sku[sku_id])
    
ans = {}


import itertools
for order_id, dims in orders.items():
    perm_dims = itertools.product(*[itertools.permutations(d) for d in dims])

    res = "UNFITTED"
    r = 1000000000.0
    for dim in perm_dims:
        dim = sorted(dim)
        for b in boxes.items():
            x, y, z = b
            for a, b, c in dim:
                if a <= x and b <= y and c <= z:
                    x -= a
                    y -= b
                    z -= c
                




# open("1_item_ans.csv", "w").write("order_number,box_number\n" + "\n".join(o + "," + b + "\n" for o, b in ans.items()) + "\n")

import code
code.interact(local=locals())