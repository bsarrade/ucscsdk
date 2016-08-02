"""This module contains the general information for TopRoot ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class TopRootConsts():
    pass


class TopRoot(ManagedObject):
    """This is TopRoot class."""

    consts = TopRootConsts()
    naming_props = set([])

    mo_meta = MoMeta("TopRoot", "topRoot", "", VersionMeta.Version101a, "InputOutput", 0xf, [], ["read-only"], [], [u'aaaLog', u'callhomeHolder', u'capabilityCatalogue', u'clitestTypeTest', u'clitestTypeTest2', u'computeResourceAggrEp', u'configImpactAnalyzerEp', u'consumerUniverse', u'controllerEp', u'domainEp', u'eventHolder', u'eventLog', u'extpolEp', u'fabricHolder', u'faultHolder', u'fcpoolUniverse', u'guiGuiCont', u'hcHolder', u'identMetaVerse', u'identpoolMetaVerse', u'ippoolUniverse', u'iqnpoolUniverse', u'macpoolUniverse', u'mgmtEp', u'nfsEp', u'observeObservedCont', u'orgDomainGroup', u'orgOrg', u'policyLocalMap', u'policyPolicyEp', u'policyUniverse', u'procManager', u'queryEp', u'smartlicenseHolder', u'statsDbSummaryMeta', u'statsHolder', u'statsStatsQueryHolder', u'storageCloud', u'syntheticFileSystem', u'topMetaInf', u'topSystem', u'uuidpoolUniverse'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "TopRoot", parent_mo_or_dn, **kwargs)

