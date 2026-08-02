---
title: User Clicking in a Style Text Document, Human Interface Guidelines
apple_id: DTS10002255
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tx/tx03.html
archived_at: '2026-07-18T02:38:59.079891Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TX03User Clicking in a Style Text Document, Human Interface Guidelines |

|  |
| --- |
| Q There doesn't appear to be a definitive answer to the following question in the Human Interface Guidelines: When a user clicks at any point in a styled text document, what font style and size settings should take effect? Does this depend on the character on which they clicked, on the final location of the insertion point, or on other factors? How does this affect the keyboard menu?   A On the surface, this seems to be a pretty simple question, but it is actually somewhat more complicated. When you write an application that may be used in foreign markets, you have to consider the needs of customers who may use script systems that incorporate right-to-left text instead of (or in addition to) the left-to-right text that is used in an American system. TextEdit (and most other implementations) supports mixed-directional text -- i.e., a combination of scripts having left-to-right and right-to-left text within a single line. You can usually rely on TextEdit to properly configure your insertion point. In a left-to-right system, when the insertion point is somewhere within a style run, the style you apply at the insertion point should be the same as the style that is already in effect for the run (for example, bold-12-point-geneva). However, the correct style isn't as easy to identify at the boundaries between runs. When you are between two style runs in a left-to-right system, the style associated with the run on the left is usually applied. This rule is essentially the same for right-to-left script systems, except that, at a boundary between runs, you use the style associated with the run on the right.  Unfortunately, it is more difficult to determine the correct style when you are at a boundary where left-to-right text meets right-to-left text. The best technique in this situation is to programmatically choose the style based on the exact point where the user clicks (if in the right-to-left run, use the style associated with this run; otherwise, use the style associated with the l-to-r run). A similar approach should be taken for situations where the user clicks in a boundary between two styles -- choose the style associated with the run closest to the place they click.  When there are multiple style runs within a selection, the style added should be added across the entire selection. In this situation, selecting bold from a style menu would apply bold to all characters in the run. If the user selects a range and enters some new text (replacing the range), apply the style associated with the first character in the run (bearing in mind that the first character of the selection is the left-most character if the script for the selection is left-to-right, and the right-most character if the script for the selection is right-to-left). For additional information on this and for other text-related questions, see _Inside Macintosh: Text._ There is an electronic version on the Developer CD: Reference Library Edition. [May 01 1995] |

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
