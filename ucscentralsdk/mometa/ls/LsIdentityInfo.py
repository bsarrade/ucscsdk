"""This module contains the general information for LsIdentityInfo ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class LsIdentityInfoConsts():
    UUID_IDENTITY_STATE_CONSISTENT = "consistent"
    UUID_IDENTITY_STATE_MISMATCH = "mismatch"
    WRITE_MODE_SYNC = "sync"
    WRITE_MODE_UNSYNC = "unsync"


class LsIdentityInfo(ManagedObject):
    """This is LsIdentityInfo class."""

    consts = LsIdentityInfoConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsIdentityInfo", "lsIdentityInfo", "ls-identity-info", None, "InputOutput", 0x1f, [], ["admin", "ls-config", "ls-server"], [u'computeBlade', u'computeRackUnit', u'computeServerUnit', u'lsServer'], [u'faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uuid_identity_state": MoPropertyMeta("uuid_identity_state", "uuidIdentityState", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["consistent", "mismatch"], []), 
        "write_mode": MoPropertyMeta("write_mode", "writeMode", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["sync", "unsync"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "uuidIdentityState": "uuid_identity_state", 
        "writeMode": "write_mode", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.uuid_identity_state = None
        self.write_mode = None

        ManagedObject.__init__(self, "LsIdentityInfo", parent_mo_or_dn, **kwargs)

