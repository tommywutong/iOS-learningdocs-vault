---
title: Using the Command key when Resizing a Window
apple_id: DTS10002206
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-08-21'
source_url: https://developer.apple.com/library/archive/qa/tb/tb20.html
archived_at: '2026-07-18T02:38:56.342049Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB20Using the Command key when Resizing a Window |

|  |
| --- |
| Q I discovered that if I held down the command key and clicked in the grow box in a window of any of the applications that my company develops, I could make the window bigger than the width I pass into GrowWindow. The grow box works as expected when the command key is not used. I don't think that this happening because of a bug on our end. Some of our applications are written in Metrowerks PowerPlant and others in Think Pascal, so they don't share common code, but this unexpected condition exists in all of our applications. I've since noticed the same problem in any application that limits the width of a window.  I haven't found any documentation discussing the relationship between the command key and the grow box. I really want to limit the width of a window, and now there's a way around it. Why is this happening? A Back in the old days when the Macintosh screen was 9" (384 pixels x 542 pixels), a lot of developers did not follow Apple's guidelines for window sizes and hardcoded the sizeRect given to GrowWindow based upon this small size. When the Macintosh II was introduced in '87, Apple engineers felt it would be frustrating for users to not be able to use the whole area of the new 13" monitors. In response, Apple implemented the 'Command key grow' feature. This meant that if the command-key was pressed while resizing the window, users could get whatever size they really wanted, because a sizeRect that was hardcoded to the dimensions of the 9" screen would be ignored.  However, Apple's implementation of the 'Command key grow' feature was not without consequence to some applications whose code was not written in accordance with Apple specifications. Certain applications were not able to accommodate the unanticipated change to the size of their windows and were prone to crashing and other problems.  As it currently stands, the 'Command key grow' feature is still in the system, as it has been since 1987, and even to this day developers should pay heed to it. As you've discovered, 'Command key grow' doesn't depend on the development environment.  Developers have been dealing with unusual monitor sizes for many years now, and few ever hardcode the sizeRect anymore. In light of this, Apple felt that there was not a need to document 'Command key grow' in the new _Inside Macintosh_ series, however it is documented on page 209 of _Inside Macintosh V_ (the old series). [Aug 21 1996] |

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
