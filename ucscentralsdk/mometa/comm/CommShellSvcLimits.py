"""This module contains the general information for CommShellSvcLimits ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class CommShellSvcLimitsConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class CommShellSvcLimits(ManagedObject):
    """This is CommShellSvcLimits class."""

    consts = CommShellSvcLimitsConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommShellSvcLimits", "commShellSvcLimits", "shell-svc-limits", VersionMeta.Version101a, "InputOutput", 0xff, [], ["aaa", "admin"], [u'orgDomainGroup', u'orgOrg', u'policyDeviceProfile'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sessions_per_user": MoPropertyMeta("sessions_per_user", "sessionsPerUser", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-32"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total_sessions": MoPropertyMeta("total_sessions", "totalSessions", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-32"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sessionsPerUser": "sessions_per_user", 
        "status": "status", 
        "totalSessions": "total_sessions", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sessions_per_user = None
        self.status = None
        self.total_sessions = None

        ManagedObject.__init__(self, "CommShellSvcLimits", parent_mo_or_dn, **kwargs)

