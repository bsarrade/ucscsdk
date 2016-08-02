"""This module contains the general information for FeatureNetworkDef ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class FeatureNetworkDefConsts():
    pass


class FeatureNetworkDef(ManagedObject):
    """This is FeatureNetworkDef class."""

    consts = FeatureNetworkDefConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FeatureNetworkDef", "featureNetworkDef", "network-feature-[name]", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["admin"], [u'featureCatalogEp'], [u'domainEnvironmentParam', u'domainNetworkParam', u'domainServerParam', u'domainStorageParam'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "feature_mask": MoPropertyMeta("feature_mask", "featureMask", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|pvlan_feature_mask|netflow_feature_mask|vlan_range_feature_mask|vnic_pairing_feature_mask|vlan_range_extended_feature_mask|usnic_vmq_feature_mask),){0,7}(defaultValue|none|pvlan_feature_mask|netflow_feature_mask|vlan_range_feature_mask|vnic_pairing_feature_mask|vlan_range_extended_feature_mask|usnic_vmq_feature_mask){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "featureMask": "feature_mask", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.description = None
        self.feature_mask = None
        self.status = None
        self.version = None

        ManagedObject.__init__(self, "FeatureNetworkDef", parent_mo_or_dn, **kwargs)

