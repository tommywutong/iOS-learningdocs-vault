---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/ICADevices.html
archived_at: '2026-07-18T02:52:30.722897Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# ICADevices Changes

## ICADevices

Added ICARawFileHeader.init()Added ICARawFileHeader.init(imageDataOffset: UInt32, version: UInt32, imageWidth: UInt32, imageHeight: UInt32, bytesPerRow: UInt32, numberOfComponents: UInt32, bitsPerComponent: UInt32, bitsPerPixel: UInt32, cgColorSpaceModel: UInt32, bitmapInfo: UInt32, orientation: UInt32, dpi: UInt32, colorSyncModeStr:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added ICD_ObjectSendMessagePB.init()Added ICD_ObjectSendMessagePB.init(header: ICDHeader, object: ICAObject, objectInfo: ICAObjectInfo, connectionID: ICAConnectionID, message: ICAMessage, totalDataSize: UInt32, result: UInt32)Added ICD_ScannerCloseSessionPB.init()Added ICD_ScannerCloseSessionPB.init(header: ICDHeader, object: ICAObject, objectInfo: ICAObjectInfo, connectionID: ICAConnectionID, sessionID: ICAScannerSessionID)Added ICD_ScannerGetParametersPB.init()Added ICD_ScannerGetParametersPB.init(header: ICDHeader, object: ICAObject, objectInfo: ICAObjectInfo, connectionID: ICAConnectionID, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICD_ScannerInitializePB.init()Added ICD_ScannerInitializePB.init(header: ICDHeader, object: ICAObject, objectInfo: ICAObjectInfo, connectionID: ICAConnectionID, sessionID: ICAScannerSessionID)Added ICD_ScannerObjectSendMessagePB.init()Added ICD_ScannerObjectSendMessagePB.init(header: ICDHeader, object: ICAObject, objectInfo: ICAObjectInfo, connectionID: ICAConnectionID, message: ICAMessage, totalDataSize: UInt32, result: UInt32)Added ICD_ScannerOpenSessionPB.init()Added ICD_ScannerOpenSessionPB.init(header: ICDHeader, object: ICAObject, objectInfo: ICAObjectInfo, connectionID: ICAConnectionID, sessionID: ICAScannerSessionID)Added ICD_ScannerSetParametersPB.init()Added ICD_ScannerSetParametersPB.init(header: ICDHeader, object: ICAObject, objectInfo: ICAObjectInfo, connectionID: ICAConnectionID, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICD_ScannerStartPB.init()Added ICD_ScannerStartPB.init(header: ICDHeader, object: ICAObject, objectInfo: ICAObjectInfo, connectionID: ICAConnectionID, sessionID: ICAScannerSessionID)Added ICD_ScannerStatusPB.init()Added ICD_ScannerStatusPB.init(header: ICDHeader, object: ICAObject, objectInfo: ICAObjectInfo, connectionID: ICAConnectionID, sessionID: ICAScannerSessionID, status: UInt32)Added ICD_Scannerscanner_callback_functions.init()Added ICD_Scannerscanner_callback_functions.init(f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice, f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath, f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice, f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask, f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo, f_ICD_ScannerCleanup: __ICD_ScannerCleanup, f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData, f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData, f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData, f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData, f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage, f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary, f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice, f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath, f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession, f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession, f_ICD_ScannerInitialize: __ICD_ScannerInitialize, f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters, f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters, f_ICD_ScannerStatus: __ICD_ScannerStatus, f_ICD_ScannerStart: __ICD_ScannerStart, f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice, f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice, f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile, f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice, f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor, f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64)Added ICD_callback_functions.init()Added ICD_callback_functions.init(f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice, f_ICD_CloseDevice: __ICD_CloseDevice, f_ICD_PeriodicTask: __ICD_PeriodicTask, f_ICD_GetObjectInfo: __ICD_GetObjectInfo, f_ICD_Cleanup: __ICD_Cleanup, f_ICD_GetPropertyData: __ICD_GetPropertyData, f_ICD_SetPropertyData: __ICD_SetPropertyData, f_ICD_ReadFileData: __ICD_ReadFileData, f_ICD_WriteFileData: __ICD_WriteFileData, f_ICD_SendMessage: __ICD_SendMessage, f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary, f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice, f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath, f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath, f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice, f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice, f_ICD_WriteDataToFile: __ICD_WriteDataToFile, f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice, f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor, f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64)Added ObjectInfo.init()Added ObjectInfo.init(icaObject: ICAObject, reserved: UInt, icaObjectInfo: ICAObjectInfo, uniqueID: UInt32, thumbnailSize: UInt32, dataSize: UInt32, dataWidth: UInt32, dataHeight: UInt32, name:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags: UInt32, privateData: Ptr, uniqueIDFireWire: UInt64, tag: UInt32, dataSize64: UInt64)Added ScannerObjectInfo.init()Added ScannerObjectInfo.init(icaObject: ICAObject, reserved: UInt, icaObjectInfo: ICAObjectInfo, uniqueID: UInt32, uniqueIDFireWire: UInt64, thumbnailSize: UInt32, dataSize: UInt32, dataWidth: UInt32, dataHeight: UInt32, name:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags: UInt32, privateData: Ptr, tag: UInt32)Modified ICARawFileHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICARawFileHeader {     var imageDataOffset: UInt32     var version: UInt32     var imageWidth: UInt32     var imageHeight: UInt32     var bytesPerRow: UInt32     var numberOfComponents: UInt32     var bitsPerComponent: UInt32     var bitsPerPixel: UInt32     var cgColorSpaceModel: UInt32     var bitmapInfo: UInt32     var orientation: UInt32     var dpi: UInt32     var colorSyncModeStr: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct ICARawFileHeader {     var imageDataOffset: UInt32     var version: UInt32     var imageWidth: UInt32     var imageHeight: UInt32     var bytesPerRow: UInt32     var numberOfComponents: UInt32     var bitsPerComponent: UInt32     var bitsPerPixel: UInt32     var cgColorSpaceModel: UInt32     var bitmapInfo: UInt32     var orientation: UInt32     var dpi: UInt32     var colorSyncModeStr: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(imageDataOffset imageDataOffset: UInt32, version version: UInt32, imageWidth imageWidth: UInt32, imageHeight imageHeight: UInt32, bytesPerRow bytesPerRow: UInt32, numberOfComponents numberOfComponents: UInt32, bitsPerComponent bitsPerComponent: UInt32, bitsPerPixel bitsPerPixel: UInt32, cgColorSpaceModel cgColorSpaceModel: UInt32, bitmapInfo bitmapInfo: UInt32, orientation orientation: UInt32, dpi dpi: UInt32, colorSyncModeStr colorSyncModeStr: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified ICD_ObjectSendMessagePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_ObjectSendMessagePB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var message: ICAMessage     var totalDataSize: UInt32     var result: UInt32 } ``` |
| To | ``` struct ICD_ObjectSendMessagePB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var message: ICAMessage     var totalDataSize: UInt32     var result: UInt32     init()     init(header header: ICDHeader, object object: ICAObject, objectInfo objectInfo: ICAObjectInfo, connectionID connectionID: ICAConnectionID, message message: ICAMessage, totalDataSize totalDataSize: UInt32, result result: UInt32) } ``` |

Modified ICD_ScannerCloseSessionPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_ScannerCloseSessionPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID } ``` |
| To | ``` struct ICD_ScannerCloseSessionPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     init()     init(header header: ICDHeader, object object: ICAObject, objectInfo objectInfo: ICAObjectInfo, connectionID connectionID: ICAConnectionID, sessionID sessionID: ICAScannerSessionID) } ``` |

Modified ICD_ScannerGetParametersPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_ScannerGetParametersPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     var theDict: Unmanaged<CFMutableDictionary>! } ``` |
| To | ``` struct ICD_ScannerGetParametersPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     var theDict: Unmanaged<CFMutableDictionary>!     init()     init(header header: ICDHeader, object object: ICAObject, objectInfo objectInfo: ICAObjectInfo, connectionID connectionID: ICAConnectionID, sessionID sessionID: ICAScannerSessionID, theDict theDict: Unmanaged<CFMutableDictionary>!) } ``` |

Modified ICD_ScannerInitializePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_ScannerInitializePB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID } ``` |
| To | ``` struct ICD_ScannerInitializePB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     init()     init(header header: ICDHeader, object object: ICAObject, objectInfo objectInfo: ICAObjectInfo, connectionID connectionID: ICAConnectionID, sessionID sessionID: ICAScannerSessionID) } ``` |

Modified ICD_ScannerObjectSendMessagePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_ScannerObjectSendMessagePB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var message: ICAMessage     var totalDataSize: UInt32     var result: UInt32 } ``` |
| To | ``` struct ICD_ScannerObjectSendMessagePB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var message: ICAMessage     var totalDataSize: UInt32     var result: UInt32     init()     init(header header: ICDHeader, object object: ICAObject, objectInfo objectInfo: ICAObjectInfo, connectionID connectionID: ICAConnectionID, message message: ICAMessage, totalDataSize totalDataSize: UInt32, result result: UInt32) } ``` |

Modified ICD_ScannerOpenSessionPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_ScannerOpenSessionPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID } ``` |
| To | ``` struct ICD_ScannerOpenSessionPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     init()     init(header header: ICDHeader, object object: ICAObject, objectInfo objectInfo: ICAObjectInfo, connectionID connectionID: ICAConnectionID, sessionID sessionID: ICAScannerSessionID) } ``` |

