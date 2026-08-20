---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/ICADevices.html
archived_at: '2026-07-18T02:51:25.589091Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# ICADevices Changes for Swift

### ICADevices

Removed ICACopyObjectDataPB.init(header: ICAHeader, object: ICAObject, startByte: Int, requestedSize: Int, data: UnsafeMutablePointer<Unmanaged<CFData>?>)Removed ICACopyObjectPropertyDictionaryPB.init(header: ICAHeader, object: ICAObject, theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>)Removed ICACopyObjectThumbnailPB.init(header: ICAHeader, object: ICAObject, thumbnailFormat: OSType, thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>)Removed ICADownloadFilePB.init(header: ICAHeader, object: ICAObject, dirFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32, fileType: OSType, fileCreator: OSType, rotationAngle: Fixed, fileFSRef: UnsafeMutablePointer<FSRef>)Removed ICAImportImagePB.init(header: ICAHeader, deviceObject: ICAObject, flags: UInt32, supportedFileTypes: Unmanaged<CFArray>!, filterProc: ICAImportFilterProc!, importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>)Removed ICAMessage.init(messageType: OSType, startByte: UInt32, dataPtr: UnsafeMutablePointer<Void>, dataSize: UInt32, dataType: OSType)Removed ICARegisterForEventNotificationPB.init(header: ICAHeader, objectOfInterest: ICAObject, eventsOfInterest: Unmanaged<CFArray>!, notificationProc: ICANotification!, options: Unmanaged<CFDictionary>!)Removed ICAUploadFilePB.init(header: ICAHeader, parentObject: ICAObject, fileFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32)Removed ICD_callback_functions.init(f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice!, f_ICD_CloseDevice: __ICD_CloseDevice!, f_ICD_PeriodicTask: __ICD_PeriodicTask!, f_ICD_GetObjectInfo: __ICD_GetObjectInfo!, f_ICD_Cleanup: __ICD_Cleanup!, f_ICD_GetPropertyData: __ICD_GetPropertyData!, f_ICD_SetPropertyData: __ICD_SetPropertyData!, f_ICD_ReadFileData: __ICD_ReadFileData!, f_ICD_WriteFileData: __ICD_WriteFileData!, f_ICD_SendMessage: __ICD_SendMessage!, f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary!, f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice!, f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath!, f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath!, f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice!, f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice!, f_ICD_WriteDataToFile: __ICD_WriteDataToFile!, f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice!, f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor!, f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64!)Removed ICD_Scannerscanner_callback_functions.init(f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice!, f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath!, f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice!, f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask!, f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo!, f_ICD_ScannerCleanup: __ICD_ScannerCleanup!, f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData!, f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData!, f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData!, f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData!, f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage!, f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary!, f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice!, f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath!, f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession!, f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession!, f_ICD_ScannerInitialize: __ICD_ScannerInitialize!, f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters!, f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters!, f_ICD_ScannerStatus: __ICD_ScannerStatus!, f_ICD_ScannerStart: __ICD_ScannerStart!, f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice!, f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice!, f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile!, f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice!, f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor!, f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64!)Removed ObjectInfo.init(icaObject: ICAObject, reserved: UInt, icaObjectInfo: ICAObjectInfo, uniqueID: UInt32, thumbnailSize: UInt32, dataSize: UInt32, dataWidth: UInt32, dataHeight: UInt32, name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags: UInt32, privateData: Ptr, uniqueIDFireWire: UInt64, tag: UInt32, dataSize64: UInt64)Removed ScannerObjectInfo.init(icaObject: ICAObject, reserved: UInt, icaObjectInfo: ICAObjectInfo, uniqueID: UInt32, uniqueIDFireWire: UInt64, thumbnailSize: UInt32, dataSize: UInt32, dataWidth: UInt32, dataHeight: UInt32, name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags: UInt32, privateData: Ptr, tag: UInt32)Removed kAddMetaDataToFinderCommentRemoved kAdjustCreationDateRemoved kCreateCustomIconRemoved kDeleteAfterDownloadRemoved kDontEmbedColorSyncProfileRemoved kICAAllowMultipleImagesRemoved kICAButtonCopyRemoved kICAButtonEMailRemoved kICAButtonScanRemoved kICAButtonWebRemoved kICACameraPassThruNotUsedRemoved kICACameraPassThruReceiveRemoved kICACameraPassThruSendRemoved kICACannotYieldDeviceRemoved kICACommunicationErrRemoved kICADataTypeNotFoundErrRemoved kICADeviceRemoved kICADeviceAlreadyOpenErrRemoved kICADeviceCameraRemoved kICADeviceGUIDNotFoundErrRemoved kICADeviceInternalErrRemoved kICADeviceInvalidParamErrRemoved kICADeviceIOServicePathNotFoundErrRemoved kICADeviceLocationIDNotFoundErrRemoved kICADeviceMemoryAllocationErrRemoved kICADeviceMFPRemoved kICADeviceNotFoundErrRemoved kICADeviceNotOpenErrRemoved kICADeviceOtherRemoved kICADevicePDARemoved kICADevicePhoneRemoved kICADeviceScannerRemoved kICADeviceUnsupportedErrRemoved kICADirectoryRemoved kICADownloadAndReturnPathArrayRemoved kICAExtensionInternalErrRemoved kICAFileRemoved kICAFileAudioRemoved kICAFileCorruptedErrRemoved kICAFileFirmwareRemoved kICAFileImageRemoved kICAFileMovieRemoved kICAFileOtherRemoved kICAFlagReadAccessRemoved kICAFlagReadWriteAccessRemoved kICAFrameworkInternalErrRemoved kICAIndexOutOfRangeErrRemoved kICAInvalidObjectErrRemoved kICAInvalidPropertyErrRemoved kICAInvalidSessionErrRemoved kICAIOPendingErrRemoved kICAListRemoved kICAMessageCameraPassThroughRemoved kICAMessageCameraReadClockRemoved kICAMessageCheckDeviceRemoved kICAMessageConnectRemoved kICAMessageDeviceYieldRemoved kICAMessageDisconnectRemoved kICAMessageGetEventDataRemoved kICAMessageGetLastButtonPressedRemoved kICAMessageResetRemoved kICAMessageScannerOverviewSelectionChangedRemoved kICAPBVersionRemoved kICAPropertyRemoved kICAPropertyColorSpaceRemoved kICAPropertyColorSyncProfileRemoved kICAPropertyImageApertureRemoved kICAPropertyImageBitDepthRemoved kICAPropertyImageDataRemoved kICAPropertyImageDateDigitizedRemoved kICAPropertyImageDateOriginalRemoved kICAPropertyImageDPIRemoved kICAPropertyImageExposureTimeRemoved kICAPropertyImageFilenameRemoved kICAPropertyImageFlashRemoved kICAPropertyImageFNumberRemoved kICAPropertyImageHeightRemoved kICAPropertyImageShutterSpeedRemoved kICAPropertyImageSizeRemoved kICAPropertyImageThumbnailRemoved kICAPropertyImageWidthRemoved kICAPropertyTypeNotFoundErrRemoved kICASandboxViolationRemoved kICASecureSessionRequiredRemoved kICAThumbnailFormatJPEGRemoved kICAThumbnailFormatPNGRemoved kICAThumbnailFormatTIFFRemoved kICATypeBooleanRemoved kICATypeDataRemoved kICATypeFixedRemoved kICATypeFloatRemoved kICATypeSInt16Removed kICATypeSInt32Removed kICATypeSInt64Removed kICATypeStringRemoved kICATypeThumbnailRemoved kICATypeUInt16Removed kICATypeUInt32Removed kICATypeUInt64Removed kICATypeUInt8Removed kICAUploadFileAsIsRemoved kICAUploadFileScaleToFitRemoved kRotateImageRemoved kSetFileTypeAndCreatorAdded ICACopyObjectDataPB.init(header: ICAHeader, object: ICAObject, startByte: Int, requestedSize: Int, data: UnsafeMutablePointer<Unmanaged<CFData>?>!)Added ICACopyObjectPropertyDictionaryPB.init(header: ICAHeader, object: ICAObject, theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!)Added ICACopyObjectThumbnailPB.init(header: ICAHeader, object: ICAObject, thumbnailFormat: OSType, thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>!)Added ICADownloadFilePB.init(header: ICAHeader, object: ICAObject, dirFSRef: UnsafeMutablePointer<FSRef>!, flags: UInt32, fileType: OSType, fileCreator: OSType, rotationAngle: Fixed, fileFSRef: UnsafeMutablePointer<FSRef>!)Added ICAImportImagePB.init(header: ICAHeader, deviceObject: ICAObject, flags: UInt32, supportedFileTypes: Unmanaged<CFArray>!, filterProc: ICADevices.ICAImportFilterProc!, importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>!)Added ICAMessage.init(messageType: OSType, startByte: UInt32, dataPtr: UnsafeMutableRawPointer!, dataSize: UInt32, dataType: OSType)Added ICARegisterForEventNotificationPB.init(header: ICAHeader, objectOfInterest: ICAObject, eventsOfInterest: Unmanaged<CFArray>!, notificationProc: ICADevices.ICANotification!, options: Unmanaged<CFDictionary>!)Added ICAUploadFilePB.init(header: ICAHeader, parentObject: ICAObject, fileFSRef: UnsafeMutablePointer<FSRef>!, flags: UInt32)Added ICD_callback_functions.init(f_ICD_OpenUSBDevice: ICADevices.__ICD_OpenUSBDevice!, f_ICD_CloseDevice: ICADevices.__ICD_CloseDevice!, f_ICD_PeriodicTask: ICADevices.__ICD_PeriodicTask!, f_ICD_GetObjectInfo: ICADevices.__ICD_GetObjectInfo!, f_ICD_Cleanup: ICADevices.__ICD_Cleanup!, f_ICD_GetPropertyData: ICADevices.__ICD_GetPropertyData!, f_ICD_SetPropertyData: ICADevices.__ICD_SetPropertyData!, f_ICD_ReadFileData: ICADevices.__ICD_ReadFileData!, f_ICD_WriteFileData: ICADevices.__ICD_WriteFileData!, f_ICD_SendMessage: ICADevices.__ICD_SendMessage!, f_ICD_AddPropertiesToCFDictionary: ICADevices.__ICD_AddPropertiesToCFDictionary!, f_ICD_OpenFireWireDevice: ICADevices.__ICD_OpenFireWireDevice!, f_ICD_OpenUSBDeviceWithIORegPath: ICADevices.__ICD_OpenUSBDeviceWithIORegPath!, f_ICD_OpenFireWireDeviceWithIORegPath: ICADevices.__ICD_OpenFireWireDeviceWithIORegPath!, f_ICD_OpenBluetoothDevice: ICADevices.__ICD_OpenBluetoothDevice!, f_ICD_OpenTCPIPDevice: ICADevices.__ICD_OpenTCPIPDevice!, f_ICD_WriteDataToFile: ICADevices.__ICD_WriteDataToFile!, f_ICD_OpenMassStorageDevice: ICADevices.__ICD_OpenMassStorageDevice!, f_ICD_WriteDataToFileDescriptor: ICADevices.__ICD_WriteDataToFileDescriptor!, f_ICD_WriteDataToFileDescriptor64: ICADevices.__ICD_WriteDataToFileDescriptor64!)Added ICD_Scannerscanner_callback_functions.init(f_ICD_ScannerOpenUSBDevice: ICADevices.__ICD_ScannerOpenUSBDevice!, f_ICD_ScannerOpenUSBDeviceWithIORegPath: ICADevices.__ICD_ScannerOpenUSBDeviceWithIORegPath!, f_ICD_ScannerCloseDevice: ICADevices.__ICD_ScannerCloseDevice!, f_ICD_ScannerPeriodicTask: ICADevices.__ICD_ScannerPeriodicTask!, f_ICD_ScannerGetObjectInfo: ICADevices.__ICD_ScannerGetObjectInfo!, f_ICD_ScannerCleanup: ICADevices.__ICD_ScannerCleanup!, f_ICD_ScannerGetPropertyData: ICADevices.__ICD_ScannerGetPropertyData!, f_ICD_ScannerSetPropertyData: ICADevices.__ICD_ScannerSetPropertyData!, f_ICD_ScannerReadFileData: ICADevices.__ICD_ScannerReadFileData!, f_ICD_ScannerWriteFileData: ICADevices.__ICD_ScannerWriteFileData!, f_ICD_ScannerSendMessage: ICADevices.__ICD_ScannerSendMessage!, f_ICD_ScannerAddPropertiesToCFDictionary: ICADevices.__ICD_ScannerAddPropertiesToCFDictionary!, f_ICD_ScannerOpenFireWireDevice: ICADevices.__ICD_ScannerOpenFireWireDevice!, f_ICD_ScannerOpenFireWireDeviceWithIORegPath: ICADevices.__ICD_ScannerOpenFireWireDeviceWithIORegPath!, f_ICD_ScannerOpenSession: ICADevices.__ICD_ScannerOpenSession!, f_ICD_ScannerCloseSession: ICADevices.__ICD_ScannerCloseSession!, f_ICD_ScannerInitialize: ICADevices.__ICD_ScannerInitialize!, f_ICD_ScannerGetParameters: ICADevices.__ICD_ScannerGetParameters!, f_ICD_ScannerSetParameters: ICADevices.__ICD_ScannerSetParameters!, f_ICD_ScannerStatus: ICADevices.__ICD_ScannerStatus!, f_ICD_ScannerStart: ICADevices.__ICD_ScannerStart!, f_ICD_ScannerOpenBluetoothDevice: ICADevices.__ICD_ScannerOpenBluetoothDevice!, f_ICD_ScannerOpenTCPIPDevice: ICADevices.__ICD_ScannerOpenTCPIPDevice!, f_ICD_ScannerWriteDataToFile: ICADevices.__ICD_ScannerWriteDataToFile!, f_ICD_ScannerOpenMassStorageDevice: ICADevices.__ICD_ScannerOpenMassStorageDevice!, f_ICD_ScannerWriteDataToFileDescriptor: ICADevices.__ICD_ScannerWriteDataToFileDescriptor!, f_ICD_ScannerWriteDataToFileDescriptor64: ICADevices.__ICD_ScannerWriteDataToFileDescriptor64!)Added ObjectInfo.init(icaObject: ICAObject, reserved: UInt, icaObjectInfo: ICAObjectInfo, uniqueID: UInt32, thumbnailSize: UInt32, dataSize: UInt32, dataWidth: UInt32, dataHeight: UInt32, name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags: UInt32, privateData: Ptr!, uniqueIDFireWire: UInt64, tag: UInt32, dataSize64: UInt64)Added ScannerObjectInfo.init(icaObject: ICAObject, reserved: UInt, icaObjectInfo: ICAObjectInfo, uniqueID: UInt32, uniqueIDFireWire: UInt64, thumbnailSize: UInt32, dataSize: UInt32, dataWidth: UInt32, dataHeight: UInt32, name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags: UInt32, privateData: Ptr!, tag: UInt32)Added kAddMetaDataToFinderCommentAdded kAdjustCreationDateAdded kCreateCustomIconAdded kDeleteAfterDownloadAdded kDontEmbedColorSyncProfileAdded kICAAllowMultipleImagesAdded kICAButtonCopyAdded kICAButtonEMailAdded kICAButtonScanAdded kICAButtonWebAdded kICACameraPassThruNotUsedAdded kICACameraPassThruReceiveAdded kICACameraPassThruSendAdded kICACannotYieldDeviceAdded kICACommunicationErrAdded kICADataTypeNotFoundErrAdded kICADeviceAdded kICADeviceAlreadyOpenErrAdded kICADeviceCameraAdded kICADeviceGUIDNotFoundErrAdded kICADeviceInternalErrAdded kICADeviceInvalidParamErrAdded kICADeviceIOServicePathNotFoundErrAdded kICADeviceLocationIDNotFoundErrAdded kICADeviceMemoryAllocationErrAdded kICADeviceMFPAdded kICADeviceNotFoundErrAdded kICADeviceNotOpenErrAdded kICADeviceOtherAdded kICADevicePDAAdded kICADevicePhoneAdded kICADeviceScannerAdded kICADeviceUnsupportedErrAdded kICADirectoryAdded kICADownloadAndReturnPathArrayAdded kICAExtensionInternalErrAdded kICAFileAdded kICAFileAudioAdded kICAFileCorruptedErrAdded kICAFileFirmwareAdded kICAFileImageAdded kICAFileMovieAdded kICAFileOtherAdded kICAFlagReadAccessAdded kICAFlagReadWriteAccessAdded kICAFrameworkInternalErrAdded kICAIndexOutOfRangeErrAdded kICAInvalidObjectErrAdded kICAInvalidPropertyErrAdded kICAInvalidSessionErrAdded kICAIOPendingErrAdded kICAListAdded kICAMessageCameraPassThroughAdded kICAMessageCameraReadClockAdded kICAMessageCheckDeviceAdded kICAMessageConnectAdded kICAMessageDeviceYieldAdded kICAMessageDisconnectAdded kICAMessageGetEventDataAdded kICAMessageGetLastButtonPressedAdded kICAMessageResetAdded kICAMessageScannerOverviewSelectionChangedAdded kICAPBVersionAdded kICAPropertyAdded kICAPropertyColorSpaceAdded kICAPropertyColorSyncProfileAdded kICAPropertyImageApertureAdded kICAPropertyImageBitDepthAdded kICAPropertyImageDataAdded kICAPropertyImageDateDigitizedAdded kICAPropertyImageDateOriginalAdded kICAPropertyImageDPIAdded kICAPropertyImageExposureTimeAdded kICAPropertyImageFilenameAdded kICAPropertyImageFlashAdded kICAPropertyImageFNumberAdded kICAPropertyImageHeightAdded kICAPropertyImageShutterSpeedAdded kICAPropertyImageSizeAdded kICAPropertyImageThumbnailAdded kICAPropertyImageWidthAdded kICAPropertyTypeNotFoundErrAdded kICASandboxViolationAdded kICASecureSessionRequiredAdded kICAThumbnailFormatJPEGAdded kICAThumbnailFormatPNGAdded kICAThumbnailFormatTIFFAdded kICATypeBooleanAdded kICATypeDataAdded kICATypeFixedAdded kICATypeFloatAdded kICATypeSInt16Added kICATypeSInt32Added kICATypeSInt64Added kICATypeStringAdded kICATypeThumbnailAdded kICATypeUInt16Added kICATypeUInt32Added kICATypeUInt64Added kICATypeUInt8Added kICAUploadFileAsIsAdded kICAUploadFileScaleToFitAdded kRotateImageAdded kSetFileTypeAndCreatorModified ICACopyObjectDataPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICACopyObjectDataPB {     var header: ICAHeader     var object: ICAObject     var startByte: Int     var requestedSize: Int     var data: UnsafeMutablePointer<Unmanaged<CFData>?>     init()     init(header header: ICAHeader, object object: ICAObject, startByte startByte: Int, requestedSize requestedSize: Int, data data: UnsafeMutablePointer<Unmanaged<CFData>?>) } ``` |
| To | ``` struct ICACopyObjectDataPB {     var header: ICAHeader     var object: ICAObject     var startByte: Int     var requestedSize: Int     var data: UnsafeMutablePointer<Unmanaged<CFData>?>!     init()     init(header header: ICAHeader, object object: ICAObject, startByte startByte: Int, requestedSize requestedSize: Int, data data: UnsafeMutablePointer<Unmanaged<CFData>?>!) } ``` |

Modified ICACopyObjectDataPB.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafeMutablePointer<Unmanaged<CFData>?> ``` |
| To | ``` var data: UnsafeMutablePointer<Unmanaged<CFData>?>! ``` |

Modified ICACopyObjectPropertyDictionaryPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICACopyObjectPropertyDictionaryPB {     var header: ICAHeader     var object: ICAObject     var theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>     init()     init(header header: ICAHeader, object object: ICAObject, theDict theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) } ``` |
| To | ``` struct ICACopyObjectPropertyDictionaryPB {     var header: ICAHeader     var object: ICAObject     var theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!     init()     init(header header: ICAHeader, object object: ICAObject, theDict theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) } ``` |

Modified ICACopyObjectPropertyDictionaryPB.theDict

|  | Declaration |
| --- | --- |
| From | ``` var theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?> ``` |
| To | ``` var theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>! ``` |

Modified ICACopyObjectThumbnailPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICACopyObjectThumbnailPB {     var header: ICAHeader     var object: ICAObject     var thumbnailFormat: OSType     var thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>     init()     init(header header: ICAHeader, object object: ICAObject, thumbnailFormat thumbnailFormat: OSType, thumbnailData thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>) } ``` |
| To | ``` struct ICACopyObjectThumbnailPB {     var header: ICAHeader     var object: ICAObject     var thumbnailFormat: OSType     var thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>!     init()     init(header header: ICAHeader, object object: ICAObject, thumbnailFormat thumbnailFormat: OSType, thumbnailData thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>!) } ``` |

