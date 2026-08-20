---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/ReplayKit.html
archived_at: '2026-07-18T02:57:27.649032Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# ReplayKit Changes for Objective-C

### ReplayKit (Added)

#### RPBroadcast.h (Added)

Added [RPBroadcastActivityViewController](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller)Added [RPBroadcastActivityViewController.delegate](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/1771691-delegate)Added [+[RPBroadcastActivityViewController loadBroadcastActivityViewControllerWithHandler:]](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/1648331-loadbroadcastactivityviewcontrol)Added [RPBroadcastActivityViewControllerDelegate](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontrollerdelegate)Added [-[RPBroadcastActivityViewControllerDelegate broadcastActivityViewController:didFinishWithBroadcastController:error:]](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontrollerdelegate/1648323-broadcastactivityviewcontroller)Added [RPBroadcastController](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller)Added [RPBroadcastController.broadcastExtensionBundleID](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143150-broadcastextensionbundleid)Added [RPBroadcastController.broadcasting](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648332-broadcasting)Added [RPBroadcastController.broadcastURL](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648337-broadcasturl)Added [RPBroadcastController.delegate](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143149-delegate)Added [-[RPBroadcastController finishBroadcastWithHandler:]](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648336-finishbroadcast)Added [-[RPBroadcastController pauseBroadcast]](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648333-pausebroadcast)Added [RPBroadcastController.paused](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143151-ispaused)Added [-[RPBroadcastController resumeBroadcast]](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648335-resumebroadcast)Added [RPBroadcastController.serviceInfo](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143153-serviceinfo)Added [-[RPBroadcastController startBroadcastWithHandler:]](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648327-startbroadcast)Added [RPBroadcastControllerDelegate](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate)Added [-[RPBroadcastControllerDelegate broadcastController:didFinishWithError:]](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/1648328-broadcastcontroller)Added [-[RPBroadcastControllerDelegate broadcastController:didUpdateServiceInfo:]](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/2143152-broadcastcontroller)

#### RPBroadcastConfiguration.h (Added)

Added [RPBroadcastConfiguration](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration)Added [RPBroadcastConfiguration.clipDuration](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration/1845249-clipduration)Added [RPBroadcastConfiguration.videoCompressionProperties](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration/1845248-videocompressionproperties)

#### RPBroadcastExtension.h (Added)

Added [-[NSExtensionContext completeRequestWithBroadcastURL:broadcastConfiguration:setupInfo:]](https://developer.apple.com/documentation/foundation/nsextensioncontext/2143167-completerequest)Added [-[NSExtensionContext loadBroadcastingApplicationInfoWithCompletion:]](https://developer.apple.com/documentation/foundation/nsextensioncontext/1845240-loadbroadcastingapplicationinfow)Added [RPBroadcastHandler](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler)Added [-[RPBroadcastHandler updateServiceInfo:]](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler/2143171-updateserviceinfo)Added [RPBroadcastMP4ClipHandler](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler)Added [-[RPBroadcastMP4ClipHandler finishedProcessingMP4ClipWithUpdatedBroadcastConfiguration:error:]](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler/2097558-finishedprocessingmp4clip)Added [-[RPBroadcastMP4ClipHandler processMP4ClipWithURL:setupInfo:finished:]](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler/2143172-processmp4clip)Added [RPBroadcastSampleHandler](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler)Added [-[RPBroadcastSampleHandler broadcastFinished]](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143169-broadcastfinished)Added [-[RPBroadcastSampleHandler broadcastPaused]](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143174-broadcastpaused)Added [-[RPBroadcastSampleHandler broadcastResumed]](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143168-broadcastresumed)Added [-[RPBroadcastSampleHandler broadcastStartedWithSetupInfo:]](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143170-broadcaststarted)Added [-[RPBroadcastSampleHandler processSampleBuffer:withType:]](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2123045-processsamplebuffer)Added NSExtensionContext(RPBroadcastExtension)Added [RPSampleBufferType](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype)Added [RPSampleBufferTypeAudioApp](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype/rpsamplebuffertypeaudioapp)Added [RPSampleBufferTypeAudioMic](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype/audiomic)Added [RPSampleBufferTypeVideo](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype/video)

#### RPError.h (Added)

Added [RPRecordingErrorBroadcastInvalidSession](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/broadcastinvalidsession)Added [RPRecordingErrorCode](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode)Added [RPRecordingErrorContentResize](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/contentresize)Added [RPRecordingErrorDisabled](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrordisabled)Added [RPRecordingErrorDomain](https://developer.apple.com/documentation/replaykit/rprecordingerrordomain)Added [RPRecordingErrorFailed](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/failed)Added [RPRecordingErrorFailedToStart](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorfailedtostart)Added [RPRecordingErrorInsufficientStorage](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/insufficientstorage)Added [RPRecordingErrorInterrupted](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorinterrupted)Added [RPRecordingErrorSystemDormancy](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorsystemdormancy)Added [RPRecordingErrorUnknown](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorunknown)Added [RPRecordingErrorUserDeclined](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerroruserdeclined)

#### RPPreviewViewController.h (Added)

Added [RPPreviewViewController](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller)Added [RPPreviewViewController.mode](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller/1841266-mode)Added [RPPreviewViewController.previewControllerDelegate](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller/1620989-previewcontrollerdelegate)Added [RPPreviewViewControllerDelegate](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate)Added [-[RPPreviewViewControllerDelegate previewControllerDidFinish:]](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate/1620988-previewcontrollerdidfinish)Added [RPPreviewViewControllerMode](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode)Added [RPPreviewViewControllerModePreview](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode/preview)Added [RPPreviewViewControllerModeShare](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode/share)

#### RPScreenRecorder.h (Added)

Added [RPScreenRecorder](https://developer.apple.com/documentation/replaykit/rpscreenrecorder)Added [RPScreenRecorder.available](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620992-available)Added [RPScreenRecorder.delegate](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620980-delegate)Added [-[RPScreenRecorder discardRecordingWithHandler:]](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620994-discardrecordingwithhandler)Added [RPScreenRecorder.recording](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620981-isrecording)Added [+[RPScreenRecorder sharedRecorder]](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620993-sharedrecorder)Added [-[RPScreenRecorder startRecordingWithHandler:]](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1649019-startrecordingwithhandler)Added [-[RPScreenRecorder startRecordingWithMicrophoneEnabled:handler:]](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620979-startrecordingwithmicrophoneenab)Added [-[RPScreenRecorder stopRecordingWithHandler:]](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620990-stoprecordingwithhandler)Added [RPScreenRecorderDelegate](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate)Added [-[RPScreenRecorderDelegate screenRecorder:didStopRecordingWithError:previewViewController:]](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/1620983-screenrecorder)Added [-[RPScreenRecorderDelegate screenRecorderDidChangeAvailability:]](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/1620986-screenrecorderdidchangeavailabil)

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
