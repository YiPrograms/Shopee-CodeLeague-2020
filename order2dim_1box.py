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

for order_id, dims in orders.items():
    if len(dims) > 1:
        continue

    res = "UNFITTED"
    r = 1000000000.0
    x, y, z = dims[0]

    for b_id, siz in boxes.items():
        a, b, c = siz
        if x < a and y < b and z < c:
            if a*b*c < r:
                res = b_id
                r = a*b*c
        if x < a and z < b and y < c:
            if a*b*c < r:
                res = b_id
                r = a*b*c
        if y < a and x < b and z < c:
            if a*b*c < r:
                res = b_id
                r = a*b*c
        if y < a and z < b and x < c:
            if a*b*c < r:
                res = b_id
                r = a*b*c
        if z < a and x < b and y < c:
            if a*b*c < r:
                res = b_id
                r = a*b*c
        if z < a and y < b and x < c:
            if a*b*c < r:
                res = b_id
                r = a*b*c
    ans[order_id] = res

open("1_item_ans.csv", "w").write("order_number,box_number\n" + "\n".join(o + "," + b for o, b in ans.items()) + "\n")

import code
code.interact(local=locals())