---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/ReplayKit.html
archived_at: '2026-07-18T02:56:57.809133Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# ReplayKit Changes for Swift

### ReplayKit (Added)

Added [RPPreviewViewController](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller)Added [RPPreviewViewController.previewControllerDelegate](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller/1620989-previewcontrollerdelegate)Added [RPPreviewViewControllerDelegate](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate)Added [RPPreviewViewControllerDelegate.previewController(_: RPPreviewViewController, didFinishWithActivityTypes: Set<String>)](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate/1620985-previewcontroller)Added [RPPreviewViewControllerDelegate.previewControllerDidFinish(_: RPPreviewViewController)](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate/1620988-previewcontrollerdidfinish)Added [RPRecordingErrorCode [enum]](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode)Added [RPRecordingErrorCode.ContentResize](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorcontentresize)Added [RPRecordingErrorCode.Disabled](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrordisabled)Added [RPRecordingErrorCode.Failed](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorfailed)Added [RPRecordingErrorCode.FailedToStart](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorfailedtostart)Added [RPRecordingErrorCode.InsufficientStorage](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/insufficientstorage)Added [RPRecordingErrorCode.Interrupted](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorinterrupted)Added [RPRecordingErrorCode.Unknown](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorunknown)Added [RPRecordingErrorCode.UserDeclined](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/userdeclined)Added [RPScreenRecorder](https://developer.apple.com/documentation/replaykit/rpscreenrecorder)Added [RPScreenRecorder.available](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620992-isavailable)Added [RPScreenRecorder.delegate](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620980-delegate)Added [RPScreenRecorder.discardRecordingWithHandler(_: () -> Void)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620994-discardrecordingwithhandler)Added [RPScreenRecorder.microphoneEnabled](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620987-ismicrophoneenabled)Added [RPScreenRecorder.recording](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620981-recording)Added [RPScreenRecorder.sharedRecorder() -> RPScreenRecorder [class]](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620993-sharedrecorder)Added [RPScreenRecorder.startRecordingWithMicrophoneEnabled(_: Bool, handler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620979-startrecording)Added [RPScreenRecorder.stopRecordingWithHandler(_: ((RPPreviewViewController?, NSError?) -> Void)?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620990-stoprecordingwithhandler)Added [RPScreenRecorderDelegate](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate)Added [RPScreenRecorderDelegate.screenRecorder(_: RPScreenRecorder, didStopRecordingWithError: NSError, previewViewController: RPPreviewViewController?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/1620983-screenrecorder)Added [RPScreenRecorderDelegate.screenRecorderDidChangeAvailability(_: RPScreenRecorder)](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/1620986-screenrecorderdidchangeavailabil)Added [RPRecordingErrorDomain](https://developer.apple.com/documentation/replaykit/rprecordingerrordomain)

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
