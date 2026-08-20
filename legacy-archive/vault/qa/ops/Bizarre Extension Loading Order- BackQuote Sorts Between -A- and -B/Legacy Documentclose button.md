---
title: 'Bizarre Extension Loading Order: BackQuote Sorts Between "A" and "B".'
apple_id: DTS10001489
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-02-09'
source_url: https://developer.apple.com/library/archive/qa/ops/ops08.html
archived_at: '2026-07-18T02:29:49.309872Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS08Bizarre Extension Loading Order: BackQuote Sorts Between "A" and "B". |

|  |
| --- |
| Q I tried to get an extension to load last in the initialization or startup sequence, so I put the back quote character, "`" , as the first character in its name. But when I did this, it actually loaded near the beginning. What's up?   A If you view the contents of any folder by name, you'll see that items whose names begin with the back quote appear last (or nearly last) in the list. The Finder calls PACK 6 to sort the list, which uses the international sorting routines; these sorting routines order words beginning with a "`" near the end of the list. During INIT loading, however, PBHGetFInfo() is called and it, in turn, calls RelString(). RelString() is called with case insensitivity and diacritical sensitivity. Unfortunately, due to a bug that HFS relies on, back quote sorts between "a" and "b". This means that extensions beginning with a "`" load after extensions beginning with an "a" (or an "A") and before those with a "b" (or a "B").  There are no plans to fix this problem in order to maintain compatibility with old HFS volumes (which were created before this bug was discovered and which use this sorting order).  Interestingly, UpperString() converts a "`" into an "a", but leaves all other non-letters unchanged.  If you want to make sure that your extension is loaded last in the initialization process, use the tilde (~) as the first character of its name. Updated: 09-Feb-96 |

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
