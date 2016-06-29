"""This module contains the general information for BiosVfSerialPortAEnable ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class BiosVfSerialPortAEnableConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_SERIAL_PORT_AENABLE_DISABLED = "disabled"
    VP_SERIAL_PORT_AENABLE_ENABLED = "enabled"
    VP_SERIAL_PORT_AENABLE_PLATFORM_DEFAULT = "platform-default"
    VP_SERIAL_PORT_AENABLE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfSerialPortAEnable(ManagedObject):
    """This is BiosVfSerialPortAEnable class."""

    consts = BiosVfSerialPortAEnableConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfSerialPortAEnable", "biosVfSerialPortAEnable", "Serial-port-A-enable", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], [u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_serial_port_a_enable": MoPropertyMeta("vp_serial_port_a_enable", "vpSerialPortAEnable", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpSerialPortAEnable": "vp_serial_port_a_enable", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_serial_port_a_enable = None

        ManagedObject.__init__(self, "BiosVfSerialPortAEnable", parent_mo_or_dn, **kwargs)

