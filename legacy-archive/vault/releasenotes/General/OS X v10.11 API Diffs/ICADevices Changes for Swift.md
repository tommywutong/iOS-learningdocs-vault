---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/ICADevices.html
archived_at: '2026-07-18T02:53:35.737751Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ICADevices Changes for Swift

### ICADevices

Removed ICD_callback_functions.init(f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice, f_ICD_CloseDevice: __ICD_CloseDevice, f_ICD_PeriodicTask: __ICD_PeriodicTask, f_ICD_GetObjectInfo: __ICD_GetObjectInfo, f_ICD_Cleanup: __ICD_Cleanup, f_ICD_GetPropertyData: __ICD_GetPropertyData, f_ICD_SetPropertyData: __ICD_SetPropertyData, f_ICD_ReadFileData: __ICD_ReadFileData, f_ICD_WriteFileData: __ICD_WriteFileData, f_ICD_SendMessage: __ICD_SendMessage, f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary, f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice, f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath, f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath, f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice, f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice, f_ICD_WriteDataToFile: __ICD_WriteDataToFile, f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice, f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor, f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64)Removed ICD_Scannerscanner_callback_functions.init(f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice, f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath, f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice, f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask, f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo, f_ICD_ScannerCleanup: __ICD_ScannerCleanup, f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData, f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData, f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData, f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData, f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage, f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary, f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice, f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath, f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession, f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession, f_ICD_ScannerInitialize: __ICD_ScannerInitialize, f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters, f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters, f_ICD_ScannerStatus: __ICD_ScannerStatus, f_ICD_ScannerStart: __ICD_ScannerStart, f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice, f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice, f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile, f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice, f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor, f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64)Added ICACloseSessionPB [struct]Added ICACloseSessionPB.headerAdded ICACloseSessionPB.init()Added ICACloseSessionPB.init(header: ICAHeader, sessionID: ICASessionID)Added ICACloseSessionPB.sessionIDAdded ICACopyObjectDataPB [struct]Added ICACopyObjectDataPB.dataAdded ICACopyObjectDataPB.headerAdded ICACopyObjectDataPB.init()Added ICACopyObjectDataPB.init(header: ICAHeader, object: ICAObject, startByte: Int, requestedSize: Int, data: UnsafeMutablePointer<Unmanaged<CFData>?>)Added ICACopyObjectDataPB.objectAdded ICACopyObjectDataPB.requestedSizeAdded ICACopyObjectDataPB.startByteAdded ICACopyObjectPropertyDictionaryPB [struct]Added ICACopyObjectPropertyDictionaryPB.headerAdded ICACopyObjectPropertyDictionaryPB.init()Added ICACopyObjectPropertyDictionaryPB.init(header: ICAHeader, object: ICAObject, theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>)Added ICACopyObjectPropertyDictionaryPB.objectAdded ICACopyObjectPropertyDictionaryPB.theDictAdded ICACopyObjectThumbnailPB [struct]Added ICACopyObjectThumbnailPB.headerAdded ICACopyObjectThumbnailPB.init()Added ICACopyObjectThumbnailPB.init(header: ICAHeader, object: ICAObject, thumbnailFormat: OSType, thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>)Added ICACopyObjectThumbnailPB.objectAdded ICACopyObjectThumbnailPB.thumbnailDataAdded ICACopyObjectThumbnailPB.thumbnailFormatAdded ICADownloadFilePB [struct]Added ICADownloadFilePB.dirFSRefAdded ICADownloadFilePB.fileCreatorAdded ICADownloadFilePB.fileFSRefAdded ICADownloadFilePB.fileTypeAdded ICADownloadFilePB.flagsAdded ICADownloadFilePB.headerAdded ICADownloadFilePB.init()Added ICADownloadFilePB.init(header: ICAHeader, object: ICAObject, dirFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32, fileType: OSType, fileCreator: OSType, rotationAngle: Fixed, fileFSRef: UnsafeMutablePointer<FSRef>)Added ICADownloadFilePB.objectAdded ICADownloadFilePB.rotationAngleAdded ICAGetDeviceListPB [struct]Added ICAGetDeviceListPB.headerAdded ICAGetDeviceListPB.init()Added ICAGetDeviceListPB.init(header: ICAHeader, object: ICAObject)Added ICAGetDeviceListPB.objectAdded ICAHeader [struct]Added ICAHeader.errAdded ICAHeader.init()Added ICAHeader.init(err: ICAError, refcon: UInt)Added ICAHeader.refconAdded ICAImportImagePB [struct]Added ICAImportImagePB.deviceObjectAdded ICAImportImagePB.filterProcAdded ICAImportImagePB.flagsAdded ICAImportImagePB.headerAdded ICAImportImagePB.importedImagesAdded ICAImportImagePB.init()Added ICAImportImagePB.init(header: ICAHeader, deviceObject: ICAObject, flags: UInt32, supportedFileTypes: Unmanaged<CFArray>!, filterProc: ICAImportFilterProc!, importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>)Added ICAImportImagePB.supportedFileTypesAdded ICALoadDeviceModulePB [struct]Added ICALoadDeviceModulePB.headerAdded ICALoadDeviceModulePB.init()Added ICALoadDeviceModulePB.init(header: ICAHeader, paramDictionary: Unmanaged<CFDictionary>!)Added ICALoadDeviceModulePB.paramDictionaryAdded ICAMessage [struct]Added ICAMessage.dataPtrAdded ICAMessage.dataSizeAdded ICAMessage.dataTypeAdded ICAMessage.init()Added ICAMessage.init(messageType: OSType, startByte: UInt32, dataPtr: UnsafeMutablePointer<Void>, dataSize: UInt32, dataType: OSType)Added ICAMessage.messageTypeAdded ICAMessage.startByteAdded ICAObjectInfo [struct]Added ICAObjectInfo.init()Added ICAObjectInfo.init(objectType: OSType, objectSubtype: OSType)Added ICAObjectInfo.objectSubtypeAdded ICAObjectInfo.objectTypeAdded ICAObjectSendMessagePB [struct]Added ICAObjectSendMessagePB.headerAdded ICAObjectSendMessagePB.init()Added ICAObjectSendMessagePB.init(header: ICAHeader, object: ICAObject, message: ICAMessage, result: UInt32)Added ICAObjectSendMessagePB.messageAdded ICAObjectSendMessagePB.objectAdded ICAObjectSendMessagePB.resultAdded ICAOpenSessionPB [struct]Added ICAOpenSessionPB.deviceObjectAdded ICAOpenSessionPB.headerAdded ICAOpenSessionPB.init()Added ICAOpenSessionPB.init(header: ICAHeader, deviceObject: ICAObject, sessionID: ICASessionID)Added ICAOpenSessionPB.sessionIDAdded ICAPTPEventDataset [struct]Added ICAPTPEventDataset.containerTypeAdded ICAPTPEventDataset.dataLengthAdded ICAPTPEventDataset.eventCodeAdded ICAPTPEventDataset.init()Added ICAPTPEventDataset.init(dataLength: UInt32, containerType: UInt16, eventCode: UInt16, transactionID: UInt32, params: (UInt32, UInt32, UInt32))Added ICAPTPEventDataset.paramsAdded ICAPTPEventDataset.transactionIDAdded ICAPTPPassThroughPB [struct]Added ICAPTPPassThroughPB.commandCodeAdded ICAPTPPassThroughPB.dataAdded ICAPTPPassThroughPB.dataSizeAdded ICAPTPPassThroughPB.dataUsageModeAdded ICAPTPPassThroughPB.flagsAdded ICAPTPPassThroughPB.init()Added ICAPTPPassThroughPB.init(commandCode: UInt32, resultCode: UInt32, numOfInputParams: UInt32, numOfOutputParams: UInt32, params: (UInt32, UInt32, UInt32, UInt32), dataUsageMode: UInt32, flags: UInt32, dataSize: UInt32, data: (UInt8))Added ICAPTPPassThroughPB.numOfInputParamsAdded ICAPTPPassThroughPB.numOfOutputParamsAdded ICAPTPPassThroughPB.paramsAdded ICAPTPPassThroughPB.resultCodeAdded ICARegisterForEventNotificationPB [struct]Added ICARegisterForEventNotificationPB.eventsOfInterestAdded ICARegisterForEventNotificationPB.headerAdded ICARegisterForEventNotificationPB.init()Added ICARegisterForEventNotificationPB.init(header: ICAHeader, objectOfInterest: ICAObject, eventsOfInterest: Unmanaged<CFArray>!, notificationProc: ICANotification!, options: Unmanaged<CFDictionary>!)Added ICARegisterForEventNotificationPB.notificationProcAdded ICARegisterForEventNotificationPB.objectOfInterestAdded ICARegisterForEventNotificationPB.optionsAdded ICAScannerCloseSessionPB [struct]Added ICAScannerCloseSessionPB.headerAdded ICAScannerCloseSessionPB.init()Added ICAScannerCloseSessionPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerCloseSessionPB.sessionIDAdded ICAScannerGetParametersPB [struct]Added ICAScannerGetParametersPB.headerAdded ICAScannerGetParametersPB.init()Added ICAScannerGetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICAScannerGetParametersPB.sessionIDAdded ICAScannerGetParametersPB.theDictAdded ICAScannerInitializePB [struct]Added ICAScannerInitializePB.headerAdded ICAScannerInitializePB.init()Added ICAScannerInitializePB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerInitializePB.sessionIDAdded ICAScannerOpenSessionPB [struct]Added ICAScannerOpenSessionPB.headerAdded ICAScannerOpenSessionPB.init()Added ICAScannerOpenSessionPB.init(header: ICAHeader, object: ICAObject, sessionID: ICAScannerSessionID)Added ICAScannerOpenSessionPB.objectAdded ICAScannerOpenSessionPB.sessionIDAdded ICAScannerSetParametersPB [struct]Added ICAScannerSetParametersPB.headerAdded ICAScannerSetParametersPB.init()Added ICAScannerSetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICAScannerSetParametersPB.sessionIDAdded ICAScannerSetParametersPB.theDictAdded ICAScannerStartPB [struct]Added ICAScannerStartPB.headerAdded ICAScannerStartPB.init()Added ICAScannerStartPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerStartPB.sessionIDAdded ICAScannerStatusPB [struct]Added ICAScannerStatusPB.headerAdded ICAScannerStatusPB.init()Added ICAScannerStatusPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, status: UInt32)Added ICAScannerStatusPB.sessionIDAdded ICAScannerStatusPB.statusAdded ICASendNotificationPB [struct]Added ICASendNotificationPB.headerAdded ICASendNotificationPB.init()Added ICASendNotificationPB.init(header: ICAHeader, notificationDictionary: Unmanaged<CFMutableDictionary>!, replyCode: UInt32)Added ICASendNotificationPB.notificationDictionaryAdded ICASendNotificationPB.replyCodeAdded ICAUnloadDeviceModulePB [struct]Added ICAUnloadDeviceModulePB.deviceObjectAdded ICAUnloadDeviceModulePB.headerAdded ICAUnloadDeviceModulePB.init()Added ICAUnloadDeviceModulePB.init(header: ICAHeader, deviceObject: ICAObject)Added ICAUploadFilePB [struct]Added ICAUploadFilePB.fileFSRefAdded ICAUploadFilePB.flagsAdded ICAUploadFilePB.headerAdded ICAUploadFilePB.init()Added ICAUploadFilePB.init(header: ICAHeader, parentObject: ICAObject, fileFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32)Added ICAUploadFilePB.parentObjectAdded ICD_callback_functions.init(f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice!, f_ICD_CloseDevice: __ICD_CloseDevice!, f_ICD_PeriodicTask: __ICD_PeriodicTask!, f_ICD_GetObjectInfo: __ICD_GetObjectInfo!, f_ICD_Cleanup: __ICD_Cleanup!, f_ICD_GetPropertyData: __ICD_GetPropertyData!, f_ICD_SetPropertyData: __ICD_SetPropertyData!, f_ICD_ReadFileData: __ICD_ReadFileData!, f_ICD_WriteFileData: __ICD_WriteFileData!, f_ICD_SendMessage: __ICD_SendMessage!, f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary!, f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice!, f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath!, f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath!, f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice!, f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice!, f_ICD_WriteDataToFile: __ICD_WriteDataToFile!, f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice!, f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor!, f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64!)Added ICD_DisposeObjectPB [struct]Added ICD_DisposeObjectPB.headerAdded ICD_DisposeObjectPB.init()Added ICD_DisposeObjectPB.init(header: ICDHeader, object: ICAObject)Added ICD_DisposeObjectPB.objectAdded ICD_NewObjectPB [struct]Added ICD_NewObjectPB.headerAdded ICD_NewObjectPB.init()Added ICD_NewObjectPB.init(header: ICDHeader, parentObject: ICAObject, objectInfo: ICAObjectInfo, object: ICAObject)Added ICD_NewObjectPB.objectAdded ICD_NewObjectPB.objectInfoAdded ICD_NewObjectPB.parentObjectAdded ICD_Scannerscanner_callback_functions.init(f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice!, f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath!, f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice!, f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask!, f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo!, f_ICD_ScannerCleanup: __ICD_ScannerCleanup!, f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData!, f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData!, f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData!, f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData!, f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage!, f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary!, f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice!, f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath!, f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession!, f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession!, f_ICD_ScannerInitialize: __ICD_ScannerInitialize!, f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters!, f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters!, f_ICD_ScannerStatus: __ICD_ScannerStatus!, f_ICD_ScannerStart: __ICD_ScannerStart!, f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice!, f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice!, f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile!, f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice!, f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor!, f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64!)Added ICDHeader [struct]Added ICDHeader.errAdded ICDHeader.init()Added ICDHeader.init(err: ICAError, refcon: UInt)Added ICDHeader.refconAdded ICACompletionAdded ICAConnectionIDAdded ICAErrorAdded ICAEventDataCookieAdded ICAImportFilterProcAdded ICANotificationAdded ICANotificationProcAdded ICAObjectAdded ICAPropertyAdded ICAScannerSessionIDAdded ICASessionIDAdded ICDCompletionAdded kAddMetaDataToFinderCommentAdded kAdjustCreationDateAdded kCreateCustomIconAdded kDeleteAfterDownloadAdded kDontEmbedColorSyncProfileAdded kICAAllowMultipleImagesAdded kICABluetoothAddressKeyAdded kICABluetoothTransportTypeAdded kICAButtonCopyAdded kICAButtonEMailAdded kICAButtonScanAdded kICAButtonWebAdded kICACameraPassThruNotUsedAdded kICACameraPassThruReceiveAdded kICACameraPassThruSendAdded kICACannotYieldDeviceAdded kICACommunicationErrAdded kICADataTypeNotFoundErrAdded kICADeviceAdded kICADeviceAlreadyOpenErrAdded kICADeviceCameraAdded kICADeviceGUIDNotFoundErrAdded kICADeviceInternalErrAdded kICADeviceInvalidParamErrAdded kICADeviceIOServicePathNotFoundErrAdded kICADeviceLocationIDNotFoundErrAdded kICADeviceMemoryAllocationErrAdded kICADeviceMFPAdded kICADeviceModulePathKeyAdded kICADeviceNotFoundErrAdded kICADeviceNotOpenErrAdded kICADeviceOtherAdded kICADevicePDAAdded kICADevicePhoneAdded kICADeviceScannerAdded kICADeviceUnsupportedErrAdded kICADirectoryAdded kICADownloadAndReturnPathArrayAdded kICAExtensionInternalErrAdded kICAFileAdded kICAFileAudioAdded kICAFileCorruptedErrAdded kICAFileFirmwareAdded kICAFileImageAdded kICAFileMovieAdded kICAFileOtherAdded kICAFireWireGUIDKeyAdded kICAFireWireTransportTypeAdded kICAFlagReadAccessAdded kICAFlagReadWriteAccessAdded kICAFrameworkInternalErrAdded kICAIndexOutOfRangeErrAdded kICAInvalidObjectErrAdded kICAInvalidPropertyErrAdded kICAInvalidSessionErrAdded kICAIOPendingErrAdded kICAIOServicePathKeyAdded kICAIPAddressKeyAdded kICAIPGUIDKeyAdded kICAIPNameKeyAdded kICAListAdded kICAMediaHeightKeyAdded kICAMediaWidthKeyAdded kICAMessageCameraPassThroughAdded kICAMessageCameraReadClockAdded kICAMessageCheckDeviceAdded kICAMessageConnectAdded kICAMessageDeviceYieldAdded kICAMessageDisconnectAdded kICAMessageGetEventDataAdded kICAMessageGetLastButtonPressedAdded kICAMessageResetAdded kICAMessageScannerOverviewSelectionChangedAdded kICANotificationSubTypeDocumentLoadedAdded kICANotificationSubTypeDocumentNotLoadedAdded kICANotificationSubTypePerformOverviewScanAdded kICANotificationTypeScannerOverviewOverlayAvailableAdded kICAPBVersionAdded kICAPropertyAdded kICAPropertyColorSpaceAdded kICAPropertyColorSyncProfileAdded kICAPropertyImageApertureAdded kICAPropertyImageBitDepthAdded kICAPropertyImageDataAdded kICAPropertyImageDateDigitizedAdded kICAPropertyImageDateOriginalAdded kICAPropertyImageDPIAdded kICAPropertyImageExposureTimeAdded kICAPropertyImageFilenameAdded kICAPropertyImageFlashAdded kICAPropertyImageFNumberAdded kICAPropertyImageHeightAdded kICAPropertyImageShutterSpeedAdded kICAPropertyImageSizeAdded kICAPropertyImageThumbnailAdded kICAPropertyImageWidthAdded kICAPropertyTypeNotFoundErrAdded kICASandboxViolationAdded kICASCSITransportTypeAdded kICASecureSessionRequiredAdded kICATCPIPTransportTypeAdded kICAThumbnailFormatJPEGAdded kICAThumbnailFormatPNGAdded kICAThumbnailFormatTIFFAdded kICATransportTypeKeyAdded kICATWAINDSPathKeyAdded kICATWAINTransportTypeAdded kICATypeBooleanAdded kICATypeDataAdded kICATypeFixedAdded kICATypeFloatAdded kICATypeSInt16Added kICATypeSInt32Added kICATypeSInt64Added kICATypeStringAdded kICATypeThumbnailAdded kICATypeUInt16Added kICATypeUInt32Added kICATypeUInt64Added kICATypeUInt8Added kICAUploadFileAsIsAdded kICAUploadFileScaleToFitAdded kICAUSBLocationIDKeyAdded kICAUSBTransportTypeAdded kRotateImageAdded kSetFileTypeAndCreatorModified ICD_callback_functions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_callback_functions {     var f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice     var f_ICD_CloseDevice: __ICD_CloseDevice     var f_ICD_PeriodicTask: __ICD_PeriodicTask     var f_ICD_GetObjectInfo: __ICD_GetObjectInfo     var f_ICD_Cleanup: __ICD_Cleanup     var f_ICD_GetPropertyData: __ICD_GetPropertyData     var f_ICD_SetPropertyData: __ICD_SetPropertyData     var f_ICD_ReadFileData: __ICD_ReadFileData     var f_ICD_WriteFileData: __ICD_WriteFileData     var f_ICD_SendMessage: __ICD_SendMessage     var f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary     var f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice     var f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath     var f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath     var f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice     var f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice     var f_ICD_WriteDataToFile: __ICD_WriteDataToFile     var f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice     var f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor     var f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64     init()     init(f_ICD_OpenUSBDevice f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice, f_ICD_CloseDevice f_ICD_CloseDevice: __ICD_CloseDevice, f_ICD_PeriodicTask f_ICD_PeriodicTask: __ICD_PeriodicTask, f_ICD_GetObjectInfo f_ICD_GetObjectInfo: __ICD_GetObjectInfo, f_ICD_Cleanup f_ICD_Cleanup: __ICD_Cleanup, f_ICD_GetPropertyData f_ICD_GetPropertyData: __ICD_GetPropertyData, f_ICD_SetPropertyData f_ICD_SetPropertyData: __ICD_SetPropertyData, f_ICD_ReadFileData f_ICD_ReadFileData: __ICD_ReadFileData, f_ICD_WriteFileData f_ICD_WriteFileData: __ICD_WriteFileData, f_ICD_SendMessage f_ICD_SendMessage: __ICD_SendMessage, f_ICD_AddPropertiesToCFDictionary f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary, f_ICD_OpenFireWireDevice f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice, f_ICD_OpenUSBDeviceWithIORegPath f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath, f_ICD_OpenFireWireDeviceWithIORegPath f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath, f_ICD_OpenBluetoothDevice f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice, f_ICD_OpenTCPIPDevice f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice, f_ICD_WriteDataToFile f_ICD_WriteDataToFile: __ICD_WriteDataToFile, f_ICD_OpenMassStorageDevice f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice, f_ICD_WriteDataToFileDescriptor f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor, f_ICD_WriteDataToFileDescriptor64 f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64) } ``` |
| To | ``` struct ICD_callback_functions {     var f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice!     var f_ICD_CloseDevice: __ICD_CloseDevice!     var f_ICD_PeriodicTask: __ICD_PeriodicTask!     var f_ICD_GetObjectInfo: __ICD_GetObjectInfo!     var f_ICD_Cleanup: __ICD_Cleanup!     var f_ICD_GetPropertyData: __ICD_GetPropertyData!     var f_ICD_SetPropertyData: __ICD_SetPropertyData!     var f_ICD_ReadFileData: __ICD_ReadFileData!     var f_ICD_WriteFileData: __ICD_WriteFileData!     var f_ICD_SendMessage: __ICD_SendMessage!     var f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary!     var f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice!     var f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath!     var f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath!     var f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice!     var f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice!     var f_ICD_WriteDataToFile: __ICD_WriteDataToFile!     var f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice!     var f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor!     var f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64!     init()     init(f_ICD_OpenUSBDevice f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice!, f_ICD_CloseDevice f_ICD_CloseDevice: __ICD_CloseDevice!, f_ICD_PeriodicTask f_ICD_PeriodicTask: __ICD_PeriodicTask!, f_ICD_GetObjectInfo f_ICD_GetObjectInfo: __ICD_GetObjectInfo!, f_ICD_Cleanup f_ICD_Cleanup: __ICD_Cleanup!, f_ICD_GetPropertyData f_ICD_GetPropertyData: __ICD_GetPropertyData!, f_ICD_SetPropertyData f_ICD_SetPropertyData: __ICD_SetPropertyData!, f_ICD_ReadFileData f_ICD_ReadFileData: __ICD_ReadFileData!, f_ICD_WriteFileData f_ICD_WriteFileData: __ICD_WriteFileData!, f_ICD_SendMessage f_ICD_SendMessage: __ICD_SendMessage!, f_ICD_AddPropertiesToCFDictionary f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary!, f_ICD_OpenFireWireDevice f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice!, f_ICD_OpenUSBDeviceWithIORegPath f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath!, f_ICD_OpenFireWireDeviceWithIORegPath f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath!, f_ICD_OpenBluetoothDevice f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice!, f_ICD_OpenTCPIPDevice f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice!, f_ICD_WriteDataToFile f_ICD_WriteDataToFile: __ICD_WriteDataToFile!, f_ICD_OpenMassStorageDevice f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice!, f_ICD_WriteDataToFileDescriptor f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor!, f_ICD_WriteDataToFileDescriptor64 f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64!) } ``` |

Modified ICD_callback_functions.f_ICD_AddPropertiesToCFDictionary

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary ``` |
| To | ``` var f_ICD_AddPropertiesToCFDictionary: __ICD_AddPropertiesToCFDictionary! ``` |

