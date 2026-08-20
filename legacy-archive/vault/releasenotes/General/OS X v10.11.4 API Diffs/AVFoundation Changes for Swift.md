---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/AVFoundation.html
archived_at: '2026-07-18T02:53:49.922860Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# AVFoundation Changes for Swift

### AVFoundation

Added [AVError.CreateContentKeyRequestFailed](https://developer.apple.com/documentation/avfoundation/averror/averrorcreatecontentkeyrequestfailed)Modified [AVError [enum]](https://developer.apple.com/documentation/avfoundation/averror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum AVError : Int {     case Unknown     case OutOfMemory     case SessionNotRunning     case DeviceAlreadyUsedByAnotherSession     case NoDataCaptured     case SessionConfigurationChanged     case DiskFull     case DeviceWasDisconnected     case MediaChanged     case MaximumDurationReached     case MaximumFileSizeReached     case MediaDiscontinuity     case MaximumNumberOfSamplesForFileFormatReached     case DeviceNotConnected     case DeviceInUseByAnotherApplication     case DeviceLockedForConfigurationByAnotherProcess     case ExportFailed     case DecodeFailed     case InvalidSourceMedia     case FileAlreadyExists     case CompositionTrackSegmentsNotContiguous     case InvalidCompositionTrackSegmentDuration     case InvalidCompositionTrackSegmentSourceStartTime     case InvalidCompositionTrackSegmentSourceDuration     case FileFormatNotRecognized     case FileFailedToParse     case MaximumStillImageCaptureRequestsExceeded     case ContentIsProtected     case NoImageAtTime     case DecoderNotFound     case EncoderNotFound     case ContentIsNotAuthorized     case ApplicationIsNotAuthorized     case OperationNotSupportedForAsset     case DecoderTemporarilyUnavailable     case EncoderTemporarilyUnavailable     case InvalidVideoComposition     case ReferenceForbiddenByReferencePolicy     case InvalidOutputURLPathExtension     case ScreenCaptureFailed     case DisplayWasDisabled     case TorchLevelUnavailable     case IncompatibleAsset     case FailedToLoadMediaData     case ServerIncorrectlyConfigured     case ApplicationIsNotAuthorizedToUseDevice     case FailedToParse     case FileTypeDoesNotSupportSampleReferences     case UndecodableMediaData     case AirPlayControllerRequiresInternet     case AirPlayReceiverRequiresInternet     case VideoCompositorFailed } extension AVError : _BridgedNSError { } extension AVError : _BridgedNSError { } ``` |
| To | ``` enum AVError : Int {     case Unknown     case OutOfMemory     case SessionNotRunning     case DeviceAlreadyUsedByAnotherSession     case NoDataCaptured     case SessionConfigurationChanged     case DiskFull     case DeviceWasDisconnected     case MediaChanged     case MaximumDurationReached     case MaximumFileSizeReached     case MediaDiscontinuity     case MaximumNumberOfSamplesForFileFormatReached     case DeviceNotConnected     case DeviceInUseByAnotherApplication     case DeviceLockedForConfigurationByAnotherProcess     case ExportFailed     case DecodeFailed     case InvalidSourceMedia     case FileAlreadyExists     case CompositionTrackSegmentsNotContiguous     case InvalidCompositionTrackSegmentDuration     case InvalidCompositionTrackSegmentSourceStartTime     case InvalidCompositionTrackSegmentSourceDuration     case FileFormatNotRecognized     case FileFailedToParse     case MaximumStillImageCaptureRequestsExceeded     case ContentIsProtected     case NoImageAtTime     case DecoderNotFound     case EncoderNotFound     case ContentIsNotAuthorized     case ApplicationIsNotAuthorized     case OperationNotSupportedForAsset     case DecoderTemporarilyUnavailable     case EncoderTemporarilyUnavailable     case InvalidVideoComposition     case ReferenceForbiddenByReferencePolicy     case InvalidOutputURLPathExtension     case ScreenCaptureFailed     case DisplayWasDisabled     case TorchLevelUnavailable     case IncompatibleAsset     case FailedToLoadMediaData     case ServerIncorrectlyConfigured     case ApplicationIsNotAuthorizedToUseDevice     case FailedToParse     case FileTypeDoesNotSupportSampleReferences     case UndecodableMediaData     case AirPlayControllerRequiresInternet     case AirPlayReceiverRequiresInternet     case VideoCompositorFailed     case CreateContentKeyRequestFailed } extension AVError : _BridgedNSError { } extension AVError : _BridgedNSError { } ``` |

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
