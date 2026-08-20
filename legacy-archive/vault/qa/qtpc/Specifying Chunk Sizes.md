---
title: Specifying Chunk Sizes
apple_id: DTS10002040
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/qtpc/qtpc08.html
archived_at: '2026-07-18T02:38:50.167554Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Design Guidelines](https://developer.apple.com/referencelibrary/QuickTime/idxDesignGuidelines-date.html)

|  |
| --- |
| Technical Q&A QTPC08Specifying Chunk Sizes |

|  |
| --- |
| Q I need some advice about setting up movie atoms. Certain values (e.g., samplesPerChunk) are variable, but I have found that extreme cases don't work. For example, I want to make a movie all in one chunk, since this results in a simple movie-atom structure. However, when I made a movie with an audio track that had only one 4MB chunk, the playback failed without any error message (ifMovie Player 2.0 had less memory than that assigned to the application). Why do movies created by most applications have a lot of chunks, even when the data is contiguous from chunk to chunk, and the chunks are all the same size? A The chunk architecture was designed for faster playback of movie material, based on the classical computer science notion that grouping material for faster caching makes the application faster overall. We use a parameter to define the default chunk sizes, based on our current strategy for playback optimization. Creating one huge chunk causes the system to read the whole chunk at once, and in your extreme case, you are truly running out of memory. The Mac operates with a very static memory model (unless VM is enabled, which we don't recommend, because page hits slow down any system that is trying to play back sound and video samples).  Our concept is that the Movie Toolbox will do the right thing concerning chunking of samples, so we don't have APIs for this purpose. We recommend that you avoid changing the default values with Dumpster and similar tools.  QuickTime 2.0 introduced the SetMediaPreferredChunkSize and GetMediaPreferredChunkSize calls for specifying the maximum chunk size for a media and for retrieving the current maximum value. Anything beyond this is outside the control of the developer. [Aug 01 1995] |

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
