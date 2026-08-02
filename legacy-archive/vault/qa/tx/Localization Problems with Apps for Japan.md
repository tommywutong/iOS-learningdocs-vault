---
title: Localization Problems with Apps for Japan
apple_id: DTS10002254
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tx/tx02.html
archived_at: '2026-07-18T02:38:58.513946Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Text & Fonts](https://developer.apple.com/referencelibrary/Carbon/idxTextFonts-date.html)
- [Text & Fonts > Carbon](https://developer.apple.com/referencelibrary/TextFonts/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A TX02Localization Problems with Apps for Japan |

|  |
| --- |
| Q I am an English-speaking software engineer, and I've been assigned the task of localizing one of our applications for Japan. I have the Japanese Language Kit installed on my development system, and ResEdit 2.1.2 seems to work fine with it. TeachText Japanese should provide the limited amount of Japanese text editing we need (for a Balloon Help rez file), and we are bringing in two interpreters who are experienced computer users. Are there other tools available that would simplify the process? Does Apple have a human-interface guide for Japan (we want to use preferred Apple/Macintosh phraseology for things such as Drag and Drop). Is there a Japanese-Macintosh tutorial or user's guide that we can get in the United States? A Your tools sound reasonable, but you might want to consider some additions: \* AppleGlot. This is a very useful automation tool that strips out text resources for translation -- ResEdit should be used only for non-text resources that AppleGlot can't handle. Note that AppleGlot 2.1 conflicts with the Modern Memory Manager, so if you use this version, use the Memory Control Panel to turn it off. This problem was fixed in AppleGlot 2.2.  \* A true Japanese word processor, such as MacWrite-J. This is very useful to have. Many of the technical documents that contain information you may need are available only in MacWrite-J format, and MacWrite-US is not compatible with them.  If your application uses 'inline input', you'll need the Text Services Manager, but for basic Kanji input support, you don't need to do anything special, since the operating system takes care of this for you.  The Developer CDs have international SSW, and the Partners Seed CD includes a System 7.5-compatible version of the Japanese Language Kit. Plan on using both of these for testing. Start off by testing your current application (as-is) on KanjiTalk to see what kinds of problems you have. Once you've identified the problems, refer to the appropriate sections in _Inside Macintosh_ to resolve them. When your application runs without errors on KanjiTalk, you are ready to start the localization process. Typically, the documentation and packaging take the longest time to localize.  The sample documentation may present a problem in that paper versions are hard to come by and expensive to ship. If possible, have someone in Japan buy a system package and ship it to you. Although there may be soft copies of some documents available, you might not have access to applications that can read the formats used.  To obtain glossaries, it's possible to use AppleGlot to strip text resources out of applications, and if you have both English and Japanese applications, you can build a useful table. However, this only works for text that exists in an application's resources -- documentation is more difficult. You may be able to obtain Japanese glossaries or references via eWorld, AppleLink, INTERNET, and so on. For additional information, see _Inside Macintosh: Text_, which covers virtually everything you need to consider when localizing your application for a world market. _Localizing for Japan_ and _Guide to Macintosh Software Localization_(published by Addison-Wesley) are also good localization references (these are on some of the older Developer CDs). [May 01 1995] |

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
