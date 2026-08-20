---
title: Kanji and Special Text-Processing
apple_id: DTS10002253
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tx/tx01.html
archived_at: '2026-07-18T02:38:58.416487Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Text & Fonts](https://developer.apple.com/referencelibrary/Carbon/idxTextFonts-date.html)

|  |
| --- |
| Technical Q&A TX01Kanji and Special Text-Processing |

|  |
| --- |
| Q Our application supports Kanji, but it still has to perform some special text-processing operations on certain documents to search for control characters, remove control characters, and other similar operations. To accomplish this, we need additional information on international character-set encoding. It appears that $0D is a carriage return, and $09 is a tab, even in Kanji (the Kanji character set seems to encompass the entire Roman character set), if they occupy the first byte of a double-byte character. However, we are finding what appear to be control characters in the second bytes of double-byte characters. Can we safely assume that $0D, or any other common control-character code, is a carriage return wherever we find one in a Kanji document? If so, does this hold true for other non-Roman script systems? A All scripts have the same low ASCII values ($00-$7F), and all double-byte scripts use only high ASCII values ($80-FF) for high-byte (first byte) values and $40-$FF for low-byte (second byte) values. Therefore, control characters, numbers, and elementary punctuation characters are all unique. To see exactly what is permitted for the particular script you are working with, call the parseTable script-manager routine to obtain a table of high/low byte values. The difficulty of dealing with control characters in scripts will disappear when Unicode (which uses 16-bit characters and can have any combination of them) is in widespread use. Because of fundamental compatibility problems with our system software and any application that assumes that $0D is always a <CR>, Unicode will never be a 'script system'. Instead, it will probably be an alternate encoding platform, with all new rules. There is no reason to plan extensively for Unicode at the present time, but you should make as few assumptions as possible in your code. This will help to minimize the effort required to make your code compatible Unicode in the future.  To obtain a more in-depth understanding of international character-set encoding, software localization, and Unicode, locate a copy of _Guide to Macintosh Software Localization_ (an Addison-Wesley publication). While this is available as soft copy on one of the developer CDs, you may find that some of the content won't display properly unless you have all of the appropriate fonts installed, so it might be best to obtain a printed copy. [May 01 1995] |

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