Modified ICD_callback_functions.f_ICD_Cleanup

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_Cleanup: __ICD_Cleanup ``` |
| To | ``` var f_ICD_Cleanup: __ICD_Cleanup! ``` |

Modified ICD_callback_functions.f_ICD_CloseDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_CloseDevice: __ICD_CloseDevice ``` |
| To | ``` var f_ICD_CloseDevice: __ICD_CloseDevice! ``` |

Modified ICD_callback_functions.f_ICD_GetObjectInfo

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_GetObjectInfo: __ICD_GetObjectInfo ``` |
| To | ``` var f_ICD_GetObjectInfo: __ICD_GetObjectInfo! ``` |

Modified ICD_callback_functions.f_ICD_GetPropertyData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_GetPropertyData: __ICD_GetPropertyData ``` |
| To | ``` var f_ICD_GetPropertyData: __ICD_GetPropertyData! ``` |

Modified ICD_callback_functions.f_ICD_OpenBluetoothDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice ``` |
| To | ``` var f_ICD_OpenBluetoothDevice: __ICD_OpenBluetoothDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenFireWireDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice ``` |
| To | ``` var f_ICD_OpenFireWireDevice: __ICD_OpenFireWireDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenFireWireDeviceWithIORegPath

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath ``` |
| To | ``` var f_ICD_OpenFireWireDeviceWithIORegPath: __ICD_OpenFireWireDeviceWithIORegPath! ``` |

Modified ICD_callback_functions.f_ICD_OpenMassStorageDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice ``` |
| To | ``` var f_ICD_OpenMassStorageDevice: __ICD_OpenMassStorageDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenTCPIPDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice ``` |
| To | ``` var f_ICD_OpenTCPIPDevice: __ICD_OpenTCPIPDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenUSBDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice ``` |
| To | ``` var f_ICD_OpenUSBDevice: __ICD_OpenUSBDevice! ``` |

