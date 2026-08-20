---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/AudioToolbox.html
archived_at: '2026-07-18T02:58:05.045528Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# AudioToolbox Changes for Swift

### AudioToolbox

Added [AUNodeInteraction.init(nodeInteractionType: UInt32, nodeInteraction: AUNodeInteraction.__Unnamed_union_nodeInteraction)](https://developer.apple.com/documentation/audiotoolbox/aunodeinteraction/1502754-init)Added [AUNodeInteraction.nodeInteraction](https://developer.apple.com/documentation/audiotoolbox/aunodeinteraction/1503339-nodeinteraction)Modified [AUNodeInteraction [struct]](https://developer.apple.com/documentation/audiotoolbox/aunodeinteraction)

|  | Declaration |
| --- | --- |
| From | ``` struct AUNodeInteraction {     var nodeInteractionType: UInt32     init() } ``` |
| To | ``` struct AUNodeInteraction {     struct __Unnamed_union_nodeInteraction {         var connection: AUNodeConnection         var inputCallback: AUNodeRenderCallback         init(connection connection: AUNodeConnection)         init(inputCallback inputCallback: AUNodeRenderCallback)         init()     }     var nodeInteractionType: UInt32     var nodeInteraction: AUNodeInteraction.__Unnamed_union_nodeInteraction     init()     init(nodeInteractionType nodeInteractionType: UInt32, nodeInteraction nodeInteraction: AUNodeInteraction.__Unnamed_union_nodeInteraction) } ``` |

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
