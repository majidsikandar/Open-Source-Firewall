from pyptables import default_tables, restore
from pyptables.rules import Rule, Accept


def set_rules():

    tables = default_tables()

    # # get the forward chain of the filter tables
    forward = tables['filter']['FORWARD']

    print(forward)

    # any packet matching an established connection should be allowed
    forward.append(Accept(match='conntrack', ctstate='ESTABLISHED'))

    # add rules to the forward chain for DNS, HTTP and HTTPS ports
    forward.append(Accept(proto='tcp', dport='53'))
    forward.append(Accept(proto='tcp', dport='80'))
    forward.append(Accept(proto='tcp', dport='443'))

    # any packet not matching a rules will be dropped
    forward.policy = Rule.DROP
    print(forward)
