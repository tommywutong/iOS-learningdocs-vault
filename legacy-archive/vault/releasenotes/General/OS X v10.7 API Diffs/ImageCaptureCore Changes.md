---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/ImageCaptureCore.html
archived_at: '2026-07-18T02:54:29.508457Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# ImageCaptureCore Changes

## ImageCaptureCore

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

ICCameraDevice.hRemoved -[ICCameraDevice requestEjectOrDisconnect]Added -[ICCameraDevice cancelDelete]Added ICCameraDevice.isAccessRestrictedAppleDeviceAdded ICCameraDevice.mountPointAdded -[ICCameraDevice requestDisableTethering]Added -[ICCameraDevice requestEnableTethering]Added ICCameraDevice.tetheredCaptureEnabledAdded -[ICCameraDeviceDelegate cameraDevice:didAddItems:]Added -[ICCameraDeviceDelegate cameraDevice:didCompleteDeleteFilesWithError:]Added -[ICCameraDeviceDelegate cameraDevice:didRemoveItems:]Added -[ICCameraDeviceDelegate cameraDevice:didRenameItems:]Added -[ICCameraDeviceDelegate deviceDidBecomeReadyWithCompleteContentCatalog:]Added ICCameraDeviceDownloadDelegateAdded -[ICCameraDeviceDownloadDelegate didDownloadFile:error:options:contextInfo:]Added -[ICCameraDeviceDownloadDelegate didReceiveDownloadProgressForFile:downloadedBytes:maxBytes:]Added ICCameraDeviceCanTakePictureUsingShutterReleaseOnCameraAdded ICDownloadSidecarFilesModified -[ICCameraDevice requestDownloadFile:options:downloadDelegate:didDownloadSelector:contextInfo:]

|  | Declaration |
| --- | --- |
| From | - (void)requestDownloadFile:(ICCameraFile \*)file options:(NSDictionary \*)options downloadDelegate:(id)downloadDelegate didDownloadSelector:(SEL)selector contextInfo:(void \*)contextInfo |
| To | - (void)requestDownloadFile:(ICCameraFile \*)file options:(NSDictionary \*)options downloadDelegate:(id < ICCameraDeviceDownloadDelegate >)downloadDelegate didDownloadSelector:(SEL)selector contextInfo:(void \*)contextInfo |

ICCameraItem.hAdded ICCameraFile.durationAdded ICCameraFile.sidecarFilesAdded ICCameraItem.addedAfterContentCatalogCompletedAdded ICCameraItem.fileSystemPathICCommonConstants.hAdded ICReturnDeleteFilesCanceledAdded ICReturnDeleteFilesFailedAdded ICReturnDeviceIsPasscodeLockedAdded ICReturnFailedToCompleteSendMessageRequestAdded ICReturnFailedToDisabeTetheringAdded ICReturnFailedToEnabeTetheringICDevice.hAdded ICDevice.fwGUIDAdded ICDevice.locationDescriptionAdded ICDevice.persistentIDStringAdded -[ICDevice requestEjectOrDisconnect]Added -[ICDevice requestSendMessage:outData:maxReturnedDataSize:sendMessageDelegate:didSendMessageSelector:contextInfo:]Added ICDevice.serialNumberStringAdded ICDevice.usbLocationIDAdded ICDevice.usbProductIDAdded ICDevice.usbVendorIDAdded ICDevice.userDataAdded -[ICDeviceDelegate device:didReceiveCustomNotification:data:]Added ICDeviceLocationDescriptionBluetoothAdded ICDeviceLocationDescriptionFireWireAdded ICDeviceLocationDescriptionMassStorageAdded ICDeviceLocationDescriptionUSBICDeviceBrowser.hAdded -[ICDeviceBrowser preferredDevice]ICScannerBandData.hAdded ICScannerBandDataAdded ICScannerBandData.bigEndianAdded ICScannerBandData.bitsPerComponentAdded ICScannerBandData.bitsPerPixelAdded ICScannerBandData.bytesPerRowAdded ICScannerBandData.colorSyncProfilePathAdded ICScannerBandData.dataBufferAdded ICScannerBandData.dataNumRowsAdded ICScannerBandData.dataSizeAdded ICScannerBandData.dataStartRowAdded ICScannerBandData.fullImageHeightAdded ICScannerBandData.fullImageWidthAdded ICScannerBandData.numComponentsAdded ICScannerBandData.pixelDataTypeICScannerDevice.hAdded ICScannerDevice.maxMemoryBandSizeAdded -[ICScannerDeviceDelegate scannerDevice:didScanToBandData:]Added -[ICScannerDeviceDelegate scannerDevice:didScanToURL:]Modified -[ICScannerDeviceDelegate scannerDevice:didScanToURL:data:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ICScannerFunctionalUnits.hAdded ICScannerFunctionalUnit.nativeXResolutionAdded ICScannerFunctionalUnit.nativeYResolutionAdded ICScannerFunctionalUnitDocumentFeeder.reverseFeederPageOrderAdded ICScannerFunctionalUnitFlatbed.documentSizeAdded ICScannerFunctionalUnitFlatbed.documentTypeAdded ICScannerFunctionalUnitFlatbed.supportedDocumentTypesAdded ICScannerFunctionalUnitNegativeTransparency.documentSizeAdded ICScannerFunctionalUnitNegativeTransparency.documentTypeAdded ICScannerFunctionalUnitNegativeTransparency.supportedDocumentTypesAdded ICScannerFunctionalUnitPositiveTransparency.documentSizeAdded ICScannerFunctionalUnitPositiveTransparency.documentTypeAdded ICScannerFunctionalUnitPositiveTransparency.supportedDocumentTypesAdded ICScannerDocumentType110Added ICScannerDocumentType135Added ICScannerDocumentTypeAPSCAdded ICScannerDocumentTypeAPSHAdded ICScannerDocumentTypeAPSPAdded ICScannerDocumentTypeLFAdded ICScannerDocumentTypeMF

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
