---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/QuickTime.html
archived_at: '2026-07-15T07:34:47.170215Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# QuickTime Changes

## QuickTime

ImageCodec.hAdded #def DisposeImageCodecDrawBandCompleteUPPAdded #def DisposeImageCodecMPDrawBandUPPAdded #def DisposeImageCodecTimeTriggerUPPAdded #def InvokeImageCodecDrawBandCompleteUPPAdded #def InvokeImageCodecMPDrawBandUPPAdded #def InvokeImageCodecTimeTriggerUPPAdded #def NewImageCodecDrawBandCompleteUPPAdded #def NewImageCodecMPDrawBandUPPAdded #def NewImageCodecTimeTriggerUPPImageCompression.hAdded #def DisposeICMAlignmentUPPAdded #def DisposeICMCompletionUPPAdded #def DisposeICMConvertDataFormatUPPAdded #def DisposeICMCursorShieldedUPPAdded #def DisposeICMDataUPPAdded #def DisposeICMFlushUPPAdded #def DisposeICMMemoryDisposedUPPAdded #def DisposeICMProgressUPPAdded #def DisposeQDPixUPPAdded #def DisposeQTComponentPropertyListenerFilterUPPAdded #def DisposeQTComponentPropertyListenerUPPAdded #def DisposeStdPixUPPAdded #def InvokeICMAlignmentUPPAdded #def InvokeICMCompletionUPPAdded #def InvokeICMConvertDataFormatUPPAdded #def InvokeICMCursorShieldedUPPAdded #def InvokeICMDataUPPAdded #def InvokeICMFlushUPPAdded #def InvokeICMMemoryDisposedUPPAdded #def InvokeICMProgressUPPAdded #def InvokeQDPixUPPAdded #def InvokeQTComponentPropertyListenerFilterUPPAdded #def InvokeQTComponentPropertyListenerUPPAdded #def InvokeStdPixUPPAdded #def NewICMAlignmentUPPAdded #def NewICMCompletionUPPAdded #def NewICMConvertDataFormatUPPAdded #def NewICMCursorShieldedUPPAdded #def NewICMDataUPPAdded #def NewICMFlushUPPAdded #def NewICMMemoryDisposedUPPAdded #def NewICMProgressUPPAdded #def NewQDPixUPPAdded #def NewQTComponentPropertyListenerFilterUPPAdded #def NewQTComponentPropertyListenerUPPAdded #def NewStdPixUPPMediaHandlers.hAdded #def DisposePrePrerollCompleteUPPAdded #def InvokePrePrerollCompleteUPPAdded #def NewPrePrerollCompleteUPPMovies.hAdded #def DisposeActionsUPPAdded #def DisposeDoMCActionUPPAdded #def DisposeGetMovieUPPAdded #def DisposeMCActionFilterUPPAdded #def DisposeMCActionFilterWithRefConUPPAdded #def DisposeMCActionNotificationUPPAdded #def DisposeMovieDrawingCompleteUPPAdded #def DisposeMovieExecuteWiredActionsUPPAdded #def DisposeMoviePrePrerollCompleteUPPAdded #def DisposeMoviePreviewCallOutUPPAdded #def DisposeMovieProgressUPPAdded #def DisposeMovieRgnCoverUPPAdded #def DisposeMoviesErrorUPPAdded #def DisposeQTBandwidthNotificationUPPAdded #def DisposeQTCallBackUPPAdded #def DisposeQTEffectListFilterUPPAdded #def DisposeQTMoviePropertyListenerUPPAdded #def DisposeQTNextTaskNeededSoonerCallbackUPPAdded #def DisposeQTSyncTaskUPPAdded #def DisposeQTTrackPropertyListenerUPPAdded #def DisposeTextMediaUPPAdded #def DisposeTrackTransferUPPAdded #def DisposeTweenerDataUPPAdded #def InvokeActionsUPPAdded #def InvokeDoMCActionUPPAdded #def InvokeGetMovieUPPAdded #def InvokeMCActionFilterUPPAdded #def InvokeMCActionFilterWithRefConUPPAdded #def InvokeMCActionNotificationUPPAdded #def InvokeMovieDrawingCompleteUPPAdded #def InvokeMovieExecuteWiredActionsUPPAdded #def InvokeMoviePrePrerollCompleteUPPAdded #def InvokeMoviePreviewCallOutUPPAdded #def InvokeMovieProgressUPPAdded #def InvokeMovieRgnCoverUPPAdded #def InvokeMoviesErrorUPPAdded #def InvokeQTBandwidthNotificationUPPAdded #def InvokeQTCallBackUPPAdded #def InvokeQTEffectListFilterUPPAdded #def InvokeQTMoviePropertyListenerUPPAdded #def InvokeQTNextTaskNeededSoonerCallbackUPPAdded #def InvokeQTSyncTaskUPPAdded #def InvokeQTTrackPropertyListenerUPPAdded #def InvokeTextMediaUPPAdded #def InvokeTrackTransferUPPAdded #def InvokeTweenerDataUPPAdded #def NewActionsUPPAdded #def NewDoMCActionUPPAdded #def NewGetMovieUPPAdded #def NewMCActionFilterUPPAdded #def NewMCActionFilterWithRefConUPPAdded #def NewMCActionNotificationUPPAdded #def NewMovieDrawingCompleteUPPAdded #def NewMovieExecuteWiredActionsUPPAdded #def NewMoviePrePrerollCompleteUPPAdded #def NewMoviePreviewCallOutUPPAdded #def NewMovieProgressUPPAdded #def NewMovieRgnCoverUPPAdded #def NewMoviesErrorUPPAdded #def NewQTBandwidthNotificationUPPAdded #def NewQTCallBackUPPAdded #def NewQTEffectListFilterUPPAdded #def NewQTMoviePropertyListenerUPPAdded #def NewQTNextTaskNeededSoonerCallbackUPPAdded #def NewQTSyncTaskUPPAdded #def NewQTTrackPropertyListenerUPPAdded #def NewTextMediaUPPAdded #def NewTrackTransferUPPAdded #def NewTweenerDataUPPAdded kQTMovieInstantiationPropertyID_GatherRefMovieCountsQTStreamingComponents.hAdded #def DisposeRTPMPDataReleaseUPPAdded #def DisposeRTPPBCallbackUPPAdded #def InvokeRTPMPDataReleaseUPPAdded #def InvokeRTPPBCallbackUPPAdded #def NewRTPMPDataReleaseUPPAdded #def NewRTPPBCallbackUPPQuickTimeComponents.hAdded #def DisposeCDataHandlerUPPAdded #def DisposeCharDataHandlerUPPAdded #def DisposeCommentHandlerUPPAdded #def DisposeDataHCompletionUPPAdded #def DisposeEndDocumentHandlerUPPAdded #def DisposeEndElementHandlerUPPAdded #def DisposeMovieExportGetDataUPPAdded #def DisposeMovieExportGetPropertyUPPAdded #def DisposeMovieExportStageReachedCallbackUPPAdded #def DisposePreprocessInstructionHandlerUPPAdded #def DisposeSCModalFilterUPPAdded #def DisposeSCModalHookUPPAdded #def DisposeSGAddFrameBottleUPPAdded #def DisposeSGCompressBottleUPPAdded #def DisposeSGCompressCompleteBottleUPPAdded #def DisposeSGDataUPPAdded #def DisposeSGDisplayBottleUPPAdded #def DisposeSGDisplayCompressBottleUPPAdded #def DisposeSGGrabBottleUPPAdded #def DisposeSGGrabCompleteBottleUPPAdded #def DisposeSGGrabCompressCompleteBottleUPPAdded #def DisposeSGModalFilterUPPAdded #def DisposeSGTransferFrameBottleUPPAdded #def DisposeStartDocumentHandlerUPPAdded #def DisposeStartElementHandlerUPPAdded #def DisposeVdigIntUPPAdded #def InvokeCDataHandlerUPPAdded #def InvokeCharDataHandlerUPPAdded #def InvokeCommentHandlerUPPAdded #def InvokeDataHCompletionUPPAdded #def InvokeEndDocumentHandlerUPPAdded #def InvokeEndElementHandlerUPPAdded #def InvokeMovieExportGetDataUPPAdded #def InvokeMovieExportGetPropertyUPPAdded #def InvokeMovieExportStageReachedCallbackUPPAdded #def InvokePreprocessInstructionHandlerUPPAdded #def InvokeSCModalFilterUPPAdded #def InvokeSCModalHookUPPAdded #def InvokeSGAddFrameBottleUPPAdded #def InvokeSGCompressBottleUPPAdded #def InvokeSGCompressCompleteBottleUPPAdded #def InvokeSGDataUPPAdded #def InvokeSGDisplayBottleUPPAdded #def InvokeSGDisplayCompressBottleUPPAdded #def InvokeSGGrabBottleUPPAdded #def InvokeSGGrabCompleteBottleUPPAdded #def InvokeSGGrabCompressCompleteBottleUPPAdded #def InvokeSGModalFilterUPPAdded #def InvokeSGTransferFrameBottleUPPAdded #def InvokeStartDocumentHandlerUPPAdded #def InvokeStartElementHandlerUPPAdded #def InvokeVdigIntUPPAdded #def NewCDataHandlerUPPAdded #def NewCharDataHandlerUPPAdded #def NewCommentHandlerUPPAdded #def NewDataHCompletionUPPAdded #def NewEndDocumentHandlerUPPAdded #def NewEndElementHandlerUPPAdded #def NewMovieExportGetDataUPPAdded #def NewMovieExportGetPropertyUPPAdded #def NewMovieExportStageReachedCallbackUPPAdded #def NewPreprocessInstructionHandlerUPPAdded #def NewSCModalFilterUPPAdded #def NewSCModalHookUPPAdded #def NewSGAddFrameBottleUPPAdded #def NewSGCompressBottleUPPAdded #def NewSGCompressCompleteBottleUPPAdded #def NewSGDataUPPAdded #def NewSGDisplayBottleUPPAdded #def NewSGDisplayCompressBottleUPPAdded #def NewSGGrabBottleUPPAdded #def NewSGGrabCompleteBottleUPPAdded #def NewSGGrabCompressCompleteBottleUPPAdded #def NewSGModalFilterUPPAdded #def NewSGTransferFrameBottleUPPAdded #def NewStartDocumentHandlerUPPAdded #def NewStartElementHandlerUPPAdded #def NewVdigIntUPPQuickTimeMusic.hAdded #def DisposeMusicMIDISendUPPAdded #def DisposeMusicOfflineDataUPPAdded #def DisposeTuneCallBackUPPAdded #def DisposeTunePlayCallBackUPPAdded #def InvokeMusicMIDISendUPPAdded #def InvokeMusicOfflineDataUPPAdded #def InvokeTuneCallBackUPPAdded #def InvokeTunePlayCallBackUPPAdded #def NewMusicMIDISendUPPAdded #def NewMusicOfflineDataUPPAdded #def NewTuneCallBackUPPAdded #def NewTunePlayCallBackUPPQuickTimeStreaming.hAdded #def DisposeQTSModalFilterUPPAdded #def DisposeQTSNotificationUPPAdded #def DisposeQTSPanelFilterUPPAdded #def InvokeQTSModalFilterUPPAdded #def InvokeQTSNotificationUPPAdded #def InvokeQTSPanelFilterUPPAdded #def NewQTSModalFilterUPPAdded #def NewQTSNotificationUPPAdded #def NewQTSPanelFilterUPPQuickTimeVR.hAdded #def DisposeQTVRBackBufferImagingUPPAdded #def DisposeQTVREnteringNodeUPPAdded #def DisposeQTVRImagingCompleteUPPAdded #def DisposeQTVRInterceptUPPAdded #def DisposeQTVRLeavingNodeUPPAdded #def DisposeQTVRMouseOverHotSpotUPPAdded #def InvokeQTVRBackBufferImagingUPPAdded #def InvokeQTVREnteringNodeUPPAdded #def InvokeQTVRImagingCompleteUPPAdded #def InvokeQTVRInterceptUPPAdded #def InvokeQTVRLeavingNodeUPPAdded #def InvokeQTVRMouseOverHotSpotUPPAdded #def NewQTVRBackBufferImagingUPPAdded #def NewQTVREnteringNodeUPPAdded #def NewQTVRImagingCompleteUPPAdded #def NewQTVRInterceptUPPAdded #def NewQTVRLeavingNodeUPPAdded #def NewQTVRMouseOverHotSpotUPP

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