Modified ICD_ScannerSetParametersPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_ScannerSetParametersPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     var theDict: Unmanaged<CFMutableDictionary>! } ``` |
| To | ``` struct ICD_ScannerSetParametersPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     var theDict: Unmanaged<CFMutableDictionary>!     init()     init(header header: ICDHeader, object object: ICAObject, objectInfo objectInfo: ICAObjectInfo, connectionID connectionID: ICAConnectionID, sessionID sessionID: ICAScannerSessionID, theDict theDict: Unmanaged<CFMutableDictionary>!) } ``` |

Modified ICD_ScannerStartPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_ScannerStartPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID } ``` |
| To | ``` struct ICD_ScannerStartPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     init()     init(header header: ICDHeader, object object: ICAObject, objectInfo objectInfo: ICAObjectInfo, connectionID connectionID: ICAConnectionID, sessionID sessionID: ICAScannerSessionID) } ``` |

Modified ICD_ScannerStatusPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_ScannerStatusPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     var status: UInt32 } ``` |
| To | ``` struct ICD_ScannerStatusPB {     var header: ICDHeader     var object: ICAObject     var objectInfo: ICAObjectInfo     var connectionID: ICAConnectionID     var sessionID: ICAScannerSessionID     var status: UInt32     init()     init(header header: ICDHeader, object object: ICAObject, objectInfo objectInfo: ICAObjectInfo, connectionID connectionID: ICAConnectionID, sessionID sessionID: ICAScannerSessionID, status status: UInt32) } ``` |

Modified ICD_Scannerscanner_callback_functions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_Scannerscanner_callback_functions {     var f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice     var f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath     var f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice     var f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask     var f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo     var f_ICD_ScannerCleanup: __ICD_ScannerCleanup     var f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData     var f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData     var f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData     var f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData     var f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage     var f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary     var f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice     var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath     var f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession     var f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession     var f_ICD_ScannerInitialize: __ICD_ScannerInitialize     var f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters     var f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters     var f_ICD_ScannerStatus: __ICD_ScannerStatus     var f_ICD_ScannerStart: __ICD_ScannerStart     var f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice     var f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice     var f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile     var f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice     var f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor     var f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64 } ``` |
| To | ``` struct ICD_Scannerscanner_callback_functions {     var f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice     var f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath     var f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice     var f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask     var f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo     var f_ICD_ScannerCleanup: __ICD_ScannerCleanup     var f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData     var f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData     var f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData     var f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData     var f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage     var f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary     var f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice     var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath     var f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession     var f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession     var f_ICD_ScannerInitialize: __ICD_ScannerInitialize     var f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters     var f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters     var f_ICD_ScannerStatus: __ICD_ScannerStatus     var f_ICD_ScannerStart: __ICD_ScannerStart     var f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice     var f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice     var f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile     var f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice     var f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor     var f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64     init()     init(f_ICD_ScannerOpenUSBDevice f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice, f_ICD_ScannerOpenUSBDeviceWithIORegPath f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath, f_ICD_ScannerCloseDevice f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice, f_ICD_ScannerPeriodicTask f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask, f_ICD_ScannerGetObjectInfo f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo, f_ICD_ScannerCleanup f_ICD_ScannerCleanup: __ICD_ScannerCleanup, f_ICD_ScannerGetPropertyData f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData, f_ICD_ScannerSetPropertyData f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData, f_ICD_ScannerReadFileData f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData, f_ICD_ScannerWriteFileData f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData, f_ICD_ScannerSendMessage f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage, f_ICD_ScannerAddPropertiesToCFDictionary f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary, f_ICD_ScannerOpenFireWireDevice f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice, f_ICD_ScannerOpenFireWireDeviceWithIORegPath f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath, f_ICD_ScannerOpenSession f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession, f_ICD_ScannerCloseSession f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession, f_ICD_ScannerInitialize f_ICD_ScannerInitialize: __ICD_ScannerInitialize, f_ICD_ScannerGetParameters f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters, f_ICD_ScannerSetParameters f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters, f_ICD_ScannerStatus f_ICD_ScannerStatus: __ICD_ScannerStatus, f_ICD_ScannerStart f_ICD_ScannerStart: __ICD_ScannerStart, f_ICD_ScannerOpenBluetoothDevice f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice, f_ICD_ScannerOpenTCPIPDevice f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice, f_ICD_ScannerWriteDataToFile f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile, f_ICD_ScannerOpenMassStorageDevice f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice, f_ICD_ScannerWriteDataToFileDescriptor f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor, f_ICD_ScannerWriteDataToFileDescriptor64 f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64) } ``` |

