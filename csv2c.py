
out = "data"

def conv(name):
    data = open(name + ".csv").read().splitlines()[1:]
    open(out + ".txt", "a").write(str(len(data)) + "\n" +
                                    "\n".join(d.replace(",", " ") for d in data) + "\n")

conv("box_dimension")
conv("order_sku")
conv("sku_dimenssion")