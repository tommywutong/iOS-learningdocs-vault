---
title: How PBDTGetAPPL Chooses Which Copy of an App to Launch
apple_id: DTS10002205
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/tb/tb19.html
archived_at: '2026-07-18T02:38:56.278227Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Human Interface Toolbox](https://developer.apple.com/library/archive/technicalqas/Carbon/idxHumanInterfaceToolbox-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB19How PBDTGetAPPL Chooses Which Copy of an App to Launch |

|  |
| --- |
| Q How does PBDTGetAPPL() choose the "best" copy of an application to launch? Sometimes the choice PBDTGetAPPL() returns information about a copy of the application that happens to be in the Trash. How can I guarantee that the copy of an application I attempt to launch is not in the Trash?   A PBDTGetAPPL is documented in _Inside Macintosh: More Macintosh Toolbox_. On page 9-5, it states, "In each call to PBDTGetAPPL, you specify a creator (which is the application's signature) and an index value. An index value of 0 retrieves the "first choice" application--that is, the one with the most recent creation date." This Inside Macintosh explanation is not really correct. When you specify and creator and pass an index value of 0, PBDTGetAPPL() actually returns information about the LAST copy of the application the Desktop Manager used to update the Desktop database, NOT the copy with the most recent creation date. In other words, PBDTGetAPPL() returns Last-In-First-Out information from the Desktop database.  To avoid launching a copy of the application that is currently in the Trash folder add a check for the application's parent ID. If the "first choice" is in the Trash, then make indexed calls (beginning with an index of 1) to PBDTGetAPPL to get information about all copies of the application and compare the ioAPPLParID and ioTagInfo (creation date) fields to find the copy of the application with the latest creation date that is not currently in the Trash. [May 14 1996] |

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