Modified ICD_callback_functions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_callback_functions {     var f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice     var f_ICD_CloseDevice: __ICD_CloseDevice     var f_ICD_PeriodicTask: __ICD_PeriodicTask     var f_ICD_GetObjectInfo: __ICD_GetObjectInfo     var f_ICD_Cleanup: __ICD_Cleanup     var f_ICD_GetPropertyData: __ICD_GetPropertyData     var f_ICD_SetPropertyData: __ICD_SetPropertyData     var f_ICD_ReadFileData: __ICD_ReadFileData     var f_ICD_WriteFileData: __ICD_WriteFileData     var f_ICD_SendMessage: __ICD_SendMessage     var f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary     var f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice     var f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath     var f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath     var f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice     var f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice     var f_ICD_WriteDataToFile: __ICD_WriteDataToFile     var f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice     var f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor     var f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64 } ``` |
| To | ``` struct ICD_callback_functions {     var f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice     var f_ICD_CloseDevice: __ICD_CloseDevice     var f_ICD_PeriodicTask: __ICD_PeriodicTask     var f_ICD_GetObjectInfo: __ICD_GetObjectInfo     var f_ICD_Cleanup: __ICD_Cleanup     var f_ICD_GetPropertyData: __ICD_GetPropertyData     var f_ICD_SetPropertyData: __ICD_SetPropertyData     var f_ICD_ReadFileData: __ICD_ReadFileData     var f_ICD_WriteFileData: __ICD_WriteFileData     var f_ICD_SendMessage: __ICD_SendMessage     var f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary     var f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice     var f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath     var f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath     var f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice     var f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice     var f_ICD_WriteDataToFile: __ICD_WriteDataToFile     var f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice     var f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor     var f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64     init()     init(f_ICD_OpenUSBDevice f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice, f_ICD_CloseDevice f_ICD_CloseDevice: __ICD_CloseDevice, f_ICD_PeriodicTask f_ICD_PeriodicTask: __ICD_PeriodicTask, f_ICD_GetObjectInfo f_ICD_GetObjectInfo: __ICD_GetObjectInfo, f_ICD_Cleanup f_ICD_Cleanup: __ICD_Cleanup, f_ICD_GetPropertyData f_ICD_GetPropertyData: __ICD_GetPropertyData, f_ICD_SetPropertyData f_ICD_SetPropertyData: __ICD_SetPropertyData, f_ICD_ReadFileData f_ICD_ReadFileData: __ICD_ReadFileData, f_ICD_WriteFileData f_ICD_WriteFileData: __ICD_WriteFileData, f_ICD_SendMessage f_ICD_SendMessage: __ICD_SendMessage, f_ICD_AddPropertiesToCFDictionary f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary, f_ICD_OpenFireWireDevice f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice, f_ICD_OpenUSBDeviceWithIORegPath f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath, f_ICD_OpenFireWireDeviceWithIORegPath f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath, f_ICD_OpenBluetoothDevice f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice, f_ICD_OpenTCPIPDevice f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice, f_ICD_WriteDataToFile f_ICD_WriteDataToFile: __ICD_WriteDataToFile, f_ICD_OpenMassStorageDevice f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice, f_ICD_WriteDataToFileDescriptor f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor, f_ICD_WriteDataToFileDescriptor64 f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64) } ``` |

Modified ObjectInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ObjectInfo {     var icaObject: ICAObject     var reserved: UInt     var icaObjectInfo: ICAObjectInfo     var uniqueID: UInt32     var thumbnailSize: UInt32     var dataSize: UInt32     var dataWidth: UInt32     var dataHeight: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var flags: UInt32     var privateData: Ptr     var uniqueIDFireWire: UInt64     var tag: UInt32     var dataSize64: UInt64 } ``` |
| To | ``` struct ObjectInfo {     var icaObject: ICAObject     var reserved: UInt     var icaObjectInfo: ICAObjectInfo     var uniqueID: UInt32     var thumbnailSize: UInt32     var dataSize: UInt32     var dataWidth: UInt32     var dataHeight: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var flags: UInt32     var privateData: Ptr     var uniqueIDFireWire: UInt64     var tag: UInt32     var dataSize64: UInt64     init()     init(icaObject icaObject: ICAObject, reserved reserved: UInt, icaObjectInfo icaObjectInfo: ICAObjectInfo, uniqueID uniqueID: UInt32, thumbnailSize thumbnailSize: UInt32, dataSize dataSize: UInt32, dataWidth dataWidth: UInt32, dataHeight dataHeight: UInt32, name name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags flags: UInt32, privateData privateData: Ptr, uniqueIDFireWire uniqueIDFireWire: UInt64, tag tag: UInt32, dataSize64 dataSize64: UInt64) } ``` |

