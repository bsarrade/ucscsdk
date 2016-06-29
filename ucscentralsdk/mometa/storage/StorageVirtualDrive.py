"""This module contains the general information for StorageVirtualDrive ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class StorageVirtualDriveConsts():
    ACCESS_POLICY_BLOCKED = "blocked"
    ACCESS_POLICY_READ_ONLY = "read-only"
    ACCESS_POLICY_READ_WRITE = "read-write"
    ACCESS_POLICY_UNKNOWN = "unknown"
    ACTUAL_WRITE_CACHE_POLICY_UNKNOWN = "unknown"
    ACTUAL_WRITE_CACHE_POLICY_WRITE_BACK = "write-back"
    ACTUAL_WRITE_CACHE_POLICY_WRITE_THROUGH = "write-through"
    ADMIN_ACTION_TRIGGER_CANCELED = "canceled"
    ADMIN_ACTION_TRIGGER_IDLE = "idle"
    ADMIN_ACTION_TRIGGER_TRIGGERED = "triggered"
    ADMIN_STATE_DEGRADED = "degraded"
    ADMIN_STATE_DELETE = "delete"
    ADMIN_STATE_OFFLINE = "offline"
    ADMIN_STATE_ONLINE = "online"
    ADMIN_STATE_RESTORE = "restore"
    ADMIN_STATE_UNDEFINED = "undefined"
    AVAILABLE_SIZE_UNKNOWN = "unknown"
    BLOCK_SIZE_UNKNOWN = "unknown"
    BOOTABLE_FALSE = "false"
    BOOTABLE_TRUE = "true"
    BOOTABLE_UNKNOWN = "unknown"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    CONFIGURED_WRITE_CACHE_POLICY_ALWAYS_WRITE_BACK = "always-write-back"
    CONFIGURED_WRITE_CACHE_POLICY_UNKNOWN = "unknown"
    CONFIGURED_WRITE_CACHE_POLICY_WRITE_BACK_GOOD_BBU = "write-back-good-bbu"
    CONFIGURED_WRITE_CACHE_POLICY_WRITE_THROUGH = "write-through"
    CONNECTION_PROTOCOL_SAS = "SAS"
    CONNECTION_PROTOCOL_SATA = "SATA"
    CONNECTION_PROTOCOL_UNSPECIFIED = "unspecified"
    DEPLOY_ACTION_ABORT_REPLICATION = "abort-replication"
    DEPLOY_ACTION_CREATE = "create"
    DEPLOY_ACTION_DELETE = "delete"
    DEPLOY_ACTION_MODIFY = "modify"
    DEPLOY_ACTION_NO_ACTION = "no-action"
    DEPLOY_ACTION_REPLACE = "replace"
    DEPLOY_ACTION_RESTORE = "restore"
    DEPLOY_ACTION_SET_OFFLINE = "set-offline"
    DEPLOY_ACTION_SET_ONLINE = "set-online"
    DRIVE_CACHE_DISABLE = "disable"
    DRIVE_CACHE_ENABLE = "enable"
    DRIVE_CACHE_NO_CHANGE = "no-change"
    DRIVE_CACHE_UNKNOWN = "unknown"
    DRIVE_STATE_CACHE_DEGRADED = "cache-degraded"
    DRIVE_STATE_DEGRADED = "degraded"
    DRIVE_STATE_OFFLINE = "offline"
    DRIVE_STATE_OPTIMAL = "optimal"
    DRIVE_STATE_PARTIALLY_DEGRADED = "partially-degraded"
    DRIVE_STATE_REBUILDING = "rebuilding"
    DRIVE_STATE_UNKNOWN = "unknown"
    IO_POLICY_CACHED = "cached"
    IO_POLICY_DIRECT = "direct"
    IO_POLICY_UNKNOWN = "unknown"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    NUMBER_OF_BLOCKS_UNKNOWN = "unknown"
    OPER_STATE_COMPUTE_DEGRADED = "compute-degraded"
    OPER_STATE_COMPUTE_INOPERABLE = "compute-inoperable"
    OPER_STATE_OFFLINE = "offline"
    OPER_STATE_ONLINE = "online"
    OPER_STATE_UNDEFINED = "undefined"
    OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPERABILITY_CONFIG = "config"
    OPERABILITY_DECOMISSIONING = "decomissioning"
    OPERABILITY_DEGRADED = "degraded"
    OPERABILITY_DISABLED = "disabled"
    OPERABILITY_DISCOVERY = "discovery"
    OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPERABILITY_IDENTIFY = "identify"
    OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPERABILITY_INOPERABLE = "inoperable"
    OPERABILITY_MALFORMED_FRU = "malformed-fru"
    OPERABILITY_NOT_SUPPORTED = "not-supported"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    OPERABILITY_POST_FAILURE = "post-failure"
    OPERABILITY_POWER_PROBLEM = "power-problem"
    OPERABILITY_POWERED_OFF = "powered-off"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    OPERABILITY_UNKNOWN = "unknown"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
    PRESENCE_EQUIPPED_UNSUPPORTED = "equipped-unsupported"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
    PRESENCE_MISSING = "missing"
    PRESENCE_MISSING_SLAVE = "missing-slave"
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    READ_POLICY_NORMAL = "normal"
    READ_POLICY_READ_AHEAD = "read-ahead"
    READ_POLICY_UNKNOWN = "unknown"
    STRIP_SIZE_UNKNOWN = "unknown"
    TYPE_MIRROR = "mirror"
    TYPE_MIRROR_STRIPE = "mirror-stripe"
    TYPE_RAID = "raid"
    TYPE_SIMPLE = "simple"
    TYPE_STRIPE = "stripe"
    TYPE_STRIPE_DUAL_PARITY = "stripe-dual-parity"
    TYPE_STRIPE_DUAL_PARITY_STRIPE = "stripe-dual-parity-stripe"
    TYPE_STRIPE_PARITY = "stripe-parity"
    TYPE_STRIPE_PARITY_STRIPE = "stripe-parity-stripe"
    TYPE_UNSPECIFIED = "unspecified"


class StorageVirtualDrive(ManagedObject):
    """This is StorageVirtualDrive class."""

    consts = StorageVirtualDriveConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("StorageVirtualDrive", "storageVirtualDrive", "vd-[id]", VersionMeta.Version131a, "InputOutput", 0xff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], [u'storageController'], [u'storageLunDisk', u'storageOperation', u'storageScsiLunRef', u'storageVDMemberEp', u'storageVirtualDriveOperation'], ["Get", "Set"])

    prop_meta = {
        "access_policy": MoPropertyMeta("access_policy", "accessPolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blocked", "read-only", "read-write", "unknown"], []), 
        "actual_write_cache_policy": MoPropertyMeta("actual_write_cache_policy", "actualWriteCachePolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown", "write-back", "write-through"], []), 
        "admin_action_trigger": MoPropertyMeta("admin_action_trigger", "adminActionTrigger", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["canceled", "idle", "triggered"], []), 
        "admin_name": MoPropertyMeta("admin_name", "adminName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,15}""", [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["degraded", "delete", "offline", "online", "restore", "undefined"], []), 
        "available_size": MoPropertyMeta("available_size", "availableSize", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true", "unknown"], []), 
        "change_qualifier": MoPropertyMeta("change_qualifier", "changeQualifier", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|no-change|policy-change|global-hotspare-change|ded-hotspare-change|name-change|size-change|boot-drive-change|scrub-change),){0,8}(defaultValue|no-change|policy-change|global-hotspare-change|ded-hotspare-change|name-change|size-change|boot-drive-change|scrub-change){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier_reason": MoPropertyMeta("config_qualifier_reason", "configQualifierReason", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned"], []), 
        "configured_write_cache_policy": MoPropertyMeta("configured_write_cache_policy", "configuredWriteCachePolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["always-write-back", "unknown", "write-back-good-bbu", "write-through"], []), 
        "connection_protocol": MoPropertyMeta("connection_protocol", "connectionProtocol", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["SAS", "SATA", "unspecified"], []), 
        "deploy_action": MoPropertyMeta("deploy_action", "deployAction", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["abort-replication", "create", "delete", "modify", "no-action", "replace", "restore", "set-offline", "set-online"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "drive_cache": MoPropertyMeta("drive_cache", "driveCache", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disable", "enable", "no-change", "unknown"], []), 
        "drive_state": MoPropertyMeta("drive_state", "driveState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cache-degraded", "degraded", "offline", "optimal", "partially-degraded", "rebuilding", "unknown"], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "io_policy": MoPropertyMeta("io_policy", "ioPolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cached", "direct", "unknown"], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "oper_device_id": MoPropertyMeta("oper_device_id", "operDeviceId", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute-degraded", "compute-inoperable", "offline", "online", "undefined"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "read_policy": MoPropertyMeta("read_policy", "readPolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["normal", "read-ahead", "unknown"], []), 
        "ref_dn": MoPropertyMeta("ref_dn", "refDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "strip_size": MoPropertyMeta("strip_size", "stripSize", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["mirror", "mirror-stripe", "raid", "simple", "stripe", "stripe-dual-parity", "stripe-dual-parity-stripe", "stripe-parity", "stripe-parity-stripe", "unspecified"], []), 
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vendor_uuid": MoPropertyMeta("vendor_uuid", "vendorUuid", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
    }

    prop_map = {
        "accessPolicy": "access_policy", 
        "actualWriteCachePolicy": "actual_write_cache_policy", 
        "adminActionTrigger": "admin_action_trigger", 
        "adminName": "admin_name", 
        "adminState": "admin_state", 
        "availableSize": "available_size", 
        "blockSize": "block_size", 
        "bootable": "bootable", 
        "changeQualifier": "change_qualifier", 
        "childAction": "child_action", 
        "configQualifierReason": "config_qualifier_reason", 
        "configState": "config_state", 
        "configuredWriteCachePolicy": "configured_write_cache_policy", 
        "connectionProtocol": "connection_protocol", 
        "deployAction": "deploy_action", 
        "descr": "descr", 
        "dn": "dn", 
        "driveCache": "drive_cache", 
        "driveState": "drive_state", 
        "id": "id", 
        "ioPolicy": "io_policy", 
        "lc": "lc", 
        "locale": "locale", 
        "model": "model", 
        "name": "name", 
        "numberOfBlocks": "number_of_blocks", 
        "operDeviceId": "oper_device_id", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "pnDn": "pn_dn", 
        "presence": "presence", 
        "readPolicy": "read_policy", 
        "refDn": "ref_dn", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "size": "size", 
        "status": "status", 
        "stripSize": "strip_size", 
        "type": "type", 
        "uuid": "uuid", 
        "vendor": "vendor", 
        "vendorUuid": "vendor_uuid", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.access_policy = None
        self.actual_write_cache_policy = None
        self.admin_action_trigger = None
        self.admin_name = None
        self.admin_state = None
        self.available_size = None
        self.block_size = None
        self.bootable = None
        self.change_qualifier = None
        self.child_action = None
        self.config_qualifier_reason = None
        self.config_state = None
        self.configured_write_cache_policy = None
        self.connection_protocol = None
        self.deploy_action = None
        self.descr = None
        self.drive_cache = None
        self.drive_state = None
        self.io_policy = None
        self.lc = None
        self.locale = None
        self.model = None
        self.name = None
        self.number_of_blocks = None
        self.oper_device_id = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.pn_dn = None
        self.presence = None
        self.read_policy = None
        self.ref_dn = None
        self.revision = None
        self.serial = None
        self.size = None
        self.status = None
        self.strip_size = None
        self.type = None
        self.uuid = None
        self.vendor = None
        self.vendor_uuid = None

        ManagedObject.__init__(self, "StorageVirtualDrive", parent_mo_or_dn, **kwargs)

