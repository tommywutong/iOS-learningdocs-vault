---
title: Correction to SetMediaDataRef, short, not pointer
apple_id: DTS10002014
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb44.html
archived_at: '2026-07-18T02:38:48.929061Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB44Correction to SetMediaDataRef, short, not pointer |

|  |
| --- |
| The online version of IM-QT on the QT2.0 CD defines the interface for the SetMediaDataRef function to be:   ```   pascal OSErr SetMediaDataRef(Media theMedia, short index, Handle dataRef,                         OSType dataRefType); ```   which is also what the prototype in the include file says.  But the actual description for the "index" field says:   ``` "Contains a pointer to a short integer. The Movie Toolbox returns the index value that is assigned to the new data reference... ```   This is wrong. SetMediaDataRef returns a short, not a pointer (as defined in the APIs). [Aug 01 1995] |

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
