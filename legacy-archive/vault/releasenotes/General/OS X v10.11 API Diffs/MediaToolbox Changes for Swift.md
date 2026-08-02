---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/MediaToolbox.html
archived_at: '2026-07-18T02:53:39.192894Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# MediaToolbox Changes for Swift

### MediaToolbox

Removed MTAudioProcessingTapCallbacks.init()Removed MTAudioProcessingTapCallbacks.init(version: Int32, clientInfo: UnsafeMutablePointer<Void>, init: MTAudioProcessingTapInitCallback, finalize: MTAudioProcessingTapFinalizeCallback, prepare: MTAudioProcessingTapPrepareCallback, unprepare: MTAudioProcessingTapUnprepareCallback, process: MTAudioProcessingTapProcessCallback)Added MTCopyLocalizedNameForMediaSubType(_: CMMediaType, _: FourCharCode) -> Unmanaged<CFString>?Added MTCopyLocalizedNameForMediaType(_: CMMediaType) -> Unmanaged<CFString>?Modified MTAudioProcessingTapCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTAudioProcessingTapCallbacks {     var version: Int32     var clientInfo: UnsafeMutablePointer<Void>     var `init`: MTAudioProcessingTapInitCallback     var finalize: MTAudioProcessingTapFinalizeCallback     var prepare: MTAudioProcessingTapPrepareCallback     var unprepare: MTAudioProcessingTapUnprepareCallback     var process: MTAudioProcessingTapProcessCallback     init()     init(version version: Int32, clientInfo clientInfo: UnsafeMutablePointer<Void>, `init` `init`: MTAudioProcessingTapInitCallback, finalize finalize: MTAudioProcessingTapFinalizeCallback, prepare prepare: MTAudioProcessingTapPrepareCallback, unprepare unprepare: MTAudioProcessingTapUnprepareCallback, process process: MTAudioProcessingTapProcessCallback) } ``` |
| To | ``` struct MTAudioProcessingTapCallbacks {     var version: Int32     var clientInfo: UnsafeMutablePointer<Void>     var `init`: MTAudioProcessingTapInitCallback?     var finalize: MTAudioProcessingTapFinalizeCallback?     var prepare: MTAudioProcessingTapPrepareCallback?     var unprepare: MTAudioProcessingTapUnprepareCallback?     var process: MTAudioProcessingTapProcessCallback } ``` |

Modified MTAudioProcessingTapCallbacks.finalize

|  | Declaration |
| --- | --- |
| From | ``` var finalize: MTAudioProcessingTapFinalizeCallback ``` |
| To | ``` var finalize: MTAudioProcessingTapFinalizeCallback? ``` |

Modified MTAudioProcessingTapCallbacks.init

|  | Declaration |
| --- | --- |
| From | ``` var `init`: MTAudioProcessingTapInitCallback ``` |
| To | ``` var `init`: MTAudioProcessingTapInitCallback? ``` |

Modified MTAudioProcessingTapCallbacks.prepare

|  | Declaration |
| --- | --- |
| From | ``` var prepare: MTAudioProcessingTapPrepareCallback ``` |
| To | ``` var prepare: MTAudioProcessingTapPrepareCallback? ``` |

Modified MTAudioProcessingTapCallbacks.unprepare

|  | Declaration |
| --- | --- |
| From | ``` var unprepare: MTAudioProcessingTapUnprepareCallback ``` |
| To | ``` var unprepare: MTAudioProcessingTapUnprepareCallback? ``` |

Modified kMTAudioProcessingTapCallbacksVersion_0

|  | Declaration |
| --- | --- |
| From | ``` var kMTAudioProcessingTapCallbacksVersion_0: Int { get } ``` |
| To | ``` var kMTAudioProcessingTapCallbacksVersion_0: Int32 { get } ``` |

Modified kMTAudioProcessingTapCreationFlag_PostEffects

|  | Declaration |
| --- | --- |
| From | ``` var kMTAudioProcessingTapCreationFlag_PostEffects: Int { get } ``` |
| To | ``` var kMTAudioProcessingTapCreationFlag_PostEffects: MTAudioProcessingTapCreationFlags { get } ``` |

Modified kMTAudioProcessingTapCreationFlag_PreEffects

|  | Declaration |
| --- | --- |
| From | ``` var kMTAudioProcessingTapCreationFlag_PreEffects: Int { get } ``` |
| To | ``` var kMTAudioProcessingTapCreationFlag_PreEffects: MTAudioProcessingTapCreationFlags { get } ``` |

Modified kMTAudioProcessingTapFlag_EndOfStream

|  | Declaration |
| --- | --- |
| From | ``` var kMTAudioProcessingTapFlag_EndOfStream: Int { get } ``` |
| To | ``` var kMTAudioProcessingTapFlag_EndOfStream: MTAudioProcessingTapFlags { get } ``` |

Modified kMTAudioProcessingTapFlag_StartOfStream

|  | Declaration |
| --- | --- |
| From | ``` var kMTAudioProcessingTapFlag_StartOfStream: Int { get } ``` |
| To | ``` var kMTAudioProcessingTapFlag_StartOfStream: MTAudioProcessingTapFlags { get } ``` |

Modified MTAudioProcessingTapCreate(_: CFAllocator?, _: UnsafePointer<MTAudioProcessingTapCallbacks>, _: MTAudioProcessingTapCreationFlags, _: UnsafeMutablePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MTAudioProcessingTapCreate(_ allocator: CFAllocator!, _ callbacks: UnsafePointer<MTAudioProcessingTapCallbacks>, _ flags: MTAudioProcessingTapCreationFlags, _ tapOut: UnsafeMutablePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus ``` |
| To | ``` func MTAudioProcessingTapCreate(_ allocator: CFAllocator?, _ callbacks: UnsafePointer<MTAudioProcessingTapCallbacks>, _ flags: MTAudioProcessingTapCreationFlags, _ tapOut: UnsafeMutablePointer<Unmanaged<MTAudioProcessingTap>?>) -> OSStatus ``` |

Modified MTAudioProcessingTapFinalizeCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapFinalizeCallback = CFunctionPointer<((MTAudioProcessingTap!) -> Void)> ``` |
| To | ``` typealias MTAudioProcessingTapFinalizeCallback = (MTAudioProcessingTap) -> Void ``` |

Modified MTAudioProcessingTapGetSourceAudio(_: MTAudioProcessingTap, _: CMItemCount, _: UnsafeMutablePointer<AudioBufferList>, _: UnsafeMutablePointer<MTAudioProcessingTapFlags>, _: UnsafeMutablePointer<CMTimeRange>, _: UnsafeMutablePointer<CMItemCount>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MTAudioProcessingTapGetSourceAudio(_ tap: MTAudioProcessingTap!, _ numberFrames: CMItemCount, _ bufferListInOut: UnsafeMutablePointer<AudioBufferList>, _ flagsOut: UnsafeMutablePointer<MTAudioProcessingTapFlags>, _ timeRangeOut: UnsafeMutablePointer<CMTimeRange>, _ numberFramesOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |
| To | ``` func MTAudioProcessingTapGetSourceAudio(_ tap: MTAudioProcessingTap, _ numberFrames: CMItemCount, _ bufferListInOut: UnsafeMutablePointer<AudioBufferList>, _ flagsOut: UnsafeMutablePointer<MTAudioProcessingTapFlags>, _ timeRangeOut: UnsafeMutablePointer<CMTimeRange>, _ numberFramesOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |

Modified MTAudioProcessingTapGetStorage(_: MTAudioProcessingTap) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func MTAudioProcessingTapGetStorage(_ tap: MTAudioProcessingTap!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func MTAudioProcessingTapGetStorage(_ tap: MTAudioProcessingTap) -> UnsafeMutablePointer<Void> ``` |

Modified MTAudioProcessingTapInitCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapInitCallback = CFunctionPointer<((MTAudioProcessingTap!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Void)> ``` |
| To | ``` typealias MTAudioProcessingTapInitCallback = (MTAudioProcessingTap, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Void ``` |

Modified MTAudioProcessingTapPrepareCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapPrepareCallback = CFunctionPointer<((MTAudioProcessingTap!, CMItemCount, UnsafePointer<AudioStreamBasicDescription>) -> Void)> ``` |
| To | ``` typealias MTAudioProcessingTapPrepareCallback = (MTAudioProcessingTap, CMItemCount, UnsafePointer<AudioStreamBasicDescription>) -> Void ``` |

Modified MTAudioProcessingTapProcessCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapProcessCallback = CFunctionPointer<((MTAudioProcessingTap!, CMItemCount, MTAudioProcessingTapFlags, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<CMItemCount>, UnsafeMutablePointer<MTAudioProcessingTapFlags>) -> Void)> ``` |
| To | ``` typealias MTAudioProcessingTapProcessCallback = (MTAudioProcessingTap, CMItemCount, MTAudioProcessingTapFlags, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<CMItemCount>, UnsafeMutablePointer<MTAudioProcessingTapFlags>) -> Void ``` |

Modified MTAudioProcessingTapUnprepareCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MTAudioProcessingTapUnprepareCallback = CFunctionPointer<((MTAudioProcessingTap!) -> Void)> ``` |
| To | ``` typealias MTAudioProcessingTapUnprepareCallback = (MTAudioProcessingTap) -> Void ``` |

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
