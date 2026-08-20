---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/TWAIN.html
archived_at: '2026-07-18T02:51:40.464717Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# TWAIN Changes for Swift

### TWAIN

Removed TW_CALLBACK.init(CallBackProc: TW_MEMREF, RefCon: TW_MEMREF, Message: TW_INT16)Removed TW_CAPABILITY.init(Cap: TW_UINT16, ConType: TW_UINT16, hContainer: TW_HANDLE)Removed TW_CUSTOMDSDATA.init(InfoLength: TW_UINT32, hData: TW_HANDLE)Removed TW_EVENT.init(pEvent: TW_MEMREF, TWMessage: TW_UINT16)Removed TW_FILESYSTEM.init(InputName: TW_STR255, OutputName: TW_STR255, Context: TW_MEMREF, Recursive: Int32, FileType: TW_INT32, Size: TW_UINT32, CreateTimeDate: TW_STR32, ModifiedTimeDate: TW_STR32, FreeSpace: TW_UINT32, NewImageSize: TW_INT32, NumberOfFiles: TW_UINT32, NumberOfSnippets: TW_UINT32, DeviceGroupMask: TW_UINT32, Reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Removed TW_IDENTITY.init(Id: TW_MEMREF, Version: TW_VERSION, ProtocolMajor: TW_UINT16, ProtocolMinor: TW_UINT16, SupportedGroups: TW_UINT32, Manufacturer: TW_STR32, ProductFamily: TW_STR32, ProductName: TW_STR32)Removed TW_MEMORY.init(Flags: TW_UINT32, Length: TW_UINT32, TheMem: TW_MEMREF)Removed TW_PASSTHRU.init(pCommand: TW_MEMREF, CommandBytes: TW_UINT32, Direction: TW_INT32, pData: TW_MEMREF, DataBytes: TW_UINT32, DataBytesXfered: TW_UINT32)Removed TW_SETUPFILEXFER2.init(FileName: TW_MEMREF, FileNameType: TW_UINT16, Format: TW_UINT16, VRefNum: TW_INT16, ParID: TW_UINT32)Removed TW_USERINTERFACE.init(ShowUI: TW_BOOL, ModalUI: TW_BOOL, hParent: TW_HANDLE)Added TW_CALLBACK.init(CallBackProc: TW_MEMREF!, RefCon: TW_MEMREF!, Message: TW_INT16)Added TW_CAPABILITY.init(Cap: TW_UINT16, ConType: TW_UINT16, hContainer: TW_HANDLE!)Added TW_CUSTOMDSDATA.init(InfoLength: TW_UINT32, hData: TW_HANDLE!)Added TW_EVENT.init(pEvent: TW_MEMREF!, TWMessage: TW_UINT16)Added TW_FILESYSTEM.init(InputName: TWAIN.TW_STR255, OutputName: TWAIN.TW_STR255, Context: TW_MEMREF!, Recursive: Int32, FileType: TW_INT32, Size: TW_UINT32, CreateTimeDate: TWAIN.TW_STR32, ModifiedTimeDate: TWAIN.TW_STR32, FreeSpace: TW_UINT32, NewImageSize: TW_INT32, NumberOfFiles: TW_UINT32, NumberOfSnippets: TW_UINT32, DeviceGroupMask: TW_UINT32, Reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added TW_IDENTITY.init(Id: TW_MEMREF!, Version: TW_VERSION, ProtocolMajor: TW_UINT16, ProtocolMinor: TW_UINT16, SupportedGroups: TW_UINT32, Manufacturer: TWAIN.TW_STR32, ProductFamily: TWAIN.TW_STR32, ProductName: TWAIN.TW_STR32)Added TW_MEMORY.init(Flags: TW_UINT32, Length: TW_UINT32, TheMem: TW_MEMREF!)Added TW_PASSTHRU.init(pCommand: TW_MEMREF!, CommandBytes: TW_UINT32, Direction: TW_INT32, pData: TW_MEMREF!, DataBytes: TW_UINT32, DataBytesXfered: TW_UINT32)Added TW_SETUPFILEXFER2.init(FileName: TW_MEMREF!, FileNameType: TW_UINT16, Format: TW_UINT16, VRefNum: TW_INT16, ParID: TW_UINT32)Added TW_USERINTERFACE.init(ShowUI: TW_BOOL, ModalUI: TW_BOOL, hParent: TW_HANDLE!)Modified TW_AUDIOINFO [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_AUDIOINFO {     var Name: TW_STR255     var Reserved: TW_UINT32     init()     init(Name Name: TW_STR255, Reserved Reserved: TW_UINT32) } ``` |
| To | ``` struct TW_AUDIOINFO {     var Name: TWAIN.TW_STR255     var Reserved: TW_UINT32     init()     init(Name Name: TWAIN.TW_STR255, Reserved Reserved: TW_UINT32) } ``` |

Modified TW_AUDIOINFO.init(Name: TWAIN.TW_STR255, Reserved: TW_UINT32)

|  | Declaration |
| --- | --- |
| From | ``` init(Name Name: TW_STR255, Reserved Reserved: TW_UINT32) ``` |
| To | ``` init(Name Name: TWAIN.TW_STR255, Reserved Reserved: TW_UINT32) ``` |

Modified TW_AUDIOINFO.Name

|  | Declaration |
| --- | --- |
| From | ``` var Name: TW_STR255 ``` |
| To | ``` var Name: TWAIN.TW_STR255 ``` |

Modified TW_CALLBACK [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_CALLBACK {     var CallBackProc: TW_MEMREF     var RefCon: TW_MEMREF     var Message: TW_INT16     init()     init(CallBackProc CallBackProc: TW_MEMREF, RefCon RefCon: TW_MEMREF, Message Message: TW_INT16) } ``` |
| To | ``` struct TW_CALLBACK {     var CallBackProc: TW_MEMREF!     var RefCon: TW_MEMREF!     var Message: TW_INT16     init()     init(CallBackProc CallBackProc: TW_MEMREF!, RefCon RefCon: TW_MEMREF!, Message Message: TW_INT16) } ``` |

Modified TW_CALLBACK.CallBackProc

|  | Declaration |
| --- | --- |
| From | ``` var CallBackProc: TW_MEMREF ``` |
| To | ``` var CallBackProc: TW_MEMREF! ``` |

Modified TW_CALLBACK.RefCon

|  | Declaration |
| --- | --- |
| From | ``` var RefCon: TW_MEMREF ``` |
| To | ``` var RefCon: TW_MEMREF! ``` |

Modified TW_CAPABILITY [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_CAPABILITY {     var Cap: TW_UINT16     var ConType: TW_UINT16     var hContainer: TW_HANDLE     init()     init(Cap Cap: TW_UINT16, ConType ConType: TW_UINT16, hContainer hContainer: TW_HANDLE) } ``` |
| To | ``` struct TW_CAPABILITY {     var Cap: TW_UINT16     var ConType: TW_UINT16     var hContainer: TW_HANDLE!     init()     init(Cap Cap: TW_UINT16, ConType ConType: TW_UINT16, hContainer hContainer: TW_HANDLE!) } ``` |

Modified TW_CAPABILITY.hContainer

|  | Declaration |
| --- | --- |
| From | ``` var hContainer: TW_HANDLE ``` |
| To | ``` var hContainer: TW_HANDLE! ``` |

Modified TW_CUSTOMDSDATA [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_CUSTOMDSDATA {     var InfoLength: TW_UINT32     var hData: TW_HANDLE     init()     init(InfoLength InfoLength: TW_UINT32, hData hData: TW_HANDLE) } ``` |
| To | ``` struct TW_CUSTOMDSDATA {     var InfoLength: TW_UINT32     var hData: TW_HANDLE!     init()     init(InfoLength InfoLength: TW_UINT32, hData hData: TW_HANDLE!) } ``` |

Modified TW_CUSTOMDSDATA.hData

|  | Declaration |
| --- | --- |
| From | ``` var hData: TW_HANDLE ``` |
| To | ``` var hData: TW_HANDLE! ``` |

Modified TW_DEVICEEVENT [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_DEVICEEVENT {     var Event: TW_UINT32     var DeviceName: TW_STR255     var BatteryMinutes: TW_UINT32     var BatteryPercentage: TW_INT16     var PowerSupply: TW_INT32     var XResolution: TW_FIX32     var YResolution: TW_FIX32     var FlashUsed2: TW_UINT32     var AutomaticCapture: TW_UINT32     var TimeBeforeFirstCapture: TW_UINT32     var TimeBetweenCaptures: TW_UINT32     init()     init(Event Event: TW_UINT32, DeviceName DeviceName: TW_STR255, BatteryMinutes BatteryMinutes: TW_UINT32, BatteryPercentage BatteryPercentage: TW_INT16, PowerSupply PowerSupply: TW_INT32, XResolution XResolution: TW_FIX32, YResolution YResolution: TW_FIX32, FlashUsed2 FlashUsed2: TW_UINT32, AutomaticCapture AutomaticCapture: TW_UINT32, TimeBeforeFirstCapture TimeBeforeFirstCapture: TW_UINT32, TimeBetweenCaptures TimeBetweenCaptures: TW_UINT32) } ``` |
| To | ``` struct TW_DEVICEEVENT {     var Event: TW_UINT32     var DeviceName: TWAIN.TW_STR255     var BatteryMinutes: TW_UINT32     var BatteryPercentage: TW_INT16     var PowerSupply: TW_INT32     var XResolution: TW_FIX32     var YResolution: TW_FIX32     var FlashUsed2: TW_UINT32     var AutomaticCapture: TW_UINT32     var TimeBeforeFirstCapture: TW_UINT32     var TimeBetweenCaptures: TW_UINT32     init()     init(Event Event: TW_UINT32, DeviceName DeviceName: TWAIN.TW_STR255, BatteryMinutes BatteryMinutes: TW_UINT32, BatteryPercentage BatteryPercentage: TW_INT16, PowerSupply PowerSupply: TW_INT32, XResolution XResolution: TW_FIX32, YResolution YResolution: TW_FIX32, FlashUsed2 FlashUsed2: TW_UINT32, AutomaticCapture AutomaticCapture: TW_UINT32, TimeBeforeFirstCapture TimeBeforeFirstCapture: TW_UINT32, TimeBetweenCaptures TimeBetweenCaptures: TW_UINT32) } ``` |

Modified TW_DEVICEEVENT.DeviceName

|  | Declaration |
| --- | --- |
| From | ``` var DeviceName: TW_STR255 ``` |
| To | ``` var DeviceName: TWAIN.TW_STR255 ``` |

Modified TW_DEVICEEVENT.init(Event: TW_UINT32, DeviceName: TWAIN.TW_STR255, BatteryMinutes: TW_UINT32, BatteryPercentage: TW_INT16, PowerSupply: TW_INT32, XResolution: TW_FIX32, YResolution: TW_FIX32, FlashUsed2: TW_UINT32, AutomaticCapture: TW_UINT32, TimeBeforeFirstCapture: TW_UINT32, TimeBetweenCaptures: TW_UINT32)

|  | Declaration |
| --- | --- |
| From | ``` init(Event Event: TW_UINT32, DeviceName DeviceName: TW_STR255, BatteryMinutes BatteryMinutes: TW_UINT32, BatteryPercentage BatteryPercentage: TW_INT16, PowerSupply PowerSupply: TW_INT32, XResolution XResolution: TW_FIX32, YResolution YResolution: TW_FIX32, FlashUsed2 FlashUsed2: TW_UINT32, AutomaticCapture AutomaticCapture: TW_UINT32, TimeBeforeFirstCapture TimeBeforeFirstCapture: TW_UINT32, TimeBetweenCaptures TimeBetweenCaptures: TW_UINT32) ``` |
| To | ``` init(Event Event: TW_UINT32, DeviceName DeviceName: TWAIN.TW_STR255, BatteryMinutes BatteryMinutes: TW_UINT32, BatteryPercentage BatteryPercentage: TW_INT16, PowerSupply PowerSupply: TW_INT32, XResolution XResolution: TW_FIX32, YResolution YResolution: TW_FIX32, FlashUsed2 FlashUsed2: TW_UINT32, AutomaticCapture AutomaticCapture: TW_UINT32, TimeBeforeFirstCapture TimeBeforeFirstCapture: TW_UINT32, TimeBetweenCaptures TimeBetweenCaptures: TW_UINT32) ``` |

Modified TW_EVENT [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_EVENT {     var pEvent: TW_MEMREF     var TWMessage: TW_UINT16     init()     init(pEvent pEvent: TW_MEMREF, TWMessage TWMessage: TW_UINT16) } ``` |
| To | ``` struct TW_EVENT {     var pEvent: TW_MEMREF!     var TWMessage: TW_UINT16     init()     init(pEvent pEvent: TW_MEMREF!, TWMessage TWMessage: TW_UINT16) } ``` |

Modified TW_EVENT.pEvent

|  | Declaration |
| --- | --- |
| From | ``` var pEvent: TW_MEMREF ``` |
| To | ``` var pEvent: TW_MEMREF! ``` |

Modified TW_FILESYSTEM [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_FILESYSTEM {     var InputName: TW_STR255     var OutputName: TW_STR255     var Context: TW_MEMREF     var Recursive: Int32     var FileType: TW_INT32     var Size: TW_UINT32     var CreateTimeDate: TW_STR32     var ModifiedTimeDate: TW_STR32     var FreeSpace: TW_UINT32     var NewImageSize: TW_INT32     var NumberOfFiles: TW_UINT32     var NumberOfSnippets: TW_UINT32     var DeviceGroupMask: TW_UINT32     var Reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(InputName InputName: TW_STR255, OutputName OutputName: TW_STR255, Context Context: TW_MEMREF, Recursive Recursive: Int32, FileType FileType: TW_INT32, Size Size: TW_UINT32, CreateTimeDate CreateTimeDate: TW_STR32, ModifiedTimeDate ModifiedTimeDate: TW_STR32, FreeSpace FreeSpace: TW_UINT32, NewImageSize NewImageSize: TW_INT32, NumberOfFiles NumberOfFiles: TW_UINT32, NumberOfSnippets NumberOfSnippets: TW_UINT32, DeviceGroupMask DeviceGroupMask: TW_UINT32, Reserved Reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |
| To | ``` struct TW_FILESYSTEM {     var InputName: TWAIN.TW_STR255     var OutputName: TWAIN.TW_STR255     var Context: TW_MEMREF!     var Recursive: Int32     var FileType: TW_INT32     var Size: TW_UINT32     var CreateTimeDate: TWAIN.TW_STR32     var ModifiedTimeDate: TWAIN.TW_STR32     var FreeSpace: TW_UINT32     var NewImageSize: TW_INT32     var NumberOfFiles: TW_UINT32     var NumberOfSnippets: TW_UINT32     var DeviceGroupMask: TW_UINT32     var Reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(InputName InputName: TWAIN.TW_STR255, OutputName OutputName: TWAIN.TW_STR255, Context Context: TW_MEMREF!, Recursive Recursive: Int32, FileType FileType: TW_INT32, Size Size: TW_UINT32, CreateTimeDate CreateTimeDate: TWAIN.TW_STR32, ModifiedTimeDate ModifiedTimeDate: TWAIN.TW_STR32, FreeSpace FreeSpace: TW_UINT32, NewImageSize NewImageSize: TW_INT32, NumberOfFiles NumberOfFiles: TW_UINT32, NumberOfSnippets NumberOfSnippets: TW_UINT32, DeviceGroupMask DeviceGroupMask: TW_UINT32, Reserved Reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified TW_FILESYSTEM.Context

|  | Declaration |
| --- | --- |
| From | ``` var Context: TW_MEMREF ``` |
| To | ``` var Context: TW_MEMREF! ``` |

Modified TW_FILESYSTEM.CreateTimeDate

|  | Declaration |
| --- | --- |
| From | ``` var CreateTimeDate: TW_STR32 ``` |
| To | ``` var CreateTimeDate: TWAIN.TW_STR32 ``` |

Modified TW_FILESYSTEM.InputName

|  | Declaration |
| --- | --- |
| From | ``` var InputName: TW_STR255 ``` |
| To | ``` var InputName: TWAIN.TW_STR255 ``` |

Modified TW_FILESYSTEM.ModifiedTimeDate

|  | Declaration |
| --- | --- |
| From | ``` var ModifiedTimeDate: TW_STR32 ``` |
| To | ``` var ModifiedTimeDate: TWAIN.TW_STR32 ``` |

Modified TW_FILESYSTEM.OutputName

|  | Declaration |
| --- | --- |
| From | ``` var OutputName: TW_STR255 ``` |
| To | ``` var OutputName: TWAIN.TW_STR255 ``` |

Modified TW_IDENTITY [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_IDENTITY {     var Id: TW_MEMREF     var Version: TW_VERSION     var ProtocolMajor: TW_UINT16     var ProtocolMinor: TW_UINT16     var SupportedGroups: TW_UINT32     var Manufacturer: TW_STR32     var ProductFamily: TW_STR32     var ProductName: TW_STR32     init()     init(Id Id: TW_MEMREF, Version Version: TW_VERSION, ProtocolMajor ProtocolMajor: TW_UINT16, ProtocolMinor ProtocolMinor: TW_UINT16, SupportedGroups SupportedGroups: TW_UINT32, Manufacturer Manufacturer: TW_STR32, ProductFamily ProductFamily: TW_STR32, ProductName ProductName: TW_STR32) } ``` |
| To | ``` struct TW_IDENTITY {     var Id: TW_MEMREF!     var Version: TW_VERSION     var ProtocolMajor: TW_UINT16     var ProtocolMinor: TW_UINT16     var SupportedGroups: TW_UINT32     var Manufacturer: TWAIN.TW_STR32     var ProductFamily: TWAIN.TW_STR32     var ProductName: TWAIN.TW_STR32     init()     init(Id Id: TW_MEMREF!, Version Version: TW_VERSION, ProtocolMajor ProtocolMajor: TW_UINT16, ProtocolMinor ProtocolMinor: TW_UINT16, SupportedGroups SupportedGroups: TW_UINT32, Manufacturer Manufacturer: TWAIN.TW_STR32, ProductFamily ProductFamily: TWAIN.TW_STR32, ProductName ProductName: TWAIN.TW_STR32) } ``` |

Modified TW_IDENTITY.Id

|  | Declaration |
| --- | --- |
| From | ``` var Id: TW_MEMREF ``` |
| To | ``` var Id: TW_MEMREF! ``` |

Modified TW_IDENTITY.Manufacturer

|  | Declaration |
| --- | --- |
| From | ``` var Manufacturer: TW_STR32 ``` |
| To | ``` var Manufacturer: TWAIN.TW_STR32 ``` |

Modified TW_IDENTITY.ProductFamily

|  | Declaration |
| --- | --- |
| From | ``` var ProductFamily: TW_STR32 ``` |
| To | ``` var ProductFamily: TWAIN.TW_STR32 ``` |

Modified TW_IDENTITY.ProductName

|  | Declaration |
| --- | --- |
| From | ``` var ProductName: TW_STR32 ``` |
| To | ``` var ProductName: TWAIN.TW_STR32 ``` |

Modified TW_MEMORY [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_MEMORY {     var Flags: TW_UINT32     var Length: TW_UINT32     var TheMem: TW_MEMREF     init()     init(Flags Flags: TW_UINT32, Length Length: TW_UINT32, TheMem TheMem: TW_MEMREF) } ``` |
| To | ``` struct TW_MEMORY {     var Flags: TW_UINT32     var Length: TW_UINT32     var TheMem: TW_MEMREF!     init()     init(Flags Flags: TW_UINT32, Length Length: TW_UINT32, TheMem TheMem: TW_MEMREF!) } ``` |

Modified TW_MEMORY.TheMem

|  | Declaration |
| --- | --- |
| From | ``` var TheMem: TW_MEMREF ``` |
| To | ``` var TheMem: TW_MEMREF! ``` |

Modified TW_PASSTHRU [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_PASSTHRU {     var pCommand: TW_MEMREF     var CommandBytes: TW_UINT32     var Direction: TW_INT32     var pData: TW_MEMREF     var DataBytes: TW_UINT32     var DataBytesXfered: TW_UINT32     init()     init(pCommand pCommand: TW_MEMREF, CommandBytes CommandBytes: TW_UINT32, Direction Direction: TW_INT32, pData pData: TW_MEMREF, DataBytes DataBytes: TW_UINT32, DataBytesXfered DataBytesXfered: TW_UINT32) } ``` |
| To | ``` struct TW_PASSTHRU {     var pCommand: TW_MEMREF!     var CommandBytes: TW_UINT32     var Direction: TW_INT32     var pData: TW_MEMREF!     var DataBytes: TW_UINT32     var DataBytesXfered: TW_UINT32     init()     init(pCommand pCommand: TW_MEMREF!, CommandBytes CommandBytes: TW_UINT32, Direction Direction: TW_INT32, pData pData: TW_MEMREF!, DataBytes DataBytes: TW_UINT32, DataBytesXfered DataBytesXfered: TW_UINT32) } ``` |

Modified TW_PASSTHRU.pCommand

|  | Declaration |
| --- | --- |
| From | ``` var pCommand: TW_MEMREF ``` |
| To | ``` var pCommand: TW_MEMREF! ``` |

Modified TW_PASSTHRU.pData

|  | Declaration |
| --- | --- |
| From | ``` var pData: TW_MEMREF ``` |
| To | ``` var pData: TW_MEMREF! ``` |

Modified TW_SETUPAUDIOFILEXFER [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_SETUPAUDIOFILEXFER {     var FileName: TW_STR255     var Format: TW_UINT16     var VRefNum: TW_INT16     init()     init(FileName FileName: TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) } ``` |
| To | ``` struct TW_SETUPAUDIOFILEXFER {     var FileName: TWAIN.TW_STR255     var Format: TW_UINT16     var VRefNum: TW_INT16     init()     init(FileName FileName: TWAIN.TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) } ``` |

Modified TW_SETUPAUDIOFILEXFER.FileName

|  | Declaration |
| --- | --- |
| From | ``` var FileName: TW_STR255 ``` |
| To | ``` var FileName: TWAIN.TW_STR255 ``` |

Modified TW_SETUPAUDIOFILEXFER.init(FileName: TWAIN.TW_STR255, Format: TW_UINT16, VRefNum: TW_INT16)

|  | Declaration |
| --- | --- |
| From | ``` init(FileName FileName: TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) ``` |
| To | ``` init(FileName FileName: TWAIN.TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) ``` |

Modified TW_SETUPFILEXFER [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_SETUPFILEXFER {     var FileName: TW_STR255     var Format: TW_UINT16     var VRefNum: TW_INT16     init()     init(FileName FileName: TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) } ``` |
| To | ``` struct TW_SETUPFILEXFER {     var FileName: TWAIN.TW_STR255     var Format: TW_UINT16     var VRefNum: TW_INT16     init()     init(FileName FileName: TWAIN.TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) } ``` |

Modified TW_SETUPFILEXFER.FileName

|  | Declaration |
| --- | --- |
| From | ``` var FileName: TW_STR255 ``` |
| To | ``` var FileName: TWAIN.TW_STR255 ``` |

Modified TW_SETUPFILEXFER.init(FileName: TWAIN.TW_STR255, Format: TW_UINT16, VRefNum: TW_INT16)

|  | Declaration |
| --- | --- |
| From | ``` init(FileName FileName: TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) ``` |
| To | ``` init(FileName FileName: TWAIN.TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) ``` |

Modified TW_SETUPFILEXFER2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_SETUPFILEXFER2 {     var FileName: TW_MEMREF     var FileNameType: TW_UINT16     var Format: TW_UINT16     var VRefNum: TW_INT16     var ParID: TW_UINT32     init()     init(FileName FileName: TW_MEMREF, FileNameType FileNameType: TW_UINT16, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16, ParID ParID: TW_UINT32) } ``` |
| To | ``` struct TW_SETUPFILEXFER2 {     var FileName: TW_MEMREF!     var FileNameType: TW_UINT16     var Format: TW_UINT16     var VRefNum: TW_INT16     var ParID: TW_UINT32     init()     init(FileName FileName: TW_MEMREF!, FileNameType FileNameType: TW_UINT16, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16, ParID ParID: TW_UINT32) } ``` |

Modified TW_SETUPFILEXFER2.FileName

|  | Declaration |
| --- | --- |
| From | ``` var FileName: TW_MEMREF ``` |
| To | ``` var FileName: TW_MEMREF! ``` |

Modified TW_TWUNKIDENTITY [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_TWUNKIDENTITY {     var identity: TW_IDENTITY     var dsPath: TW_STR255     init()     init(identity identity: TW_IDENTITY, dsPath dsPath: TW_STR255) } ``` |
| To | ``` struct TW_TWUNKIDENTITY {     var identity: TW_IDENTITY     var dsPath: TWAIN.TW_STR255     init()     init(identity identity: TW_IDENTITY, dsPath dsPath: TWAIN.TW_STR255) } ``` |

Modified TW_TWUNKIDENTITY.dsPath

|  | Declaration |
| --- | --- |
| From | ``` var dsPath: TW_STR255 ``` |
| To | ``` var dsPath: TWAIN.TW_STR255 ``` |

Modified TW_TWUNKIDENTITY.init(identity: TW_IDENTITY, dsPath: TWAIN.TW_STR255)

|  | Declaration |
| --- | --- |
| From | ``` init(identity identity: TW_IDENTITY, dsPath dsPath: TW_STR255) ``` |
| To | ``` init(identity identity: TW_IDENTITY, dsPath dsPath: TWAIN.TW_STR255) ``` |

Modified TW_USERINTERFACE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_USERINTERFACE {     var ShowUI: TW_BOOL     var ModalUI: TW_BOOL     var hParent: TW_HANDLE     init()     init(ShowUI ShowUI: TW_BOOL, ModalUI ModalUI: TW_BOOL, hParent hParent: TW_HANDLE) } ``` |
| To | ``` struct TW_USERINTERFACE {     var ShowUI: TW_BOOL     var ModalUI: TW_BOOL     var hParent: TW_HANDLE!     init()     init(ShowUI ShowUI: TW_BOOL, ModalUI ModalUI: TW_BOOL, hParent hParent: TW_HANDLE!) } ``` |

Modified TW_USERINTERFACE.hParent

|  | Declaration |
| --- | --- |
| From | ``` var hParent: TW_HANDLE ``` |
| To | ``` var hParent: TW_HANDLE! ``` |

Modified TW_VERSION [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_VERSION {     var MajorNum: TW_UINT16     var MinorNum: TW_UINT16     var Language: TW_UINT16     var Country: TW_UINT16     var Info: TW_STR32     init()     init(MajorNum MajorNum: TW_UINT16, MinorNum MinorNum: TW_UINT16, Language Language: TW_UINT16, Country Country: TW_UINT16, Info Info: TW_STR32) } ``` |
| To | ``` struct TW_VERSION {     var MajorNum: TW_UINT16     var MinorNum: TW_UINT16     var Language: TW_UINT16     var Country: TW_UINT16     var Info: TWAIN.TW_STR32     init()     init(MajorNum MajorNum: TW_UINT16, MinorNum MinorNum: TW_UINT16, Language Language: TW_UINT16, Country Country: TW_UINT16, Info Info: TWAIN.TW_STR32) } ``` |

Modified TW_VERSION.Info

|  | Declaration |
| --- | --- |
| From | ``` var Info: TW_STR32 ``` |
| To | ``` var Info: TWAIN.TW_STR32 ``` |

Modified TW_VERSION.init(MajorNum: TW_UINT16, MinorNum: TW_UINT16, Language: TW_UINT16, Country: TW_UINT16, Info: TWAIN.TW_STR32)

|  | Declaration |
| --- | --- |
| From | ``` init(MajorNum MajorNum: TW_UINT16, MinorNum MinorNum: TW_UINT16, Language Language: TW_UINT16, Country Country: TW_UINT16, Info Info: TW_STR32) ``` |
| To | ``` init(MajorNum MajorNum: TW_UINT16, MinorNum MinorNum: TW_UINT16, Language Language: TW_UINT16, Country Country: TW_UINT16, Info Info: TWAIN.TW_STR32) ``` |

Modified DS_Entry(_: pTW_IDENTITY!, _: TW_UINT32, _: TW_UINT16, _: TW_UINT16, _: TW_MEMREF!) -> TW_UINT16

|  | Declaration |
| --- | --- |
| From | ``` func DS_Entry(_ pOrigin: pTW_IDENTITY, _ DG: TW_UINT32, _ DAT: TW_UINT16, _ MSG: TW_UINT16, _ pData: TW_MEMREF) -> TW_UINT16 ``` |
| To | ``` func DS_Entry(_ pOrigin: pTW_IDENTITY!, _ DG: TW_UINT32, _ DAT: TW_UINT16, _ MSG: TW_UINT16, _ pData: TW_MEMREF!) -> TW_UINT16 ``` |

Modified DSENTRYPROC

|  | Declaration |
| --- | --- |
| From | ``` typealias DSENTRYPROC = (pTW_IDENTITY, TW_UINT32, TW_UINT16, TW_UINT16, TW_MEMREF) -> TW_UINT16 ``` |
| To | ``` typealias DSENTRYPROC = (pTW_IDENTITY?, TW_UINT32, TW_UINT16, TW_UINT16, TW_MEMREF?) -> TW_UINT16 ``` |

Modified DSM_Entry(_: pTW_IDENTITY!, _: pTW_IDENTITY!, _: TW_UINT32, _: TW_UINT16, _: TW_UINT16, _: TW_MEMREF!) -> TW_UINT16

|  | Declaration |
| --- | --- |
| From | ``` func DSM_Entry(_ pOrigin: pTW_IDENTITY, _ pDest: pTW_IDENTITY, _ DG: TW_UINT32, _ DAT: TW_UINT16, _ MSG: TW_UINT16, _ pData: TW_MEMREF) -> TW_UINT16 ``` |
| To | ``` func DSM_Entry(_ pOrigin: pTW_IDENTITY!, _ pDest: pTW_IDENTITY!, _ DG: TW_UINT32, _ DAT: TW_UINT16, _ MSG: TW_UINT16, _ pData: TW_MEMREF!) -> TW_UINT16 ``` |

Modified DSMENTRYPROC

|  | Declaration |
| --- | --- |
| From | ``` typealias DSMENTRYPROC = (pTW_IDENTITY, pTW_IDENTITY, TW_UINT32, TW_UINT16, TW_UINT16, TW_MEMREF) -> TW_UINT16 ``` |
| To | ``` typealias DSMENTRYPROC = (pTW_IDENTITY?, pTW_IDENTITY?, TW_UINT32, TW_UINT16, TW_UINT16, TW_MEMREF?) -> TW_UINT16 ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
