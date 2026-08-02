---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/CoreText.html
archived_at: '2026-07-18T02:54:55.122849Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


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

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 6.0 |

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
