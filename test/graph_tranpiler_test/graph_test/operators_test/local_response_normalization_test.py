import numpy as np

from graph_transpiler.graph.operators.local_response_normalization import LocalResponseNormalization
from graph_transpiler.graph.variable import Variable
from graph_transpiler.graph.variables.attributes.order import OrderNHWC, OrderHWNC, OrderHWCN, OrderCNHW, \
    OrderCHWN, OrderNCHW


# FIXME 各orderをテストにわけられないか
def test_every_order():
    orders = [OrderNHWC, OrderHWNC, OrderHWCN, OrderNCHW, OrderCNHW, OrderCHWN]

    for order in orders:
        op = LocalResponseNormalization(None, n=1, k=2, alpha=0.1, beta=0.2)

        x = Variable(np.arange(order.ndim) + 1, OrderNHWC)
        x.change_order(order)

        y, = op(x)

        for axis in y.order.axes:
            assert y.shape_dict[axis] == x.shape_dict[axis]