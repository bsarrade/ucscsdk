"""This module contains the general information for AdaptorIpV6RssHashProfile ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class AdaptorIpV6RssHashProfileConsts():
    pass


class AdaptorIpV6RssHashProfile(ManagedObject):
    """This is AdaptorIpV6RssHashProfile class."""

    consts = AdaptorIpV6RssHashProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorIpV6RssHashProfile", "adaptorIpV6RssHashProfile", "ipv6-rss-hash", VersionMeta.Version111a, "InputOutput", 0xf, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], [u'adaptorHostEthIfProfile', u'adaptorUsnicConnDef'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ip_hash": MoPropertyMeta("ip_hash", "ipHash", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tcp_hash": MoPropertyMeta("tcp_hash", "tcpHash", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ipHash": "ip_hash", 
        "rn": "rn", 
        "status": "status", 
        "tcpHash": "tcp_hash", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.ip_hash = None
        self.status = None
        self.tcp_hash = None

        ManagedObject.__init__(self, "AdaptorIpV6RssHashProfile", parent_mo_or_dn, **kwargs)

