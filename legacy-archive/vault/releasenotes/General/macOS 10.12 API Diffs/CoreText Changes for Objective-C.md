---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/CoreText.html
archived_at: '2026-07-18T02:50:38.405136Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CoreText Changes for Objective-C

### CoreText

#### CoreText.h

Added [#def kCTVersionNumber10_12](https://developer.apple.com/documentation/coretext/kctversionnumber10_12)

#### CTDefines.h

Added #def CT_EXPORT

#### CTFontDescriptor.h

Added [kCTFontDownloadedAttribute](https://developer.apple.com/documentation/coretext/kctfontdownloadedattribute)

#### CTParagraphStyle.h

Modified [kCTParagraphStyleSpecifierLineSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierlinespacing)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

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
