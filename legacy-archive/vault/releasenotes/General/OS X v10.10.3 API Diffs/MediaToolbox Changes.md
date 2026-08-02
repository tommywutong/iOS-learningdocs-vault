---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/MediaToolbox.html
archived_at: '2026-07-18T02:52:33.898841Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# MediaToolbox Changes

## MediaToolbox

Added MTAudioProcessingTapCallbacks.init()Added MTAudioProcessingTapCallbacks.init(version: Int32, clientInfo: UnsafeMutablePointer<Void>, init: MTAudioProcessingTapInitCallback, finalize: MTAudioProcessingTapFinalizeCallback, prepare: MTAudioProcessingTapPrepareCallback, unprepare: MTAudioProcessingTapUnprepareCallback, process: MTAudioProcessingTapProcessCallback)Modified MTAudioProcessingTapCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTAudioProcessingTapCallbacks {     var version: Int32     var clientInfo: UnsafePointer<()>     var `init`: MTAudioProcessingTapInitCallback     var finalize: MTAudioProcessingTapFinalizeCallback     var prepare: MTAudioProcessingTapPrepareCallback     var unprepare: MTAudioProcessingTapUnprepareCallback     var process: MTAudioProcessingTapProcessCallback } ``` |
| To | ``` struct MTAudioProcessingTapCallbacks {     var version: Int32     var clientInfo: UnsafeMutablePointer<Void>     var `init`: MTAudioProcessingTapInitCallback     var finalize: MTAudioProcessingTapFinalizeCallback     var prepare: MTAudioProcessingTapPrepareCallback     var unprepare: MTAudioProcessingTapUnprepareCallback     var process: MTAudioProcessingTapProcessCallback     init()     init(version version: Int32, clientInfo clientInfo: UnsafeMutablePointer<Void>, `init` `init`: MTAudioProcessingTapInitCallback, finalize finalize: MTAudioProcessingTapFinalizeCallback, prepare prepare: MTAudioProcessingTapPrepareCallback, unprepare unprepare: MTAudioProcessingTapUnprepareCallback, process process: MTAudioProcessingTapProcessCallback) } ``` |

Modified MTAudioProcessingTapCallbacks.clientInfo

|  | Declaration |
| --- | --- |
| From | ``` var clientInfo: UnsafePointer<()> ``` |
| To | ``` var clientInfo: UnsafeMutablePointer<Void> ``` |

Modified MTAudioProcessingTapCreate(CFAllocator!, UnsafePointer<MTAudioProcessingTapCallbacks>, MTAudioProcessingTapCreationFlags, UnsafeMutablePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MTAudioProcessingTapCreate(_ allocator: CFAllocator!, _ callbacks: ConstUnsafePointer<MTAudioProcessingTapCallbacks>, _ flags: MTAudioProcessingTapCreationFlags, _ tapOut: UnsafePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MTAudioProcessingTapCreate(_ allocator: CFAllocator!, _ callbacks: UnsafePointer<MTAudioProcessingTapCallbacks>, _ flags: MTAudioProcessingTapCreationFlags, _ tapOut: UnsafeMutablePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus ``` | OS X 10.9 |

Modified MTAudioProcessingTapGetSourceAudio(MTAudioProcessingTap!, CMItemCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<MTAudioProcessingTapFlags>, UnsafeMutablePointer<CMTimeRange>, UnsafeMutablePointer<CMItemCount>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MTAudioProcessingTapGetSourceAudio(_ tap: MTAudioProcessingTap!, _ numberFrames: CMItemCount, _ bufferListInOut: UnsafePointer<AudioBufferList>, _ flagsOut: UnsafePointer<MTAudioProcessingTapFlags>, _ timeRangeOut: UnsafePointer<CMTimeRange>, _ numberFramesOut: UnsafePointer<CMItemCount>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MTAudioProcessingTapGetSourceAudio(_ tap: MTAudioProcessingTap!, _ numberFrames: CMItemCount, _ bufferListInOut: UnsafeMutablePointer<AudioBufferList>, _ flagsOut: UnsafeMutablePointer<MTAudioProcessingTapFlags>, _ timeRangeOut: UnsafeMutablePointer<CMTimeRange>, _ numberFramesOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` | OS X 10.9 |

Modified MTAudioProcessingTapGetStorage(MTAudioProcessingTap!) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MTAudioProcessingTapGetStorage(_ tap: MTAudioProcessingTap!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func MTAudioProcessingTapGetStorage(_ tap: MTAudioProcessingTap!) -> UnsafeMutablePointer<Void> ``` | OS X 10.9 |

Modified MTAudioProcessingTapGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MTAudioProcessingTapInitCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapInitCallback = CFunctionPointer<((MTAudioProcessingTap!, UnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> Void)> ``` |
| To | ``` typealias MTAudioProcessingTapInitCallback = CFunctionPointer<((MTAudioProcessingTap!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Void)> ``` |

Modified MTAudioProcessingTapPrepareCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapPrepareCallback = CFunctionPointer<((MTAudioProcessingTap!, CMItemCount, ConstUnsafePointer<AudioStreamBasicDescription>) -> Void)> ``` |
| To | ``` typealias MTAudioProcessingTapPrepareCallback = CFunctionPointer<((MTAudioProcessingTap!, CMItemCount, UnsafePointer<AudioStreamBasicDescription>) -> Void)> ``` |

Modified MTAudioProcessingTapProcessCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapProcessCallback = CFunctionPointer<((MTAudioProcessingTap!, CMItemCount, MTAudioProcessingTapFlags, UnsafePointer<AudioBufferList>, UnsafePointer<CMItemCount>, UnsafePointer<MTAudioProcessingTapFlags>) -> Void)> ``` |
| To | ``` typealias MTAudioProcessingTapProcessCallback = CFunctionPointer<((MTAudioProcessingTap!, CMItemCount, MTAudioProcessingTapFlags, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<CMItemCount>, UnsafeMutablePointer<MTAudioProcessingTapFlags>) -> Void)> ``` |

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
