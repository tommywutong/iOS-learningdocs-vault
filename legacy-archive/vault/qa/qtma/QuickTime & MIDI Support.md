---
title: QuickTime & MIDI Support
apple_id: DTS10001939
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtma/qtma02.html
archived_at: '2026-07-18T02:38:46.251985Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Audio](https://developer.apple.com/referencelibrary/QuickTime/idxMusicAudio-date.html)

|  |
| --- |
| Technical Q&A QTMA02QuickTime & MIDI Support |

|  |
| --- |
| Q How can I determine if QuickTime 2.0's MIDI music function is available and if the larger set of 41 instruments is available? If the MIDI function is available, we need to add code to enable the music portion of our game.   A The QuickTime music architecture became available in version 2.0, so checking the QuickTime version in a Gestalt call (selector: gestaltQuickTimeVersion) will tell you if the MIDI function is present. When you install System 7.5 from the CD, the QuickTime Musical Instruments Extension is installed in your system folder. This gives you the number of musical instruments supported by Apple. The QuickTime Musical Instruments Extension is actually a component. If you need to know if the instruments are present, issue FindNextComponent, searching for a component that has a type of 'inst' and subtype of 'ss '. To verify the results of the search, use MacsBug dcmd 'thing' or CDEV 'Things!'. Both are on the QuickTime 2.0 SDK CD ("Mac: QuickTime Tools: Things!" and "Mac: Programming stuff: QuickTime Debugging").  Here is a code snippet that ought to help you:   ``` pascal Boolean AreQuickTimeMusicInstrumentsPresent(void) {     ComponentDescription aCD;      aCD.componentType = 'inst';     aCD.componentSubType = 'ss  ';     aCD.componentManufacturer = 'appl';      if(FindNextComponent((Component)0, &aCD) != NULL)         return true;     else         return false; } ```  [May 01 1995] |

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
