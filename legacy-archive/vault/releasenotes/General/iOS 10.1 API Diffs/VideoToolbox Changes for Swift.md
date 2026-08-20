---
title: iOS 10.1 API Diffs
apple_id: TP40017545
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS101APIDiffs/Swift/VideoToolbox.html
archived_at: '2026-07-18T02:54:48.526915Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.1 API Diffs](iOS%2010.0%20to%20iOS%2010.1%20API%20Differences.md)


# VideoToolbox Changes for Swift

### VideoToolbox

Modified [VTCompressionSessionEncodeFrameWithOutputHandler(_: VTCompressionSession, _: CVImageBuffer, _: CMTime, _: CMTime, _: CFDictionary?, _: UnsafeMutablePointer<VTEncodeInfoFlags>?, _: VideoToolbox.VTCompressionOutputHandler) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428281-vtcompressionsessionencodeframew)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionEncodeFrameWithOutputHandler(_ session: VTCompressionSession, _ imageBuffer: CVImageBuffer, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary?, _ infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, _ outputHandler: VideoToolbox.VTCompressionOutputHandler) -> OSStatus ``` |
| To | ``` func VTCompressionSessionEncodeFrameWithOutputHandler(_ session: VTCompressionSession, _ imageBuffer: CVImageBuffer, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary?, _ infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, _ outputHandler: @escaping VideoToolbox.VTCompressionOutputHandler) -> OSStatus ``` |

Modified [VTDecompressionSessionDecodeFrameWithOutputHandler(_: VTDecompressionSession, _: CMSampleBuffer, _: VTDecodeFrameFlags, _: UnsafeMutablePointer<VTDecodeInfoFlags>?, _: VideoToolbox.VTDecompressionOutputHandler) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536067-vtdecompressionsessiondecodefram)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionDecodeFrameWithOutputHandler(_ session: VTDecompressionSession, _ sampleBuffer: CMSampleBuffer, _ decodeFlags: VTDecodeFrameFlags, _ infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, _ outputHandler: VideoToolbox.VTDecompressionOutputHandler) -> OSStatus ``` |
| To | ``` func VTDecompressionSessionDecodeFrameWithOutputHandler(_ session: VTDecompressionSession, _ sampleBuffer: CMSampleBuffer, _ decodeFlags: VTDecodeFrameFlags, _ infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, _ outputHandler: @escaping VideoToolbox.VTDecompressionOutputHandler) -> OSStatus ``` |

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
