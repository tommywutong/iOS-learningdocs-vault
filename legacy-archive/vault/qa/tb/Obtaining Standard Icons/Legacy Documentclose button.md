---
title: Obtaining Standard Icons
apple_id: DTS10002221
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-12-23'
source_url: https://developer.apple.com/library/archive/qa/tb/tb35.html
archived_at: '2026-07-18T02:38:56.897330Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)
- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB35Obtaining Standard Icons |

|  |
| --- |
| Q Where do I get the standard icons for a folder, generic document, disk volume, etc.?   A The resource ID's of many of the desirable icon suites are documented starting on page 1-129 of _Inside Macintosh: More Macintosh Toolbox_ in the section called ["Standard Icons"](https://developer.apple.com/documentation/mac/MoreToolbox/MoreToolbox-104.html#HEADING104-0). It's a safe bet these resource ID's will remain usable into the indefinite future. However, some commonly requested icons are not available programmatically, or at least their resource ID's are not documented in _Inside Macintosh_. These icons include many of the icons Finder displays for `FindFolder` selectors new to Mac OS 8. Probably the most often requested icon is the icon Finder 8 displays for hard disk volumes controlled by an Apple driver. (It's not the same icon produced by the disk driver; at the time Finder 8 was built, disk drivers could provide only black-and-white icons.) At present, there is no good way to obtain these icons programmatically.  For now, the best way to obtain an icon whose ID is not documented in _Inside Macintosh_ is to find the icon you like (most of the interesting ones can be found in the "System", "Finder", or "Appearance Extension" files) and copy it into your application resource fork (being careful to renumber it to something above 127, of course).  One thing you'll want to avoid is searching the system files for icons and using their ID's in your program. In the future, icons with undocumented ID's may not have the ID's they have today, and in fact they may not even have the same resource type!  We do not expect that any of these icons (including the documented ones) will change according to theme. [Dec 23 1997] |

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
