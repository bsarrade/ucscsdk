"""This module contains the general information for HcCatalogSource ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class HcCatalogSourceConsts():
    LAST_DOWNLOAD_NEVER = "never"
    TRIGGER_STATE_NONE = "none"
    TRIGGER_STATE_TRIGGER_DELETE = "trigger-delete"
    TRIGGER_STATE_TRIGGER_DOWNLOAD = "trigger-download"
    TYPE_CISCO = "Cisco"
    TYPE_LOCAL = "local"


class HcCatalogSource(ManagedObject):
    """This is HcCatalogSource class."""

    consts = HcCatalogSourceConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("HcCatalogSource", "hcCatalogSource", "catalog-source-[type]", None, "InputOutput", 0x3f, [], ["admin"], [u'hcCatalogList'], [u'hcDownloadPolicy'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "download_error": MoPropertyMeta("download_error", "downloadError", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "last_download": MoPropertyMeta("last_download", "lastDownload", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_state": MoPropertyMeta("trigger_state", "triggerState", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["none", "trigger-delete", "trigger-download"], []), 
        "type": MoPropertyMeta("type", "type", "string", None, MoPropertyMeta.NAMING, 0x20, None, None, None, ["Cisco", "local"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "downloadError": "download_error", 
        "lastDownload": "last_download", 
        "rn": "rn", 
        "status": "status", 
        "triggerState": "trigger_state", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.download_error = None
        self.last_download = None
        self.status = None
        self.trigger_state = None

        ManagedObject.__init__(self, "HcCatalogSource", parent_mo_or_dn, **kwargs)

