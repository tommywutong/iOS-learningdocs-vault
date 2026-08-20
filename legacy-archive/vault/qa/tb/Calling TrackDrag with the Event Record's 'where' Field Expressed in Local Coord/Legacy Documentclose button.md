---
title: Calling TrackDrag with the Event Record's 'where' Field Expressed in Local
  Coordinates
apple_id: DTS10002215
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-11-27'
source_url: https://developer.apple.com/library/archive/qa/tb/tb29.html
archived_at: '2026-07-18T02:38:56.648396Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB29Calling TrackDrag with the Event Record's 'where' Field Expressed in Local Coordinates |

|  |
| --- |
| Q When my application calls TrackDrag, it crashes in low memory at an illegal instruction. The MacsBug stack crawl doesn't produce any useful information. (I think the errant code did a JMP to the bad instruction, as opposed to a JSR.) I've stared and stared at all my app's calls to the Drag Manager and all the parameters appear to be valid. My drag tracking handler is never called, incidentally. If I take all calls to Drag Manager out of my application, it runs just fine. I've been investigating this crash for two months. Why is life so cruel?   A You've unearthed a really ugly problem. Early versions of Drag Manager did not enjoy the benefits of a drag-enabled Finder, so Drag Manager plays a little fast and loose with Finder's jump table. Yes, that means what it sounds like: Drag Manager calls Finder routines through its jump table. (It disgusted me at first, too.)  The even more interesting story concerns the method by which Drag Manager decides your application is Finder. When TrackDrag is called, Drag Manager determines whether the drag originates in any of the windows in the window list of the current process. If not, Drag Manager determines whether the drag originates in any Finder window. Since the desktop is a window for these purposes, there is a large area which qualifies.  Once Drag Manager has decided the drag originates in a Finder window, it assumes that Finder is the current process. (This is the fatal mistake.) Once this assumption is in place, the next thing for Drag Manager to do in order to coax Finder into exhibiting the correct drag behavior is call an entry in whatever jump table can be found by offsetting the current value of register A5. This is a valid assumption if Finder is the current process, which of course it is not. This is where things go terribly astray: Drag Manager calls a jump table entry in your application thinking your app is Finder, your app's routine doesn't do the same thing as the Finder routine, and any number of spectacular effects can result.  Now wait a minute, you're thinking, the drag originated in one of my application's windows; how is this stuff about Finder relevant? Consider the event record your app is passing to TrackDrag. An event record is supposed to contain a 'where' field expressed in global coordinates. However, the 'where' field your app is passing is expressed in local coordinates. How? Well, that depends on your application, but often this can result from application frameworks (like PowerPlant, MacApp, or THINK Class Library) modifying the event record before passing it to your code. There's no language-level way to specify the record has been modified, so the compiler doesn't warn you. (Honestly, this is Not Your Fault.)  Your code blithely calls TrackDrag with what it ought to be able to assume is a valid event record but is not. TrackDrag interprets the 'where' field, which is actually expressed in local coordinates, as global coordinates. This point is somewhere up and to the left of where your application expects, and quite often it's in the desktop, which as we said above is considered a Finder window for these purposes. Drag Manager reacts by going through its ritual for drags originating in Finder windows and eventually crashes after calling some odd routine in your application, as described above.  To solve this problem, simply call LocalToGlobal on the 'where' field of the event record before calling TrackDrag. [Nov 27 1996] |

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