Modified ICD_callback_functions.f_ICD_OpenUSBDeviceWithIORegPath

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath ``` |
| To | ``` var f_ICD_OpenUSBDeviceWithIORegPath: __ICD_OpenUSBDeviceWithIORegPath! ``` |

Modified ICD_callback_functions.f_ICD_PeriodicTask

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_PeriodicTask: __ICD_PeriodicTask ``` |
| To | ``` var f_ICD_PeriodicTask: __ICD_PeriodicTask! ``` |

Modified ICD_callback_functions.f_ICD_ReadFileData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ReadFileData: __ICD_ReadFileData ``` |
| To | ``` var f_ICD_ReadFileData: __ICD_ReadFileData! ``` |

Modified ICD_callback_functions.f_ICD_SendMessage

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_SendMessage: __ICD_SendMessage ``` |
| To | ``` var f_ICD_SendMessage: __ICD_SendMessage! ``` |

Modified ICD_callback_functions.f_ICD_SetPropertyData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_SetPropertyData: __ICD_SetPropertyData ``` |
| To | ``` var f_ICD_SetPropertyData: __ICD_SetPropertyData! ``` |

Modified ICD_callback_functions.f_ICD_WriteDataToFile

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_WriteDataToFile: __ICD_WriteDataToFile ``` |
| To | ``` var f_ICD_WriteDataToFile: __ICD_WriteDataToFile! ``` |

