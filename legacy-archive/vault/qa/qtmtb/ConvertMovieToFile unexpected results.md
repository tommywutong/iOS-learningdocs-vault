---
title: ConvertMovieToFile unexpected results
apple_id: DTS10002021
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb51.html
archived_at: '2026-07-18T02:38:49.305531Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Basics](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieBasics-date.html) >

|  |
| --- |
| Technical Q&A QTMTB51ConvertMovieToFile unexpected results |

|  |
| --- |
| ---   Q: When I call the `ConvertMovieToFile` function to convert a movie to a specified file and type, I get unexpected results unless I've first displayed and played the movie. I'm not using a movie controller, just the movie toolbox. If I display and play the movie first, `ConvertMovieToFile` correctly saves the movie with no problems. However, if I don't display and play the movie first, I get just a white movie of the right size and length along with the sound track. In neither case do I get an error from `ConvertMovieToFile`. What's going on?  A: The white frames you are seeing in the video track are a result of the movie not being active. Use the `SetMovieActive` function described in Inside Macintosh:QuickTime pages 2-145 to activate the movie before calling `ConvertMovieToFile` (if not already active). You can determine whether a movie is active by calling the `GetMovieActive` function, which is described on pages 2-146 of Inside Macintosh:QuickTime.  Finally, don't forget to set a valid port for the movie. Use the `SetMovieGWorld` function (Inside Macintosh:QuickTime, pages 2-159) to set the graphics world for displaying a movie. [Jun 14 1999] |

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
