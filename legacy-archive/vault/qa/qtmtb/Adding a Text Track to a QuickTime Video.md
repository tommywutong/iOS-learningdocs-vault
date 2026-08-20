---
title: Adding a Text Track to a QuickTime Video
apple_id: DTS10002011
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb41.html
archived_at: '2026-07-18T02:38:48.757155Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Creation](https://developer.apple.com/referencelibrary/QuickTime/idxMovieCreation-date.html)

|  |
| --- |
| Technical Q&A QTMTB41Adding a Text Track to a QuickTime Video |

|  |
| --- |
| Q We want to add a text track to a QuickTime video for a four-title project we're starting. We're including videos in an activity-based educational CD for children. Part of our design is a sing-along to the video, and we want to include the text of the lyrics, which the user could turn on or off, as part of the video. What is the best tool or method for adding (and tuning) a text track to a QuickTime 2.0 video? Are there any performance issues or other drawbacks associated with adding a text track? Can you suggest a good example of a product that has text in a video as a reference? How can I control where text is displayed on the video window? How can I control the font, color, and so on? A You can use MoviePlayer to insert a text track into a video. Start with a text file, with each line in the file being a "frame" of the text video. Next, import it into MoviePlayer. This makes each line of the text file a printed line of text in a movie (it stores the text, not the bitmap, so it takes up very little space). Each frame of the movie is two seconds long. Then, edit the length of each "frame" to make it last the duration that the text is sung in the video, and add this text track to the actual video (like copying and pasting). There are instructions in the QuickTime 2.0 SDK CD on how to do this in a document entitled, Guide to MoviePlayer. This also describes how to position the text on the screen.  Note that you must add the text with MoviePlayer on the Mac, not in Windows. To make it playable across the two platforms, you have to use "burnt text". This is also described in the SDK, and there are some movie samples on the CD that include "burnt text" -- 'Assimilation+Burnt Text' and 'Beverage+Burnt Text'.  There is another good article in issue 20 of _develop_ entitled, Supporting Text Tracks in Your Application. The CD that accompanies _develop_ also includes sample code that demonstrates this technology. [May 01 1995] |

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