Modified ICD_callback_functions.f_ICD_WriteDataToFileDescriptor

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor ``` |
| To | ``` var f_ICD_WriteDataToFileDescriptor: __ICD_WriteDataToFileDescriptor! ``` |

Modified ICD_callback_functions.f_ICD_WriteDataToFileDescriptor64

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64 ``` |
| To | ``` var f_ICD_WriteDataToFileDescriptor64: __ICD_WriteDataToFileDescriptor64! ``` |

Modified ICD_callback_functions.f_ICD_WriteFileData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_WriteFileData: __ICD_WriteFileData ``` |
| To | ``` var f_ICD_WriteFileData: __ICD_WriteFileData! ``` |

Modified ICD_Scannerscanner_callback_functions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICD_Scannerscanner_callback_functions {     var f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice     var f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath     var f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice     var f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask     var f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo     var f_ICD_ScannerCleanup: __ICD_ScannerCleanup     var f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData     var f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData     var f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData     var f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData     var f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage     var f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary     var f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice     var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath     var f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession     var f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession     var f_ICD_ScannerInitialize: __ICD_ScannerInitialize     var f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters     var f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters     var f_ICD_ScannerStatus: __ICD_ScannerStatus     var f_ICD_ScannerStart: __ICD_ScannerStart     var f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice     var f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice     var f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile     var f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice     var f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor     var f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64     init()     init(f_ICD_ScannerOpenUSBDevice f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice, f_ICD_ScannerOpenUSBDeviceWithIORegPath f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath, f_ICD_ScannerCloseDevice f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice, f_ICD_ScannerPeriodicTask f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask, f_ICD_ScannerGetObjectInfo f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo, f_ICD_ScannerCleanup f_ICD_ScannerCleanup: __ICD_ScannerCleanup, f_ICD_ScannerGetPropertyData f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData, f_ICD_ScannerSetPropertyData f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData, f_ICD_ScannerReadFileData f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData, f_ICD_ScannerWriteFileData f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData, f_ICD_ScannerSendMessage f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage, f_ICD_ScannerAddPropertiesToCFDictionary f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary, f_ICD_ScannerOpenFireWireDevice f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice, f_ICD_ScannerOpenFireWireDeviceWithIORegPath f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath, f_ICD_ScannerOpenSession f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession, f_ICD_ScannerCloseSession f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession, f_ICD_ScannerInitialize f_ICD_ScannerInitialize: __ICD_ScannerInitialize, f_ICD_ScannerGetParameters f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters, f_ICD_ScannerSetParameters f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters, f_ICD_ScannerStatus f_ICD_ScannerStatus: __ICD_ScannerStatus, f_ICD_ScannerStart f_ICD_ScannerStart: __ICD_ScannerStart, f_ICD_ScannerOpenBluetoothDevice f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice, f_ICD_ScannerOpenTCPIPDevice f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice, f_ICD_ScannerWriteDataToFile f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile, f_ICD_ScannerOpenMassStorageDevice f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice, f_ICD_ScannerWriteDataToFileDescriptor f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor, f_ICD_ScannerWriteDataToFileDescriptor64 f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64) } ``` |
| To | ``` struct ICD_Scannerscanner_callback_functions {     var f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice!     var f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath!     var f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice!     var f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask!     var f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo!     var f_ICD_ScannerCleanup: __ICD_ScannerCleanup!     var f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData!     var f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData!     var f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData!     var f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData!     var f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage!     var f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary!     var f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice!     var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath!     var f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession!     var f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession!     var f_ICD_ScannerInitialize: __ICD_ScannerInitialize!     var f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters!     var f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters!     var f_ICD_ScannerStatus: __ICD_ScannerStatus!     var f_ICD_ScannerStart: __ICD_ScannerStart!     var f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice!     var f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice!     var f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile!     var f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice!     var f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor!     var f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64!     init()     init(f_ICD_ScannerOpenUSBDevice f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice!, f_ICD_ScannerOpenUSBDeviceWithIORegPath f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath!, f_ICD_ScannerCloseDevice f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice!, f_ICD_ScannerPeriodicTask f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask!, f_ICD_ScannerGetObjectInfo f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo!, f_ICD_ScannerCleanup f_ICD_ScannerCleanup: __ICD_ScannerCleanup!, f_ICD_ScannerGetPropertyData f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData!, f_ICD_ScannerSetPropertyData f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData!, f_ICD_ScannerReadFileData f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData!, f_ICD_ScannerWriteFileData f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData!, f_ICD_ScannerSendMessage f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage!, f_ICD_ScannerAddPropertiesToCFDictionary f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary!, f_ICD_ScannerOpenFireWireDevice f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice!, f_ICD_ScannerOpenFireWireDeviceWithIORegPath f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath!, f_ICD_ScannerOpenSession f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession!, f_ICD_ScannerCloseSession f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession!, f_ICD_ScannerInitialize f_ICD_ScannerInitialize: __ICD_ScannerInitialize!, f_ICD_ScannerGetParameters f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters!, f_ICD_ScannerSetParameters f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters!, f_ICD_ScannerStatus f_ICD_ScannerStatus: __ICD_ScannerStatus!, f_ICD_ScannerStart f_ICD_ScannerStart: __ICD_ScannerStart!, f_ICD_ScannerOpenBluetoothDevice f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice!, f_ICD_ScannerOpenTCPIPDevice f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice!, f_ICD_ScannerWriteDataToFile f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile!, f_ICD_ScannerOpenMassStorageDevice f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice!, f_ICD_ScannerWriteDataToFileDescriptor f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor!, f_ICD_ScannerWriteDataToFileDescriptor64 f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64!) } ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerAddPropertiesToCFDictionary

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary ``` |
| To | ``` var f_ICD_ScannerAddPropertiesToCFDictionary: __ICD_ScannerAddPropertiesToCFDictionary! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerCleanup

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerCleanup: __ICD_ScannerCleanup ``` |
| To | ``` var f_ICD_ScannerCleanup: __ICD_ScannerCleanup! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerCloseDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice ``` |
| To | ``` var f_ICD_ScannerCloseDevice: __ICD_ScannerCloseDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerCloseSession

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession ``` |
| To | ``` var f_ICD_ScannerCloseSession: __ICD_ScannerCloseSession! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerGetObjectInfo

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo ``` |
| To | ``` var f_ICD_ScannerGetObjectInfo: __ICD_ScannerGetObjectInfo! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerGetParameters

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters ``` |
| To | ``` var f_ICD_ScannerGetParameters: __ICD_ScannerGetParameters! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerGetPropertyData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData ``` |
| To | ``` var f_ICD_ScannerGetPropertyData: __ICD_ScannerGetPropertyData! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerInitialize

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerInitialize: __ICD_ScannerInitialize ``` |
| To | ``` var f_ICD_ScannerInitialize: __ICD_ScannerInitialize! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenBluetoothDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice ``` |
| To | ``` var f_ICD_ScannerOpenBluetoothDevice: __ICD_ScannerOpenBluetoothDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenFireWireDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice ``` |
| To | ``` var f_ICD_ScannerOpenFireWireDevice: __ICD_ScannerOpenFireWireDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenFireWireDeviceWithIORegPath

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath ``` |
| To | ``` var f_ICD_ScannerOpenFireWireDeviceWithIORegPath: __ICD_ScannerOpenFireWireDeviceWithIORegPath! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenMassStorageDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice ``` |
| To | ``` var f_ICD_ScannerOpenMassStorageDevice: __ICD_ScannerOpenMassStorageDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenSession

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession ``` |
| To | ``` var f_ICD_ScannerOpenSession: __ICD_ScannerOpenSession! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenTCPIPDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice ``` |
| To | ``` var f_ICD_ScannerOpenTCPIPDevice: __ICD_ScannerOpenTCPIPDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenUSBDevice

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice ``` |
| To | ``` var f_ICD_ScannerOpenUSBDevice: __ICD_ScannerOpenUSBDevice! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerOpenUSBDeviceWithIORegPath

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath ``` |
| To | ``` var f_ICD_ScannerOpenUSBDeviceWithIORegPath: __ICD_ScannerOpenUSBDeviceWithIORegPath! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerPeriodicTask

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask ``` |
| To | ``` var f_ICD_ScannerPeriodicTask: __ICD_ScannerPeriodicTask! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerReadFileData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData ``` |
| To | ``` var f_ICD_ScannerReadFileData: __ICD_ScannerReadFileData! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerSendMessage

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage ``` |
| To | ``` var f_ICD_ScannerSendMessage: __ICD_ScannerSendMessage! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerSetParameters

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters ``` |
| To | ``` var f_ICD_ScannerSetParameters: __ICD_ScannerSetParameters! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerSetPropertyData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData ``` |
| To | ``` var f_ICD_ScannerSetPropertyData: __ICD_ScannerSetPropertyData! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerStart

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerStart: __ICD_ScannerStart ``` |
| To | ``` var f_ICD_ScannerStart: __ICD_ScannerStart! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerStatus

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerStatus: __ICD_ScannerStatus ``` |
| To | ``` var f_ICD_ScannerStatus: __ICD_ScannerStatus! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerWriteDataToFile

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile ``` |
| To | ``` var f_ICD_ScannerWriteDataToFile: __ICD_ScannerWriteDataToFile! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerWriteDataToFileDescriptor

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor ``` |
| To | ``` var f_ICD_ScannerWriteDataToFileDescriptor: __ICD_ScannerWriteDataToFileDescriptor! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerWriteDataToFileDescriptor64

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64 ``` |
| To | ``` var f_ICD_ScannerWriteDataToFileDescriptor64: __ICD_ScannerWriteDataToFileDescriptor64! ``` |

