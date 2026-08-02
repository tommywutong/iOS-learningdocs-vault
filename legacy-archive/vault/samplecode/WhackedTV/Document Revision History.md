---
title: WhackedTV
apple_id: DTS10003727
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/WhackedTV/History/History.html
archived_at: '2026-07-18T03:28:11.655786Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WhackedTV](WhackedTV.md)


[Previous](Sources-WhackedDebugMacros.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#samplecode/AVRecorder/Introduction/Intro.html](https://developer.apple.com/library/mac/#samplecode/AVRecorder/Introduction/Intro.html)

# Document Revision History

This table describes the changes to _WhackedTV_.

| __Date__ | __Notes__ |
| 2011-09-06 | Marked sample as Legacy. |
| 2008-05-09 | Fixed two bugs: (1) "Select Output Format" in the audio dialog failed with error -206 if the source audio were set to 20 or 24 bits on an Intel Mac. The source format is 24-bits aligned low in 32-bits. WhackedTV was setting this as the default output format. But QuickTime movies can only contain packed samples. Added a utility function to conform the output format for movie-safety. (2) Began preferring the kQTSGAudioPropertyID_CodecSpecificSettingsArray property to the kQTSGAudioPropertyID_MagicCookie property. See QuickTimeComponents.h for an explanation of the differences between these properties, and why CodecSpecificSettingsArray should always be preferred over MagicCookie. |
| 2008-01-18 | Fixed a bug in SGAudioSettings.mm where multiple audio devices with the same name would only be listed once. |
| 2007-08-14 | Updated code for WhackedTV to 1) demonstrate the .noindex technique for holding off Spotlight from prematurely indexing files being written by Sequence Grabber. This avoids frame droppage. 2) demonstrate the newish GainScalarToDecibels property of SGAudioChannel. 3) clean up some of the threaded code (alert dialogs were being invoked from secondary threads). |
| 2007-03-09 | Added better handling for notifications, including the use of an AutoreleasePool in the SGAudio listener callback, which may be called on non cocoa threads. |
| 2005-07-22 | Incorporated a workaround for a bug in the SGAudioChannel's kQTSGAudioPropertyID_SoundDescription SetProperty call. This SetProperty call (as of QT 7.0.1) does not correctly clear the previously set output magic cookie, if one exists. So if you choose an output format of AAC, then go to LPCM, the previous format's magic cookie confuses the SGAudioChannel, and it crashes the next time you preview or record. This bug will be fixed in a future software update, but this revision of WhackedTV shows how to work around the problem by setting the output StreamFormat, ChannelLayout, and MagicCookie separately, rather than setting them in one shot with kQTSGAudioPropertyID_SoundDescription SetProperty. |

[Previous](Sources-WhackedDebugMacros.h.md)

