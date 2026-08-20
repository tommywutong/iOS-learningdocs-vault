---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/AudioUnit.html
archived_at: '2026-07-18T02:57:14.988468Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# AudioUnit Changes for Swift

### AudioUnit

Added [AudioUnitParameterEvent.eventValues](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/1439066-eventvalues)Added [AudioUnitParameterEvent.init(scope: AudioUnitScope, element: AudioUnitElement, parameter: AudioUnitParameterID, eventType: AUParameterEventType, eventValues: AudioUnitParameterEvent.__Unnamed_union_eventValues)](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/1438724-init)Modified [AudioUnitParameterEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterEvent {     var scope: AudioUnitScope     var element: AudioUnitElement     var parameter: AudioUnitParameterID     var eventType: AUParameterEventType     init() } ``` |
| To | ``` struct AudioUnitParameterEvent {     struct __Unnamed_union_eventValues {         struct __Unnamed_struct_ramp {             var startBufferOffset: Int32             var durationInFrames: UInt32             var startValue: AudioUnitParameterValue             var endValue: AudioUnitParameterValue             init()             init(startBufferOffset startBufferOffset: Int32, durationInFrames durationInFrames: UInt32, startValue startValue: AudioUnitParameterValue, endValue endValue: AudioUnitParameterValue)         }         struct __Unnamed_struct_immediate {             var bufferOffset: UInt32             var value: AudioUnitParameterValue             init()             init(bufferOffset bufferOffset: UInt32, value value: AudioUnitParameterValue)         }         var ramp: AudioUnitParameterEvent.__Unnamed_union_eventValues.__Unnamed_struct_ramp         var immediate: AudioUnitParameterEvent.__Unnamed_union_eventValues.__Unnamed_struct_immediate         init(ramp ramp: AudioUnitParameterEvent.__Unnamed_union_eventValues.__Unnamed_struct_ramp)         init(immediate immediate: AudioUnitParameterEvent.__Unnamed_union_eventValues.__Unnamed_struct_immediate)         init()     }     var scope: AudioUnitScope     var element: AudioUnitElement     var parameter: AudioUnitParameterID     var eventType: AUParameterEventType     var eventValues: AudioUnitParameterEvent.__Unnamed_union_eventValues     init()     init(scope scope: AudioUnitScope, element element: AudioUnitElement, parameter parameter: AudioUnitParameterID, eventType eventType: AUParameterEventType, eventValues eventValues: AudioUnitParameterEvent.__Unnamed_union_eventValues) } ``` |

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
