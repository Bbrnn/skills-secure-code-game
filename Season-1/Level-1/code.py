'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0

    for item in order.items:
        if item.type == 'payment':
            net += item.amount
        elif item.type == 'product':
            #ensure quantity is positive to avoid underflow vulnearbility
            if item.quantity <= 0:
                return "Invalid item quantity: %s for item type: %s" % (item.quantity, item.type)
            net -= item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
    


    """"
    An underflow vulnerability occurs when a numeric value is reduced below its minimum limit, often due to the subtraction of a large value from a smaller one. Here’s how it can happen here:

    If item.quantity is a negative number (or an unexpected large value), the net calculation may incorrectly increase rather than decrease, leading to an inaccurate balance check.
    Since there is no validation on item.quantity, a malicious input with a negative quantity could bypass the intended balance check by artificially increasing net.

    Fixing the Vulnerability:

    To avoid this underflow vulnerability, we can validate that quantity is a positive integer before including it in the net calculation.
    """


    