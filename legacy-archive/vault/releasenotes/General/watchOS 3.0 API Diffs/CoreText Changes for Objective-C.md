---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Objective-C/CoreText.html
archived_at: '2026-07-18T02:58:13.540377Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# CoreText Changes for Objective-C

### CoreText

#### CoreText.h

Added [#def kCTVersionNumber10_12](https://developer.apple.com/documentation/coretext/kctversionnumber10_12)

#### CTDefines.h

Added #def CT_EXPORT

#### CTFontManager.h

Added [CTFontManagerCopyAvailableFontFamilyNames()](https://developer.apple.com/documentation/coretext/1499494-ctfontmanagercopyavailablefontfa)Added [CTFontManagerCopyAvailablePostScriptNames()](https://developer.apple.com/documentation/coretext/1499516-ctfontmanagercopyavailablepostsc)

#### CTParagraphStyle.h

Modified [kCTParagraphStyleSpecifierLineSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierlinespacing)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | watchOS 2.2 | -- |
| To | watchOS 2.0 | watchOS 2.0 |

#### CTRubyAnnotation.h

Added [CTRubyAnnotationCreateWithAttributes()](https://developer.apple.com/documentation/coretext/1642000-ctrubyannotationcreatewithattrib)Added [kCTRubyAnnotationScaleToFitAttributeName](https://developer.apple.com/documentation/coretext/kctrubyannotationscaletofitattributename)Added [kCTRubyAnnotationSizeFactorAttributeName](https://developer.apple.com/documentation/coretext/kctrubyannotationsizefactorattributename)

#### CTStringAttributes.h

Added [kCTBackgroundColorAttributeName](https://developer.apple.com/documentation/coretext/kctbackgroundcolorattributename)Added [kCTHorizontalInVerticalFormsAttributeName](https://developer.apple.com/documentation/coretext/kcthorizontalinverticalformsattributename)

#### SFNTLayoutTypes.h

Added [kKERXValuesAreLong](https://developer.apple.com/documentation/coretext/1643710-anonymous/kkerxvaluesarelong)Added kSFNTLookupVectorAdded [SFNTLookupVectorHeader](https://developer.apple.com/documentation/coretext/sfntlookupvectorheader)

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
