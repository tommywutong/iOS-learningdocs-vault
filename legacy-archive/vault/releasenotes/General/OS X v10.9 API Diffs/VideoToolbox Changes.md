---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/VideoToolbox.html
archived_at: '2026-07-18T02:54:22.259297Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# VideoToolbox Changes

## VideoToolbox

VTBase.hAdded #def VT_AVAILABLE_STARTINGVTCompressionProperties.hAdded [kVTCompressionPropertyKey_H264EntropyMode](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_h264entropymode)Added [kVTCompressionPropertyKey_RealTime](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_realtime)Added [kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_usinghardwareacceleratedvideoencoder)Added [kVTH264EntropyMode_CABAC](https://developer.apple.com/documentation/videotoolbox/kvth264entropymode_cabac)Added [kVTH264EntropyMode_CAVLC](https://developer.apple.com/documentation/videotoolbox/kvth264entropymode_cavlc)Added [kVTProfileLevel_H264_Baseline_4_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_4_0)Added [kVTProfileLevel_H264_Baseline_4_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_4_2)Added [kVTProfileLevel_H264_Baseline_5_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_5_0)Added [kVTProfileLevel_H264_Baseline_5_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_5_1)Added [kVTProfileLevel_H264_Baseline_5_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_5_2)Added [kVTProfileLevel_H264_Baseline_AutoLevel](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_autolevel)Added [kVTProfileLevel_H264_Extended_AutoLevel](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_extended_autolevel)Added [kVTProfileLevel_H264_High_3_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_3_0)Added [kVTProfileLevel_H264_High_3_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_3_1)Added [kVTProfileLevel_H264_High_3_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_3_2)Added [kVTProfileLevel_H264_High_4_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_4_0)Added [kVTProfileLevel_H264_High_4_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_4_1)Added [kVTProfileLevel_H264_High_4_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_4_2)Added [kVTProfileLevel_H264_High_5_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_5_1)Added [kVTProfileLevel_H264_High_5_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_5_2)Added [kVTProfileLevel_H264_High_AutoLevel](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_autolevel)Added [kVTProfileLevel_H264_Main_4_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_4_2)Added [kVTProfileLevel_H264_Main_5_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_5_1)Added [kVTProfileLevel_H264_Main_5_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_5_2)Added [kVTProfileLevel_H264_Main_AutoLevel](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_autolevel)Added [kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_enablehardwareacceleratedvideoencoder)Added [kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_requirehardwareacceleratedvideoencoder)VTCompressionSession.hAdded [VTCompressionSessionPrepareToEncodeFrames()](https://developer.apple.com/documentation/videotoolbox/1428283-vtcompressionsessionpreparetoenc)VTDecompressionProperties.hAdded [kVTDecompressionPropertyKey_OutputPoolRequestedMinimumBufferCount](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_outputpoolrequestedminimumbuffercount)Added [kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_usinghardwareacceleratedvideodecoder)Added [kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder](https://developer.apple.com/documentation/videotoolbox/kvtvideodecoderspecification_enablehardwareacceleratedvideodecoder)Added [kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder](https://developer.apple.com/documentation/videotoolbox/kvtvideodecoderspecification_requirehardwareacceleratedvideodecoder)VTProfessionalVideoWorkflow.hAdded [VTRegisterProfessionalVideoWorkflowVideoDecoders()](https://developer.apple.com/documentation/videotoolbox/1437860-vtregisterprofessionalvideoworkf)

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