Modified ICD_Scannerscanner_callback_functions.f_ICD_ScannerWriteFileData

|  | Declaration |
| --- | --- |
| From | ``` var f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData ``` |
| To | ``` var f_ICD_ScannerWriteFileData: __ICD_ScannerWriteFileData! ``` |

Modified ICDNewObjectCreated(_: UnsafePointer<ObjectInfo>, _: UnsafePointer<ObjectInfo>, _: ICDNewObjectCreatedCompletion!) -> ICAError

|  | Declaration |
| --- | --- |
| From | ``` func ICDNewObjectCreated(_ parentInfo: UnsafePointer<ObjectInfo>, _ objectInfo: UnsafePointer<ObjectInfo>, _ completion: ICDNewObjectCreatedCompletion) -> ICAError ``` |
| To | ``` func ICDNewObjectCreated(_ parentInfo: UnsafePointer<ObjectInfo>, _ objectInfo: UnsafePointer<ObjectInfo>, _ completion: ICDNewObjectCreatedCompletion!) -> ICAError ``` |

Modified ICDNewObjectCreatedCompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias ICDNewObjectCreatedCompletion = CFunctionPointer<((UnsafePointer<ObjectInfo>) -> Void)> ``` |
| To | ``` typealias ICDNewObjectCreatedCompletion = (UnsafePointer<ObjectInfo>) -> Void ``` |

Modified kICABonjourServiceNameKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICABonjourServiceTypeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICABonjourTXTRecordKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICACreationDateStringKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADataPropertyKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADataSizeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADataTypeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADeviceBrowserDeviceRefKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADeviceCapabilitiesKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADeviceIconPathKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropArtist

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropBatteryLevel

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropBurstInterval

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropBurstNumber

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropCaptureDelay

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropCompressionSetting

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropContrast

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropCopyrightInfo

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropDateTime

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropDigitalZoom

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropEffectMode

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropExposureBiasCompensation

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropExposureIndex

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropExposureMeteringMode

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropExposureProgramMode

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropExposureTime

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropFlashMode

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropFNumber

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropFocalLength

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropFocusDistance

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropFocusMeteringMode

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropFocusMode

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropFunctionalMode

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropImageSize

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropRGBGain

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropSharpness

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropStillCaptureMode

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropTimelapseInterval

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropTimelapseNumber

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropUndefined

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropUploadURL

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicePropWhiteBalance

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADevicesArrayKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADeviceSharedKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADeviceTypeCamera

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADeviceTypeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADeviceTypeScanner

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADeviceUsedKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICADeviceWebSharedKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAErrorKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAExecutableArchitectureKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAIPPortKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICALockStatusKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAMediaDurationInSecondsKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAModificationDateStringKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationClassKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationClassProprietary

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationClassPTPStandard

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationClassPTPVendor

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationDataCookieKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationDataIsBigEndianKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationDataKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationDataSizeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationDeviceICAObjectKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationDeviceListICAObjectKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationICAObjectKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationImageBytesPerRowKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationImageDataKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationImageDataSizeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationImageHeightKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationImageKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationImageNumberOfRowsKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationImageStartRowKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationImageWidthKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationNumerOfImagesRemainingKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationPercentDownloadedKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationRawEventKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationScannerButtonTypeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationScannerDocumentNameKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationSubTypeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationSubTypeWarmUpDone

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationSubTypeWarmUpStarted

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeCaptureComplete

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeDeviceAdded

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeDeviceConnectionProgress

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeDeviceInfoChanged

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeDevicePropertyChanged

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeDeviceRemoved

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeDeviceStatusError

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeDeviceStatusInfo

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeDeviceWasReset

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeDownloadProgressStatus

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeObjectAdded

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeObjectInfoChanged

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeObjectRemoved

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeProprietary

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeRequestObjectTransfer

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeScannerButtonPressed

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeScannerPageDone

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeScannerScanDone

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeScannerSessionClosed

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeScanProgressStatus

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeStoreAdded

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeStoreFull

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeStoreInfoChanged

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeStoreRemoved

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeTransactionCanceled

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationTypeUnreportedStatus

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICANotificationVendorErrorCodeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAObjectKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAObjectNameKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICARawKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICARefconKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICARemoteDeviceKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAThumbnailPropertyKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAThumbnailSizeKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAUSBProductIDKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAUSBVendorIDKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kICAUserAssignedDeviceNameKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

Modified kMetaDataDictionaryKey

|  | Module |
| --- | --- |
| From | Carbon |
| To | ICADevices |

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
