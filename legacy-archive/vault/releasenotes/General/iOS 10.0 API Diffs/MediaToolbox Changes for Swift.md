---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/MediaToolbox.html
archived_at: '2026-07-18T02:55:32.069644Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# MediaToolbox Changes for Swift

### MediaToolbox

Modified MTAudioProcessingTapCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTAudioProcessingTapCallbacks {     var version: Int32     var clientInfo: UnsafeMutablePointer<Void>     var `init`: MTAudioProcessingTapInitCallback?     var finalize: MTAudioProcessingTapFinalizeCallback?     var prepare: MTAudioProcessingTapPrepareCallback?     var unprepare: MTAudioProcessingTapUnprepareCallback?     var process: MTAudioProcessingTapProcessCallback } ``` |
| To | ``` struct MTAudioProcessingTapCallbacks {     var version: Int32     var clientInfo: UnsafeMutableRawPointer?     var `init`: MediaToolbox.MTAudioProcessingTapInitCallback?     var finalize: MediaToolbox.MTAudioProcessingTapFinalizeCallback?     var prepare: MediaToolbox.MTAudioProcessingTapPrepareCallback?     var unprepare: MediaToolbox.MTAudioProcessingTapUnprepareCallback?     var process: MediaToolbox.MTAudioProcessingTapProcessCallback } ``` |

Modified MTAudioProcessingTapCallbacks.clientInfo

|  | Declaration |
| --- | --- |
| From | ``` var clientInfo: UnsafeMutablePointer<Void> ``` |
| To | ``` var clientInfo: UnsafeMutableRawPointer? ``` |

Modified MTAudioProcessingTapCallbacks.finalize

|  | Declaration |
| --- | --- |
| From | ``` var finalize: MTAudioProcessingTapFinalizeCallback? ``` |
| To | ``` var finalize: MediaToolbox.MTAudioProcessingTapFinalizeCallback? ``` |

Modified MTAudioProcessingTapCallbacks.init

|  | Declaration |
| --- | --- |
| From | ``` var `init`: MTAudioProcessingTapInitCallback? ``` |
| To | ``` var `init`: MediaToolbox.MTAudioProcessingTapInitCallback? ``` |

Modified MTAudioProcessingTapCallbacks.prepare

|  | Declaration |
| --- | --- |
| From | ``` var prepare: MTAudioProcessingTapPrepareCallback? ``` |
| To | ``` var prepare: MediaToolbox.MTAudioProcessingTapPrepareCallback? ``` |

Modified MTAudioProcessingTapCallbacks.process

|  | Declaration |
| --- | --- |
| From | ``` var process: MTAudioProcessingTapProcessCallback ``` |
| To | ``` var process: MediaToolbox.MTAudioProcessingTapProcessCallback ``` |

Modified MTAudioProcessingTapCallbacks.unprepare

|  | Declaration |
| --- | --- |
| From | ``` var unprepare: MTAudioProcessingTapUnprepareCallback? ``` |
| To | ``` var unprepare: MediaToolbox.MTAudioProcessingTapUnprepareCallback? ``` |

Modified MTAudioProcessingTapFinalizeCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapFinalizeCallback = (MTAudioProcessingTap) -> Void ``` |
| To | ``` typealias MTAudioProcessingTapFinalizeCallback = (MTAudioProcessingTap) -> Swift.Void ``` |

Modified MTAudioProcessingTapGetSourceAudio(_: MTAudioProcessingTap, _: CMItemCount, _: UnsafeMutablePointer<AudioBufferList>, _: UnsafeMutablePointer<MTAudioProcessingTapFlags>?, _: UnsafeMutablePointer<CMTimeRange>?, _: UnsafeMutablePointer<CMItemCount>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MTAudioProcessingTapGetSourceAudio(_ tap: MTAudioProcessingTap, _ numberFrames: CMItemCount, _ bufferListInOut: UnsafeMutablePointer<AudioBufferList>, _ flagsOut: UnsafeMutablePointer<MTAudioProcessingTapFlags>, _ timeRangeOut: UnsafeMutablePointer<CMTimeRange>, _ numberFramesOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |
| To | ``` func MTAudioProcessingTapGetSourceAudio(_ tap: MTAudioProcessingTap, _ numberFrames: CMItemCount, _ bufferListInOut: UnsafeMutablePointer<AudioBufferList>, _ flagsOut: UnsafeMutablePointer<MTAudioProcessingTapFlags>?, _ timeRangeOut: UnsafeMutablePointer<CMTimeRange>?, _ numberFramesOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus ``` |

Modified MTAudioProcessingTapGetStorage(_: MTAudioProcessingTap) -> UnsafeMutableRawPointer

|  | Declaration |
| --- | --- |
| From | ``` func MTAudioProcessingTapGetStorage(_ tap: MTAudioProcessingTap) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func MTAudioProcessingTapGetStorage(_ tap: MTAudioProcessingTap) -> UnsafeMutableRawPointer ``` |

Modified MTAudioProcessingTapInitCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapInitCallback = (MTAudioProcessingTap, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Void ``` |
| To | ``` typealias MTAudioProcessingTapInitCallback = (MTAudioProcessingTap, UnsafeMutableRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>) -> Swift.Void ``` |

Modified MTAudioProcessingTapPrepareCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapPrepareCallback = (MTAudioProcessingTap, CMItemCount, UnsafePointer<AudioStreamBasicDescription>) -> Void ``` |
| To | ``` typealias MTAudioProcessingTapPrepareCallback = (MTAudioProcessingTap, CMItemCount, UnsafePointer<AudioStreamBasicDescription>) -> Swift.Void ``` |

Modified MTAudioProcessingTapProcessCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapProcessCallback = (MTAudioProcessingTap, CMItemCount, MTAudioProcessingTapFlags, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<CMItemCount>, UnsafeMutablePointer<MTAudioProcessingTapFlags>) -> Void ``` |
| To | ``` typealias MTAudioProcessingTapProcessCallback = (MTAudioProcessingTap, CMItemCount, MTAudioProcessingTapFlags, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<CMItemCount>, UnsafeMutablePointer<MTAudioProcessingTapFlags>) -> Swift.Void ``` |

Modified MTAudioProcessingTapUnprepareCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapUnprepareCallback = (MTAudioProcessingTap) -> Void ``` |
| To | ``` typealias MTAudioProcessingTapUnprepareCallback = (MTAudioProcessingTap) -> Swift.Void ``` |

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
