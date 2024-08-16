# pip install wmi
from wmi import WMI

def ideviceid():
    for device in WMI().Win32_PnPEntity(ConfigManagerErrorCode=0):
        if 'Apple' in str(device.Caption):
            DeviceHardwareID  = device.HardwareID[-1].split("&")
            DeviceVID = DeviceHardwareID[0].split("_")[-1]
            DevicePID = DeviceHardwareID[1].split("_")[-1]

            return DeviceVID, DevicePID
        
    return 0, 0

def idevicegetstate(): # -1=none 0=normal, 1=recovery, 2=dfu, 3=pwndfu
    DeviceVID, DevicePID = ideviceid()
    DeviceVID = int(f"0x{DeviceVID}", 16)
    DevicePID = int(f"0x{DevicePID}", 16)

    print("iDevice: VID =", str(hex(DeviceVID)).upper().replace("X", "x"), "PID =", hex(DevicePID))

    if DevicePID == 0x12a8: # Normal Mode
        print("iDevice in Normal Mode")
        return 0
    elif DevicePID == 0x1281: # Recovery Mode
        print("iDevice in Recovery Mode")
        return 1
    elif DevicePID == 0x1227: # DFU Mode
        print("iDevice in DFU Mode")
        return 2
    
    print("iDevice not Connected")
    return -1
