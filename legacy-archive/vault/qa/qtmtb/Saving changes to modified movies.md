---
title: Saving changes to modified movies
apple_id: DTS10002030
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb60.html
archived_at: '2026-07-18T02:38:49.730887Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Basics](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieBasics-date.html) >

|  |
| --- |
| Technical Q&A QTMTB60Saving changes to modified movies |

|  |
| --- |
| ---   Q: I'm using the QuickTime APIs to open up an existing QuickTime movie and make various changes to the movie. For example, I use the `QTRemoveAtom` function to delete atoms in the movie, and I also add sample data to the media in the movie using the `AddMediaSample` function. After I've made my changes, I make sure to close the movie file using the `CloseMovieFile` function. However, once I close the movie file my changes are not actually saved to the file. Why aren't my changes being saved?  A: After you have edited the movie, use the `UpdateMovieResource` function to save your changes. This will update the existing movie. If you would rather keep the existing movie and save your changes to a new movie, create a new movie by calling the `AddMovieResource` function (a movie file may contain more than one movie resource). You should, of course, then close the movie file by calling the `CloseMovieFile` function. [Sep 05 2000] |

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
