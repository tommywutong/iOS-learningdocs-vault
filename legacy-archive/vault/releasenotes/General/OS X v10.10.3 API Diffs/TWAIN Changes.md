---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/TWAIN.html
archived_at: '2026-07-18T02:52:42.964990Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# TWAIN Changes

## TWAIN

Added TW_ARRAY.init()Added TW_ARRAY.init(ItemType: TW_UINT16, NumItems: TW_UINT32, ItemList:(TW_UINT8))Added TW_AUDIOINFO.init()Added TW_AUDIOINFO.init(Name: TW_STR255, Reserved: TW_UINT32)Added TW_CALLBACK.init()Added TW_CALLBACK.init(CallBackProc: TW_MEMREF, RefCon: TW_MEMREF, Message: TW_INT16)Added TW_CAPABILITY.init()Added TW_CAPABILITY.init(Cap: TW_UINT16, ConType: TW_UINT16, hContainer: TW_HANDLE)Added TW_CAPEXT.init()Added TW_CAPEXT.init(Cap: TW_UINT16, Properties: TW_UINT16)Added TW_CIECOLOR.init()Added TW_CIECOLOR.init(ColorSpace: TW_UINT16, LowEndian: TW_INT16, DeviceDependent: TW_INT16, VersionNumber: TW_INT32, StageABC: TW_TRANSFORMSTAGE, StageLMN: TW_TRANSFORMSTAGE, WhitePoint: TW_CIEPOINT, BlackPoint: TW_CIEPOINT, WhitePaper: TW_CIEPOINT, BlackInk: TW_CIEPOINT, Samples:(TW_FIX32))Added TW_CIEPOINT.init()Added TW_CIEPOINT.init(X: TW_FIX32, Y: TW_FIX32, Z: TW_FIX32)Added TW_CUSTOMDSDATA.init()Added TW_CUSTOMDSDATA.init(InfoLength: TW_UINT32, hData: TW_HANDLE)Added TW_DECODEFUNCTION.init()Added TW_DECODEFUNCTION.init(StartIn: TW_FIX32, BreakIn: TW_FIX32, EndIn: TW_FIX32, StartOut: TW_FIX32, BreakOut: TW_FIX32, EndOut: TW_FIX32, Gamma: TW_FIX32, SampleCount: TW_FIX32)Added TW_DEVICEEVENT.init()Added TW_DEVICEEVENT.init(Event: TW_UINT32, DeviceName: TW_STR255, BatteryMinutes: TW_UINT32, BatteryPercentage: TW_INT16, PowerSupply: TW_INT32, XResolution: TW_FIX32, YResolution: TW_FIX32, FlashUsed2: TW_UINT32, AutomaticCapture: TW_UINT32, TimeBeforeFirstCapture: TW_UINT32, TimeBetweenCaptures: TW_UINT32)Added TW_ELEMENT8.init()Added TW_ELEMENT8.init(Index: TW_UINT8, Channel1: TW_UINT8, Channel2: TW_UINT8, Channel3: TW_UINT8)Added TW_ENUMERATION.init()Added TW_ENUMERATION.init(ItemType: TW_UINT16, NumItems: TW_UINT32, CurrentIndex: TW_UINT32, DefaultIndex: TW_UINT32, ItemList:(TW_UINT8))Added TW_EVENT.init()Added TW_EVENT.init(pEvent: TW_MEMREF, TWMessage: TW_UINT16)Added TW_EXTIMAGEINFO.init()Added TW_EXTIMAGEINFO.init(NumInfos: TW_UINT32, Info:(TW_INFO))Added TW_FILESYSTEM.init()Added TW_FILESYSTEM.init(InputName: TW_STR255, OutputName: TW_STR255, Context: TW_MEMREF, Recursive: Int32, FileType: TW_INT32, Size: TW_UINT32, CreateTimeDate: TW_STR32, ModifiedTimeDate: TW_STR32, FreeSpace: TW_UINT32, NewImageSize: TW_INT32, NumberOfFiles: TW_UINT32, NumberOfSnippets: TW_UINT32, DeviceGroupMask: TW_UINT32, Reserved:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added TW_FIX32.init()Added TW_FIX32.init(Whole: TW_INT16, Frac: TW_UINT16)Added TW_FRAME.init()Added TW_FRAME.init(Left: TW_FIX32, Top: TW_FIX32, Right: TW_FIX32, Bottom: TW_FIX32)Added TW_GRAYRESPONSE.init()Added TW_GRAYRESPONSE.init(Response: (TW_ELEMENT8))Added TW_IDENTITY.init()Added TW_IDENTITY.init(Id: TW_MEMREF, Version: TW_VERSION, ProtocolMajor: TW_UINT16, ProtocolMinor: TW_UINT16, SupportedGroups: TW_UINT32, Manufacturer: TW_STR32, ProductFamily: TW_STR32, ProductName: TW_STR32)Added TW_IMAGEINFO.init()Added TW_IMAGEINFO.init(XResolution: TW_FIX32, YResolution: TW_FIX32, ImageWidth: TW_INT32, ImageLength: TW_INT32, SamplesPerPixel: TW_INT16, BitsPerSample:(TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16), BitsPerPixel: TW_INT16, Planar: TW_BOOL, PixelType: TW_INT16, Compression: TW_UINT16)Added TW_IMAGELAYOUT.init()Added TW_IMAGELAYOUT.init(Frame: TW_FRAME, DocumentNumber: TW_UINT32, PageNumber: TW_UINT32, FrameNumber: TW_UINT32)Added TW_IMAGEMEMXFER.init()Added TW_IMAGEMEMXFER.init(Compression: TW_UINT16, BytesPerRow: TW_UINT32, Columns: TW_UINT32, Rows: TW_UINT32, XOffset: TW_UINT32, YOffset: TW_UINT32, BytesWritten: TW_UINT32, Memory: TW_MEMORY)Added TW_INFO.init()Added TW_INFO.init(InfoID: TW_UINT16, ItemType: TW_UINT16, NumItems: TW_UINT16, CondCode: TW_UINT16, Item: TW_UINT32)Added TW_JPEGCOMPRESSION.init()Added TW_JPEGCOMPRESSION.init(ColorSpace: TW_UINT16, SubSampling: TW_UINT32, NumComponents: TW_UINT16, RestartFrequency: TW_UINT16, QuantMap:(TW_UINT16, TW_UINT16, TW_UINT16, TW_UINT16), QuantTable:(TW_MEMORY, TW_MEMORY, TW_MEMORY, TW_MEMORY), HuffmanMap:(TW_UINT16, TW_UINT16, TW_UINT16, TW_UINT16), HuffmanDC:(TW_MEMORY, TW_MEMORY), HuffmanAC:(TW_MEMORY, TW_MEMORY))Added TW_MEMORY.init()Added TW_MEMORY.init(Flags: TW_UINT32, Length: TW_UINT32, TheMem: TW_MEMREF)Added TW_ONEVALUE.init()Added TW_ONEVALUE.init(ItemType: TW_UINT16, Item: TW_UINT32)Added TW_PALETTE8.init()Added TW_PALETTE8.init(NumColors: TW_UINT16, PaletteType: TW_UINT16, Colors:(TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8))Added TW_PASSTHRU.init()Added TW_PASSTHRU.init(pCommand: TW_MEMREF, CommandBytes: TW_UINT32, Direction: TW_INT32, pData: TW_MEMREF, DataBytes: TW_UINT32, DataBytesXfered: TW_UINT32)Added TW_PENDINGXFERS.init()Added TW_RANGE.init()Added TW_RANGE.init(ItemType: TW_UINT16, MinValue: TW_UINT32, MaxValue: TW_UINT32, StepSize: TW_UINT32, DefaultValue: TW_UINT32, CurrentValue: TW_UINT32)Added TW_RGBRESPONSE.init()Added TW_RGBRESPONSE.init(Response: (TW_ELEMENT8))Added TW_SETUPAUDIOFILEXFER.init()Added TW_SETUPAUDIOFILEXFER.init(FileName: TW_STR255, Format: TW_UINT16, VRefNum: TW_INT16)Added TW_SETUPFILEXFER.init()Added TW_SETUPFILEXFER.init(FileName: TW_STR255, Format: TW_UINT16, VRefNum: TW_INT16)Added TW_SETUPFILEXFER2.init()Added TW_SETUPFILEXFER2.init(FileName: TW_MEMREF, FileNameType: TW_UINT16, Format: TW_UINT16, VRefNum: TW_INT16, ParID: TW_UINT32)Added TW_SETUPMEMXFER.init()Added TW_SETUPMEMXFER.init(MinBufSize: TW_UINT32, MaxBufSize: TW_UINT32, Preferred: TW_UINT32)Added TW_STATUS.init()Added TW_STATUS.init(ConditionCode: TW_UINT16, Reserved: TW_UINT16)Added TW_TRANSFORMSTAGE.init()Added TW_TRANSFORMSTAGE.init(Decode: (TW_DECODEFUNCTION, TW_DECODEFUNCTION, TW_DECODEFUNCTION), Mix:((TW_FIX32, TW_FIX32, TW_FIX32),(TW_FIX32, TW_FIX32, TW_FIX32),(TW_FIX32, TW_FIX32, TW_FIX32)))Added TW_TWUNKDSENTRYPARAMS.init()Added TW_TWUNKDSENTRYPARAMS.init(destFlag: TW_INT8, dest: TW_IDENTITY, dataGroup: TW_INT32, dataArgType: TW_INT16, message: TW_INT16, pDataSize: TW_INT32)Added TW_TWUNKDSENTRYRETURN.init()Added TW_TWUNKDSENTRYRETURN.init(returnCode: TW_UINT16, conditionCode: TW_UINT16, pDataSize: TW_INT32)Added TW_TWUNKIDENTITY.init()Added TW_TWUNKIDENTITY.init(identity: TW_IDENTITY, dsPath: TW_STR255)Added TW_USERINTERFACE.init()Added TW_USERINTERFACE.init(ShowUI: TW_BOOL, ModalUI: TW_BOOL, hParent: TW_HANDLE)Added TW_VERSION.init()Added TW_VERSION.init(MajorNum: TW_UINT16, MinorNum: TW_UINT16, Language: TW_UINT16, Country: TW_UINT16, Info: TW_STR32)Modified TW_ARRAY [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_ARRAY {     var ItemType: TW_UINT16     var NumItems: TW_UINT32     var ItemList: (TW_UINT8) } ``` |
| To | ``` struct TW_ARRAY {     var ItemType: TW_UINT16     var NumItems: TW_UINT32     var ItemList: (TW_UINT8)     init()     init(ItemType ItemType: TW_UINT16, NumItems NumItems: TW_UINT32, ItemList ItemList: (TW_UINT8)) } ``` |

Modified TW_AUDIOINFO [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_AUDIOINFO {     var Name: TW_STR255     var Reserved: TW_UINT32 } ``` |
| To | ``` struct TW_AUDIOINFO {     var Name: TW_STR255     var Reserved: TW_UINT32     init()     init(Name Name: TW_STR255, Reserved Reserved: TW_UINT32) } ``` |

Modified TW_CALLBACK [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_CALLBACK {     var CallBackProc: TW_MEMREF     var RefCon: TW_MEMREF     var Message: TW_INT16 } ``` |
| To | ``` struct TW_CALLBACK {     var CallBackProc: TW_MEMREF     var RefCon: TW_MEMREF     var Message: TW_INT16     init()     init(CallBackProc CallBackProc: TW_MEMREF, RefCon RefCon: TW_MEMREF, Message Message: TW_INT16) } ``` |

Modified TW_CAPABILITY [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_CAPABILITY {     var Cap: TW_UINT16     var ConType: TW_UINT16     var hContainer: TW_HANDLE } ``` |
| To | ``` struct TW_CAPABILITY {     var Cap: TW_UINT16     var ConType: TW_UINT16     var hContainer: TW_HANDLE     init()     init(Cap Cap: TW_UINT16, ConType ConType: TW_UINT16, hContainer hContainer: TW_HANDLE) } ``` |

Modified TW_CAPEXT [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_CAPEXT {     var Cap: TW_UINT16     var Properties: TW_UINT16 } ``` |
| To | ``` struct TW_CAPEXT {     var Cap: TW_UINT16     var Properties: TW_UINT16     init()     init(Cap Cap: TW_UINT16, Properties Properties: TW_UINT16) } ``` |

Modified TW_CIECOLOR [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_CIECOLOR {     var ColorSpace: TW_UINT16     var LowEndian: TW_INT16     var DeviceDependent: TW_INT16     var VersionNumber: TW_INT32     var StageABC: TW_TRANSFORMSTAGE     var StageLMN: TW_TRANSFORMSTAGE     var WhitePoint: TW_CIEPOINT     var BlackPoint: TW_CIEPOINT     var WhitePaper: TW_CIEPOINT     var BlackInk: TW_CIEPOINT     var Samples: (TW_FIX32) } ``` |
| To | ``` struct TW_CIECOLOR {     var ColorSpace: TW_UINT16     var LowEndian: TW_INT16     var DeviceDependent: TW_INT16     var VersionNumber: TW_INT32     var StageABC: TW_TRANSFORMSTAGE     var StageLMN: TW_TRANSFORMSTAGE     var WhitePoint: TW_CIEPOINT     var BlackPoint: TW_CIEPOINT     var WhitePaper: TW_CIEPOINT     var BlackInk: TW_CIEPOINT     var Samples: (TW_FIX32)     init()     init(ColorSpace ColorSpace: TW_UINT16, LowEndian LowEndian: TW_INT16, DeviceDependent DeviceDependent: TW_INT16, VersionNumber VersionNumber: TW_INT32, StageABC StageABC: TW_TRANSFORMSTAGE, StageLMN StageLMN: TW_TRANSFORMSTAGE, WhitePoint WhitePoint: TW_CIEPOINT, BlackPoint BlackPoint: TW_CIEPOINT, WhitePaper WhitePaper: TW_CIEPOINT, BlackInk BlackInk: TW_CIEPOINT, Samples Samples: (TW_FIX32)) } ``` |

Modified TW_CIEPOINT [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_CIEPOINT {     var X: TW_FIX32     var Y: TW_FIX32     var Z: TW_FIX32 } ``` |
| To | ``` struct TW_CIEPOINT {     var X: TW_FIX32     var Y: TW_FIX32     var Z: TW_FIX32     init()     init(X X: TW_FIX32, Y Y: TW_FIX32, Z Z: TW_FIX32) } ``` |

Modified TW_CUSTOMDSDATA [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_CUSTOMDSDATA {     var InfoLength: TW_UINT32     var hData: TW_HANDLE } ``` |
| To | ``` struct TW_CUSTOMDSDATA {     var InfoLength: TW_UINT32     var hData: TW_HANDLE     init()     init(InfoLength InfoLength: TW_UINT32, hData hData: TW_HANDLE) } ``` |

Modified TW_DECODEFUNCTION [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_DECODEFUNCTION {     var StartIn: TW_FIX32     var BreakIn: TW_FIX32     var EndIn: TW_FIX32     var StartOut: TW_FIX32     var BreakOut: TW_FIX32     var EndOut: TW_FIX32     var Gamma: TW_FIX32     var SampleCount: TW_FIX32 } ``` |
| To | ``` struct TW_DECODEFUNCTION {     var StartIn: TW_FIX32     var BreakIn: TW_FIX32     var EndIn: TW_FIX32     var StartOut: TW_FIX32     var BreakOut: TW_FIX32     var EndOut: TW_FIX32     var Gamma: TW_FIX32     var SampleCount: TW_FIX32     init()     init(StartIn StartIn: TW_FIX32, BreakIn BreakIn: TW_FIX32, EndIn EndIn: TW_FIX32, StartOut StartOut: TW_FIX32, BreakOut BreakOut: TW_FIX32, EndOut EndOut: TW_FIX32, Gamma Gamma: TW_FIX32, SampleCount SampleCount: TW_FIX32) } ``` |

Modified TW_DEVICEEVENT [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_DEVICEEVENT {     var Event: TW_UINT32     var DeviceName: TW_STR255     var BatteryMinutes: TW_UINT32     var BatteryPercentage: TW_INT16     var PowerSupply: TW_INT32     var XResolution: TW_FIX32     var YResolution: TW_FIX32     var FlashUsed2: TW_UINT32     var AutomaticCapture: TW_UINT32     var TimeBeforeFirstCapture: TW_UINT32     var TimeBetweenCaptures: TW_UINT32 } ``` |
| To | ``` struct TW_DEVICEEVENT {     var Event: TW_UINT32     var DeviceName: TW_STR255     var BatteryMinutes: TW_UINT32     var BatteryPercentage: TW_INT16     var PowerSupply: TW_INT32     var XResolution: TW_FIX32     var YResolution: TW_FIX32     var FlashUsed2: TW_UINT32     var AutomaticCapture: TW_UINT32     var TimeBeforeFirstCapture: TW_UINT32     var TimeBetweenCaptures: TW_UINT32     init()     init(Event Event: TW_UINT32, DeviceName DeviceName: TW_STR255, BatteryMinutes BatteryMinutes: TW_UINT32, BatteryPercentage BatteryPercentage: TW_INT16, PowerSupply PowerSupply: TW_INT32, XResolution XResolution: TW_FIX32, YResolution YResolution: TW_FIX32, FlashUsed2 FlashUsed2: TW_UINT32, AutomaticCapture AutomaticCapture: TW_UINT32, TimeBeforeFirstCapture TimeBeforeFirstCapture: TW_UINT32, TimeBetweenCaptures TimeBetweenCaptures: TW_UINT32) } ``` |

Modified TW_ELEMENT8 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_ELEMENT8 {     var Index: TW_UINT8     var Channel1: TW_UINT8     var Channel2: TW_UINT8     var Channel3: TW_UINT8 } ``` |
| To | ``` struct TW_ELEMENT8 {     var Index: TW_UINT8     var Channel1: TW_UINT8     var Channel2: TW_UINT8     var Channel3: TW_UINT8     init()     init(Index Index: TW_UINT8, Channel1 Channel1: TW_UINT8, Channel2 Channel2: TW_UINT8, Channel3 Channel3: TW_UINT8) } ``` |

Modified TW_ENUMERATION [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_ENUMERATION {     var ItemType: TW_UINT16     var NumItems: TW_UINT32     var CurrentIndex: TW_UINT32     var DefaultIndex: TW_UINT32     var ItemList: (TW_UINT8) } ``` |
| To | ``` struct TW_ENUMERATION {     var ItemType: TW_UINT16     var NumItems: TW_UINT32     var CurrentIndex: TW_UINT32     var DefaultIndex: TW_UINT32     var ItemList: (TW_UINT8)     init()     init(ItemType ItemType: TW_UINT16, NumItems NumItems: TW_UINT32, CurrentIndex CurrentIndex: TW_UINT32, DefaultIndex DefaultIndex: TW_UINT32, ItemList ItemList: (TW_UINT8)) } ``` |

Modified TW_EVENT [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_EVENT {     var pEvent: TW_MEMREF     var TWMessage: TW_UINT16 } ``` |
| To | ``` struct TW_EVENT {     var pEvent: TW_MEMREF     var TWMessage: TW_UINT16     init()     init(pEvent pEvent: TW_MEMREF, TWMessage TWMessage: TW_UINT16) } ``` |

Modified TW_EXTIMAGEINFO [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_EXTIMAGEINFO {     var NumInfos: TW_UINT32     var Info: (TW_INFO) } ``` |
| To | ``` struct TW_EXTIMAGEINFO {     var NumInfos: TW_UINT32     var Info: (TW_INFO)     init()     init(NumInfos NumInfos: TW_UINT32, Info Info: (TW_INFO)) } ``` |

Modified TW_FILESYSTEM [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_FILESYSTEM {     var InputName: TW_STR255     var OutputName: TW_STR255     var Context: TW_MEMREF     var Recursive: Int32     var FileType: TW_INT32     var Size: TW_UINT32     var CreateTimeDate: TW_STR32     var ModifiedTimeDate: TW_STR32     var FreeSpace: TW_UINT32     var NewImageSize: TW_INT32     var NumberOfFiles: TW_UINT32     var NumberOfSnippets: TW_UINT32     var DeviceGroupMask: TW_UINT32     var Reserved: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ```  ``` |

Modified TW_FIX32 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_FIX32 {     var Whole: TW_INT16     var Frac: TW_UINT16 } ``` |
| To | ``` struct TW_FIX32 {     var Whole: TW_INT16     var Frac: TW_UINT16     init()     init(Whole Whole: TW_INT16, Frac Frac: TW_UINT16) } ``` |

Modified TW_FRAME [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_FRAME {     var Left: TW_FIX32     var Top: TW_FIX32     var Right: TW_FIX32     var Bottom: TW_FIX32 } ``` |
| To | ``` struct TW_FRAME {     var Left: TW_FIX32     var Top: TW_FIX32     var Right: TW_FIX32     var Bottom: TW_FIX32     init()     init(Left Left: TW_FIX32, Top Top: TW_FIX32, Right Right: TW_FIX32, Bottom Bottom: TW_FIX32) } ``` |

Modified TW_GRAYRESPONSE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_GRAYRESPONSE {     var Response: (TW_ELEMENT8) } ``` |
| To | ``` struct TW_GRAYRESPONSE {     var Response: (TW_ELEMENT8)     init()     init(Response Response: (TW_ELEMENT8)) } ``` |

Modified TW_IDENTITY [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_IDENTITY {     var Id: TW_MEMREF     var Version: TW_VERSION     var ProtocolMajor: TW_UINT16     var ProtocolMinor: TW_UINT16     var SupportedGroups: TW_UINT32     var Manufacturer: TW_STR32     var ProductFamily: TW_STR32     var ProductName: TW_STR32 } ``` |
| To | ``` struct TW_IDENTITY {     var Id: TW_MEMREF     var Version: TW_VERSION     var ProtocolMajor: TW_UINT16     var ProtocolMinor: TW_UINT16     var SupportedGroups: TW_UINT32     var Manufacturer: TW_STR32     var ProductFamily: TW_STR32     var ProductName: TW_STR32     init()     init(Id Id: TW_MEMREF, Version Version: TW_VERSION, ProtocolMajor ProtocolMajor: TW_UINT16, ProtocolMinor ProtocolMinor: TW_UINT16, SupportedGroups SupportedGroups: TW_UINT32, Manufacturer Manufacturer: TW_STR32, ProductFamily ProductFamily: TW_STR32, ProductName ProductName: TW_STR32) } ``` |

Modified TW_IMAGEINFO [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_IMAGEINFO {     var XResolution: TW_FIX32     var YResolution: TW_FIX32     var ImageWidth: TW_INT32     var ImageLength: TW_INT32     var SamplesPerPixel: TW_INT16     var BitsPerSample: (TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16)     var BitsPerPixel: TW_INT16     var Planar: TW_BOOL     var PixelType: TW_INT16     var Compression: TW_UINT16 } ``` |
| To | ``` struct TW_IMAGEINFO {     var XResolution: TW_FIX32     var YResolution: TW_FIX32     var ImageWidth: TW_INT32     var ImageLength: TW_INT32     var SamplesPerPixel: TW_INT16     var BitsPerSample: (TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16)     var BitsPerPixel: TW_INT16     var Planar: TW_BOOL     var PixelType: TW_INT16     var Compression: TW_UINT16     init()     init(XResolution XResolution: TW_FIX32, YResolution YResolution: TW_FIX32, ImageWidth ImageWidth: TW_INT32, ImageLength ImageLength: TW_INT32, SamplesPerPixel SamplesPerPixel: TW_INT16, BitsPerSample BitsPerSample: (TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16, TW_INT16), BitsPerPixel BitsPerPixel: TW_INT16, Planar Planar: TW_BOOL, PixelType PixelType: TW_INT16, Compression Compression: TW_UINT16) } ``` |

Modified TW_IMAGELAYOUT [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_IMAGELAYOUT {     var Frame: TW_FRAME     var DocumentNumber: TW_UINT32     var PageNumber: TW_UINT32     var FrameNumber: TW_UINT32 } ``` |
| To | ``` struct TW_IMAGELAYOUT {     var Frame: TW_FRAME     var DocumentNumber: TW_UINT32     var PageNumber: TW_UINT32     var FrameNumber: TW_UINT32     init()     init(Frame Frame: TW_FRAME, DocumentNumber DocumentNumber: TW_UINT32, PageNumber PageNumber: TW_UINT32, FrameNumber FrameNumber: TW_UINT32) } ``` |

Modified TW_IMAGEMEMXFER [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_IMAGEMEMXFER {     var Compression: TW_UINT16     var BytesPerRow: TW_UINT32     var Columns: TW_UINT32     var Rows: TW_UINT32     var XOffset: TW_UINT32     var YOffset: TW_UINT32     var BytesWritten: TW_UINT32     var Memory: TW_MEMORY } ``` |
| To | ``` struct TW_IMAGEMEMXFER {     var Compression: TW_UINT16     var BytesPerRow: TW_UINT32     var Columns: TW_UINT32     var Rows: TW_UINT32     var XOffset: TW_UINT32     var YOffset: TW_UINT32     var BytesWritten: TW_UINT32     var Memory: TW_MEMORY     init()     init(Compression Compression: TW_UINT16, BytesPerRow BytesPerRow: TW_UINT32, Columns Columns: TW_UINT32, Rows Rows: TW_UINT32, XOffset XOffset: TW_UINT32, YOffset YOffset: TW_UINT32, BytesWritten BytesWritten: TW_UINT32, Memory Memory: TW_MEMORY) } ``` |

Modified TW_INFO [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_INFO {     var InfoID: TW_UINT16     var ItemType: TW_UINT16     var NumItems: TW_UINT16     var CondCode: TW_UINT16     var Item: TW_UINT32 } ``` |
| To | ``` struct TW_INFO {     var InfoID: TW_UINT16     var ItemType: TW_UINT16     var NumItems: TW_UINT16     var CondCode: TW_UINT16     var Item: TW_UINT32     init()     init(InfoID InfoID: TW_UINT16, ItemType ItemType: TW_UINT16, NumItems NumItems: TW_UINT16, CondCode CondCode: TW_UINT16, Item Item: TW_UINT32) } ``` |

Modified TW_JPEGCOMPRESSION [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_JPEGCOMPRESSION {     var ColorSpace: TW_UINT16     var SubSampling: TW_UINT32     var NumComponents: TW_UINT16     var RestartFrequency: TW_UINT16     var QuantMap: (TW_UINT16, TW_UINT16, TW_UINT16, TW_UINT16)     var QuantTable: (TW_MEMORY, TW_MEMORY, TW_MEMORY, TW_MEMORY)     var HuffmanMap: (TW_UINT16, TW_UINT16, TW_UINT16, TW_UINT16)     var HuffmanDC: (TW_MEMORY, TW_MEMORY)     var HuffmanAC: (TW_MEMORY, TW_MEMORY) } ``` |
| To | ``` struct TW_JPEGCOMPRESSION {     var ColorSpace: TW_UINT16     var SubSampling: TW_UINT32     var NumComponents: TW_UINT16     var RestartFrequency: TW_UINT16     var QuantMap: (TW_UINT16, TW_UINT16, TW_UINT16, TW_UINT16)     var QuantTable: (TW_MEMORY, TW_MEMORY, TW_MEMORY, TW_MEMORY)     var HuffmanMap: (TW_UINT16, TW_UINT16, TW_UINT16, TW_UINT16)     var HuffmanDC: (TW_MEMORY, TW_MEMORY)     var HuffmanAC: (TW_MEMORY, TW_MEMORY)     init()     init(ColorSpace ColorSpace: TW_UINT16, SubSampling SubSampling: TW_UINT32, NumComponents NumComponents: TW_UINT16, RestartFrequency RestartFrequency: TW_UINT16, QuantMap QuantMap: (TW_UINT16, TW_UINT16, TW_UINT16, TW_UINT16), QuantTable QuantTable: (TW_MEMORY, TW_MEMORY, TW_MEMORY, TW_MEMORY), HuffmanMap HuffmanMap: (TW_UINT16, TW_UINT16, TW_UINT16, TW_UINT16), HuffmanDC HuffmanDC: (TW_MEMORY, TW_MEMORY), HuffmanAC HuffmanAC: (TW_MEMORY, TW_MEMORY)) } ``` |

Modified TW_MEMORY [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_MEMORY {     var Flags: TW_UINT32     var Length: TW_UINT32     var TheMem: TW_MEMREF } ``` |
| To | ``` struct TW_MEMORY {     var Flags: TW_UINT32     var Length: TW_UINT32     var TheMem: TW_MEMREF     init()     init(Flags Flags: TW_UINT32, Length Length: TW_UINT32, TheMem TheMem: TW_MEMREF) } ``` |

Modified TW_ONEVALUE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_ONEVALUE {     var ItemType: TW_UINT16     var Item: TW_UINT32 } ``` |
| To | ``` struct TW_ONEVALUE {     var ItemType: TW_UINT16     var Item: TW_UINT32     init()     init(ItemType ItemType: TW_UINT16, Item Item: TW_UINT32) } ``` |

Modified TW_PALETTE8 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_PALETTE8 {     var NumColors: TW_UINT16     var PaletteType: TW_UINT16     var Colors: (TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8, TW_ELEMENT8) } ``` |
| To | ```  ``` |

Modified TW_PASSTHRU [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_PASSTHRU {     var pCommand: TW_MEMREF     var CommandBytes: TW_UINT32     var Direction: TW_INT32     var pData: TW_MEMREF     var DataBytes: TW_UINT32     var DataBytesXfered: TW_UINT32 } ``` |
| To | ``` struct TW_PASSTHRU {     var pCommand: TW_MEMREF     var CommandBytes: TW_UINT32     var Direction: TW_INT32     var pData: TW_MEMREF     var DataBytes: TW_UINT32     var DataBytesXfered: TW_UINT32     init()     init(pCommand pCommand: TW_MEMREF, CommandBytes CommandBytes: TW_UINT32, Direction Direction: TW_INT32, pData pData: TW_MEMREF, DataBytes DataBytes: TW_UINT32, DataBytesXfered DataBytesXfered: TW_UINT32) } ``` |

Modified TW_PENDINGXFERS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_PENDINGXFERS {     var Count: TW_UINT16 } ``` |
| To | ``` struct TW_PENDINGXFERS {     var Count: TW_UINT16     init() } ``` |

Modified TW_RANGE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_RANGE {     var ItemType: TW_UINT16     var MinValue: TW_UINT32     var MaxValue: TW_UINT32     var StepSize: TW_UINT32     var DefaultValue: TW_UINT32     var CurrentValue: TW_UINT32 } ``` |
| To | ``` struct TW_RANGE {     var ItemType: TW_UINT16     var MinValue: TW_UINT32     var MaxValue: TW_UINT32     var StepSize: TW_UINT32     var DefaultValue: TW_UINT32     var CurrentValue: TW_UINT32     init()     init(ItemType ItemType: TW_UINT16, MinValue MinValue: TW_UINT32, MaxValue MaxValue: TW_UINT32, StepSize StepSize: TW_UINT32, DefaultValue DefaultValue: TW_UINT32, CurrentValue CurrentValue: TW_UINT32) } ``` |

Modified TW_RGBRESPONSE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_RGBRESPONSE {     var Response: (TW_ELEMENT8) } ``` |
| To | ``` struct TW_RGBRESPONSE {     var Response: (TW_ELEMENT8)     init()     init(Response Response: (TW_ELEMENT8)) } ``` |

Modified TW_SETUPAUDIOFILEXFER [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_SETUPAUDIOFILEXFER {     var FileName: TW_STR255     var Format: TW_UINT16     var VRefNum: TW_INT16 } ``` |
| To | ``` struct TW_SETUPAUDIOFILEXFER {     var FileName: TW_STR255     var Format: TW_UINT16     var VRefNum: TW_INT16     init()     init(FileName FileName: TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) } ``` |

Modified TW_SETUPFILEXFER [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_SETUPFILEXFER {     var FileName: TW_STR255     var Format: TW_UINT16     var VRefNum: TW_INT16 } ``` |
| To | ``` struct TW_SETUPFILEXFER {     var FileName: TW_STR255     var Format: TW_UINT16     var VRefNum: TW_INT16     init()     init(FileName FileName: TW_STR255, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16) } ``` |

Modified TW_SETUPFILEXFER2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_SETUPFILEXFER2 {     var FileName: TW_MEMREF     var FileNameType: TW_UINT16     var Format: TW_UINT16     var VRefNum: TW_INT16     var ParID: TW_UINT32 } ``` |
| To | ``` struct TW_SETUPFILEXFER2 {     var FileName: TW_MEMREF     var FileNameType: TW_UINT16     var Format: TW_UINT16     var VRefNum: TW_INT16     var ParID: TW_UINT32     init()     init(FileName FileName: TW_MEMREF, FileNameType FileNameType: TW_UINT16, Format Format: TW_UINT16, VRefNum VRefNum: TW_INT16, ParID ParID: TW_UINT32) } ``` |

Modified TW_SETUPMEMXFER [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_SETUPMEMXFER {     var MinBufSize: TW_UINT32     var MaxBufSize: TW_UINT32     var Preferred: TW_UINT32 } ``` |
| To | ``` struct TW_SETUPMEMXFER {     var MinBufSize: TW_UINT32     var MaxBufSize: TW_UINT32     var Preferred: TW_UINT32     init()     init(MinBufSize MinBufSize: TW_UINT32, MaxBufSize MaxBufSize: TW_UINT32, Preferred Preferred: TW_UINT32) } ``` |

Modified TW_STATUS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_STATUS {     var ConditionCode: TW_UINT16     var Reserved: TW_UINT16 } ``` |
| To | ``` struct TW_STATUS {     var ConditionCode: TW_UINT16     var Reserved: TW_UINT16     init()     init(ConditionCode ConditionCode: TW_UINT16, Reserved Reserved: TW_UINT16) } ``` |

Modified TW_TRANSFORMSTAGE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_TRANSFORMSTAGE {     var Decode: (TW_DECODEFUNCTION, TW_DECODEFUNCTION, TW_DECODEFUNCTION)     var Mix: ((TW_FIX32, TW_FIX32, TW_FIX32), (TW_FIX32, TW_FIX32, TW_FIX32), (TW_FIX32, TW_FIX32, TW_FIX32)) } ``` |
| To | ``` struct TW_TRANSFORMSTAGE {     var Decode: (TW_DECODEFUNCTION, TW_DECODEFUNCTION, TW_DECODEFUNCTION)     var Mix: ((TW_FIX32, TW_FIX32, TW_FIX32), (TW_FIX32, TW_FIX32, TW_FIX32), (TW_FIX32, TW_FIX32, TW_FIX32))     init()     init(Decode Decode: (TW_DECODEFUNCTION, TW_DECODEFUNCTION, TW_DECODEFUNCTION), Mix Mix: ((TW_FIX32, TW_FIX32, TW_FIX32), (TW_FIX32, TW_FIX32, TW_FIX32), (TW_FIX32, TW_FIX32, TW_FIX32))) } ``` |

Modified TW_TWUNKDSENTRYPARAMS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_TWUNKDSENTRYPARAMS {     var destFlag: TW_INT8     var dest: TW_IDENTITY     var dataGroup: TW_INT32     var dataArgType: TW_INT16     var message: TW_INT16     var pDataSize: TW_INT32 } ``` |
| To | ``` struct TW_TWUNKDSENTRYPARAMS {     var destFlag: TW_INT8     var dest: TW_IDENTITY     var dataGroup: TW_INT32     var dataArgType: TW_INT16     var message: TW_INT16     var pDataSize: TW_INT32     init()     init(destFlag destFlag: TW_INT8, dest dest: TW_IDENTITY, dataGroup dataGroup: TW_INT32, dataArgType dataArgType: TW_INT16, message message: TW_INT16, pDataSize pDataSize: TW_INT32) } ``` |

Modified TW_TWUNKDSENTRYRETURN [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_TWUNKDSENTRYRETURN {     var returnCode: TW_UINT16     var conditionCode: TW_UINT16     var pDataSize: TW_INT32 } ``` |
| To | ``` struct TW_TWUNKDSENTRYRETURN {     var returnCode: TW_UINT16     var conditionCode: TW_UINT16     var pDataSize: TW_INT32     init()     init(returnCode returnCode: TW_UINT16, conditionCode conditionCode: TW_UINT16, pDataSize pDataSize: TW_INT32) } ``` |

Modified TW_TWUNKIDENTITY [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_TWUNKIDENTITY {     var identity: TW_IDENTITY     var dsPath: TW_STR255 } ``` |
| To | ``` struct TW_TWUNKIDENTITY {     var identity: TW_IDENTITY     var dsPath: TW_STR255     init()     init(identity identity: TW_IDENTITY, dsPath dsPath: TW_STR255) } ``` |

Modified TW_USERINTERFACE [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_USERINTERFACE {     var ShowUI: TW_BOOL     var ModalUI: TW_BOOL     var hParent: TW_HANDLE } ``` |
| To | ``` struct TW_USERINTERFACE {     var ShowUI: TW_BOOL     var ModalUI: TW_BOOL     var hParent: TW_HANDLE     init()     init(ShowUI ShowUI: TW_BOOL, ModalUI ModalUI: TW_BOOL, hParent hParent: TW_HANDLE) } ``` |

Modified TW_VERSION [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_VERSION {     var MajorNum: TW_UINT16     var MinorNum: TW_UINT16     var Language: TW_UINT16     var Country: TW_UINT16     var Info: TW_STR32 } ``` |
| To | ``` struct TW_VERSION {     var MajorNum: TW_UINT16     var MinorNum: TW_UINT16     var Language: TW_UINT16     var Country: TW_UINT16     var Info: TW_STR32     init()     init(MajorNum MajorNum: TW_UINT16, MinorNum MinorNum: TW_UINT16, Language Language: TW_UINT16, Country Country: TW_UINT16, Info Info: TW_STR32) } ``` |

Modified TW_MEMREF

|  | Declaration |
| --- | --- |
| From | ``` typealias TW_MEMREF = UnsafePointer<Int8> ``` |
| To | ``` typealias TW_MEMREF = UnsafeMutablePointer<Int8> ``` |

Modified pTW_ARRAY

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_ARRAY = UnsafePointer<TW_ARRAY> ``` |
| To | ``` typealias pTW_ARRAY = UnsafeMutablePointer<TW_ARRAY> ``` |

Modified pTW_AUDIOINFO

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_AUDIOINFO = UnsafePointer<TW_AUDIOINFO> ``` |
| To | ``` typealias pTW_AUDIOINFO = UnsafeMutablePointer<TW_AUDIOINFO> ``` |

Modified pTW_BOOL

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_BOOL = UnsafePointer<UInt16> ``` |
| To | ``` typealias pTW_BOOL = UnsafeMutablePointer<UInt16> ``` |

Modified pTW_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_CALLBACK = UnsafePointer<TW_CALLBACK> ``` |
| To | ``` typealias pTW_CALLBACK = UnsafeMutablePointer<TW_CALLBACK> ``` |

Modified pTW_CAPABILITY

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_CAPABILITY = UnsafePointer<TW_CAPABILITY> ``` |
| To | ``` typealias pTW_CAPABILITY = UnsafeMutablePointer<TW_CAPABILITY> ``` |

Modified pTW_CAPEXT

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_CAPEXT = UnsafePointer<TW_CAPEXT> ``` |
| To | ``` typealias pTW_CAPEXT = UnsafeMutablePointer<TW_CAPEXT> ``` |

Modified pTW_CIECOLOR

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_CIECOLOR = UnsafePointer<TW_CIECOLOR> ``` |
| To | ``` typealias pTW_CIECOLOR = UnsafeMutablePointer<TW_CIECOLOR> ``` |

Modified pTW_CIEPOINT

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_CIEPOINT = UnsafePointer<TW_CIEPOINT> ``` |
| To | ``` typealias pTW_CIEPOINT = UnsafeMutablePointer<TW_CIEPOINT> ``` |

Modified pTW_CUSTOMDSDATA

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_CUSTOMDSDATA = UnsafePointer<TW_CUSTOMDSDATA> ``` |
| To | ``` typealias pTW_CUSTOMDSDATA = UnsafeMutablePointer<TW_CUSTOMDSDATA> ``` |

Modified pTW_DECODEFUNCTION

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_DECODEFUNCTION = UnsafePointer<TW_DECODEFUNCTION> ``` |
| To | ``` typealias pTW_DECODEFUNCTION = UnsafeMutablePointer<TW_DECODEFUNCTION> ``` |

Modified pTW_DEVICEEVENT

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_DEVICEEVENT = UnsafePointer<TW_DEVICEEVENT> ``` |
| To | ``` typealias pTW_DEVICEEVENT = UnsafeMutablePointer<TW_DEVICEEVENT> ``` |

Modified pTW_ELEMENT8

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_ELEMENT8 = UnsafePointer<TW_ELEMENT8> ``` |
| To | ``` typealias pTW_ELEMENT8 = UnsafeMutablePointer<TW_ELEMENT8> ``` |

Modified pTW_ENUMERATION

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_ENUMERATION = UnsafePointer<TW_ENUMERATION> ``` |
| To | ``` typealias pTW_ENUMERATION = UnsafeMutablePointer<TW_ENUMERATION> ``` |

Modified pTW_EVENT

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_EVENT = UnsafePointer<TW_EVENT> ``` |
| To | ``` typealias pTW_EVENT = UnsafeMutablePointer<TW_EVENT> ``` |

Modified pTW_EXTIMAGEINFO

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_EXTIMAGEINFO = UnsafePointer<TW_EXTIMAGEINFO> ``` |
| To | ``` typealias pTW_EXTIMAGEINFO = UnsafeMutablePointer<TW_EXTIMAGEINFO> ``` |

Modified pTW_FILESYSTEM

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_FILESYSTEM = UnsafePointer<TW_FILESYSTEM> ``` |
| To | ``` typealias pTW_FILESYSTEM = UnsafeMutablePointer<TW_FILESYSTEM> ``` |

Modified pTW_FIX32

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_FIX32 = UnsafePointer<TW_FIX32> ``` |
| To | ``` typealias pTW_FIX32 = UnsafeMutablePointer<TW_FIX32> ``` |

Modified pTW_FRAME

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_FRAME = UnsafePointer<TW_FRAME> ``` |
| To | ``` typealias pTW_FRAME = UnsafeMutablePointer<TW_FRAME> ``` |

Modified pTW_GRAYRESPONSE

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_GRAYRESPONSE = UnsafePointer<TW_GRAYRESPONSE> ``` |
| To | ``` typealias pTW_GRAYRESPONSE = UnsafeMutablePointer<TW_GRAYRESPONSE> ``` |

Modified pTW_IDENTITY

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_IDENTITY = UnsafePointer<TW_IDENTITY> ``` |
| To | ``` typealias pTW_IDENTITY = UnsafeMutablePointer<TW_IDENTITY> ``` |

Modified pTW_IMAGEINFO

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_IMAGEINFO = UnsafePointer<TW_IMAGEINFO> ``` |
| To | ``` typealias pTW_IMAGEINFO = UnsafeMutablePointer<TW_IMAGEINFO> ``` |

Modified pTW_IMAGELAYOUT

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_IMAGELAYOUT = UnsafePointer<TW_IMAGELAYOUT> ``` |
| To | ``` typealias pTW_IMAGELAYOUT = UnsafeMutablePointer<TW_IMAGELAYOUT> ``` |

Modified pTW_IMAGEMEMXFER

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_IMAGEMEMXFER = UnsafePointer<TW_IMAGEMEMXFER> ``` |
| To | ``` typealias pTW_IMAGEMEMXFER = UnsafeMutablePointer<TW_IMAGEMEMXFER> ``` |

Modified pTW_INFO

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_INFO = UnsafePointer<TW_INFO> ``` |
| To | ``` typealias pTW_INFO = UnsafeMutablePointer<TW_INFO> ``` |

Modified pTW_INT16

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_INT16 = UnsafePointer<Int16> ``` |
| To | ``` typealias pTW_INT16 = UnsafeMutablePointer<Int16> ``` |

Modified pTW_INT32

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_INT32 = UnsafePointer<Int32> ``` |
| To | ``` typealias pTW_INT32 = UnsafeMutablePointer<Int32> ``` |

Modified pTW_INT8

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_INT8 = UnsafePointer<Int8> ``` |
| To | ``` typealias pTW_INT8 = UnsafeMutablePointer<Int8> ``` |

Modified pTW_JPEGCOMPRESSION

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_JPEGCOMPRESSION = UnsafePointer<TW_JPEGCOMPRESSION> ``` |
| To | ``` typealias pTW_JPEGCOMPRESSION = UnsafeMutablePointer<TW_JPEGCOMPRESSION> ``` |

Modified pTW_MEMORY

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_MEMORY = UnsafePointer<TW_MEMORY> ``` |
| To | ``` typealias pTW_MEMORY = UnsafeMutablePointer<TW_MEMORY> ``` |

Modified pTW_ONEVALUE

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_ONEVALUE = UnsafePointer<TW_ONEVALUE> ``` |
| To | ``` typealias pTW_ONEVALUE = UnsafeMutablePointer<TW_ONEVALUE> ``` |

Modified pTW_PALETTE8

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_PALETTE8 = UnsafePointer<TW_PALETTE8> ``` |
| To | ``` typealias pTW_PALETTE8 = UnsafeMutablePointer<TW_PALETTE8> ``` |

Modified pTW_PASSTHRU

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_PASSTHRU = UnsafePointer<TW_PASSTHRU> ``` |
| To | ``` typealias pTW_PASSTHRU = UnsafeMutablePointer<TW_PASSTHRU> ``` |

Modified pTW_PENDINGXFERS

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_PENDINGXFERS = UnsafePointer<TW_PENDINGXFERS> ``` |
| To | ``` typealias pTW_PENDINGXFERS = UnsafeMutablePointer<TW_PENDINGXFERS> ``` |

Modified pTW_RANGE

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_RANGE = UnsafePointer<TW_RANGE> ``` |
| To | ``` typealias pTW_RANGE = UnsafeMutablePointer<TW_RANGE> ``` |

Modified pTW_RGBRESPONSE

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_RGBRESPONSE = UnsafePointer<TW_RGBRESPONSE> ``` |
| To | ``` typealias pTW_RGBRESPONSE = UnsafeMutablePointer<TW_RGBRESPONSE> ``` |

Modified pTW_SETUPAUDIOFILEXFER

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_SETUPAUDIOFILEXFER = UnsafePointer<TW_SETUPAUDIOFILEXFER> ``` |
| To | ``` typealias pTW_SETUPAUDIOFILEXFER = UnsafeMutablePointer<TW_SETUPAUDIOFILEXFER> ``` |

Modified pTW_SETUPFILEXFER

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_SETUPFILEXFER = UnsafePointer<TW_SETUPFILEXFER> ``` |
| To | ``` typealias pTW_SETUPFILEXFER = UnsafeMutablePointer<TW_SETUPFILEXFER> ``` |

Modified pTW_SETUPFILEXFER2

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_SETUPFILEXFER2 = UnsafePointer<TW_SETUPFILEXFER2> ``` |
| To | ``` typealias pTW_SETUPFILEXFER2 = UnsafeMutablePointer<TW_SETUPFILEXFER2> ``` |

Modified pTW_SETUPMEMXFER

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_SETUPMEMXFER = UnsafePointer<TW_SETUPMEMXFER> ``` |
| To | ``` typealias pTW_SETUPMEMXFER = UnsafeMutablePointer<TW_SETUPMEMXFER> ``` |

Modified pTW_STATUS

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_STATUS = UnsafePointer<TW_STATUS> ``` |
| To | ``` typealias pTW_STATUS = UnsafeMutablePointer<TW_STATUS> ``` |

Modified pTW_STR128

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_STR128 = UnsafePointer<UInt8> ``` |
| To | ``` typealias pTW_STR128 = UnsafeMutablePointer<UInt8> ``` |

Modified pTW_STR255

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_STR255 = UnsafePointer<UInt8> ``` |
| To | ``` typealias pTW_STR255 = UnsafeMutablePointer<UInt8> ``` |

Modified pTW_STR32

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_STR32 = UnsafePointer<UInt8> ``` |
| To | ``` typealias pTW_STR32 = UnsafeMutablePointer<UInt8> ``` |

Modified pTW_STR64

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_STR64 = UnsafePointer<UInt8> ``` |
| To | ``` typealias pTW_STR64 = UnsafeMutablePointer<UInt8> ``` |

Modified pTW_TRANSFORMSTAGE

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_TRANSFORMSTAGE = UnsafePointer<TW_TRANSFORMSTAGE> ``` |
| To | ``` typealias pTW_TRANSFORMSTAGE = UnsafeMutablePointer<TW_TRANSFORMSTAGE> ``` |

Modified pTW_TWUNKDSENTRYPARAMS

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_TWUNKDSENTRYPARAMS = UnsafePointer<TW_TWUNKDSENTRYPARAMS> ``` |
| To | ``` typealias pTW_TWUNKDSENTRYPARAMS = UnsafeMutablePointer<TW_TWUNKDSENTRYPARAMS> ``` |

Modified pTW_TWUNKDSENTRYRETURN

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_TWUNKDSENTRYRETURN = UnsafePointer<TW_TWUNKDSENTRYRETURN> ``` |
| To | ``` typealias pTW_TWUNKDSENTRYRETURN = UnsafeMutablePointer<TW_TWUNKDSENTRYRETURN> ``` |

Modified pTW_TWUNKIDENTITY

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_TWUNKIDENTITY = UnsafePointer<TW_TWUNKIDENTITY> ``` |
| To | ``` typealias pTW_TWUNKIDENTITY = UnsafeMutablePointer<TW_TWUNKIDENTITY> ``` |

Modified pTW_UINT16

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_UINT16 = UnsafePointer<UInt16> ``` |
| To | ``` typealias pTW_UINT16 = UnsafeMutablePointer<UInt16> ``` |

Modified pTW_UINT32

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_UINT32 = UnsafePointer<UInt32> ``` |
| To | ``` typealias pTW_UINT32 = UnsafeMutablePointer<UInt32> ``` |

Modified pTW_UINT8

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_UINT8 = UnsafePointer<UInt8> ``` |
| To | ``` typealias pTW_UINT8 = UnsafeMutablePointer<UInt8> ``` |

Modified pTW_USERINTERFACE

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_USERINTERFACE = UnsafePointer<TW_USERINTERFACE> ``` |
| To | ``` typealias pTW_USERINTERFACE = UnsafeMutablePointer<TW_USERINTERFACE> ``` |

Modified pTW_VERSION

|  | Declaration |
| --- | --- |
| From | ``` typealias pTW_VERSION = UnsafePointer<TW_VERSION> ``` |
| To | ``` typealias pTW_VERSION = UnsafeMutablePointer<TW_VERSION> ``` |

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
