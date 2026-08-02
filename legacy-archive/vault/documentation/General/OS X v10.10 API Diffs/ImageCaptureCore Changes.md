---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/ImageCaptureCore.html
archived_at: '2026-07-15T07:34:46.291729Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# ImageCaptureCore Changes

## ImageCaptureCore

ICCameraDevice.hAdded -[ICCameraDeviceDelegate cameraDevice:shouldGetMetadataOfItem:]Added -[ICCameraDeviceDelegate cameraDevice:shouldGetThumbnailOfItem:]Modified -[ICCameraDeviceDelegate cameraDevice:didAddItem:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate cameraDevice:didAddItems:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate cameraDevice:didCompleteDeleteFilesWithError:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate cameraDevice:didReceiveMetadataForItem:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate cameraDevice:didReceivePTPEvent:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate cameraDevice:didReceiveThumbnailForItem:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate cameraDevice:didRemoveItem:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate cameraDevice:didRemoveItems:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate cameraDevice:didRenameItems:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate cameraDeviceDidChangeCapability:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDelegate deviceDidBecomeReadyWithCompleteContentCatalog:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDownloadDelegate didDownloadFile:error:options:contextInfo:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICCameraDeviceDownloadDelegate didReceiveDownloadProgressForFile:downloadedBytes:maxBytes:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

ICDevice.hModified -[ICDeviceDelegate device:didCloseSessionWithError:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceDelegate device:didEncounterError:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceDelegate device:didOpenSessionWithError:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceDelegate device:didReceiveButtonPress:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceDelegate device:didReceiveCustomNotification:data:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceDelegate device:didReceiveStatusInformation:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceDelegate deviceDidBecomeReady:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceDelegate deviceDidChangeName:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceDelegate deviceDidChangeSharingState:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

ICDeviceBrowser.hModified -[ICDeviceBrowserDelegate deviceBrowser:deviceDidChangeName:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceBrowserDelegate deviceBrowser:deviceDidChangeSharingState:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceBrowserDelegate deviceBrowser:requestsSelectDevice:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICDeviceBrowserDelegate deviceBrowserDidEnumerateLocalDevices:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

ICScannerDevice.hModified -[ICScannerDeviceDelegate scannerDevice:didCompleteOverviewScanWithError:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICScannerDeviceDelegate scannerDevice:didCompleteScanWithError:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICScannerDeviceDelegate scannerDevice:didScanToBandData:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICScannerDeviceDelegate scannerDevice:didScanToURL:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICScannerDeviceDelegate scannerDevice:didScanToURL:data:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICScannerDeviceDelegate scannerDevice:didSelectFunctionalUnit:error:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[ICScannerDeviceDelegate scannerDeviceDidBecomeAvailable:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

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
