---
title: Adding QuickTime Movie Data to Non-QuickTime Files
apple_id: DTS10002001
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb31.html
archived_at: '2026-07-18T02:38:48.203553Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB31Adding QuickTime Movie Data to Non-QuickTime Files |

|  |
| --- |
| Q Is there a way to embed a QuickTime movie into a Macintosh file containing non-QuickTime material and have the Movie Toolbox play the movie back correctly? If so, can we pass the same movie handle to QuickTime for Windows and get it to play back the same data from the same file?   A To add QuickTime movie data to non-QuickTime files, store the movie data in the file using `FlattenMovieData` with the `flattenAddMovieToDataFork` flag. Since `FlattenMovieData` simply appends to a data fork of a file, it appends the movie data to any data file you pass to it. The data stored before or after the movie data doesn't matter to QuickTime, as long as you don't reposition the movie data within the data file. If you do, the movie references are no longer correct, since they aren't updated when you edit the file. The returned movie (from `FlattenMovieData`) resolves properly to that data file. You can then save the movie in the data fork with `PutMovieIntoDataFork`, or in the resource fork with `AddMovieResource`. If the movie is saved in the data fork, you can retrieve it with `NewMovieFromDataFork` for both QuickTime and QuickTime for Windows. It is possible to store multiple movies simply by calling `FlattenMovieData` and `PutMovieIntoDataFork` several times on the same file. Each FlattenMovieData call appends new data, assuming the `createMovieFileDataCurFile` flag isn't set. For more information, see "Cross-Platform Compatibility and Multiple-Movie Files" in _develop_ #17. [May 01 1995] |

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
