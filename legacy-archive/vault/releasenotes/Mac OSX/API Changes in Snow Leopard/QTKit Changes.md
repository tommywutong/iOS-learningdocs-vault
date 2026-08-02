---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/QTKit.html
archived_at: '2026-07-18T02:58:45.312455Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# QTKit Changes

## QTKit

QTCaptureAudioDataOutput.hAdded -[NSObject captureOutput:didOutputAudioSampleBuffer:fromConnection:]Added QTCaptureAudioDataOutputAdded -[QTCaptureAudioDataOutput delegate]Added -[QTCaptureAudioDataOutput outputAudioSampleBuffer:fromConnection:]Added -[QTCaptureAudioDataOutput setDelegate:]Added NSObject(QTCaptureAudioDataOutput_Delegate)Added #def QTCAPTUREAUDIODATAOUTPUT_HQTCaptureDecompressedVideoOutput.hRemoved NSObject(QTCaptureDecompressedVideoOutputDelegate)Added -[NSObject captureOutput:didDropVideoFrameWithSampleBuffer:fromConnection:]Added -[QTCaptureDecompressedVideoOutput automaticallyDropsLateVideoFrames]Added -[QTCaptureDecompressedVideoOutput minimumVideoFrameInterval]Added -[QTCaptureDecompressedVideoOutput setAutomaticallyDropsLateVideoFrames:]Added -[QTCaptureDecompressedVideoOutput setMinimumVideoFrameInterval:]Added NSObject(QTCaptureDecompressedVideoOutput_Delegate)Added #def QTCAPTUREDECOMPRESSEDVIDEOOUTPUT_HQTCaptureFileOutput.hRemoved NSObject(QTCaptureFileOutputDelegate)Added -[QTCaptureFileOutput isRecordingPaused]Added -[QTCaptureFileOutput maximumVideoSize]Added -[QTCaptureFileOutput minimumVideoFrameInterval]Added -[QTCaptureFileOutput pauseRecording]Added -[QTCaptureFileOutput resumeRecording]Added -[QTCaptureFileOutput setMaximumVideoSize:]Added -[QTCaptureFileOutput setMinimumVideoFrameInterval:]Added NSObject(QTCaptureFileOutput_Delegate)Added #def QTCAPTUREFILEOUTPUT_HQTCaptureVideoPreviewOutput.hRemoved NSObject(QTCaptureVideoPreviewOutputDelegate)Added NSObject(QTCaptureVideoPreviewOutput_Delegate)Added #def QTCAPTUREVIDEOPREVIEWOUTPUT_HQTCaptureView.hRemoved NSObject(QTCaptureViewDelegate)Added NSObject(QTCaptureView_Delegate)Added #def QTCAPTUREVIEW_HQTError.hAdded QTErrorMovieOpeningCannotBeAsynchronousQTKitDefines.hRemoved AliasDataHandlerSubTypeRemoved BaseMediaTypeRemoved FlashMediaTypeRemoved HandleDataHandlerSubTypeRemoved MPEGMediaTypeRemoved MovieMediaTypeRemoved MusicMediaTypeRemoved NullDataHandlerSubTypeRemoved PointerDataHandlerSubTypeRemoved ResourceDataHandlerSubTypeRemoved SkinMediaTypeRemoved SoundMediaTypeRemoved SpriteMediaTypeRemoved TextMediaTypeRemoved ThreeDeeMediaTypeRemoved TimeCode64MediaTypeRemoved TimeCodeMediaTypeRemoved TweenMediaTypeRemoved URLDataHandlerSubTypeRemoved VideoMediaTypeRemoved WiredActionHandlerTypeRemoved k16GrayCodecTypeRemoved k32AlphaGrayCodecTypeRemoved k422YpCbCr10CodecTypeRemoved k422YpCbCr16CodecTypeRemoved k422YpCbCr8CodecTypeRemoved k4444YpCbCrA8CodecTypeRemoved k4444YpCbCrA8RCodecTypeRemoved k444YpCbCr10CodecTypeRemoved k444YpCbCr8CodecTypeRemoved k48RGBCodecTypeRemoved k64ARGBCodecTypeRemoved kAVRJPEGCodecTypeRemoved kAnimationCodecTypeRemoved kBMPCodecTypeRemoved kBaseCodecTypeRemoved kCMYKCodecTypeRemoved kCinepakCodecTypeRemoved kCloudCodecTypeRemoved kComponentVideoCodecTypeRemoved kComponentVideoSignedRemoved kComponentVideoUnsignedRemoved kDVCNTSCCodecTypeRemoved kDVCPALCodecTypeRemoved kDVCPROHD1080i50CodecTypeRemoved kDVCPROHD1080i60CodecTypeRemoved kDVCPROHD720pCodecTypeRemoved kDVCPro100NTSCCodecTypeRemoved kDVCPro100PALCodecTypeRemoved kDVCPro50NTSCCodecTypeRemoved kDVCPro50PALCodecTypeRemoved kDVCProPALCodecTypeRemoved kFLCCodecTypeRemoved kFireCodecTypeRemoved kGIFCodecTypeRemoved kGraphicsCodecTypeRemoved kH261CodecTypeRemoved kH263CodecTypeRemoved kH264CodecTypeRemoved kIndeo4CodecTypeRemoved kJPEG2000CodecTypeRemoved kJPEGCodecTypeRemoved kMPEG4VisualCodecTypeRemoved kMacPaintCodecTypeRemoved kMicrosoftVideo1CodecTypeRemoved kMotionJPEGACodecTypeRemoved kMotionJPEGBCodecTypeRemoved kMpegYUV420CodecTypeRemoved kOpenDMLJPEGCodecTypeRemoved kPNGCodecTypeRemoved kPhotoCDCodecTypeRemoved kPixletCodecTypeRemoved kPlanarRGBCodecTypeRemoved kQTQuartzComposerMediaTypeRemoved kQuickDrawCodecTypeRemoved kQuickDrawGXCodecTypeRemoved kRawCodecTypeRemoved kSGICodecTypeRemoved kSorenson3CodecTypeRemoved kSorensonCodecTypeRemoved kSorensonYUV9CodecTypeRemoved kTIFFCodecTypeRemoved kTargaCodecTypeRemoved kVectorCodecTypeRemoved kVideoCodecTypeRemoved kWaterRippleCodecTypeRemoved kWindowsRawCodecTypeRemoved kYUV420CodecTypeAdded #def AVAILABLE_MAC_OS_X_VERSION_10_6_AND_LATERAdded #def MAC_OS_X_VERSION_10_6Added #def QTKIT_VERSION_7_6QTMovie.hRemoved NSObject(QTMovieDelegate)Removed QTMovie(QTDelegate)Removed QTMovie(QTEditing)Removed QTMovie(QTMovieChapters)Removed QTMovie(QTMovieFormat)Removed QTMovie(QTMovieImage)Removed QTMovie(QTMovieInitialization)Removed QTMovie(QTMovieInspection)Removed QTMovie(QTMoviePlaybackControl)Removed QTMovie(QTMovieThreading)Removed QTMovie(QTMovieTime)Removed QTMovie(QTMovieVisualContext)Removed QTMovie(QTMovieVisualSupport)Removed QTMovie(QTPrimitives)Removed QTMovie(QTSelection)Added -[QTMovie cancelLoading]Added NSObject(QTMovie_Delegate)Added #def QTMOVIE_HAdded QTMovie(QTMovie_Chapters)Added QTMovie(QTMovie_Delegate)Added QTMovie(QTMovie_Editing)Added QTMovie(QTMovie_Format)Added QTMovie(QTMovie_Image)Added QTMovie(QTMovie_Initialization)Added QTMovie(QTMovie_Inspection)Added QTMovie(QTMovie_PlaybackControl)Added QTMovie(QTMovie_Primitives)Added QTMovie(QTMovie_Selection)Added QTMovie(QTMovie_Threading)Added QTMovie(QTMovie_Time)Added QTMovie(QTMovie_VisualContext)Added QTMovie(QTMovie_VisualSupport)Added QTMovieOpenAsyncRequiredAttributeAdded QTMovieOpenForPlaybackAttributeQTMovieView.hRemoved -[QTMovieView initWithFrame:]Removed NSObject(QTMovieViewDelegate)Added NSObject(QTMovieView_Delegate)Added #def QTMOVIEVIEW_HQTSampleBuffer.hRemoved QTSampleBuffer(QTSampleBufferUseCount)Added QTSampleBuffer(QTSampleBuffer_UseCount)QTTrack.hRemoved QTTrack(QTTrackVisualSupport)Added #def QTTRACK_HAdded QTTrack(QTTrack_VisualSupport)QTUtilities.hAdded #def QTUTILITIES_H

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
