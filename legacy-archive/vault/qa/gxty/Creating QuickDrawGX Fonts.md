---
title: Creating QuickDrawGX Fonts
apple_id: DTS10001260
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxty/gxty01.html
archived_at: '2026-07-18T02:29:34.475778Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Text & Fonts](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTextFonts-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Text & Fonts](https://developer.apple.com/referencelibrary/TextFonts/index.html)

|  |
| --- |
| Technical Q&A GXTY01Creating QuickDrawGX Fonts |

|  |
| --- |
| ---   Q:We make foreign-language fonts for Macintosh computers for 270 languages, and we'd like to also make some QuickDrawGX fonts. How do we create QuickDraw GX fonts?  A: There are a number of sources of information to help you create GX fonts. All of the information and tools are on the QuickDrawGX SDK (the Golden Master and the MacOS SDK).  You should also become familiar with the additions Apple has made to the TrueType specification for QuickDraw GX. In general, the changes for GX are added to the TrueType specification as additional tables that support the features found within the GX Line Layout engine. All of the documentation you need is on the previously mentioned CDs. Look at the following documents in the "Documents" folder:  Inside Macintosh -- QuickDraw GX Docs (folder): QuickDraw GX Font Formats (the complete specification of QD GX fonts)  [QuickDraw GX Font Feature Registry](http://fonts.apple.com/)  QuickDraw GX Font HI Guidelines  [Font Quality Specification](http://fonts.apple.com/)  [Type 1 GX Font Format](http://fonts.apple.com/)  On the Mac OS SDK, there is a folder titled QuickDraw GX that uses the same paths as those mentioned above. All of the QuickDrawGX Font tools used at Apple are also on the CDs in the following path: Goodies : Font Tools.  While all of these tools are useful, two are of particular interest:   1. Font Validator verifies the condition of all the tables in your QuickDraw GX font. If any table is damaged (or otherwise unusable), Font Validator supplies information to help you identify the problem. Always use this tool before shipping any of your QuickDraw GX fonts. 2. TrueEdit creates the major pieces of your QuickDraw GX font. While it does its job well, it isn't complete, and has limited international support. We're working to improve TrueEdit, but for some languages, it does not create all of the tables listed and required within the QuickDraw GX Font Formats specification. It does support the Roman, Japanese, Chinese, and Arabic languages.   The latest version of TrueEdit is available on the Internet at ftp.info.apple.com. As they become available, new versions of TrueEdit will also be included on new MacOS CDs as they are released. |

#### [May 01 1995]

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
