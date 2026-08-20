---
title: Recording Compressed Sounds
apple_id: DTS10002181
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-04-12'
source_url: https://developer.apple.com/library/archive/qa/snd/snd14.html
archived_at: '2026-07-18T02:38:54.644125Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND14Recording Compressed Sounds |

|  |
| --- |
| Q I can only record sounds compressed by 'MAC3' and 'MAC6. Why can't I record sounds compressed by 'ima4' or 'ulaw'?   A The Sound Input Manager doesn't do the compression when you record: the sound input __driver__ does, and the Apple input drivers don't know how to do any compression except for MACE (furthermore, the MACE compression they use isn't the component one, it's a version that is built into the driver). The reason for this is that you can call `SPBRecord` at interrupt time, but components can't be opened at interrupt time, so the sound input driver can't use the Component Manager to access compression codes. Therefore, the driver's compression options are limited to those implemented in the driver.  You can use the `siCompressionAvailable` selector with `SPBGetDeviceInfo` to find out which compressions are supported by a particular driver.  __Note:__  QuickTime can record with any available compression format because it compresses the sound after it has been recorded: it does not rely on the driver to do the compression for it. You can use this technique yourself by using Sound Manager 3.2.1 (or later) and the SoundConverter routines to convert each input buffer as you record it (or the whole sound once it has been recorded). [Apr 12 1998] |

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
