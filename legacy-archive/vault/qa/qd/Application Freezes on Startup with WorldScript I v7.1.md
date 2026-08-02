---
title: Application Freezes on Startup with WorldScript I v7.1
apple_id: DTS10001772
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd13.html
archived_at: '2026-07-18T02:38:35.937758Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Text & Fonts](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTextFonts-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Text & Fonts](https://developer.apple.com/referencelibrary/TextFonts/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD13Application Freezes on Startup with WorldScript I v7.1 |

|  |
| --- |
| ---   Q: We're having a problem with LaserWriter 8.3 which causes our app to freeze on startup. When we first installed LaserWriter 8.3 everything worked properly. However, when we attempted to install WorldScript I v7.1 onto a Quadra 650 the problem occurred. What's going on here?  A: The latest 7.5.1 WorldScript I requires updated script systems, and you should not install it unless you get these all from the same system. The Developer CD is currently the only source for these files. LaserWriter 8.3 is not compatible with older WorldScript I, because it requires 7.5.1.  The best solution is to perform a clean install of 7.5, install the 7.5.1 upgrade, install LaserWriter 8.3, and then test it. After confirming that this configuration works, install WorldScript I 7.5.1, the compatible script resources, and the power adaptor (if you have a PPC). It is best to get them all from the Developer CD (there is a 7.5 Arabic system with WS 7.5.1 on the CD). |

#### [Jul 01 1995]

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

---
