---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/ImageCaptureCore.html
archived_at: '2026-07-18T02:51:46.288214Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# ImageCaptureCore Changes for Swift

### ImageCaptureCore

Added ICReturnCode.deviceCommandGeneralFailureModified ICReturnCode [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICReturnCode : Int {     case success     case invalidParam     case communicationTimedOut     case scanOperationCanceled     case scannerInUseByLocalUser     case scannerInUseByRemoteUser     case deviceFailedToOpenSession     case deviceFailedToCloseSession     case scannerFailedToSelectFunctionalUnit     case scannerFailedToCompleteOverviewScan     case scannerFailedToCompleteScan     case receivedUnsolicitedScannerStatusInfo     case receivedUnsolicitedScannerErrorInfo     case downloadFailed     case uploadFailed     case failedToCompletePassThroughCommand     case downloadCanceled     case failedToEnabeTethering     case failedToDisabeTethering     case failedToCompleteSendMessageRequest     case deleteFilesFailed     case deleteFilesCanceled     case deviceIsPasscodeLocked     case deviceFailedToTakePicture     case deviceSoftwareNotInstalled     case deviceSoftwareIsBeingInstalled     case deviceSoftwareInstallationCompleted     case deviceSoftwareInstallationCanceled     case deviceSoftwareInstallationFailed     case deviceSoftwareNotAvailable     case deviceCouldNotPair     case deviceCouldNotUnpair     case deviceNeedsCredentials     case deviceIsBusyEnumerating } ``` |
| To | ``` enum ICReturnCode : Int {     case success     case invalidParam     case communicationTimedOut     case scanOperationCanceled     case scannerInUseByLocalUser     case scannerInUseByRemoteUser     case deviceFailedToOpenSession     case deviceFailedToCloseSession     case scannerFailedToSelectFunctionalUnit     case scannerFailedToCompleteOverviewScan     case scannerFailedToCompleteScan     case receivedUnsolicitedScannerStatusInfo     case receivedUnsolicitedScannerErrorInfo     case downloadFailed     case uploadFailed     case failedToCompletePassThroughCommand     case downloadCanceled     case failedToEnabeTethering     case failedToDisabeTethering     case failedToCompleteSendMessageRequest     case deleteFilesFailed     case deleteFilesCanceled     case deviceIsPasscodeLocked     case deviceFailedToTakePicture     case deviceSoftwareNotInstalled     case deviceSoftwareIsBeingInstalled     case deviceSoftwareInstallationCompleted     case deviceSoftwareInstallationCanceled     case deviceSoftwareInstallationFailed     case deviceSoftwareNotAvailable     case deviceCouldNotPair     case deviceCouldNotUnpair     case deviceNeedsCredentials     case deviceIsBusyEnumerating     case deviceCommandGeneralFailure } ``` |

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