Modified ScannerObjectInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScannerObjectInfo {     var icaObject: ICAObject     var reserved: UInt     var icaObjectInfo: ICAObjectInfo     var uniqueID: UInt32     var uniqueIDFireWire: UInt64     var thumbnailSize: UInt32     var dataSize: UInt32     var dataWidth: UInt32     var dataHeight: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var flags: UInt32     var privateData: Ptr     var tag: UInt32 } ``` |
| To | ``` struct ScannerObjectInfo {     var icaObject: ICAObject     var reserved: UInt     var icaObjectInfo: ICAObjectInfo     var uniqueID: UInt32     var uniqueIDFireWire: UInt64     var thumbnailSize: UInt32     var dataSize: UInt32     var dataWidth: UInt32     var dataHeight: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var flags: UInt32     var privateData: Ptr     var tag: UInt32     init()     init(icaObject icaObject: ICAObject, reserved reserved: UInt, icaObjectInfo icaObjectInfo: ICAObjectInfo, uniqueID uniqueID: UInt32, uniqueIDFireWire uniqueIDFireWire: UInt64, thumbnailSize thumbnailSize: UInt32, dataSize dataSize: UInt32, dataWidth dataWidth: UInt32, dataHeight dataHeight: UInt32, name name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags flags: UInt32, privateData privateData: Ptr, tag tag: UInt32) } ``` |

Modified ICDAddBandInfoToNotificationDictionary(CFMutableDictionary!, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UnsafeMutablePointer<Void>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDAddBandInfoToNotificationDictionary(_ dict: CFMutableDictionary!, _ width: UInt32, _ height: UInt32, _ bitsPerPixel: UInt32, _ bitsPerComponent: UInt32, _ numComponents: UInt32, _ endianness: UInt32, _ pixelDataType: UInt32, _ bytesPerRow: UInt32, _ dataStartRow: UInt32, _ dataNumberOfRows: UInt32, _ dataSize: UInt32, _ dataBuffer: UnsafePointer<()>) -> ICAError ``` |
| To | ``` func ICDAddBandInfoToNotificationDictionary(_ dict: CFMutableDictionary!, _ width: UInt32, _ height: UInt32, _ bitsPerPixel: UInt32, _ bitsPerComponent: UInt32, _ numComponents: UInt32, _ endianness: UInt32, _ pixelDataType: UInt32, _ bytesPerRow: UInt32, _ dataStartRow: UInt32, _ dataNumberOfRows: UInt32, _ dataSize: UInt32, _ dataBuffer: UnsafeMutablePointer<Void>) -> ICAError ``` |

