---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/ReplayKit.html
archived_at: '2026-07-18T02:57:54.462495Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# ReplayKit Changes for Swift

### ReplayKit (Added)

Added [NSExtensionContext.completeRequest(withBroadcast: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : NSCoding & NSObjectProtocol]?)](https://developer.apple.com/documentation/foundation/nsextensioncontext/2143167-completerequest)Added [NSExtensionContext.loadBroadcastingApplicationInfo(completion: (String, String, UIImage?) -> Swift.Void)](https://developer.apple.com/documentation/foundation/nsextensioncontext/1845240-loadbroadcastingapplicationinfow)Added [RPBroadcastActivityViewController](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller)Added [RPBroadcastActivityViewController.delegate](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/1771691-delegate)Added [RPBroadcastActivityViewController.load(handler: (RPBroadcastActivityViewController?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/1648331-loadbroadcastactivityviewcontrol)Added [RPBroadcastActivityViewControllerDelegate](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontrollerdelegate)Added [RPBroadcastActivityViewControllerDelegate.broadcastActivityViewController(_: RPBroadcastActivityViewController, didFinishWith: RPBroadcastController?, error: Error?)](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontrollerdelegate/1648323-broadcastactivityviewcontroller)Added [RPBroadcastConfiguration](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration)Added [RPBroadcastConfiguration.clipDuration](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration/1845249-clipduration)Added [RPBroadcastConfiguration.videoCompressionProperties](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration/1845248-videocompressionproperties)Added [RPBroadcastController](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller)Added [RPBroadcastController.broadcastExtensionBundleID](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143150-broadcastextensionbundleid)Added [RPBroadcastController.broadcastURL](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648337-broadcasturl)Added [RPBroadcastController.delegate](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143149-delegate)Added [RPBroadcastController.finishBroadcast(handler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648336-finishbroadcastwithhandler)Added [RPBroadcastController.isBroadcasting](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648332-broadcasting)Added [RPBroadcastController.isPaused](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143151-paused)Added [RPBroadcastController.pauseBroadcast()](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648333-pausebroadcast)Added [RPBroadcastController.resumeBroadcast()](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648335-resumebroadcast)Added [RPBroadcastController.serviceInfo](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143153-serviceinfo)Added [RPBroadcastController.startBroadcast(handler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648327-startbroadcastwithhandler)Added [RPBroadcastControllerDelegate](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate)Added [RPBroadcastControllerDelegate.broadcastController(_: RPBroadcastController, didFinishWithError: Error?)](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/1648328-broadcastcontroller)Added [RPBroadcastControllerDelegate.broadcastController(_: RPBroadcastController, didUpdateServiceInfo: [String : NSCoding & NSObjectProtocol])](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/2143152-broadcastcontroller)Added [RPBroadcastHandler](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler)Added [RPBroadcastHandler.updateServiceInfo(_: [String : NSCoding & NSObjectProtocol])](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler/2143171-updateserviceinfo)Added [RPBroadcastMP4ClipHandler](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler)Added [RPBroadcastMP4ClipHandler.finishedProcessingMP4Clip(withUpdatedBroadcastConfiguration: RPBroadcastConfiguration?, error: Error?)](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler/2097558-finishedprocessingmp4clipwithupd)Added [RPBroadcastMP4ClipHandler.processMP4Clip(with: URL?, setupInfo: [String : NSObject]?, finished: Bool)](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler/2143172-processmp4clip)Added [RPBroadcastSampleHandler](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler)Added [RPBroadcastSampleHandler.broadcastFinished()](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143169-broadcastfinished)Added [RPBroadcastSampleHandler.broadcastPaused()](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143174-broadcastpaused)Added [RPBroadcastSampleHandler.broadcastResumed()](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143168-broadcastresumed)Added [RPBroadcastSampleHandler.broadcastStarted(withSetupInfo: [String : NSObject]?)](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143170-broadcaststarted)Added [RPBroadcastSampleHandler.processSampleBuffer(_: CMSampleBuffer, with: RPSampleBufferType)](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2123045-processsamplebuffer)Added [RPPreviewViewController](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller)Added [RPPreviewViewController.mode](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller/1841266-mode)Added [RPPreviewViewController.previewControllerDelegate](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller/1620989-previewcontrollerdelegate)Added [RPPreviewViewControllerDelegate](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate)Added [RPPreviewViewControllerDelegate.previewControllerDidFinish(_: RPPreviewViewController)](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate/1620988-previewcontrollerdidfinish)Added [RPPreviewViewControllerMode [enum]](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode)Added [RPPreviewViewControllerMode.preview](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode/rppreviewviewcontrollermodepreview)Added [RPPreviewViewControllerMode.share](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode/share)Added [RPRecordingErrorCode [enum]](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode)Added [RPRecordingErrorCode.broadcastInvalidSession](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/broadcastinvalidsession)Added [RPRecordingErrorCode.contentResize](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorcontentresize)Added [RPRecordingErrorCode.disabled](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrordisabled)Added [RPRecordingErrorCode.failed](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorfailed)Added [RPRecordingErrorCode.failedToStart](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorfailedtostart)Added [RPRecordingErrorCode.insufficientStorage](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/insufficientstorage)Added [RPRecordingErrorCode.interrupted](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorinterrupted)Added [RPRecordingErrorCode.systemDormancy](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorsystemdormancy)Added [RPRecordingErrorCode.unknown](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorunknown)Added [RPRecordingErrorCode.userDeclined](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/userdeclined)Added [RPSampleBufferType [enum]](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype)Added [RPSampleBufferType.audioApp](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype/rpsamplebuffertypeaudioapp)Added [RPSampleBufferType.audioMic](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype/audiomic)Added [RPSampleBufferType.video](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype/rpsamplebuffertypevideo)Added [RPScreenRecorder](https://developer.apple.com/documentation/replaykit/rpscreenrecorder)Added [RPScreenRecorder.delegate](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620980-delegate)Added [RPScreenRecorder.discardRecording(handler: () -> Swift.Void)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620994-discardrecordingwithhandler)Added [RPScreenRecorder.isAvailable](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620992-isavailable)Added [RPScreenRecorder.isRecording](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620981-recording)Added [RPScreenRecorder.shared() -> RPScreenRecorder [class]](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620993-sharedrecorder)Added [RPScreenRecorder.startRecording(handler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1649019-startrecordingwithhandler)Added [RPScreenRecorder.startRecording(withMicrophoneEnabled: Bool, handler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620979-startrecording)Added [RPScreenRecorder.stopRecording(handler: ( (RPPreviewViewController?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620990-stoprecordingwithhandler)Added [RPScreenRecorderDelegate](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate)Added [RPScreenRecorderDelegate.screenRecorder(_: RPScreenRecorder, didStopRecordingWithError: Error, previewViewController: RPPreviewViewController?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/1620983-screenrecorder)Added [RPScreenRecorderDelegate.screenRecorderDidChangeAvailability(_: RPScreenRecorder)](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/1620986-screenrecorderdidchangeavailabil)Added [RPRecordingErrorDomain](https://developer.apple.com/documentation/replaykit/rprecordingerrordomain)

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
