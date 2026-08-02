---
title: Maximum number of fonts
apple_id: DTS10002265
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-01-04'
source_url: https://developer.apple.com/library/archive/qa/tx/tx13.html
archived_at: '2026-07-18T02:38:59.337893Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Text & Fonts](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTextFonts-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Text & Fonts > Typography](https://developer.apple.com/referencelibrary/TextFonts/idxTypography-date.html)

|  |
| --- |
| Technical Q&A TX13Maximum number of fonts |

|  |
| --- |
| ---   Q: What is the maximum number of fonts that can be installed in the Fonts folder with Mac OS 9?  A: Mac OS 9 supports up to 1,024 font suitcase files in the Fonts folder. But until Mac OS 8.6, the limit was 128 font suitcase files. Note that this is the number of font suitcase files, not the actual number of font families displayed in the font menu. The increase in the number of supported font suitcase files is due to a change in the way FCBs are handled starting with Mac OS 9. For details, see [Technote 1184 "FCBs, Now and Forever](https://developer.apple.com/library/archive/technotes/tn/tn1184.html)"  As in the past, you can install multiple font families per font suitcase file. However, the realistic limit is approximately 1800 font families. This is an operational limit set by the Menu Manager (a menu's maximum height is limited to 16,384 or 215 pixels).  If the user only has 32 MB of physical RAM, the limit of 1,800 font families may not be reached. The Font Manager doesn't have hard limits on the number of font families, but it does have a limited amount of space for its bookkeeping. This space is shared among font files, font families, and outline font strikes. The amount of space allocated depends on the amount of physical RAM present. For every 32MB of RAM,the system will allocate 256K, up to a maximum of 1MB.  It's hard to translate these heap sizes into hard limits on the number of fonts the system can handle. That total is sensitive both to the structure of the fonts as well as the order in which the system sees them. But under normal circumstances the range is about 700-1,800 font families.  Another limitation is that each script (with the exception of U.S. Roman) can only support up to 512 font families. For example, the Japanese version of the Mac OS can support up to 512 Japanese font families and 1,288 (1,800 minus 512) U.S. Roman font families. (Of course, the limit of 1024 font suitcases still applies.) [Jan 04 2000] |

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
