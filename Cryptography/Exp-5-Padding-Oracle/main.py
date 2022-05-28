from paddingoracle import PaddingOracle, decode

t = "http://localhost:9000/po?er="
c = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"

po = PaddingOracle(t)
p = po.decrypt4blocks(c)

print(p)
