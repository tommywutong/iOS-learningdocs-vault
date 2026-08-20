---
title: MPEG Compression in QuickTime
apple_id: DTS10001935
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/qticm/qticm16.html
archived_at: '2026-07-18T02:38:46.120658Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Creation](https://developer.apple.com/referencelibrary/QuickTime/idxMovieCreation-date.html)

|  |
| --- |
| Technical Q&A QTICM16MPEG Compression in QuickTime |

|  |
| --- |
| Q What hardware and software are required to compress and save a QuickTime movie using MPEG?  A At present, QuickTime won't do MPEG compression, so you have to create MPEG-compressed files using something else. However, you can extract information from an MPEG-movie file and place it in a specific MPEG track.   The Movie Toolbox adds binary information to the data of the original MPEG file by adding text-track information. but this changes the configuration of the MPEG file. To keep MPEG files pure and intact, you should build new movie files that contain references to the MPEG file and the actual text-track information. These movie files can also contain other QuickTime-related information, tracks, and media.    Here's the way to do this:    1. Use CreateMovieFile() to create the new movie file on disk.  2. Create and set up the needed tracks and media in the new file.  3. Open the MPEG file as a separate movie.  4. Select the entire MPEG movie.  5. Call AddMovieSelection() to add a reference to the MPEG movie in the new movie.    Note that this does not work under QuickTime for Windows 2.0x, as this version does not yet support file references. [Aug 01 1995] |

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