Modified ICACopyObjectThumbnailPB.thumbnailData

|  | Declaration |
| --- | --- |
| From | ``` var thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?> ``` |
| To | ``` var thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>! ``` |

Modified ICADownloadFilePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICADownloadFilePB {     var header: ICAHeader     var object: ICAObject     var dirFSRef: UnsafeMutablePointer<FSRef>     var flags: UInt32     var fileType: OSType     var fileCreator: OSType     var rotationAngle: Fixed     var fileFSRef: UnsafeMutablePointer<FSRef>     init()     init(header header: ICAHeader, object object: ICAObject, dirFSRef dirFSRef: UnsafeMutablePointer<FSRef>, flags flags: UInt32, fileType fileType: OSType, fileCreator fileCreator: OSType, rotationAngle rotationAngle: Fixed, fileFSRef fileFSRef: UnsafeMutablePointer<FSRef>) } ``` |
| To | ``` struct ICADownloadFilePB {     var header: ICAHeader     var object: ICAObject     var dirFSRef: UnsafeMutablePointer<FSRef>!     var flags: UInt32     var fileType: OSType     var fileCreator: OSType     var rotationAngle: Fixed     var fileFSRef: UnsafeMutablePointer<FSRef>!     init()     init(header header: ICAHeader, object object: ICAObject, dirFSRef dirFSRef: UnsafeMutablePointer<FSRef>!, flags flags: UInt32, fileType fileType: OSType, fileCreator fileCreator: OSType, rotationAngle rotationAngle: Fixed, fileFSRef fileFSRef: UnsafeMutablePointer<FSRef>!) } ``` |

Modified ICADownloadFilePB.dirFSRef

|  | Declaration |
| --- | --- |
| From | ``` var dirFSRef: UnsafeMutablePointer<FSRef> ``` |
| To | ``` var dirFSRef: UnsafeMutablePointer<FSRef>! ``` |

Modified ICADownloadFilePB.fileFSRef

|  | Declaration |
| --- | --- |
| From | ``` var fileFSRef: UnsafeMutablePointer<FSRef> ``` |
| To | ``` var fileFSRef: UnsafeMutablePointer<FSRef>! ``` |

Modified ICAImportImagePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAImportImagePB {     var header: ICAHeader     var deviceObject: ICAObject     var flags: UInt32     var supportedFileTypes: Unmanaged<CFArray>!     var filterProc: ICAImportFilterProc!     var importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>     init()     init(header header: ICAHeader, deviceObject deviceObject: ICAObject, flags flags: UInt32, supportedFileTypes supportedFileTypes: Unmanaged<CFArray>!, filterProc filterProc: ICAImportFilterProc!, importedImages importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>) } ``` |
| To | ``` struct ICAImportImagePB {     var header: ICAHeader     var deviceObject: ICAObject     var flags: UInt32     var supportedFileTypes: Unmanaged<CFArray>!     var filterProc: ICADevices.ICAImportFilterProc!     var importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>!     init()     init(header header: ICAHeader, deviceObject deviceObject: ICAObject, flags flags: UInt32, supportedFileTypes supportedFileTypes: Unmanaged<CFArray>!, filterProc filterProc: ICADevices.ICAImportFilterProc!, importedImages importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>!) } ``` |

Modified ICAImportImagePB.filterProc

|  | Declaration |
| --- | --- |
| From | ``` var filterProc: ICAImportFilterProc! ``` |
| To | ``` var filterProc: ICADevices.ICAImportFilterProc! ``` |

Modified ICAImportImagePB.importedImages

|  | Declaration |
| --- | --- |
| From | ``` var importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?> ``` |
| To | ``` var importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>! ``` |

