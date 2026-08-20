---
title: Small System Font Size on a Korean System
apple_id: DTS10002257
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/tx/tx05.html
archived_at: '2026-07-18T02:38:59.181667Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TX05Small System Font Size on a Korean System |

|  |
| --- |
| Q We are localizing our software for Korea, and we have found that the Korean System 7.1 uses a different "Small System Font Size" than System 7.1.2. In System KH-7.1, the Small System Font is 12pt, but in System 7.1.2, it is 9pt. How can I localize my software so that it will look right on each of the System's versions? A There are three ways to set the font information. These methods have certain advantages and disadvantages in various situations: 1. Have the system decide the font.  If the text to be displayed belongs to the system, it makes sense to use the font that the system recommends. This is the easiest and safest approach, and Apple has encouraged it for a long time.  2. Hard-code the font in the application.  Some applications have very specific functions, and they must use a specific font for which there is no substitute. This approach is discouraged, but it may be legitimate in a few special cases where a product is not meant to be localized.  3. Associate the font with the text.  Usually, text resources that are part of an application are tagged to use an appropriate font. If the application has other resources/code that makes assumptions about the layout of the text, it is also appropriate to include text-size information. A resource with font information is easier to localize with text, when necessary.  For example, if you have Roman text in a resource, and you want to display it faithfully, you should associate it with a Roman font -- not the font suggested by the system. This approach prevents scrambled text when the wrong font is used (e.g., extended MacRoman characters cannot be displayed faithfully with a Japanese font).  Note: This only works when the text is completely static.  4. Allow the user to select the font.  The user should have control over the fonts that are used to display information, and letting the user have control of the font size even better. Unfortunately, this makes it more difficult for the programmer, because the code for this has to be very flexible -- forms need to be intelligent, dialogs have to adjust their sizes, and everything is dynamic. Word Processors and Worldwide Web Browsers are good examples of this kind of flexibility.  If your application is not smart enough to adjust to unexpected sizes, that information should be associated with the localized resources.  Depending on the system to recommend a small font can cause problems, because the system is not smart enough to determine which fonts are actually installed. If the 9pt font is not available, and another size is scaled, you may get illegible results, and the results can be even worse when another font is substituted. You can check for the presence of the actual font, but determining what the user is actually seeing and whether it is satisfactory is a very complex process. The best solution is to give the user some control over preferences. [Jun 01 1995] |

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
