---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/CoreMedia.html
archived_at: '2026-07-18T02:51:45.321698Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# CoreMedia Changes for Swift

### CoreMedia

Modified [CMBlockBufferCustomBlockSource [struct]](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource)

|  | Declaration |
| --- | --- |
| From | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?     var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?     var refCon: UnsafeMutableRawPointer?     init()     init(version version: UInt32, AllocateBlock AllocateBlock: (@escaping (UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?, FreeBlock FreeBlock: (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?, refCon refCon: UnsafeMutableRawPointer?) } ``` |
| To | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?     var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?     var refCon: UnsafeMutableRawPointer?     init()     init(version version: UInt32, AllocateBlock AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?, FreeBlock FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?, refCon refCon: UnsafeMutableRawPointer?) } ``` |

Modified [CMBlockBufferCustomBlockSource.init(version: UInt32, AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?, FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?, refCon: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/1489216-init)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: UInt32, AllocateBlock AllocateBlock: (@escaping (UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?, FreeBlock FreeBlock: (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?, refCon refCon: UnsafeMutableRawPointer?) ``` |
| To | ``` init(version version: UInt32, AllocateBlock AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?, FreeBlock FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Swift.Void)?, refCon refCon: UnsafeMutableRawPointer?) ``` |

Modified [CMTime [struct]](https://developer.apple.com/documentation/coremedia/cmtime)

|  | Declaration |
| --- | --- |
| From | ``` struct CMTime {     var value: CMTimeValue     var timescale: CMTimeScale     var flags: CMTimeFlags     var epoch: CMTimeEpoch     init()     init(value value: CMTimeValue, timescale timescale: CMTimeScale, flags flags: CMTimeFlags, epoch epoch: CMTimeEpoch)     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale)     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime {     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale) } extension CMTime {     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime : Equatable, Comparable { } ``` |
| To | ``` struct CMTime {     var value: CMTimeValue     var timescale: CMTimeScale     var flags: CMTimeFlags     var epoch: CMTimeEpoch     init()     init(value value: CMTimeValue, timescale timescale: CMTimeScale, flags flags: CMTimeFlags, epoch epoch: CMTimeEpoch)     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale)     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime { } extension CMTime {     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale) } extension CMTime {     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime : Equatable, Comparable { } ``` |

Modified [CMTimeMapping [struct]](https://developer.apple.com/documentation/coremedia/cmtimemapping)

|  | Declaration |
| --- | --- |
| From | ``` struct CMTimeMapping {     var source: CMTimeRange     var target: CMTimeRange     init()     init(source source: CMTimeRange, target target: CMTimeRange) } ``` |
| To | ``` struct CMTimeMapping {     var source: CMTimeRange     var target: CMTimeRange     init()     init(source source: CMTimeRange, target target: CMTimeRange) } extension CMTimeMapping { } ``` |

Modified [CMTimeRange [struct]](https://developer.apple.com/documentation/coremedia/cmtimerange)

|  | Declaration |
| --- | --- |
| From | ``` struct CMTimeRange {     var start: CMTime     var duration: CMTime     init()     init(start start: CMTime, duration duration: CMTime)     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     func union(_ otherRange: CMTimeRange) -> CMTimeRange     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     func containsTime(_ time: CMTime) -> Bool     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange {     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     func union(_ otherRange: CMTimeRange) -> CMTimeRange     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     func containsTime(_ time: CMTime) -> Bool     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange : Equatable { } ``` |
| To | ``` struct CMTimeRange {     var start: CMTime     var duration: CMTime     init()     init(start start: CMTime, duration duration: CMTime)     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     func union(_ otherRange: CMTimeRange) -> CMTimeRange     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     func containsTime(_ time: CMTime) -> Bool     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange { } extension CMTimeRange {     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     func union(_ otherRange: CMTimeRange) -> CMTimeRange     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     func containsTime(_ time: CMTime) -> Bool     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange : Equatable { } ``` |

Modified [CMBufferQueueSetValidationCallback(_: CMBufferQueue, _: CoreMedia.CMBufferValidationCallback, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489350-cmbufferqueuesetvalidationcallba)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueSetValidationCallback(_ queue: CMBufferQueue, _ validationCallback: CoreMedia.CMBufferValidationCallback, _ validationRefCon: UnsafeMutableRawPointer?) -> OSStatus ``` |
| To | ``` func CMBufferQueueSetValidationCallback(_ queue: CMBufferQueue, _ validationCallback: @escaping CoreMedia.CMBufferValidationCallback, _ validationRefCon: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [CMSampleBufferSetInvalidateCallback(_: CMSampleBuffer, _: CoreMedia.CMSampleBufferInvalidateCallback, _: UInt64) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489773-cmsamplebuffersetinvalidatecallb)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetInvalidateCallback(_ sbuf: CMSampleBuffer, _ invalidateCallback: CoreMedia.CMSampleBufferInvalidateCallback, _ invalidateRefCon: UInt64) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetInvalidateCallback(_ sbuf: CMSampleBuffer, _ invalidateCallback: @escaping CoreMedia.CMSampleBufferInvalidateCallback, _ invalidateRefCon: UInt64) -> OSStatus ``` |

Modified [CMSampleBufferSetInvalidateHandler(_: CMSampleBuffer, _: CoreMedia.CMSampleBufferInvalidateHandler) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489256-cmsamplebuffersetinvalidatehandl)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetInvalidateHandler(_ sbuf: CMSampleBuffer, _ invalidateHandler: CoreMedia.CMSampleBufferInvalidateHandler) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetInvalidateHandler(_ sbuf: CMSampleBuffer, _ invalidateHandler: @escaping CoreMedia.CMSampleBufferInvalidateHandler) -> OSStatus ``` |

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