Modified ICAMessage [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAMessage {     var messageType: OSType     var startByte: UInt32     var dataPtr: UnsafeMutablePointer<Void>     var dataSize: UInt32     var dataType: OSType     init()     init(messageType messageType: OSType, startByte startByte: UInt32, dataPtr dataPtr: UnsafeMutablePointer<Void>, dataSize dataSize: UInt32, dataType dataType: OSType) } ``` |
| To | ``` struct ICAMessage {     var messageType: OSType     var startByte: UInt32     var dataPtr: UnsafeMutableRawPointer!     var dataSize: UInt32     var dataType: OSType     init()     init(messageType messageType: OSType, startByte startByte: UInt32, dataPtr dataPtr: UnsafeMutableRawPointer!, dataSize dataSize: UInt32, dataType dataType: OSType) } ``` |

Modified ICAMessage.dataPtr

|  | Declaration |
| --- | --- |
| From | ``` var dataPtr: UnsafeMutablePointer<Void> ``` |
| To | ``` var dataPtr: UnsafeMutableRawPointer! ``` |

Modified ICARegisterForEventNotificationPB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICARegisterForEventNotificationPB {     var header: ICAHeader     var objectOfInterest: ICAObject     var eventsOfInterest: Unmanaged<CFArray>!     var notificationProc: ICANotification!     var options: Unmanaged<CFDictionary>!     init()     init(header header: ICAHeader, objectOfInterest objectOfInterest: ICAObject, eventsOfInterest eventsOfInterest: Unmanaged<CFArray>!, notificationProc notificationProc: ICANotification!, options options: Unmanaged<CFDictionary>!) } ``` |
| To | ``` struct ICARegisterForEventNotificationPB {     var header: ICAHeader     var objectOfInterest: ICAObject     var eventsOfInterest: Unmanaged<CFArray>!     var notificationProc: ICADevices.ICANotification!     var options: Unmanaged<CFDictionary>!     init()     init(header header: ICAHeader, objectOfInterest objectOfInterest: ICAObject, eventsOfInterest eventsOfInterest: Unmanaged<CFArray>!, notificationProc notificationProc: ICADevices.ICANotification!, options options: Unmanaged<CFDictionary>!) } ``` |

Modified ICARegisterForEventNotificationPB.notificationProc

|  | Declaration |
| --- | --- |
| From | ``` var notificationProc: ICANotification! ``` |
| To | ``` var notificationProc: ICADevices.ICANotification! ``` |

Modified ICAUploadFilePB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAUploadFilePB {     var header: ICAHeader     var parentObject: ICAObject     var fileFSRef: UnsafeMutablePointer<FSRef>     var flags: UInt32     init()     init(header header: ICAHeader, parentObject parentObject: ICAObject, fileFSRef fileFSRef: UnsafeMutablePointer<FSRef>, flags flags: UInt32) } ``` |
| To | ``` struct ICAUploadFilePB {     var header: ICAHeader     var parentObject: ICAObject     var fileFSRef: UnsafeMutablePointer<FSRef>!     var flags: UInt32     init()     init(header header: ICAHeader, parentObject parentObject: ICAObject, fileFSRef fileFSRef: UnsafeMutablePointer<FSRef>!, flags flags: UInt32) } ``` |

Modified ICAUploadFilePB.fileFSRef

|  | Declaration |
| --- | --- |
| From | ``` var fileFSRef: UnsafeMutablePointer<FSRef> ``` |
| To | ``` var fileFSRef: UnsafeMutablePointer<FSRef>! ``` |

Modified ICD_callback_functions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_callback_functions {     var f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice!     var f_ICD_CloseDevice: __ICD_CloseDevice!     var f_ICD_PeriodicTask: __ICD_PeriodicTask!     var f_ICD_GetObjectInfo: __ICD_GetObjectInfo!     var f_ICD_Cleanup: __ICD_Cleanup!     var f_ICD_GetPropertyData: __ICD_GetPropertyData!     var f_ICD_SetPropertyData: __ICD_SetPropertyData!     var f_ICD_ReadFileData: __ICD_ReadFileData!     var f_ICD_WriteFileData: __ICD_WriteFileData!     var f_ICD_SendMessage: __ICD_SendMessage!     var f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary!     var f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice!     var f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath!     var f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath!     var f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice!     var f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice!     var f_ICD_WriteDataToFile: __ICD_WriteDataToFile!     var f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice!     var f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor!     var f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64!     init()     init(f_ICD_OpenUSBDevice f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice!, f_ICD_CloseDevice f_ICD_CloseDevice: __ICD_CloseDevice!, f_ICD_PeriodicTask f_ICD_PeriodicTask: __ICD_PeriodicTask!, f_ICD_GetObjectInfo f_ICD_GetObjectInfo: __ICD_GetObjectInfo!, f_ICD_Cleanup f_ICD_Cleanup: __ICD_Cleanup!, f_ICD_GetPropertyData f_ICD_GetPropertyData: __ICD_GetPropertyData!, f_ICD_SetPropertyData f_ICD_SetPropertyData: __ICD_SetPropertyData!, f_ICD_ReadFileData f_ICD_ReadFileData: __ICD_ReadFileData!, f_ICD_WriteFileData f_ICD_WriteFileData: __ICD_WriteFileData!, f_ICD_SendMessage f_ICD_SendMessage: __ICD_SendMessage!, f_ICD_AddPropertiesToCFDictionary f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary!, f_ICD_OpenFireWireDevice f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice!, f_ICD_OpenUSBDeviceWithIORegPath f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath!, f_ICD_OpenFireWireDeviceWithIORegPath f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath!, f_ICD_OpenBluetoothDevice f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice!, f_ICD_OpenTCPIPDevice f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice!, f_ICD_WriteDataToFile f_ICD_WriteDataToFile: __ICD_WriteDataToFile!, f_ICD_OpenMassStorageDevice f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice!, f_ICD_WriteDataToFileDescriptor f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor!, f_ICD_WriteDataToFileDescriptor64 f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64!) } ``` |
| To | ``` struct ICD_callback_functions {     var f_ICD_OpenUSBDevice: ICADevices.__ICD_OpenUSBDevice!     var f_ICD_CloseDevice: ICADevices.__ICD_CloseDevice!     var f_ICD_PeriodicTask: ICADevices.__ICD_PeriodicTask!     var f_ICD_GetObjectInfo: ICADevices.__ICD_GetObjectInfo!     var f_ICD_Cleanup: ICADevices.__ICD_Cleanup!     var f_ICD_GetPropertyData: ICADevices.__ICD_GetPropertyData!     var f_ICD_SetPropertyData: ICADevices.__ICD_SetPropertyData!     var f_ICD_ReadFileData: ICADevices.__ICD_ReadFileData!     var f_ICD_WriteFileData: ICADevices.__ICD_WriteFileData!     var f_ICD_SendMessage: ICADevices.__ICD_SendMessage!     var f_ICD_AddPropertiesToCFDictionary: ICADevices.__ICD_AddPropertiesToCFDictionary!     var f_ICD_OpenFireWireDevice: ICADevices.__ICD_OpenFireWireDevice!     var f_ICD_OpenUSBDeviceWithIORegPath: ICADevices.__ICD_OpenUSBDeviceWithIORegPath!     var f_ICD_OpenFireWireDeviceWithIORegPath: ICADevices.__ICD_OpenFireWireDeviceWithIORegPath!     var f_ICD_OpenBluetoothDevice: ICADevices.__ICD_OpenBluetoothDevice!     var f_ICD_OpenTCPIPDevice: ICADevices.__ICD_OpenTCPIPDevice!     var f_ICD_WriteDataToFile: ICADevices.__ICD_WriteDataToFile!     var f_ICD_OpenMassStorageDevice: ICADevices.__ICD_OpenMassStorageDevice!     var f_ICD_WriteDataToFileDescriptor: ICADevices.__ICD_WriteDataToFileDescriptor!     var f_ICD_WriteDataToFileDescriptor64: ICADevices.__ICD_WriteDataToFileDescriptor64!     init()     init(f_ICD_OpenUSBDevice f_ICD_OpenUSBDevice: ICADevices.__ICD_OpenUSBDevice!, f_ICD_CloseDevice f_ICD_CloseDevice: ICADevices.__ICD_CloseDevice!, f_ICD_PeriodicTask f_ICD_PeriodicTask: ICADevices.__ICD_PeriodicTask!, f_ICD_GetObjectInfo f_ICD_GetObjectInfo: ICADevices.__ICD_GetObjectInfo!, f_ICD_Cleanup f_ICD_Cleanup: ICADevices.__ICD_Cleanup!, f_ICD_GetPropertyData f_ICD_GetPropertyData: ICADevices.__ICD_GetPropertyData!, f_ICD_SetPropertyData f_ICD_SetPropertyData: ICADevices.__ICD_SetPropertyData!, f_ICD_ReadFileData f_ICD_ReadFileData: ICADevices.__ICD_ReadFileData!, f_ICD_WriteFileData f_ICD_WriteFileData: ICADevices.__ICD_WriteFileData!, f_ICD_SendMessage f_ICD_SendMessage: ICADevices.__ICD_SendMessage!, f_ICD_AddPropertiesToCFDictionary f_ICD_AddPropertiesToCFDictionary: ICADevices.__ICD_AddPropertiesToCFDictionary!, f_ICD_OpenFireWireDevice f_ICD_OpenFireWireDevice: ICADevices.__ICD_OpenFireWireDevice!, f_ICD_OpenUSBDeviceWithIORegPath f_ICD_OpenUSBDeviceWithIORegPath: ICADevices.__ICD_OpenUSBDeviceWithIORegPath!, f_ICD_OpenFireWireDeviceWithIORegPath f_ICD_OpenFireWireDeviceWithIORegPath: ICADevices.__ICD_OpenFireWireDeviceWithIORegPath!, f_ICD_OpenBluetoothDevice f_ICD_OpenBluetoothDevice: ICADevices.__ICD_OpenBluetoothDevice!, f_ICD_OpenTCPIPDevice f_ICD_OpenTCPIPDevice: ICADevices.__ICD_OpenTCPIPDevice!, f_ICD_WriteDataToFile f_ICD_WriteDataToFile: ICADevices.__ICD_WriteDataToFile!, f_ICD_OpenMassStorageDevice f_ICD_OpenMassStorageDevice: ICADevices.__ICD_OpenMassStorageDevice!, f_ICD_WriteDataToFileDescriptor f_ICD_WriteDataToFileDescriptor: ICADevices.__ICD_WriteDataToFileDescriptor!, f_ICD_WriteDataToFileDescriptor64 f_ICD_WriteDataToFileDescriptor64: ICADevices.__ICD_WriteDataToFileDescriptor64!) } ``` |

Modified ICD_callback_functions.f_ICD_AddPropertiesToCFDictionary

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary! ``` |
| To | ``` var f_ICD_AddPropertiesToCFDictionary: ICADevices.__ICD_AddPropertiesToCFDictionary! ``` |

Modified ICD_callback_functions.f_ICD_Cleanup

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_Cleanup: __ICD_Cleanup! ``` |
| To | ``` var f_ICD_Cleanup: ICADevices.__ICD_Cleanup! ``` |

Modified ICD_callback_functions.f_ICD_CloseDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_CloseDevice: __ICD_CloseDevice! ``` |
| To | ``` var f_ICD_CloseDevice: ICADevices.__ICD_CloseDevice! ``` |

Modified ICD_callback_functions.f_ICD_GetObjectInfo

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_GetObjectInfo: __ICD_GetObjectInfo! ``` |
| To | ``` var f_ICD_GetObjectInfo: ICADevices.__ICD_GetObjectInfo! ``` |

Modified ICD_callback_functions.f_ICD_GetPropertyData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_GetPropertyData: __ICD_GetPropertyData! ``` |
| To | ``` var f_ICD_GetPropertyData: ICADevices.__ICD_GetPropertyData! ``` |

Modified ICD_callback_functions.f_ICD_OpenBluetoothDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice! ``` |
| To | ``` var f_ICD_OpenBluetoothDevice: ICADevices.__ICD_OpenBluetoothDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenFireWireDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice! ``` |
| To | ``` var f_ICD_OpenFireWireDevice: ICADevices.__ICD_OpenFireWireDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenFireWireDeviceWithIORegPath

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath! ``` |
| To | ``` var f_ICD_OpenFireWireDeviceWithIORegPath: ICADevices.__ICD_OpenFireWireDeviceWithIORegPath! ``` |

Modified ICD_callback_functions.f_ICD_OpenMassStorageDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice! ``` |
| To | ``` var f_ICD_OpenMassStorageDevice: ICADevices.__ICD_OpenMassStorageDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenTCPIPDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice! ``` |
| To | ``` var f_ICD_OpenTCPIPDevice: ICADevices.__ICD_OpenTCPIPDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenUSBDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice! ``` |
| To | ``` var f_ICD_OpenUSBDevice: ICADevices.__ICD_OpenUSBDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenUSBDeviceWithIORegPath

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath! ``` |
| To | ``` var f_ICD_OpenUSBDeviceWithIORegPath: ICADevices.__ICD_OpenUSBDeviceWithIORegPath! ``` |

Modified ICD_callback_functions.f_ICD_PeriodicTask

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_PeriodicTask: __ICD_PeriodicTask! ``` |
| To | ``` var f_ICD_PeriodicTask: ICADevices.__ICD_PeriodicTask! ``` |

Modified ICD_callback_functions.f_ICD_ReadFileData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ReadFileData: __ICD_ReadFileData! ``` |
| To | ``` var f_ICD_ReadFileData: ICADevices.__ICD_ReadFileData! ``` |

Modified ICD_callback_functions.f_ICD_SendMessage

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_SendMessage: __ICD_SendMessage! ``` |
| To | ``` var f_ICD_SendMessage: ICADevices.__ICD_SendMessage! ``` |

Modified ICD_callback_functions.f_ICD_SetPropertyData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_SetPropertyData: __ICD_SetPropertyData! ``` |
| To | ``` var f_ICD_SetPropertyData: ICADevices.__ICD_SetPropertyData! ``` |

Modified ICD_callback_functions.f_ICD_WriteDataToFile

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_WriteDataToFile: __ICD_WriteDataToFile! ``` |
| To | ``` var f_ICD_WriteDataToFile: ICADevices.__ICD_WriteDataToFile! ``` |

Modified ICD_callback_functions.f_ICD_WriteDataToFileDescriptor

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor! ``` |
| To | ``` var f_ICD_WriteDataToFileDescriptor: ICADevices.__ICD_WriteDataToFileDescriptor! ``` |

Modified ICD_callback_functions.f_ICD_WriteDataToFileDescriptor64

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64! ``` |
| To | ``` var f_ICD_WriteDataToFileDescriptor64: ICADevices.__ICD_WriteDataToFileDescriptor64! ``` |

Modified ICD_callback_functions.f_ICD_WriteFileData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_WriteFileData: __ICD_WriteFileData! ``` |
| To | ``` var f_ICD_WriteFileData: ICADevices.__ICD_WriteFileData! ``` |

Modified ICD_Scannerscanner_callback_functions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_Scannerscanner_callback_functions {     var f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice!     var f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath!     var f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice!     var f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask!     var f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo!     var f_ICD_ScannerCleanup: __ICD_ScannerCleanup!     var f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData!     var f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData!     var f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData!     var f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData!     var f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage!     var f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary!     var f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice!     var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath!     var f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession!     var f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession!     var f_ICD_ScannerInitialize: __ICD_ScannerInitialize!     var f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters!     var f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters!     var f_ICD_ScannerStatus: __ICD_ScannerStatus!     var f_ICD_ScannerStart: __ICD_ScannerStart!     var f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice!     var f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice!     var f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile!     var f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice!     var f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor!     var f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64!     init()     init(f_ICD_ScannerOpenUSBDevice f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice!, f_ICD_ScannerOpenUSBDeviceWithIORegPath f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath!, f_ICD_ScannerCloseDevice f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice!, f_ICD_ScannerPeriodicTask f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask!, f_ICD_ScannerGetObjectInfo f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo!, f_ICD_ScannerCleanup f_ICD_ScannerCleanup: __ICD_ScannerCleanup!, f_ICD_ScannerGetPropertyData f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData!, f_ICD_ScannerSetPropertyData f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData!, f_ICD_ScannerReadFileData f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData!, f_ICD_ScannerWriteFileData f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData!, f_ICD_ScannerSendMessage f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage!, f_ICD_ScannerAddPropertiesToCFDictionary f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary!, f_ICD_ScannerOpenFireWireDevice f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice!, f_ICD_ScannerOpenFireWireDeviceWithIORegPath f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath!, f_ICD_ScannerOpenSession f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession!, f_ICD_ScannerCloseSession f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession!, f_ICD_ScannerInitialize f_ICD_ScannerInitialize: __ICD_ScannerInitialize!, f_ICD_ScannerGetParameters f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters!, f_ICD_ScannerSetParameters f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters!, f_ICD_ScannerStatus f_ICD_ScannerStatus: __ICD_ScannerStatus!, f_ICD_ScannerStart f_ICD_ScannerStart: __ICD_ScannerStart!, f_ICD_ScannerOpenBluetoothDevice f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice!, f_ICD_ScannerOpenTCPIPDevice f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice!, f_ICD_ScannerWriteDataToFile f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile!, f_ICD_ScannerOpenMassStorageDevice f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice!, f_ICD_ScannerWriteDataToFileDescriptor f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor!, f_ICD_ScannerWriteDataToFileDescriptor64 f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64!) } ``` |
| To | ``` struct ICD_Scannerscanner_callback_functions {     var f_ICD_ScannerOpenUSBDevice: ICADevices.__ICD_ScannerOpenUSBDevice!     var f_ICD_ScannerOpenUSBDeviceWithIORegPath: ICADevices.__ICD_ScannerOpenUSBDeviceWithIORegPath!     var f_ICD_ScannerCloseDevice: ICADevices.__ICD_ScannerCloseDevice!     var f_ICD_ScannerPeriodicTask: ICADevices.__ICD_ScannerPeriodicTask!     var f_ICD_ScannerGetObjectInfo: ICADevices.__ICD_ScannerGetObjectInfo!     var f_ICD_ScannerCleanup: ICADevices.__ICD_ScannerCleanup!     var f_ICD_ScannerGetPropertyData: ICADevices.__ICD_ScannerGetPropertyData!     var f_ICD_ScannerSetPropertyData: ICADevices.__ICD_ScannerSetPropertyData!     var f_ICD_ScannerReadFileData: ICADevices.__ICD_ScannerReadFileData!     var f_ICD_ScannerWriteFileData: ICADevices.__ICD_ScannerWriteFileData!     var f_ICD_ScannerSendMessage: ICADevices.__ICD_ScannerSendMessage!     var f_ICD_ScannerAddPropertiesToCFDictionary: ICADevices.__ICD_ScannerAddPropertiesToCFDictionary!     var f_ICD_ScannerOpenFireWireDevice: ICADevices.__ICD_ScannerOpenFireWireDevice!     var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: ICADevices.__ICD_ScannerOpenFireWireDeviceWithIORegPath!     var f_ICD_ScannerOpenSession: ICADevices.__ICD_ScannerOpenSession!     var f_ICD_ScannerCloseSession: ICADevices.__ICD_ScannerCloseSession!     var f_ICD_ScannerInitialize: ICADevices.__ICD_ScannerInitialize!     var f_ICD_ScannerGetParameters: ICADevices.__ICD_ScannerGetParameters!     var f_ICD_ScannerSetParameters: ICADevices.__ICD_ScannerSetParameters!     var f_ICD_ScannerStatus: ICADevices.__ICD_ScannerStatus!     var f_ICD_ScannerStart: ICADevices.__ICD_ScannerStart!     var f_ICD_ScannerOpenBluetoothDevice: ICADevices.__ICD_ScannerOpenBluetoothDevice!     var f_ICD_ScannerOpenTCPIPDevice: ICADevices.__ICD_ScannerOpenTCPIPDevice!     var f_ICD_ScannerWriteDataToFile: ICADevices.__ICD_ScannerWriteDataToFile!     var f_ICD_ScannerOpenMassStorageDevice: ICADevices.__ICD_ScannerOpenMassStorageDevice!     var f_ICD_ScannerWriteDataToFileDescriptor: ICADevices.__ICD_ScannerWriteDataToFileDescriptor!     var f_ICD_ScannerWriteDataToFileDescriptor64: ICADevices.__ICD_ScannerWriteDataToFileDescriptor64!     init()     init(f_ICD_ScannerOpenUSBDevice f_ICD_ScannerOpenUSBDevice: ICADevices.__ICD_ScannerOpenUSBDevice!, f_ICD_ScannerOpenUSBDeviceWithIORegPath f_ICD_ScannerOpenUSBDeviceWithIORegPath: ICADevices.__ICD_ScannerOpenUSBDeviceWithIORegPath!, f_ICD_ScannerCloseDevice f_ICD_ScannerCloseDevice: ICADevices.__ICD_ScannerCloseDevice!, f_ICD_ScannerPeriodicTask f_ICD_ScannerPeriodicTask: ICADevices.__ICD_ScannerPeriodicTask!, f_ICD_ScannerGetObjectInfo f_ICD_ScannerGetObjectInfo: ICADevices.__ICD_ScannerGetObjectInfo!, f_ICD_ScannerCleanup f_ICD_ScannerCleanup: ICADevices.__ICD_ScannerCleanup!, f_ICD_ScannerGetPropertyData f_ICD_ScannerGetPropertyData: ICADevices.__ICD_ScannerGetPropertyData!, f_ICD_ScannerSetPropertyData f_ICD_ScannerSetPropertyData: ICADevices.__ICD_ScannerSetPropertyData!, f_ICD_ScannerReadFileData f_ICD_ScannerReadFileData: ICADevices.__ICD_ScannerReadFileData!, f_ICD_ScannerWriteFileData f_ICD_ScannerWriteFileData: ICADevices.__ICD_ScannerWriteFileData!, f_ICD_ScannerSendMessage f_ICD_ScannerSendMessage: ICADevices.__ICD_ScannerSendMessage!, f_ICD_ScannerAddPropertiesToCFDictionary f_ICD_ScannerAddPropertiesToCFDictionary: ICADevices.__ICD_ScannerAddPropertiesToCFDictionary!, f_ICD_ScannerOpenFireWireDevice f_ICD_ScannerOpenFireWireDevice: ICADevices.__ICD_ScannerOpenFireWireDevice!, f_ICD_ScannerOpenFireWireDeviceWithIORegPath f_ICD_ScannerOpenFireWireDeviceWithIORegPath: ICADevices.__ICD_ScannerOpenFireWireDeviceWithIORegPath!, f_ICD_ScannerOpenSession f_ICD_ScannerOpenSession: ICADevices.__ICD_ScannerOpenSession!, f_ICD_ScannerCloseSession f_ICD_ScannerCloseSession: ICADevices.__ICD_ScannerCloseSession!, f_ICD_ScannerInitialize f_ICD_ScannerInitialize: ICADevices.__ICD_ScannerInitialize!, f_ICD_ScannerGetParameters f_ICD_ScannerGetParameters: ICADevices.__ICD_ScannerGetParameters!, f_ICD_ScannerSetParameters f_ICD_ScannerSetParameters: ICADevices.__ICD_ScannerSetParameters!, f_ICD_ScannerStatus f_ICD_ScannerStatus: ICADevices.__ICD_ScannerStatus!, f_ICD_ScannerStart f_ICD_ScannerStart: ICADevices.__ICD_ScannerStart!, f_ICD_ScannerOpenBluetoothDevice f_ICD_ScannerOpenBluetoothDevice: ICADevices.__ICD_ScannerOpenBluetoothDevice!, f_ICD_ScannerOpenTCPIPDevice f_ICD_ScannerOpenTCPIPDevice: ICADevices.__ICD_ScannerOpenTCPIPDevice!, f_ICD_ScannerWriteDataToFile f_ICD_ScannerWriteDataToFile: ICADevices.__ICD_ScannerWriteDataToFile!, f_ICD_ScannerOpenMassStorageDevice f_ICD_ScannerOpenMassStorageDevice: ICADevices.__ICD_ScannerOpenMassStorageDevice!, f_ICD_ScannerWriteDataToFileDescriptor f_ICD_ScannerWriteDataToFileDescriptor: ICADevices.__ICD_ScannerWriteDataToFileDescriptor!, f_ICD_ScannerWriteDataToFileDescriptor64 f_ICD_ScannerWriteDataToFileDescriptor64: ICADevices.__ICD_ScannerWriteDataToFileDescriptor64!) } ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerAddPropertiesToCFDictionary

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary! ``` |
| To | ``` var f_ICD_ScannerAddPropertiesToCFDictionary: ICADevices.__ICD_ScannerAddPropertiesToCFDictionary! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerCleanup

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerCleanup: __ICD_ScannerCleanup! ``` |
| To | ``` var f_ICD_ScannerCleanup: ICADevices.__ICD_ScannerCleanup! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerCloseDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice! ``` |
| To | ``` var f_ICD_ScannerCloseDevice: ICADevices.__ICD_ScannerCloseDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerCloseSession

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession! ``` |
| To | ``` var f_ICD_ScannerCloseSession: ICADevices.__ICD_ScannerCloseSession! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerGetObjectInfo

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo! ``` |
| To | ``` var f_ICD_ScannerGetObjectInfo: ICADevices.__ICD_ScannerGetObjectInfo! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerGetParameters

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters! ``` |
| To | ``` var f_ICD_ScannerGetParameters: ICADevices.__ICD_ScannerGetParameters! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerGetPropertyData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData! ``` |
| To | ``` var f_ICD_ScannerGetPropertyData: ICADevices.__ICD_ScannerGetPropertyData! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerInitialize

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerInitialize: __ICD_ScannerInitialize! ``` |
| To | ``` var f_ICD_ScannerInitialize: ICADevices.__ICD_ScannerInitialize! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenBluetoothDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice! ``` |
| To | ``` var f_ICD_ScannerOpenBluetoothDevice: ICADevices.__ICD_ScannerOpenBluetoothDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenFireWireDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice! ``` |
| To | ``` var f_ICD_ScannerOpenFireWireDevice: ICADevices.__ICD_ScannerOpenFireWireDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenFireWireDeviceWithIORegPath

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath! ``` |
| To | ``` var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: ICADevices.__ICD_ScannerOpenFireWireDeviceWithIORegPath! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenMassStorageDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice! ``` |
| To | ``` var f_ICD_ScannerOpenMassStorageDevice: ICADevices.__ICD_ScannerOpenMassStorageDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenSession

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession! ``` |
| To | ``` var f_ICD_ScannerOpenSession: ICADevices.__ICD_ScannerOpenSession! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenTCPIPDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice! ``` |
| To | ``` var f_ICD_ScannerOpenTCPIPDevice: ICADevices.__ICD_ScannerOpenTCPIPDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenUSBDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice! ``` |
| To | ``` var f_ICD_ScannerOpenUSBDevice: ICADevices.__ICD_ScannerOpenUSBDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenUSBDeviceWithIORegPath

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath! ``` |
| To | ``` var f_ICD_ScannerOpenUSBDeviceWithIORegPath: ICADevices.__ICD_ScannerOpenUSBDeviceWithIORegPath! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerPeriodicTask

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask! ``` |
| To | ``` var f_ICD_ScannerPeriodicTask: ICADevices.__ICD_ScannerPeriodicTask! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerReadFileData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData! ``` |
| To | ``` var f_ICD_ScannerReadFileData: ICADevices.__ICD_ScannerReadFileData! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerSendMessage

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage! ``` |
| To | ``` var f_ICD_ScannerSendMessage: ICADevices.__ICD_ScannerSendMessage! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerSetParameters

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters! ``` |
| To | ``` var f_ICD_ScannerSetParameters: ICADevices.__ICD_ScannerSetParameters! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerSetPropertyData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData! ``` |
| To | ``` var f_ICD_ScannerSetPropertyData: ICADevices.__ICD_ScannerSetPropertyData! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerStart

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerStart: __ICD_ScannerStart! ``` |
| To | ``` var f_ICD_ScannerStart: ICADevices.__ICD_ScannerStart! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerStatus

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerStatus: __ICD_ScannerStatus! ``` |
| To | ``` var f_ICD_ScannerStatus: ICADevices.__ICD_ScannerStatus! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerWriteDataToFile

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile! ``` |
| To | ``` var f_ICD_ScannerWriteDataToFile: ICADevices.__ICD_ScannerWriteDataToFile! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerWriteDataToFileDescriptor

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor! ``` |
| To | ``` var f_ICD_ScannerWriteDataToFileDescriptor: ICADevices.__ICD_ScannerWriteDataToFileDescriptor! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerWriteDataToFileDescriptor64

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64! ``` |
| To | ``` var f_ICD_ScannerWriteDataToFileDescriptor64: ICADevices.__ICD_ScannerWriteDataToFileDescriptor64! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerWriteFileData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData! ``` |
| To | ``` var f_ICD_ScannerWriteFileData: ICADevices.__ICD_ScannerWriteFileData! ``` |

Modified ObjectInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ObjectInfo {     var icaObject: ICAObject     var reserved: UInt     var icaObjectInfo: ICAObjectInfo     var uniqueID: UInt32     var thumbnailSize: UInt32     var dataSize: UInt32     var dataWidth: UInt32     var dataHeight: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var flags: UInt32     var privateData: Ptr     var uniqueIDFireWire: UInt64     var tag: UInt32     var dataSize64: UInt64     init()     init(icaObject icaObject: ICAObject, reserved reserved: UInt, icaObjectInfo icaObjectInfo: ICAObjectInfo, uniqueID uniqueID: UInt32, thumbnailSize thumbnailSize: UInt32, dataSize dataSize: UInt32, dataWidth dataWidth: UInt32, dataHeight dataHeight: UInt32, name name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags flags: UInt32, privateData privateData: Ptr, uniqueIDFireWire uniqueIDFireWire: UInt64, tag tag: UInt32, dataSize64 dataSize64: UInt64) } ``` |
| To | ``` struct ObjectInfo {     var icaObject: ICAObject     var reserved: UInt     var icaObjectInfo: ICAObjectInfo     var uniqueID: UInt32     var thumbnailSize: UInt32     var dataSize: UInt32     var dataWidth: UInt32     var dataHeight: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var flags: UInt32     var privateData: Ptr!     var uniqueIDFireWire: UInt64     var tag: UInt32     var dataSize64: UInt64     init()     init(icaObject icaObject: ICAObject, reserved reserved: UInt, icaObjectInfo icaObjectInfo: ICAObjectInfo, uniqueID uniqueID: UInt32, thumbnailSize thumbnailSize: UInt32, dataSize dataSize: UInt32, dataWidth dataWidth: UInt32, dataHeight dataHeight: UInt32, name name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags flags: UInt32, privateData privateData: Ptr!, uniqueIDFireWire uniqueIDFireWire: UInt64, tag tag: UInt32, dataSize64 dataSize64: UInt64) } ``` |

Modified ObjectInfo.privateData

|  | Declaration |
| --- | --- |
| From | ``` var privateData: Ptr ``` |
| To | ``` var privateData: Ptr! ``` |

Modified ScannerObjectInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScannerObjectInfo {     var icaObject: ICAObject     var reserved: UInt     var icaObjectInfo: ICAObjectInfo     var uniqueID: UInt32     var uniqueIDFireWire: UInt64     var thumbnailSize: UInt32     var dataSize: UInt32     var dataWidth: UInt32     var dataHeight: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var flags: UInt32     var privateData: Ptr     var tag: UInt32     init()     init(icaObject icaObject: ICAObject, reserved reserved: UInt, icaObjectInfo icaObjectInfo: ICAObjectInfo, uniqueID uniqueID: UInt32, uniqueIDFireWire uniqueIDFireWire: UInt64, thumbnailSize thumbnailSize: UInt32, dataSize dataSize: UInt32, dataWidth dataWidth: UInt32, dataHeight dataHeight: UInt32, name name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags flags: UInt32, privateData privateData: Ptr, tag tag: UInt32) } ``` |
| To | ``` struct ScannerObjectInfo {     var icaObject: ICAObject     var reserved: UInt     var icaObjectInfo: ICAObjectInfo     var uniqueID: UInt32     var uniqueIDFireWire: UInt64     var thumbnailSize: UInt32     var dataSize: UInt32     var dataWidth: UInt32     var dataHeight: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var flags: UInt32     var privateData: Ptr!     var tag: UInt32     init()     init(icaObject icaObject: ICAObject, reserved reserved: UInt, icaObjectInfo icaObjectInfo: ICAObjectInfo, uniqueID uniqueID: UInt32, uniqueIDFireWire uniqueIDFireWire: UInt64, thumbnailSize thumbnailSize: UInt32, dataSize dataSize: UInt32, dataWidth dataWidth: UInt32, dataHeight dataHeight: UInt32, name name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), creationDate creationDate: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), flags flags: UInt32, privateData privateData: Ptr!, tag tag: UInt32) } ``` |

Modified ScannerObjectInfo.privateData

|  | Declaration |
| --- | --- |
| From | ``` var privateData: Ptr ``` |
| To | ``` var privateData: Ptr! ``` |

Modified ICACompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias ICACompletion = (UnsafeMutablePointer<ICAHeader>) -> Void ``` |
| To | ``` typealias ICACompletion = (UnsafeMutablePointer<ICAHeader>?) -> Swift.Void ``` |

Modified ICAImportFilterProc

|  | Declaration |
| --- | --- |
| From | ``` typealias ICAImportFilterProc = (CFDictionary!, UInt) -> DarwinBoolean ``` |
| To | ``` typealias ICAImportFilterProc = (CFDictionary?, UInt) -> DarwinBoolean ``` |

Modified ICANotification

|  | Declaration |
| --- | --- |
| From | ``` typealias ICANotification = (CFString!, CFDictionary!) -> Void ``` |
| To | ``` typealias ICANotification = (CFString?, CFDictionary?) -> Swift.Void ``` |

Modified ICANotificationProc

|  | Declaration |
| --- | --- |
| From | ``` typealias ICANotificationProc = (CFString!, CFDictionary!) -> Void ``` |
| To | ``` typealias ICANotificationProc = (CFString?, CFDictionary?) -> Swift.Void ``` |

Modified ICD_main(_: Int32, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ICD_main(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32 ``` |
| To | ``` func ICD_main(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafePointer<Int8>?>!) -> Int32 ``` |

Modified ICD_ScannerMain(_: Int32, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ICD_ScannerMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int32 ``` |
| To | ``` func ICD_ScannerMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafePointer<Int8>?>!) -> Int32 ``` |

Modified ICDAddBandInfoToNotificationDictionary(_: CFMutableDictionary!, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UnsafeMutableRawPointer!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDAddBandInfoToNotificationDictionary(_ dict: CFMutableDictionary!, _ width: UInt32, _ height: UInt32, _ bitsPerPixel: UInt32, _ bitsPerComponent: UInt32, _ numComponents: UInt32, _ endianness: UInt32, _ pixelDataType: UInt32, _ bytesPerRow: UInt32, _ dataStartRow: UInt32, _ dataNumberOfRows: UInt32, _ dataSize: UInt32, _ dataBuffer: UnsafeMutablePointer<Void>) -> ICAError ``` |
| To | ``` func ICDAddBandInfoToNotificationDictionary(_ dict: CFMutableDictionary!, _ width: UInt32, _ height: UInt32, _ bitsPerPixel: UInt32, _ bitsPerComponent: UInt32, _ numComponents: UInt32, _ endianness: UInt32, _ pixelDataType: UInt32, _ bytesPerRow: UInt32, _ dataStartRow: UInt32, _ dataNumberOfRows: UInt32, _ dataSize: UInt32, _ dataBuffer: UnsafeMutableRawPointer!) -> ICAError ``` |

Modified ICDAddImageInfoToNotificationDictionary(_: CFMutableDictionary!, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UnsafeMutableRawPointer!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDAddImageInfoToNotificationDictionary(_ dict: CFMutableDictionary!, _ width: UInt32, _ height: UInt32, _ bytesPerRow: UInt32, _ dataStartRow: UInt32, _ dataNumberOfRows: UInt32, _ dataSize: UInt32, _ dataBuffer: UnsafeMutablePointer<Void>) -> ICAError ``` |
| To | ``` func ICDAddImageInfoToNotificationDictionary(_ dict: CFMutableDictionary!, _ width: UInt32, _ height: UInt32, _ bytesPerRow: UInt32, _ dataStartRow: UInt32, _ dataNumberOfRows: UInt32, _ dataSize: UInt32, _ dataBuffer: UnsafeMutableRawPointer!) -> ICAError ``` |

Modified ICDCompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias ICDCompletion = (UnsafeMutablePointer<ICDHeader>) -> Void ``` |
| To | ``` typealias ICDCompletion = (UnsafeMutablePointer<ICDHeader>?) -> Swift.Void ``` |

Modified ICDConnectFWDeviceWithIORegPath(_: UInt64, _: UnsafeMutablePointer<Int8>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDConnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDConnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>!) -> ICAError ``` |

Modified ICDConnectUSBDeviceWithIORegPath(_: UInt32, _: UnsafeMutablePointer<Int8>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDConnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDConnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>!) -> ICAError ``` |

Modified ICDCopyDeviceInfoDictionary(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDCopyDeviceInfoDictionary(_ deviceName: UnsafePointer<Int8>, _ theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> ICAError ``` |
| To | ``` func ICDCopyDeviceInfoDictionary(_ deviceName: UnsafePointer<Int8>!, _ theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> ICAError ``` |

Modified ICDCreateColorSpace(_: UInt32, _: UInt32, _: ICAObject, _: CFString!, _: CFData!, _: UnsafeMutablePointer<Int8>!) -> Unmanaged<CGColorSpace>!

|  | Declaration |
| --- | --- |
| From | ``` func ICDCreateColorSpace(_ bitsPerPixel: UInt32, _ samplesPerPixel: UInt32, _ icaObject: ICAObject, _ colorSyncMode: CFString!, _ abstractProfile: CFData!, _ tmpProfilePath: UnsafeMutablePointer<Int8>) -> Unmanaged<CGColorSpace>! ``` |
| To | ``` func ICDCreateColorSpace(_ bitsPerPixel: UInt32, _ samplesPerPixel: UInt32, _ icaObject: ICAObject, _ colorSyncMode: CFString!, _ abstractProfile: CFData!, _ tmpProfilePath: UnsafeMutablePointer<Int8>!) -> Unmanaged<CGColorSpace>! ``` |

Modified ICDCreateEventDataCookie(_: ICAObject, _: UnsafeMutablePointer<ICAEventDataCookie>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDCreateEventDataCookie(_ object: ICAObject, _ cookie: UnsafeMutablePointer<ICAEventDataCookie>) -> ICAError ``` |
| To | ``` func ICDCreateEventDataCookie(_ object: ICAObject, _ cookie: UnsafeMutablePointer<ICAEventDataCookie>!) -> ICAError ``` |

Modified ICDDisconnectFWDeviceWithIORegPath(_: UInt64, _: UnsafeMutablePointer<Int8>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDDisconnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDDisconnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>!) -> ICAError ``` |

Modified ICDDisconnectUSBDeviceWithIORegPath(_: UInt32, _: UnsafeMutablePointer<Int8>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDDisconnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDDisconnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>!) -> ICAError ``` |

Modified ICDGetStandardPropertyData(_: UnsafePointer<ObjectInfo>!, _: UnsafeMutableRawPointer!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDGetStandardPropertyData(_ objectInfo: UnsafePointer<ObjectInfo>, _ pb: UnsafeMutablePointer<Void>) -> ICAError ``` |
| To | ``` func ICDGetStandardPropertyData(_ objectInfo: UnsafePointer<ObjectInfo>!, _ pb: UnsafeMutableRawPointer!) -> ICAError ``` |

Modified ICDNewObjectCreated(_: UnsafePointer<ObjectInfo>!, _: UnsafePointer<ObjectInfo>!, _: ICADevices.ICDNewObjectCreatedCompletion!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDNewObjectCreated(_ parentInfo: UnsafePointer<ObjectInfo>, _ objectInfo: UnsafePointer<ObjectInfo>, _ completion: ICDNewObjectCreatedCompletion!) -> ICAError ``` |
| To | ``` func ICDNewObjectCreated(_ parentInfo: UnsafePointer<ObjectInfo>!, _ objectInfo: UnsafePointer<ObjectInfo>!, _ completion: ICADevices.ICDNewObjectCreatedCompletion!) -> ICAError ``` |

Modified ICDNewObjectCreatedCompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias ICDNewObjectCreatedCompletion = (UnsafePointer<ObjectInfo>) -> Void ``` |
| To | ``` typealias ICDNewObjectCreatedCompletion = (UnsafePointer<ObjectInfo>?) -> Swift.Void ``` |

Modified ICDNewObjectInfoCreated(_: UnsafePointer<ObjectInfo>!, _: UInt32, _: UnsafeMutablePointer<ICAObject>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDNewObjectInfoCreated(_ parentInfo: UnsafePointer<ObjectInfo>, _ index: UInt32, _ newICAObject: UnsafeMutablePointer<ICAObject>) -> ICAError ``` |
| To | ``` func ICDNewObjectInfoCreated(_ parentInfo: UnsafePointer<ObjectInfo>!, _ index: UInt32, _ newICAObject: UnsafeMutablePointer<ICAObject>!) -> ICAError ``` |

Modified ICDScannerConnectFWDeviceWithIORegPath(_: UInt64, _: UnsafeMutablePointer<Int8>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerConnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDScannerConnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>!) -> ICAError ``` |

Modified ICDScannerConnectUSBDeviceWithIORegPath(_: UInt32, _: UnsafeMutablePointer<Int8>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerConnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDScannerConnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>!) -> ICAError ``` |

Modified ICDScannerCopyDeviceInfoDictionary(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerCopyDeviceInfoDictionary(_ deviceName: UnsafePointer<Int8>, _ theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> ICAError ``` |
| To | ``` func ICDScannerCopyDeviceInfoDictionary(_ deviceName: UnsafePointer<Int8>!, _ theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> ICAError ``` |

Modified ICDScannerCreateEventDataCookie(_: ICAObject, _: UnsafeMutablePointer<ICAEventDataCookie>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerCreateEventDataCookie(_ object: ICAObject, _ cookie: UnsafeMutablePointer<ICAEventDataCookie>) -> ICAError ``` |
| To | ``` func ICDScannerCreateEventDataCookie(_ object: ICAObject, _ cookie: UnsafeMutablePointer<ICAEventDataCookie>!) -> ICAError ``` |

Modified ICDScannerDisconnectFWDeviceWithIORegPath(_: UInt64, _: UnsafeMutablePointer<Int8>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerDisconnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDScannerDisconnectFWDeviceWithIORegPath(_ guid: UInt64, _ ioregPath: UnsafeMutablePointer<Int8>!) -> ICAError ``` |

Modified ICDScannerDisconnectUSBDeviceWithIORegPath(_: UInt32, _: UnsafeMutablePointer<Int8>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerDisconnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>) -> ICAError ``` |
| To | ``` func ICDScannerDisconnectUSBDeviceWithIORegPath(_ locationID: UInt32, _ ioregPath: UnsafeMutablePointer<Int8>!) -> ICAError ``` |

Modified ICDScannerGetStandardPropertyData(_: UnsafePointer<ScannerObjectInfo>!, _: UnsafeMutableRawPointer!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerGetStandardPropertyData(_ objectInfo: UnsafePointer<ScannerObjectInfo>, _ pb: UnsafeMutablePointer<Void>) -> ICAError ``` |
| To | ``` func ICDScannerGetStandardPropertyData(_ objectInfo: UnsafePointer<ScannerObjectInfo>!, _ pb: UnsafeMutableRawPointer!) -> ICAError ``` |

Modified ICDScannerNewObjectInfoCreated(_: UnsafePointer<ScannerObjectInfo>!, _: UInt32, _: UnsafeMutablePointer<ICAObject>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDScannerNewObjectInfoCreated(_ parentInfo: UnsafePointer<ScannerObjectInfo>, _ index: UInt32, _ newICAObject: UnsafeMutablePointer<ICAObject>) -> ICAError ``` |
| To | ``` func ICDScannerNewObjectInfoCreated(_ parentInfo: UnsafePointer<ScannerObjectInfo>!, _ index: UInt32, _ newICAObject: UnsafeMutablePointer<ICAObject>!) -> ICAError ``` |

Modified ICDSendNotification(_: UnsafeMutablePointer<ICASendNotificationPB>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDSendNotification(_ pb: UnsafeMutablePointer<ICASendNotificationPB>) -> ICAError ``` |
| To | ``` func ICDSendNotification(_ pb: UnsafeMutablePointer<ICASendNotificationPB>!) -> ICAError ``` |

Modified ICDSendNotificationAndWaitForReply(_: UnsafeMutablePointer<ICASendNotificationPB>!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDSendNotificationAndWaitForReply(_ pb: UnsafeMutablePointer<ICASendNotificationPB>) -> ICAError ``` |
| To | ``` func ICDSendNotificationAndWaitForReply(_ pb: UnsafeMutablePointer<ICASendNotificationPB>!) -> ICAError ``` |

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
