---
title: siOSTypeInput Selectors
apple_id: DTS10002179
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-04-12'
source_url: https://developer.apple.com/library/archive/qa/snd/snd12.html
archived_at: '2026-07-18T02:38:54.511832Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [siMonitorSource Selector](Not%20Recommended%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND12siOSTypeInput Selectors |

|  |
| --- |
| Q How do I use the new `siOSTypeInputSource` and `siOSTypeInputAvailable` selectors?   A The `siOSTypeInputSource` selector works just like the `siInputSource` selector. It works with both `SPBGetDeviceInfo` and `SPBSetDeviceInfo`. To use it, pass a pointer to an `OSType` for the input source you wish to select. For example:  ```     inputSource = kCDSource;     err = SPBSetDeviceInfo (soundRefNum, siOSTypeInputSource, &inputSource);      ```   or pass a pointer to an `OSType` to hold the result of a call to `SPBGetDeviceInfo`, for example:   ```     OSType        inputSource;     err = SPBGetDeviceInfo (soundRefNum, siOSTypeInputSource, &inputSource); ```   The `siOSTypeInputAvailable` selector works with `SPBGetDeviceInfo` and returns a `SoundInfoList` structure, which is a `short` followed by a `Handle`, as its result. You can then parse the `SoundInfoList` to get the number of `OSTypes` that are in the returned handle.  Here is a simple example of how to walk the returned handle extracting each `OSType`.   ``` SErr GetSoundInputSourceOSTypes (long siRefNum) {     OSErr                err;     SoundInfoList            sourceTypes;     long                offset            = 0;     short                numTypes;     int                i;     char                sourceType[5];     Handle                OSTypes            = nil;      err = SPBGetDeviceInfo (siRefNum, siOSTypeInputAvailable, &sourceTypes);     if (err != noErr) {         printf ("\nGot error #%d from siOSTypeInputAvailable\n\n", err);     }      if (err == noErr) {         printf ("\nThe sound input source OSTypes are:\n");          numTypes = sourceTypes.count;         OSTypes = sourceTypes.infoHandle;          for (i = 0; i < numTypes; i++) {             BlockMoveData (&(*OSTypes)[offset], sourceType, 4);             sourceType[4] = 0;             printf ("  %s\n", sourceType);             offset += sizeof (OSType);         }     }      if (OSTypes != nil) {         DisposeHandle (OSTypes);     }      return err; } ```   The input source constants are defined in Universal Headers 3.1 and later. Here are the currently defined constants:   ``` /* input source Types*/  enum {     kNoSource            = FOUR_CHAR_CODE('none'),   /*no source selection*/     kCDSource            = FOUR_CHAR_CODE('cd  '),   /*internal CD player input*/     kExtMicSource        = FOUR_CHAR_CODE('emic'),   /*external mic input*/     kRCAInSource         = FOUR_CHAR_CODE('irca'),   /*RCA jack input*/     kTVFMTunerSource     = FOUR_CHAR_CODE('tvfm'),     kDAVInSource         = FOUR_CHAR_CODE('idav'),   /*DAV analog input*/     kIntMicSource        = FOUR_CHAR_CODE('imic'),   /*internal mic input*/     kMediaBaySource      = FOUR_CHAR_CODE('mbay'),   /*media bay input*/     kModemSource         = FOUR_CHAR_CODE('modm'),   /*modem input*/     kZoomVideoSource     = FOUR_CHAR_CODE('zvpc')    /*zoom video input*/ };      siOSTypeInputSource    = FOUR_CHAR_CODE('inpt'),  /*input source by OSType*/     siOSTypeInputAvailable = FOUR_CHAR_CODE('inav'),          /*list of available input source OSTypes*/ ```    [Apr 12 1998] |

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
