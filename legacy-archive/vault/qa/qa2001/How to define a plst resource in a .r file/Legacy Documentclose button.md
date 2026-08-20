---
title: How to define a plst resource in a .r file
apple_id: DTS10001586
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-05-09'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1034.html
archived_at: '2026-07-18T02:38:03.831662Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Runtime Architecture](https://developer.apple.com/referencelibrary/Carbon/idxRuntimeArchitecture-date.html)

|  |
| --- |
| Technical Q&A QA1034How to define a plst resource in a .r file |

|  |
| --- |
| ---   Q: What's the syntax for defining a plst resource in a .r file? Is there a plist resource template?  A: There is no plst resource template but you can use the PropertyList Editor under Mac OS X or any text editor to create your XML .plist file. You can then add this file to your project by reading it in with the following line in any .r file:  read 'plst' (0) "MyFile.plist"  If the .r and .plist files are not in the same folder make sure that you use a full or relative path.  __Further Reference:__   [Technical Note TN2013, "The 'plst' Resource"](https://developer.apple.com/library/archive/technotes/tn/tn2013.html).   ---  [May 09 2001] |

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
