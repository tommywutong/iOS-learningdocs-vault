---
title: Specifying a Non-Panorama
apple_id: DTS10002051
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qtvr/qtvr07.html
archived_at: '2026-07-18T02:38:50.634916Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Virtual Reality](https://developer.apple.com/referencelibrary/QuickTime/idxVirtualReality-date.html)

|  |
| --- |
| Technical Q&A QTVR07Specifying a Non-Panorama |

|  |
| --- |
| Q We use the Stitch768nowrap script, which obviously doesn't use the "-wrap" switch. However, when we run p2mv and then msnm, the edges of the partial panorama are joined in our movie. The QuickTime VR Player spins the image as if it were a 360-degree panorama. There doesn't appear to be anything in the documentation that explains how to specify the nature of a non-panorama. For example, we need something that allows us to notify the software that one input PICT represents a 170-degree pan, while another one represents a 120-degree pan.   A The msnm command has a switch called -hPanRange. When you use this switch and follow it with a starting horizontal angle and an ending horizontal angle, a partial panorama is created. You can get a list of all of the switches for any tool by entering the tool's name followed by a "-" (dash). For example, if you type msnm-<enter>, you get a list of all of the things switches for msnm. [Jun 01 1995] |

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
