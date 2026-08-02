---
title: QuickTime Music Architecture Header Update
apple_id: DTS10001943
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-08-21'
source_url: https://developer.apple.com/library/archive/qa/qtma/qtma06.html
archived_at: '2026-07-18T02:38:46.492003Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMusicAudio-date.html) >

|  |
| --- |
| Technical Q&A QTMA06QuickTime Music Architecture Header Update |

|  |
| --- |
| Q I noticed the following QTMA items are either missing or changed:  - TuneResume - TuneFlush - TuneGetState - _StuffXNoteEvent   Can you provide me with more information on their current status?  I would also like to know why _EventLength(x) is now qtma_EventLengthForward(xP,ulen) and qtma_EventLengthBackward(xP,ulen). A The calls, TuneResume, TuneFlush, and TuneGetState were poorly defined, and in fact were unimplemented in QuickTime 2.0/2.1. They have been removed from the headers. In the last few hours before we called QuickTime 2.5 final, _StuffXNoteEvent was repaired in the header file that was to generate that macro. Unfortunately, it didn't make it into the final release header. However, you can copy the macro from the older header file if needed. It is (pardon the line wrap):   ``` #define qtma_StuffXNoteEvent(w1, w2, part, pitch, volume, duration) w1 =     (kXNoteEventType << kXEventTypeFieldPos)|((long)(part) << kXEventPartFieldPos)|((long)(pitch) << kXNoteEventPitchFieldPos), w2 =    (kXEventLengthBits << kEventLengthFieldPos)|((long)(duration) <<  kXNoteEventDurationFieldPos)|((long)(volume) <<kXNoteEventVolumeFieldPos) ```   Regarding your question about _EventLength(x) and the two new macros, _EventLength(x) had to be changed because of some new event types. We needed separate macros to determine length from the first longword of a music event and from the last. Typically, you'll be using qtma_EventLengthForward. [Aug 21 1996] |

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
