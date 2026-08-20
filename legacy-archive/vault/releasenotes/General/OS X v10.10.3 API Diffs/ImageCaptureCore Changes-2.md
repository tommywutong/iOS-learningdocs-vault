---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/ImageCaptureCore.html
archived_at: '2026-07-18T02:52:31.922233Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# ImageCaptureCore Changes

## ImageCaptureCore

Added ICReturnDeviceCouldNotPairAdded ICReturnDeviceCouldNotUnpairModified ICCameraDevice.requestDownloadFile(ICCameraFile!, options:[NSObject: AnyObject]!, downloadDelegate: ICCameraDeviceDownloadDelegate!, didDownloadSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestDownloadFile(_ file: ICCameraFile!, options options: [NSObject : AnyObject]!, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate!, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func requestDownloadFile(_ file: ICCameraFile!, options options: [NSObject : AnyObject]!, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate!, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICCameraDevice.requestReadDataFromFile(ICCameraFile!, atOffset: off_t, length: off_t, readDelegate: AnyObject!, didReadDataSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestReadDataFromFile(_ file: ICCameraFile!, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: AnyObject!, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func requestReadDataFromFile(_ file: ICCameraFile!, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: AnyObject!, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICCameraDevice.requestSendPTPCommand(NSData!, outData: NSData!, sendCommandDelegate: AnyObject!, didSendCommandSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestSendPTPCommand(_ command: NSData!, outData data: NSData!, sendCommandDelegate sendCommandDelegate: AnyObject!, didSendCommandSelector selector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func requestSendPTPCommand(_ command: NSData!, outData data: NSData!, sendCommandDelegate sendCommandDelegate: AnyObject!, didSendCommandSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICCameraDevice.requestUploadFile(NSURL!, options:[NSObject: AnyObject]!, uploadDelegate: AnyObject!, didUploadSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestUploadFile(_ fileURL: NSURL!, options options: [NSObject : AnyObject]!, uploadDelegate uploadDelegate: AnyObject!, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func requestUploadFile(_ fileURL: NSURL!, options options: [NSObject : AnyObject]!, uploadDelegate uploadDelegate: AnyObject!, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, didAddItem: ICCameraItem!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, didAddItems:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, didCompleteDeleteFilesWithError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, didReceiveMetadataForItem: ICCameraItem!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, didReceivePTPEvent: NSData!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, didReceiveThumbnailForItem: ICCameraItem!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, didRemoveItem: ICCameraItem!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, didRemoveItems:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, didRenameItems:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, shouldGetMetadataOfItem: ICCameraItem!) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDevice(ICCameraDevice!, shouldGetThumbnailOfItem: ICCameraItem!) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.cameraDeviceDidChangeCapability(ICCameraDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDelegate.deviceDidBecomeReadyWithCompleteContentCatalog(ICDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICCameraDeviceDownloadDelegate.didDownloadFile(ICCameraFile!, error: NSError!, options:[NSObject: AnyObject]!, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func didDownloadFile(_ file: ICCameraFile!, error error: NSError!, options options: [NSObject : AnyObject]!, contextInfo contextInfo: UnsafePointer<()>) ``` | -- |
| To | ``` optional func didDownloadFile(_ file: ICCameraFile!, error error: NSError!, options options: [NSObject : AnyObject]!, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` | yes |

Modified ICCameraDeviceDownloadDelegate.didReceiveDownloadProgressForFile(ICCameraFile!, downloadedBytes: off_t, maxBytes: off_t)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDevice.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: ICDeviceDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: ICDeviceDelegate! ``` |

Modified ICDevice.requestSendMessage(UInt32, outData: NSData!, maxReturnedDataSize: UInt32, sendMessageDelegate: AnyObject!, didSendMessageSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func requestSendMessage(_ messageCode: UInt32, outData data: NSData!, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: AnyObject!, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func requestSendMessage(_ messageCode: UInt32, outData data: NSData!, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: AnyObject!, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified ICDeviceBrowser.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified ICDeviceBrowser.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: ICDeviceBrowserDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: ICDeviceBrowserDelegate! ``` |

Modified ICDeviceBrowserDelegate.deviceBrowser(ICDeviceBrowser!, deviceDidChangeName: ICDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceBrowserDelegate.deviceBrowser(ICDeviceBrowser!, deviceDidChangeSharingState: ICDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceBrowserDelegate.deviceBrowser(ICDeviceBrowser!, requestsSelectDevice: ICDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceBrowserDelegate.deviceBrowserDidEnumerateLocalDevices(ICDeviceBrowser!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceDelegate.device(ICDevice!, didCloseSessionWithError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceDelegate.device(ICDevice!, didEncounterError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceDelegate.device(ICDevice!, didOpenSessionWithError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceDelegate.device(ICDevice!, didReceiveButtonPress: String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceDelegate.device(ICDevice!, didReceiveCustomNotification:[NSObject: AnyObject]!, data: NSData!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceDelegate.device(ICDevice!, didReceiveStatusInformation:[NSObject: AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceDelegate.deviceDidBecomeReady(ICDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceDelegate.deviceDidChangeName(ICDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICDeviceDelegate.deviceDidChangeSharingState(ICDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICScannerDeviceDelegate.scannerDevice(ICScannerDevice!, didCompleteOverviewScanWithError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICScannerDeviceDelegate.scannerDevice(ICScannerDevice!, didCompleteScanWithError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICScannerDeviceDelegate.scannerDevice(ICScannerDevice!, didScanToBandData: ICScannerBandData!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICScannerDeviceDelegate.scannerDevice(ICScannerDevice!, didScanToURL: NSURL!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICScannerDeviceDelegate.scannerDevice(ICScannerDevice!, didSelectFunctionalUnit: ICScannerFunctionalUnit!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICScannerDeviceDelegate.scannerDeviceDidBecomeAvailable(ICScannerDevice!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified ICScannerFeatureEnumeration.currentValue

|  | Declaration |
| --- | --- |
| From | ``` var currentValue: AnyObject! ``` |
| To | ``` unowned(unsafe) var currentValue: AnyObject! ``` |

Modified ICButtonTypeCopy

|  | Declaration |
| --- | --- |
| From | ``` let ICButtonTypeCopy: NSString! ``` |
| To | ``` let ICButtonTypeCopy: String ``` |

Modified ICButtonTypeMail

|  | Declaration |
| --- | --- |
| From | ``` let ICButtonTypeMail: NSString! ``` |
| To | ``` let ICButtonTypeMail: String ``` |

Modified ICButtonTypePrint

|  | Declaration |
| --- | --- |
| From | ``` let ICButtonTypePrint: NSString! ``` |
| To | ``` let ICButtonTypePrint: String ``` |

Modified ICButtonTypeScan

|  | Declaration |
| --- | --- |
| From | ``` let ICButtonTypeScan: NSString! ``` |
| To | ``` let ICButtonTypeScan: String ``` |

Modified ICButtonTypeTransfer

|  | Declaration |
| --- | --- |
| From | ``` let ICButtonTypeTransfer: NSString! ``` |
| To | ``` let ICButtonTypeTransfer: String ``` |

Modified ICButtonTypeWeb

|  | Declaration |
| --- | --- |
| From | ``` let ICButtonTypeWeb: NSString! ``` |
| To | ``` let ICButtonTypeWeb: String ``` |

Modified ICCameraDeviceCanAcceptPTPCommands

|  | Declaration |
| --- | --- |
| From | ``` let ICCameraDeviceCanAcceptPTPCommands: NSString! ``` |
| To | ``` let ICCameraDeviceCanAcceptPTPCommands: String ``` |

Modified ICCameraDeviceCanDeleteAllFiles

|  | Declaration |
| --- | --- |
| From | ``` let ICCameraDeviceCanDeleteAllFiles: NSString! ``` |
| To | ``` let ICCameraDeviceCanDeleteAllFiles: String ``` |

Modified ICCameraDeviceCanDeleteOneFile

|  | Declaration |
| --- | --- |
| From | ``` let ICCameraDeviceCanDeleteOneFile: NSString! ``` |
| To | ``` let ICCameraDeviceCanDeleteOneFile: String ``` |

Modified ICCameraDeviceCanReceiveFile

|  | Declaration |
| --- | --- |
| From | ``` let ICCameraDeviceCanReceiveFile: NSString! ``` |
| To | ``` let ICCameraDeviceCanReceiveFile: String ``` |

Modified ICCameraDeviceCanSyncClock

|  | Declaration |
| --- | --- |
| From | ``` let ICCameraDeviceCanSyncClock: NSString! ``` |
| To | ``` let ICCameraDeviceCanSyncClock: String ``` |

Modified ICCameraDeviceCanTakePicture

|  | Declaration |
| --- | --- |
| From | ``` let ICCameraDeviceCanTakePicture: NSString! ``` |
| To | ``` let ICCameraDeviceCanTakePicture: String ``` |

Modified ICCameraDeviceCanTakePictureUsingShutterReleaseOnCamera

|  | Declaration |
| --- | --- |
| From | ``` let ICCameraDeviceCanTakePictureUsingShutterReleaseOnCamera: NSString! ``` |
| To | ``` let ICCameraDeviceCanTakePictureUsingShutterReleaseOnCamera: String ``` |

Modified ICDeleteAfterSuccessfulDownload

|  | Declaration |
| --- | --- |
| From | ``` let ICDeleteAfterSuccessfulDownload: NSString! ``` |
| To | ``` let ICDeleteAfterSuccessfulDownload: String ``` |

Modified ICDeviceCanEjectOrDisconnect

|  | Declaration |
| --- | --- |
| From | ``` let ICDeviceCanEjectOrDisconnect: NSString! ``` |
| To | ``` let ICDeviceCanEjectOrDisconnect: String ``` |

Modified ICDeviceLocationDescriptionBluetooth

|  | Declaration |
| --- | --- |
| From | ``` let ICDeviceLocationDescriptionBluetooth: NSString! ``` |
| To | ``` let ICDeviceLocationDescriptionBluetooth: String ``` |

Modified ICDeviceLocationDescriptionFireWire

|  | Declaration |
| --- | --- |
| From | ``` let ICDeviceLocationDescriptionFireWire: NSString! ``` |
| To | ``` let ICDeviceLocationDescriptionFireWire: String ``` |

Modified ICDeviceLocationDescriptionMassStorage

|  | Declaration |
| --- | --- |
| From | ``` let ICDeviceLocationDescriptionMassStorage: NSString! ``` |
| To | ``` let ICDeviceLocationDescriptionMassStorage: String ``` |

Modified ICDeviceLocationDescriptionUSB

|  | Declaration |
| --- | --- |
| From | ``` let ICDeviceLocationDescriptionUSB: NSString! ``` |
| To | ``` let ICDeviceLocationDescriptionUSB: String ``` |

Modified ICDownloadSidecarFiles

|  | Declaration |
| --- | --- |
| From | ``` let ICDownloadSidecarFiles: NSString! ``` |
| To | ``` let ICDownloadSidecarFiles: String ``` |

Modified ICDownloadsDirectoryURL

|  | Declaration |
| --- | --- |
| From | ``` let ICDownloadsDirectoryURL: NSString! ``` |
| To | ``` let ICDownloadsDirectoryURL: String ``` |

Modified ICLocalizedStatusNotificationKey

|  | Declaration |
| --- | --- |
| From | ``` let ICLocalizedStatusNotificationKey: NSString! ``` |
| To | ``` let ICLocalizedStatusNotificationKey: String ``` |

Modified ICOverwrite

|  | Declaration |
| --- | --- |
| From | ``` let ICOverwrite: NSString! ``` |
| To | ``` let ICOverwrite: String ``` |

Modified ICSaveAsFilename

|  | Declaration |
| --- | --- |
| From | ``` let ICSaveAsFilename: NSString! ``` |
| To | ``` let ICSaveAsFilename: String ``` |

Modified ICSavedAncillaryFiles

|  | Declaration |
| --- | --- |
| From | ``` let ICSavedAncillaryFiles: NSString! ``` |
| To | ``` let ICSavedAncillaryFiles: String ``` |

Modified ICSavedFilename

|  | Declaration |
| --- | --- |
| From | ``` let ICSavedFilename: NSString! ``` |
| To | ``` let ICSavedFilename: String ``` |

Modified ICScannerStatusRequestsOverviewScan

|  | Declaration |
| --- | --- |
| From | ``` let ICScannerStatusRequestsOverviewScan: NSString! ``` |
| To | ``` let ICScannerStatusRequestsOverviewScan: String ``` |

Modified ICScannerStatusWarmUpDone

|  | Declaration |
| --- | --- |
| From | ``` let ICScannerStatusWarmUpDone: NSString! ``` |
| To | ``` let ICScannerStatusWarmUpDone: String ``` |

Modified ICScannerStatusWarmingUp

|  | Declaration |
| --- | --- |
| From | ``` let ICScannerStatusWarmingUp: NSString! ``` |
| To | ``` let ICScannerStatusWarmingUp: String ``` |

Modified ICStatusCodeKey

|  | Declaration |
| --- | --- |
| From | ``` let ICStatusCodeKey: NSString! ``` |
| To | ``` let ICStatusCodeKey: String ``` |

Modified ICStatusNotificationKey

|  | Declaration |
| --- | --- |
| From | ``` let ICStatusNotificationKey: NSString! ``` |
| To | ``` let ICStatusNotificationKey: String ``` |

Modified ICTransportTypeBluetooth

|  | Declaration |
| --- | --- |
| From | ``` let ICTransportTypeBluetooth: NSString! ``` |
| To | ``` let ICTransportTypeBluetooth: String ``` |

Modified ICTransportTypeFireWire

|  | Declaration |
| --- | --- |
| From | ``` let ICTransportTypeFireWire: NSString! ``` |
| To | ``` let ICTransportTypeFireWire: String ``` |

Modified ICTransportTypeMassStorage

|  | Declaration |
| --- | --- |
| From | ``` let ICTransportTypeMassStorage: NSString! ``` |
| To | ``` let ICTransportTypeMassStorage: String ``` |

Modified ICTransportTypeTCPIP

|  | Declaration |
| --- | --- |
| From | ``` let ICTransportTypeTCPIP: NSString! ``` |
| To | ``` let ICTransportTypeTCPIP: String ``` |

Modified ICTransportTypeUSB

|  | Declaration |
| --- | --- |
| From | ``` let ICTransportTypeUSB: NSString! ``` |
| To | ``` let ICTransportTypeUSB: String ``` |

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
