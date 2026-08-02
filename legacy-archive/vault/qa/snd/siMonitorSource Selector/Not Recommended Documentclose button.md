---
title: siMonitorSource Selector
apple_id: DTS10002180
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-04-12'
source_url: https://developer.apple.com/library/archive/qa/snd/snd13.html
archived_at: '2026-07-18T02:38:54.600940Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND13siMonitorSource Selector |

|  |
| --- |
| Q How do I use the new `siMonitorAvailable` and `siMonitorSource` selectors?   A These selectors work with the sound output component to select the source that the user hears and makes that source the default recording source. Because this selector works with only with the sound output component, you don't need a sound channel to use it. The `siMonitorAvailable` selector returns a `SoundInfoList` just like [`siOSTypeInputAvailable`](snd12.md) does; it is a structure to a `short` and a `Handle`. The handle contains an array of `OSTypes` which are the input sources that can be monitored. See [Q&A SND12](Not%20Recommended%20Documentclose%20button-2.md) for more information about working with a `SoundInfoList` structure.  Here is some sample code showing how to find a sound output component and use the `siMonitorSource` and `siMonitorAvailable` selectors:   ``` include    <Sound.h> #include    <Errors.h> #include    <Memory.h>  // A simple application that gets the available monitor sources, // finds each of the monitor source names, // determines which sources are enabled, and sets various sources.  void main(void) {     NumVersionVariant       smVersion;     ComponentResult         err;     OSType                  source;     SoundInfoList           monitorList;     Component               device;     ComponentDescription    looking;      smVersion.parts = SndSoundManagerVersion();      // Only Sound Manager 3.1 or later implements the SoundComponentGet/SetInfo calls.     // If you know you're going to run on System 7.5 or later,     // you can skip the SM version check.      if (smVersion.whole >= 0x03100000) {         looking.componentType = kSoundOutputDeviceType;         looking.componentSubType = 0;         looking.componentManufacturer = kAppleManufacturer;         looking.componentFlags = 0;         looking.componentFlagsMask = 0;         device = FindNextComponent (0, &looking);          // here's how to get a list of the available monitor sources         // (and tell if monitor sources are supported)         // this returns a list of the OSTypes for the sources         // (don't forget to dispose of the handle later)          err = GetSoundOutputInfo(device, siMonitorAvailable, &monitorList);          if (err != noErr)   // monitor sources not supported, bail in your own way             goto Exit;          DisposeHandle(monitorList.infoHandle);          // don't forget to dispose of the returned handle          // find out which source is monitored         GetSoundOutputInfo(device, siMonitorSource, &source);          // set CD as the monitor source         (if it is present - err <> noErr if not available)         err = SetSoundOutputInfo(device, siMonitorSource, (void *)kCDSource);          // find out which source is monitored again,         to check that the setting made above worked         err = GetSoundOutputInfo(device, siMonitorSource, &source);     }  Exit:     return; } ```   The selectors are defined in Universal Headers 3.1 and later. They are:   ```    siMonitorAvailable            = FOUR_CHAR_CODE('mnav'),    siMonitorSource               = FOUR_CHAR_CODE('mons'), ```    [Apr 12 1998] |

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
