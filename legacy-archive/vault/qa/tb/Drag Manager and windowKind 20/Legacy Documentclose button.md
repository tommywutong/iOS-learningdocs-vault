---
title: Drag Manager and windowKind 20
apple_id: DTS10002214
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-11-27'
source_url: https://developer.apple.com/library/archive/qa/tb/tb28.html
archived_at: '2026-07-18T02:38:56.614953Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB28Drag Manager and windowKind 20 |

|  |
| --- |
| Q When I drag from my application into a Finder window, the system crashes. I noticed Finder uses a windowKind value of 20 for its windows, and so does my app. When my app avoids windowKind 20, everything's hunky-dory. What gives?   A Through the Drag Manager, Finder has gotten access to the windows in your app's window list (specifically, by using undocumented calls to obtain the source window of a drag). If your window's windowKind field is 20, Finder assumes the window is one of its own (as opposed to a driver window, whose windowKind would be negative, or a dialog window, whose windowKind would be 2, etc.). Finder grabs the value in the window's refCon field and type-casts it to a pointer to a C++ object in Finder's heap. I think you can see where this is going: when Finder attempts to dereference the pointer, various crashing behaviors result. The upshot of this Finder bug is that your application should not use windowKind values of 20. [Nov 27 1996] |

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