Modified ICDAddImageInfoToNotificationDictionary(CFMutableDictionary!, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UnsafeMutablePointer<Void>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDAddImageInfoToNotificationDictionary(_ dict: CFMutableDictionary!, _ width: UInt32, _ height: UInt32, _ bytesPerRow: UInt32, _ dataStartRow: UInt32, _ dataNumberOfRows: UInt32, _ dataSize: UInt32, _ dataBuffer: UnsafePointer<()>) -> ICAError ``` |
| To | ``` func ICDAddImageInfoToNotificationDictionary(_ dict: CFMutableDictionary!, _ width: UInt32, _ height: UInt32, _ bytesPerRow: UInt32, _ dataStartRow: UInt32, _ dataNumberOfRows: UInt32, _ dataSize: UInt32, _ dataBuffer: UnsafeMutablePointer<Void>) -> ICAError ``` |

Modified ICDConnectFWDeviceWithIORegPath(UInt64, UnsafeMutablePointer<Int8>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDConnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDConnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |

Modified ICDConnectUSBDeviceWithIORegPath(UInt32, UnsafeMutablePointer<Int8>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDConnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDConnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |

Modified ICDCopyDeviceInfoDictionary(UnsafePointer<Int8>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDCopyDeviceInfoDictionary(_ deviceName: ConstUnsafePointer<Int8>, _ theDict: UnsafePointer<Unmanaged<CFDictionary>?>) -> ICAError ``` |
| To | ``` func ICDCopyDeviceInfoDictionary(_ deviceName: UnsafePointer<Int8>, _ theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> ICAError ``` |

Modified ICDCreateColorSpace(UInt32, UInt32, ICAObject, CFString!, CFData!, UnsafeMutablePointer<Int8>) -> Unmanaged<CGColorSpace>!

|  | Declaration |
| --- | --- |
| From | ``` func ICDCreateColorSpace(_ bitsPerPixel: UInt32, _ samplesPerPixel: UInt32, _ icaObject: ICAObject, _ colorSyncMode: CFString!, _ abstractProfile: CFData!, _ tmpProfilePath: UnsafePointer<Int8>) -> Unmanaged<CGColorSpace>! ``` |
| To | ``` func ICDCreateColorSpace(_ bitsPerPixel: UInt32, _ samplesPerPixel: UInt32, _ icaObject: ICAObject, _ colorSyncMode: CFString!, _ abstractProfile: CFData!, _ tmpProfilePath: UnsafeMutablePointer<Int8>) -> Unmanaged<CGColorSpace>! ``` |

Modified ICDCreateEventDataCookie(ICAObject, UnsafeMutablePointer<ICAEventDataCookie>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDCreateEventDataCookie(_ object: ICAObject, _ cookie: UnsafePointer<ICAEventDataCookie>) -> ICAError ``` |
| To | ``` func ICDCreateEventDataCookie(_ object: ICAObject, _ cookie: UnsafeMutablePointer<ICAEventDataCookie>) -> ICAError ``` |

Modified ICDDisconnectFWDeviceWithIORegPath(UInt64, UnsafeMutablePointer<Int8>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDDisconnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDDisconnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |

Modified ICDDisconnectUSBDeviceWithIORegPath(UInt32, UnsafeMutablePointer<Int8>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDDisconnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDDisconnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |

Modified ICDGetStandardPropertyData(UnsafePointer<ObjectInfo>, UnsafeMutablePointer<Void>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDGetStandardPropertyData(_ objectInfo: ConstUnsafePointer<ObjectInfo>, _ pb: UnsafePointer<()>) -> ICAError ``` |
| To | ``` func ICDGetStandardPropertyData(_ objectInfo: UnsafePointer<ObjectInfo>, _ pb: UnsafeMutablePointer<Void>) -> ICAError ``` |

Modified ICDNewObjectCreated(UnsafePointer<ObjectInfo>, UnsafePointer<ObjectInfo>, ICDNewObjectCreatedCompletion) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDNewObjectCreated(_ parentInfo: ConstUnsafePointer<ObjectInfo>, _ objectInfo: ConstUnsafePointer<ObjectInfo>, _ completion: ICDNewObjectCreatedCompletion) -> ICAError ``` |
| To | ``` func ICDNewObjectCreated(_ parentInfo: UnsafePointer<ObjectInfo>, _ objectInfo: UnsafePointer<ObjectInfo>, _ completion: ICDNewObjectCreatedCompletion) -> ICAError ``` |

Modified ICDNewObjectCreatedCompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias ICDNewObjectCreatedCompletion = CFunctionPointer<((ConstUnsafePointer<ObjectInfo>) -> Void)> ``` |
| To | ``` typealias ICDNewObjectCreatedCompletion = CFunctionPointer<((UnsafePointer<ObjectInfo>) -> Void)> ``` |

Modified ICDNewObjectInfoCreated(UnsafePointer<ObjectInfo>, UInt32, UnsafeMutablePointer<ICAObject>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDNewObjectInfoCreated(_ parentInfo: ConstUnsafePointer<ObjectInfo>, _ index: UInt32, _ newICAObject: UnsafePointer<ICAObject>) -> ICAError ``` |
| To | ``` func ICDNewObjectInfoCreated(_ parentInfo: UnsafePointer<ObjectInfo>, _ index: UInt32, _ newICAObject: UnsafeMutablePointer<ICAObject>) -> ICAError ``` |

Modified ICDScannerConnectFWDeviceWithIORegPath(UInt64, UnsafeMutablePointer<Int8>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerConnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDScannerConnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |

Modified ICDScannerConnectUSBDeviceWithIORegPath(UInt32, UnsafeMutablePointer<Int8>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerConnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDScannerConnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |

Modified ICDScannerCopyDeviceInfoDictionary(UnsafePointer<Int8>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerCopyDeviceInfoDictionary(_ deviceName: ConstUnsafePointer<Int8>, _ theDict: UnsafePointer<Unmanaged<CFDictionary>?>) -> ICAError ``` |
| To | ``` func ICDScannerCopyDeviceInfoDictionary(_ deviceName: UnsafePointer<Int8>, _ theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> ICAError ``` |

Modified ICDScannerCreateEventDataCookie(ICAObject, UnsafeMutablePointer<ICAEventDataCookie>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerCreateEventDataCookie(_ object: ICAObject, _ cookie: UnsafePointer<ICAEventDataCookie>) -> ICAError ``` |
| To | ``` func ICDScannerCreateEventDataCookie(_ object: ICAObject, _ cookie: UnsafeMutablePointer<ICAEventDataCookie>) -> ICAError ``` |

Modified ICDScannerDisconnectFWDeviceWithIORegPath(UInt64, UnsafeMutablePointer<Int8>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerDisconnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDScannerDisconnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |

Modified ICDScannerDisconnectUSBDeviceWithIORegPath(UInt32, UnsafeMutablePointer<Int8>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerDisconnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDScannerDisconnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |

Modified ICDScannerGetStandardPropertyData(UnsafePointer<ScannerObjectInfo>, UnsafeMutablePointer<Void>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerGetStandardPropertyData(_ objectInfo: ConstUnsafePointer<ScannerObjectInfo>, _ pb: UnsafePointer<()>) -> ICAError ``` |
| To | ``` func ICDScannerGetStandardPropertyData(_ objectInfo: UnsafePointer<ScannerObjectInfo>, _ pb: UnsafeMutablePointer<Void>) -> ICAError ``` |

Modified ICDScannerNewObjectInfoCreated(UnsafePointer<ScannerObjectInfo>, UInt32, UnsafeMutablePointer<ICAObject>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerNewObjectInfoCreated(_ parentInfo: ConstUnsafePointer<ScannerObjectInfo>, _ index: UInt32, _ newICAObject: UnsafePointer<ICAObject>) -> ICAError ``` |
| To | ``` func ICDScannerNewObjectInfoCreated(_ parentInfo: UnsafePointer<ScannerObjectInfo>, _ index: UInt32, _ newICAObject: UnsafeMutablePointer<ICAObject>) -> ICAError ``` |

Modified ICDSendNotification(UnsafeMutablePointer<ICASendNotificationPB>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDSendNotification(_ pb: UnsafePointer<ICASendNotificationPB>) -> ICAError ``` |
| To | ``` func ICDSendNotification(_ pb: UnsafeMutablePointer<ICASendNotificationPB>) -> ICAError ``` |

Modified ICDSendNotificationAndWaitForReply(UnsafeMutablePointer<ICASendNotificationPB>) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDSendNotificationAndWaitForReply(_ pb: UnsafePointer<ICASendNotificationPB>) -> ICAError ``` |
| To | ``` func ICDSendNotificationAndWaitForReply(_ pb: UnsafeMutablePointer<ICASendNotificationPB>) -> ICAError ``` |

Modified ICD_ScannerMain(Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ICD_ScannerMain(_ argc: Int32, _ argv: UnsafePointer<ConstUnsafePointer<Int8>>) -> Int32 ``` |
| To | ``` func ICD_ScannerMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32 ``` |

Modified ICD_main(Int32, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ICD_main(_ argc: Int32, _ argv: UnsafePointer<ConstUnsafePointer<Int8>>) -> Int32 ``` |
| To | ``` func ICD_main(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32 ``` |

Modified kICUTTypeRaw

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

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
