---
title: Workaround for Converting Lower to Uppercase Characters while Keeping Diacritical
  Marks
apple_id: DTS10002256
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tx/tx04.html
archived_at: '2026-07-18T02:38:59.128662Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Text & Fonts](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTextFonts-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Text & Fonts > Text Manipulation](https://developer.apple.com/referencelibrary/TextFonts/idxTextManipulation-date.html)

|  |
| --- |
| Technical Q&A TX04Workaround for Converting Lower to Uppercase Characters while Keeping Diacritical Marks |

|  |
| --- |
| Q Calling UpperString with a single-character string containing a grave-accent (ASCII $60) returns a lower-case 'a' (ASCII $61). Is this supposed to happen?   A This is a bug that was fixed sometime ago, but the fix broke some file-system code that depends on the incorrect translation. There is a workaround: To convert lowercase characters to uppercase (keeping diacritical marks), use UppercaseText(). To strip diacritical marks while converting from lowercase to uppercase characters, use UppercaseStripDiacritics(). Both of these routines are described in _Inside Macintosh:Text_ on pages 5-67 through 5-70. Both of these calls use tables in the string-manipulation ('itl2') resource to perform their character-mapping operations, which allows you to customize their operation for different countries.  For example, to convert the Pascal string 'myTestStr' to all uppercase, use UppercaseText() in the following way:   ```         UppercaseText(myTestStr, myTestStr[0],  smSystemScript); ```  [May 01 1995] |

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
