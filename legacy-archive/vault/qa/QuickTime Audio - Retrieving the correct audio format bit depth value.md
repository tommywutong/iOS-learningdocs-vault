---
title: QuickTime Audio - Retrieving the correct audio format bit depth value
apple_id: DTS10003942
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-11-05'
source_url: https://developer.apple.com/library/archive/qa/qa1477/_index.html
archived_at: '2026-07-18T02:31:22.828325Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1477

# QuickTime Audio - Retrieving the correct audio format bit depth value

## Q:  I'm importing AIFF files containing 24-bit audio ( `k24BitFormat` ). However, when I examine the sound media `SoundDescription`, `sampleSize` always says 16. How can I find the actual audio bit depth without having to check the `dataFormat` field?

A: The value reflected in the `sampleSize` field is a remnant of the old Sound Manager where the native resolution was 16-bit integer samples through the processing chain, and all formats reported a sample size of either 8-bit or 16-bit.

In order to find the true sample size, you'll need to retrieve the `AudioStreamBasicDescription` from the `SoundDescriptionHandle` by calling `QTSoundDescriptionGetProperty` using the `kQTSoundDescriptionPropertyID_AudioStreamBasicDescription` property.

__Listing 1__  Retrieving the ASBD from a `SoundDescriptionHandle` snippet.

```
 SoundDescriptionHandle hSoundDescription = (SoundDescriptionHandle)NewHandle(0);
    AudioStreamBasicDescription asbd = {0};
    OSStatus err;

    ...

    GetMediaSampleDescription(aSoundMedia, index, (SoundDescriptionHandle)hSoundDescription);
    if (err = GetMoviesError()) goto bail;

    err = QTSoundDescriptionGetProperty(hSoundDescription, kQTPropertyClass_SoundDescription,
                  kQTSoundDescriptionPropertyID_AudioStreamBasicDescription, sizeof(asbd), &asbd, NULL);

    ...

bail:

    If (hSoundDescription) DisposeHandle((Handle) hSoundDescription);
```

In the returned `AudioStreamBasicDescription`, check the `mBitsPerChannel` field. This is the number of bits of sample data for each channel in a frame of data.

If `mBitsPerChannel` is zero, you're dealing with a compressed format. The `mFormatID` field of the `AudioStreamBasicDescription` indicates the general kind of data in the stream.

Some compressed formats have the ability to indicate the precision of the original source data. Apple Lossless for example ( `mFormatID` field == `kAudioFormatAppleLossless` ) performs true lossless compression and reports the precision of the original source data though flags set in the `mFormatFlags` field of the `AudioStreamBasicDescription`.

The `kAppleLosslessFormatFlags_xxx` flags are located in `CoreAudioTypes.h`


```
kAppleLosslessFormatFlag_16BitSourceData - This flag is set for Apple Lossless data that was sourced
from 16 bit native endian signed integer data.

kAppleLosslessFormatFlag_20BitSourceData - This flag is set for Apple Lossless data that was sourced
from 20 bit native endian signed integer data aligned high in 24 bits.

kAppleLosslessFormatFlag_24BitSourceData - This flag is set for Apple Lossless data that was sourced
from 24 bit native endian signed integer data.

kAppleLosslessFormatFlag_32BitSourceData - This flag is set for Apple Lossless data that was sourced
from 32 bit native endian signed integer data.
```


[AudioStreamBasicDescription - Contains all the information needed for describing streams of audio data.](https://developer.apple.com/documentation/MusicAudio/Reference/CoreAudio/core_audio_types/chapter_6_section_4.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-11-05 | editorial |
| 2006-05-17 | New document that discusses how to retrieve accurate audio format bit depth. |

