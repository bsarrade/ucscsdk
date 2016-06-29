"""This module contains the general information for IqnpoolBlock ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class IqnpoolBlockConsts():
    CONFIG_SCOPE_PRIVATE = "private"
    CONFIG_SCOPE_PUBLIC = "public"
    SCOPE_PRIVATE = "private"
    SCOPE_PUBLIC = "public"


class IqnpoolBlock(ManagedObject):
    """This is IqnpoolBlock class."""

    consts = IqnpoolBlockConsts()
    naming_props = set([u'suffix', u'from', u'to'])

    mo_meta = MoMeta("IqnpoolBlock", "iqnpoolBlock", "iqn-suffix-[suffix]-from-[r_from]-to-[to]", VersionMeta.Version101a, "InputOutput", 0xff, [], ["admin", "ls-storage-policy"], [u'iqnpoolPool'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_scope": MoPropertyMeta("config_scope", "configScope", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["private", "public"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "r_from": MoPropertyMeta("r_from", "from", "ushort", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], ["0-65535"]), 
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "scope": MoPropertyMeta("scope", "scope", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["private", "public"], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suffix": MoPropertyMeta("suffix", "suffix", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[0-9a-zA-Z\.:-]{0,64}$""", [], []), 
        "to": MoPropertyMeta("to", "to", "ushort", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x80, None, None, None, [], ["0-65535"]), 
    }

    prop_map = {
        "assigned": "assigned", 
        "childAction": "child_action", 
        "configScope": "config_scope", 
        "dn": "dn", 
        "from": "r_from", 
        "qualifier": "qualifier", 
        "rn": "rn", 
        "scope": "scope", 
        "size": "size", 
        "status": "status", 
        "suffix": "suffix", 
        "to": "to", 
    }

    def __init__(self, parent_mo_or_dn, suffix, r_from, to, **kwargs):
        self._dirty_mask = 0
        self.suffix = suffix
        self.r_from = r_from
        self.to = to
        self.assigned = None
        self.child_action = None
        self.config_scope = None
        self.qualifier = None
        self.scope = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "IqnpoolBlock", parent_mo_or_dn, **kwargs)

