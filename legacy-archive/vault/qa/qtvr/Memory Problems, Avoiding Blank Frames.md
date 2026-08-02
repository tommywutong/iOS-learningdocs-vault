---
title: Memory Problems, Avoiding Blank Frames
apple_id: DTS10002049
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qtvr/qtvr05.html
archived_at: '2026-07-18T02:38:50.530765Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Virtual Reality](https://developer.apple.com/referencelibrary/QuickTime/idxVirtualReality-date.html)

|  |
| --- |
| Technical Q&A QTVR05Memory Problems, Avoiding Blank Frames |

|  |
| --- |
| Q When QuickTime VR doesn't have enough memory, it returns blank frames, but it doesn't tell us it's failing. Isn't QuickTime VR supposed to return an error message when there's insufficient RAM available for a QuickTime VR scene to be displayed? The only way we can avoid the blank frames is to scale the system (System 7.5 on a PowerMac 7100-66 with 16MB) down to 5.5MB of system memory, 6MB for Director, and the remainder for QuickTime VR A The most important factor regarding run-time memory requirements is the size of the source image. If you're not using dual-resolution files, and your source images are 768 x [something], you'll need approximately 4MB of RAM at run-time. Dropping to 384 x [something] images reduces the memory requirements to approximately 1MB at run-time.   [Jun 01 1995] |

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
