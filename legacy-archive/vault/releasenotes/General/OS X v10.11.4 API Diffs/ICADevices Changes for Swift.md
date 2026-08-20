---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/ICADevices.html
archived_at: '2026-07-18T02:53:52.027358Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# ICADevices Changes for Swift

### ICADevices

Removed ICACloseSessionPB.init()Removed ICACloseSessionPB.init(header: ICAHeader, sessionID: ICASessionID)Removed ICACopyObjectDataPB.init()Removed ICACopyObjectDataPB.init(header: ICAHeader, object: ICAObject, startByte: Int, requestedSize: Int, data: UnsafeMutablePointer<Unmanaged<CFData>?>)Removed ICACopyObjectPropertyDictionaryPB.init()Removed ICACopyObjectPropertyDictionaryPB.init(header: ICAHeader, object: ICAObject, theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>)Removed ICACopyObjectThumbnailPB.init()Removed ICACopyObjectThumbnailPB.init(header: ICAHeader, object: ICAObject, thumbnailFormat: OSType, thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>)Removed ICADownloadFilePB.init()Removed ICADownloadFilePB.init(header: ICAHeader, object: ICAObject, dirFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32, fileType: OSType, fileCreator: OSType, rotationAngle: Fixed, fileFSRef: UnsafeMutablePointer<FSRef>)Removed ICAGetDeviceListPB.init()Removed ICAGetDeviceListPB.init(header: ICAHeader, object: ICAObject)Removed ICAHeader.init()Removed ICAHeader.init(err: ICAError, refcon: UInt)Removed ICAImportImagePB.init()Removed ICAImportImagePB.init(header: ICAHeader, deviceObject: ICAObject, flags: UInt32, supportedFileTypes: Unmanaged<CFArray>!, filterProc: ICAImportFilterProc!, importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>)Removed ICALoadDeviceModulePB.init()Removed ICALoadDeviceModulePB.init(header: ICAHeader, paramDictionary: Unmanaged<CFDictionary>!)Removed ICAMessage.init()Removed ICAMessage.init(messageType: OSType, startByte: UInt32, dataPtr: UnsafeMutablePointer<Void>, dataSize: UInt32, dataType: OSType)Removed ICAObjectInfo.init()Removed ICAObjectInfo.init(objectType: OSType, objectSubtype: OSType)Removed ICAObjectSendMessagePB.init()Removed ICAObjectSendMessagePB.init(header: ICAHeader, object: ICAObject, message: ICAMessage, result: UInt32)Removed ICAOpenSessionPB.init()Removed ICAOpenSessionPB.init(header: ICAHeader, deviceObject: ICAObject, sessionID: ICASessionID)Removed ICAPTPEventDataset.init()Removed ICAPTPEventDataset.init(dataLength: UInt32, containerType: UInt16, eventCode: UInt16, transactionID: UInt32, params: (UInt32, UInt32, UInt32))Removed ICAPTPPassThroughPB.init()Removed ICAPTPPassThroughPB.init(commandCode: UInt32, resultCode: UInt32, numOfInputParams: UInt32, numOfOutputParams: UInt32, params: (UInt32, UInt32, UInt32, UInt32), dataUsageMode: UInt32, flags: UInt32, dataSize: UInt32, data: (UInt8))Removed ICARegisterForEventNotificationPB.init()Removed ICARegisterForEventNotificationPB.init(header: ICAHeader, objectOfInterest: ICAObject, eventsOfInterest: Unmanaged<CFArray>!, notificationProc: ICANotification!, options: Unmanaged<CFDictionary>!)Removed ICAScannerCloseSessionPB.init()Removed ICAScannerCloseSessionPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Removed ICAScannerGetParametersPB.init()Removed ICAScannerGetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Removed ICAScannerInitializePB.init()Removed ICAScannerInitializePB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Removed ICAScannerOpenSessionPB.init()Removed ICAScannerOpenSessionPB.init(header: ICAHeader, object: ICAObject, sessionID: ICAScannerSessionID)Removed ICAScannerSetParametersPB.init()Removed ICAScannerSetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Removed ICAScannerStartPB.init()Removed ICAScannerStartPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Removed ICAScannerStatusPB.init()Removed ICAScannerStatusPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, status: UInt32)Removed ICASendNotificationPB.init()Removed ICASendNotificationPB.init(header: ICAHeader, notificationDictionary: Unmanaged<CFMutableDictionary>!, replyCode: UInt32)Removed ICAUnloadDeviceModulePB.init()Removed ICAUnloadDeviceModulePB.init(header: ICAHeader, deviceObject: ICAObject)Removed ICAUploadFilePB.init()Removed ICAUploadFilePB.init(header: ICAHeader, parentObject: ICAObject, fileFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32)Removed ICD_DisposeObjectPB.init()Removed ICD_DisposeObjectPB.init(header: ICDHeader, object: ICAObject)Removed ICD_NewObjectPB.init()Removed ICD_NewObjectPB.init(header: ICDHeader, parentObject: ICAObject, objectInfo: ICAObjectInfo, object: ICAObject)Removed ICDHeader.init()Removed ICDHeader.init(err: ICAError, refcon: UInt)Added ICACloseSessionPB.init()Added ICACloseSessionPB.init(header: ICAHeader, sessionID: ICASessionID)Added ICACopyObjectDataPB.init()Added ICACopyObjectDataPB.init(header: ICAHeader, object: ICAObject, startByte: Int, requestedSize: Int, data: UnsafeMutablePointer<Unmanaged<CFData>?>)Added ICACopyObjectPropertyDictionaryPB.init()Added ICACopyObjectPropertyDictionaryPB.init(header: ICAHeader, object: ICAObject, theDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>)Added ICACopyObjectThumbnailPB.init()Added ICACopyObjectThumbnailPB.init(header: ICAHeader, object: ICAObject, thumbnailFormat: OSType, thumbnailData: UnsafeMutablePointer<Unmanaged<CFData>?>)Added ICADownloadFilePB.init()Added ICADownloadFilePB.init(header: ICAHeader, object: ICAObject, dirFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32, fileType: OSType, fileCreator: OSType, rotationAngle: Fixed, fileFSRef: UnsafeMutablePointer<FSRef>)Added ICAGetDeviceListPB.init()Added ICAGetDeviceListPB.init(header: ICAHeader, object: ICAObject)Added ICAHeader.init()Added ICAHeader.init(err: ICAError, refcon: UInt)Added ICAImportImagePB.init()Added ICAImportImagePB.init(header: ICAHeader, deviceObject: ICAObject, flags: UInt32, supportedFileTypes: Unmanaged<CFArray>!, filterProc: ICAImportFilterProc!, importedImages: UnsafeMutablePointer<Unmanaged<CFArray>?>)Added ICALoadDeviceModulePB.init()Added ICALoadDeviceModulePB.init(header: ICAHeader, paramDictionary: Unmanaged<CFDictionary>!)Added ICAMessage.init()Added ICAMessage.init(messageType: OSType, startByte: UInt32, dataPtr: UnsafeMutablePointer<Void>, dataSize: UInt32, dataType: OSType)Added ICAObjectInfo.init()Added ICAObjectInfo.init(objectType: OSType, objectSubtype: OSType)Added ICAObjectSendMessagePB.init()Added ICAObjectSendMessagePB.init(header: ICAHeader, object: ICAObject, message: ICAMessage, result: UInt32)Added ICAOpenSessionPB.init()Added ICAOpenSessionPB.init(header: ICAHeader, deviceObject: ICAObject, sessionID: ICASessionID)Added ICAPTPEventDataset.init()Added ICAPTPEventDataset.init(dataLength: UInt32, containerType: UInt16, eventCode: UInt16, transactionID: UInt32, params: (UInt32, UInt32, UInt32))Added ICAPTPPassThroughPB.init()Added ICAPTPPassThroughPB.init(commandCode: UInt32, resultCode: UInt32, numOfInputParams: UInt32, numOfOutputParams: UInt32, params: (UInt32, UInt32, UInt32, UInt32), dataUsageMode: UInt32, flags: UInt32, dataSize: UInt32, data: (UInt8))Added ICARegisterForEventNotificationPB.init()Added ICARegisterForEventNotificationPB.init(header: ICAHeader, objectOfInterest: ICAObject, eventsOfInterest: Unmanaged<CFArray>!, notificationProc: ICANotification!, options: Unmanaged<CFDictionary>!)Added ICAScannerCloseSessionPB.init()Added ICAScannerCloseSessionPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerGetParametersPB.init()Added ICAScannerGetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICAScannerInitializePB.init()Added ICAScannerInitializePB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerOpenSessionPB.init()Added ICAScannerOpenSessionPB.init(header: ICAHeader, object: ICAObject, sessionID: ICAScannerSessionID)Added ICAScannerSetParametersPB.init()Added ICAScannerSetParametersPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, theDict: Unmanaged<CFMutableDictionary>!)Added ICAScannerStartPB.init()Added ICAScannerStartPB.init(header: ICAHeader, sessionID: ICAScannerSessionID)Added ICAScannerStatusPB.init()Added ICAScannerStatusPB.init(header: ICAHeader, sessionID: ICAScannerSessionID, status: UInt32)Added ICASendNotificationPB.init()Added ICASendNotificationPB.init(header: ICAHeader, notificationDictionary: Unmanaged<CFMutableDictionary>!, replyCode: UInt32)Added ICAUnloadDeviceModulePB.init()Added ICAUnloadDeviceModulePB.init(header: ICAHeader, deviceObject: ICAObject)Added ICAUploadFilePB.init()Added ICAUploadFilePB.init(header: ICAHeader, parentObject: ICAObject, fileFSRef: UnsafeMutablePointer<FSRef>, flags: UInt32)Added ICD_DisposeObjectPB.init()Added ICD_DisposeObjectPB.init(header: ICDHeader, object: ICAObject)Added ICD_NewObjectPB.init()Added ICD_NewObjectPB.init(header: ICDHeader, parentObject: ICAObject, objectInfo: ICAObjectInfo, object: ICAObject)Added ICDHeader.init()Added ICDHeader.init(err: ICAError, refcon: UInt)

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
