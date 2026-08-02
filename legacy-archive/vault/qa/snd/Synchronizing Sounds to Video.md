---
title: Synchronizing Sounds to Video
apple_id: DTS10002186
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-05'
source_url: https://developer.apple.com/library/archive/qa/snd/snd19.html
archived_at: '2026-07-18T02:38:54.834617Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND19Synchronizing Sounds to Video |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: With Mac OS 9.0 and Sound Manager 4.0, my sound callbacks are no longer being called in a regular manner. This makes it very hard to synchronize sound to video. How can I get my sound callbacks to be called regularly?  A: The big change with Sound Manager 4.0 is that your callbacks happen as soon as the sound has been given to the DMA engine to give to the hardware, and that the DMA buffer has increased in size. This means that the callbacks are getting called a little sooner than they used to. This problem is exasperated by having a buffer that is smaller than the hardware’s (or in this case the DMA buffer’s).  When you have a buffer of sound data to play that is smaller than the hardware’s buffer, it will be copied completely into the hardware’s buffer. At that point the sound is considered to be “done,” and the next command in the sound channel’s queue will be called. Typically the next command in the queue would be a `callBackCmd`. If you were expecting that the sound be done when your callback was called, you are in for a problem because the sound is probably not done.  The solution to this problem is simple: increase the size of the buffers that you play. You want the buffer’s size to be at least the size of the hardware’s, and for most situations, twice the hardware’s buffer size is a good choice.  Currently, with Sound Manager 4.0 the buffer size without VM on is 512 samples, and with VM on is 4,096 samples.  However, you should not assume that you know these values as they may change in the future. You can query the hardware to get these values using the following code:   |  | | --- | | ``` /*     Returns the size of the output buffer in bytes. */ static long GetSoundOutputBufferSize (Component outputDevice, short sampleSize, short numChannels,    UnsignedFixed sampleRate) {     SoundComponentData  outputFormat;     OSErr               err;     SndChannelPtr       chan            = nil;     SndCommand          cmd;     ExtSoundHeader      sndHeader;     long                bufSize         = 0;      err = SndNewChannel (&chan, 0, 0, nil);      sndHeader.samplePtr = nil;     sndHeader.numChannels = numChannels;     sndHeader.sampleRate = sampleRate;     sndHeader.loopStart = 0;     sndHeader.loopEnd = 0;     sndHeader.encode = extSH;     sndHeader.baseFrequency = kMiddleC;     sndHeader.numFrames = 0;     sndHeader.markerChunk = nil;     sndHeader.instrumentChunks = nil;     sndHeader.AESRecording = nil;     sndHeader.sampleSize = sampleSize;     sndHeader.futureUse1 = 0;     sndHeader.futureUse2 = 0;     sndHeader.futureUse3 = 0;     sndHeader.futureUse4 = 0;     sndHeader.sampleArea[0] = 0;      // This really isn't needed since the Sound Manager currently     // ignores this value.     UnsignedFixedTox80 (sampleRate, &sndHeader.AIFFSampleRate);      // Get the sound channel setup so we can query it.     cmd.cmd = soundCmd;     cmd.param2 = (long)&sndHeader;     err = SndDoCommand (chan, &cmd, true);      if (err == noErr) {         err = GetSoundOutputInfo (outputDevice, siHardwareFormat, &outputFormat);     }  #if DEBUG     if (err != noErr) {         printf ("Got error #%d trying to do GetSoundOutputInfo with         siHardwareFormat\n\n", err);     } else {         bufSize = outputFormat.sampleCount * (sampleSize / 8) * numChannels;         printf ("Sound output buffer is %d samples, ", outputFormat.sampleCount);         printf ("which is %d bytes.\n\n", bufSize);     } #endif      return (bufSize); } ``` |     |  | | --- | | If the `GetSoundOutputInfo` call fails, you can fall back to assuming that the size of the sound output buffer is the size of the sound input buffer, and you can get that information with this call: |     |  | | --- | | ``` /*     Returns the size of the input buffer in bytes. */ static long GetSoundInputBufferSize (UInt32 siRefNum) {     OSErr               err;     long                inputBufferSize;      err = SPBGetDeviceInfo (siRefNum, siDeviceBufferInfo, &inputBufferSize);  #if DEBUG     if (err != noErr) {         printf ("\nGet device buffer info error, err: %d\n", err);     } else {         printf ("\nSound input buffer is %d bytes\n", inputBufferSize);     } #endif      return (inputBufferSize); } ``` |    [Oct 05 1999] |

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
