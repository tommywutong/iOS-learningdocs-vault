---
title: Setting the Background Color of a Control
apple_id: DTS10002248
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-03'
source_url: https://developer.apple.com/library/archive/qa/tb/tb62.html
archived_at: '2026-07-18T02:38:58.046991Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB62Setting the Background Color of a Control |

|  |
| --- |
| ---   Q: I'm having trouble setting the background color of a control. It looks to me like the control color table contains an entry for background color, but the standard controls seem to be ignoring this entry. What should I do?  A: Unfortunately, since Mac OS 8 and the Appearance SDK were introduced, there are many answers to this question. Without the Appearance extension (whose functionality is built into Mac OS 8.5 and later), controls get their background color from the content entry of the window color table. Otherwise, controls get their background color in a considerably more complicated way, which is best expressed in sample code. We've updated the "ControlBackground" sample accordingly, and it should be appearing on the appropriate Developer CDs and FTP sites soon. [May 03 1999] |

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
