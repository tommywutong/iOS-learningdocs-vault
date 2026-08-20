---
title: Synchronous SysBeep
apple_id: DTS10002185
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-05'
source_url: https://developer.apple.com/library/archive/qa/snd/snd18.html
archived_at: '2026-07-18T02:38:54.780443Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND18Synchronous SysBeep |

|  |  |
| --- | --- |
| ---   Q: With Sound Manager 3.1 the system beep, `SysBeep`, became asynchronous. For my particular application I need to wait until the `SysBeep` is done playing the sound before I want to continue. How do I get the functionality of the old synchronous `SysBeep`?  A: The answer to getting a synchronous `SysBeep` is very simple, and doesn’t involve you trying to figure out how long to wait. Just ask the Sound Manager to play `SysBeep` synchronously and it will.   |  | | --- | | ``` OSErr MakeSysBeepSynchronous (SInt16 *oldState) {     OSErr        err;      SndGetSysBeepState (oldState);     err = SndSetSysBeepState (sysBeepEnable | sysBeepSynchronous);      return err; } ``` |    [Oct 05 1999] |

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
