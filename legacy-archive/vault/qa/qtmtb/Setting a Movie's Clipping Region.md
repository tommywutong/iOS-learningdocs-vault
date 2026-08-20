---
title: Setting a Movie's Clipping Region
apple_id: DTS10001993
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb23.html
archived_at: '2026-07-18T02:38:47.911670Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB23Setting a Movie's Clipping Region |

|  |
| --- |
| Q Our application uses the movie poster as a still frame in a cell (similar to using a PICT). If a user sizes the cell width so that it's narrower than the poster, QuickTime posters are drawn full width, writing over whatever is in the way, even though we clip the drawing to the cell size. Since Pictures clip through DrawPicture, why doesn't ShowMoviePoster stay within the clipping region?   A ShowMoviePoster and the movie- and preview-showing calls use the movie clipping characteristics rather than the destination port's clipping region. You must set the movie's clipping region to obtain the results you want. You can accomplish the same thing by getting the picture for the poster by calling GetMoviePosterPict and using DrawPicture to display the poster. Because this is just a picture, the clipping region of the port is honored, so you don't need different code for movies and pictures.   [May 01 1995] |

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
