---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/AudioToolbox.html
archived_at: '2026-07-18T02:53:50.278178Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# AudioToolbox Changes for Swift

### AudioToolbox

Added [AudioUnitEvent.init(mEventType: AudioUnitEventType, mArgument: AudioUnitEvent.__Unnamed_union_mArgument)](https://developer.apple.com/documentation/audiotoolbox/audiounitevent/1503126-init)Added [AudioUnitEvent.mArgument](https://developer.apple.com/documentation/audiotoolbox/audiounitevent/1503012-margument)Added [AUNodeInteraction.init(nodeInteractionType: UInt32, nodeInteraction: AUNodeInteraction.__Unnamed_union_nodeInteraction)](https://developer.apple.com/documentation/audiotoolbox/aunodeinteraction/1502754-init)Added [AUNodeInteraction.nodeInteraction](https://developer.apple.com/documentation/audiotoolbox/aunodeinteraction/1503339-nodeinteraction)Added [CAClockTime.init(format: CAClockTimeFormat, reserved: UInt32, time: CAClockTime.__Unnamed_union_time)](https://developer.apple.com/documentation/audiotoolbox/caclocktime/1501944-init)Added [CAClockTime.time](https://developer.apple.com/documentation/audiotoolbox/caclocktime/1501631-time)Modified [AudioUnitEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitevent)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitEvent {     var mEventType: AudioUnitEventType     init() } ``` |
| To | ``` struct AudioUnitEvent {     struct __Unnamed_union_mArgument {         var mParameter: AudioUnitParameter         var mProperty: AudioUnitProperty         init(mParameter mParameter: AudioUnitParameter)         init(mProperty mProperty: AudioUnitProperty)         init()     }     var mEventType: AudioUnitEventType     var mArgument: AudioUnitEvent.__Unnamed_union_mArgument     init()     init(mEventType mEventType: AudioUnitEventType, mArgument mArgument: AudioUnitEvent.__Unnamed_union_mArgument) } ``` |

Modified [AUNodeInteraction [struct]](https://developer.apple.com/documentation/audiotoolbox/aunodeinteraction)

|  | Declaration |
| --- | --- |
| From | ``` struct AUNodeInteraction {     var nodeInteractionType: UInt32     init() } ``` |
| To | ``` struct AUNodeInteraction {     struct __Unnamed_union_nodeInteraction {         var connection: AUNodeConnection         var inputCallback: AUNodeRenderCallback         init(connection connection: AUNodeConnection)         init(inputCallback inputCallback: AUNodeRenderCallback)         init()     }     var nodeInteractionType: UInt32     var nodeInteraction: AUNodeInteraction.__Unnamed_union_nodeInteraction     init()     init(nodeInteractionType nodeInteractionType: UInt32, nodeInteraction nodeInteraction: AUNodeInteraction.__Unnamed_union_nodeInteraction) } ``` |

Modified [CAClockTime [struct]](https://developer.apple.com/documentation/audiotoolbox/caclocktime)

|  | Declaration |
| --- | --- |
| From | ``` struct CAClockTime {     var format: CAClockTimeFormat     var reserved: UInt32     init() } ``` |
| To | ``` struct CAClockTime {     struct __Unnamed_union_time {         var hostTime: UInt64         var samples: CAClockSamples         var beats: CAClockBeats         var seconds: CAClockSeconds         var smpte: SMPTETime         init(hostTime hostTime: UInt64)         init(samples samples: CAClockSamples)         init(beats beats: CAClockBeats)         init(seconds seconds: CAClockSeconds)         init(smpte smpte: SMPTETime)         init()     }     var format: CAClockTimeFormat     var reserved: UInt32     var time: CAClockTime.__Unnamed_union_time     init()     init(format format: CAClockTimeFormat, reserved reserved: UInt32, time time: CAClockTime.__Unnamed_union_time) } ``` |

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
