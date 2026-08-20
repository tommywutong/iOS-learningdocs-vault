---
title: Saving QuickTime Movie Files
apple_id: DTS10002017
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1997-01-31'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb47.html
archived_at: '2026-07-18T02:38:49.136483Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB47Saving QuickTime Movie Files |

|  |
| --- |
| Here is a series of questions and answers about some complications you might face in creating and saving QuickTime movies:Q What is the proper way to save existing QuickTime movies after they have been edited?  AMoviePlayer is a good example:   - "Save" always updates the movie resource in the movie file that you   opened and keeps data "alias" references in the movie file. After   editing, the file is typically no longer in optimal format for playback. - "Save As" gives the user two options:   1. Creating a new movie file (which maintain data references to the original) 2. Creating a 'self contained' movie.  In case 1, MoviePlayer calls CreateMovieFile (with the 'createMovieFileDontCreateMovie' flag set) and then calls AddMovieResource using the edited 'original' movie resource.  If the user selects option 2 above, 'create self contained', MoviePlayer calls FlattenMovie and creates a new movie file and resource. (The original file remains open, however.) Q My application has a Movie resource from the original file which has been modified -- tracks have been added, as well as data (using data references). Should I choose option 1 or 2?   A Either method will work. If you use option 2 (FlattenMovie), the new file is interleaved, which is a good idea since we've got to write all the movie data to disk anyway. FlattenMovie optimizes the file for movie playback. (Be sure to flatten to a new file and don't try to overwrite the original file.)   Q What if I want to keep working with the new movie?  A If you want to work with the new flattened movie, FlattenMovieData is the way to go, since it automatically returns the new movie resource to you. (Use AddMovieResource to write this resource to the new file.)   Q If I use the FlattenMovieData/AddMovieResource method, can I close the original file? I want any further changes to take place in the new movie, not in the original one.   A Yes, you can close the file (and be sure to use DisposeMovie on your original movie resource, which still points back to the original file.) One more note: going this route does not store the movie in the "fast start" format, so the movie will not be stored optimally for Web or CD playback. (Hard drives typically aren't affected by this.) If you want the file to be in the very best playback format for cross-platform play, use FlattenMovie with the 'flattenAddMovieToDataFork' flag set. You'll then need to open this movie just as you did the original (i.e., with OpenMovieFile/ NewMovieFromFile). [Jan 31 1997] |

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
