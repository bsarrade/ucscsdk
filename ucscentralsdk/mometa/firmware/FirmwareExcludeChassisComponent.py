"""This module contains the general information for FirmwareExcludeChassisComponent ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class FirmwareExcludeChassisComponentConsts():
    CHASSIS_COMPONENT_CHASSIS_BOARD_CONTROLLER = "chassis-board-controller"
    CHASSIS_COMPONENT_CMC = "cmc"
    CHASSIS_COMPONENT_IOCARD = "iocard"
    CHASSIS_COMPONENT_LOCAL_DISK = "local-disk"
    CHASSIS_COMPONENT_SAS_EXPANDER = "sas-expander"
    CHASSIS_COMPONENT_STORAGE_CONTROLLER = "storage-controller"
    CHASSIS_COMPONENT_UNSPECIFIED = "unspecified"


class FirmwareExcludeChassisComponent(ManagedObject):
    """This is FirmwareExcludeChassisComponent class."""

    consts = FirmwareExcludeChassisComponentConsts()
    naming_props = set([u'chassisComponent'])

    mo_meta = MoMeta("FirmwareExcludeChassisComponent", "firmwareExcludeChassisComponent", "exclude-chassis-component-[chassis_component]", None, "InputOutput", 0x1f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [u'firmwareChassisPack'], [], [None])

    prop_meta = {
        "chassis_component": MoPropertyMeta("chassis_component", "chassisComponent", "string", None, MoPropertyMeta.NAMING, 0x2, None, None, None, ["chassis-board-controller", "cmc", "iocard", "local-disk", "sas-expander", "storage-controller", "unspecified"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "chassisComponent": "chassis_component", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, chassis_component, **kwargs):
        self._dirty_mask = 0
        self.chassis_component = chassis_component
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareExcludeChassisComponent", parent_mo_or_dn, **kwargs)

