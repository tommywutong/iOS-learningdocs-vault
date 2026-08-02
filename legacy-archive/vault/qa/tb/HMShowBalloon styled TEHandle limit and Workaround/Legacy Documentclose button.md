---
title: HMShowBalloon styled TEHandle limit and Workaround
apple_id: DTS10002193
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb07.html
archived_at: '2026-07-18T02:38:55.313423Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB07HMShowBalloon styled TEHandle limit and Workaround |

|  |
| --- |
| Q Sometimes balloons won't show up when I call HMShowBalloon; I get a paramErr (-50) instead. The hmHelpType is khmmTEHandle. The HMShowBalloon function calls TextWidth on the hText of my TEHandle (the result of which is 1511 (338 chars)), then multiplies that by the lineHeight (12), yielding 18132. It then compares this to 17000, doesn't like the result, puts -50 into a register and backs out of everything it has done previously. What is the Help Manager doing?   A The Help Manager checks against 17000 to ensure that the help balloon window is always smaller than the Macintosh system screen. However, the value used (17000) should be a much larger value. As it is right now in System 7, you're limited to about the same number of characters with a styled TEHandle as you are with a Pascal string: 255 characters. To avoid this limitation, use clear concise phrases to make your help system as short as possible. If you've already done that and your help message still isn't short enough, you can use khmmPict or khmmPictHandle and use a picture for your help message. Using a picture has a disadvantage in the fact that pictures use a little more memory for the same help message and you'll have to add carriage returns for the line breaks yourself where you need them. You can use MacDraw or a similar program to create the pictures. [May 01 1995] |

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
