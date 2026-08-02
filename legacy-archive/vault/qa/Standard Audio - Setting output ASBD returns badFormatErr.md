---
title: Standard Audio - Setting output ASBD returns badFormatErr
apple_id: DTS10004096
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-11-15'
source_url: https://developer.apple.com/library/archive/qa/qa1489/_index.html
archived_at: '2026-07-18T02:31:25.272386Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1489

# Standard Audio - Setting output ASBD returns badFormatErr

## Q:  I'm trying to set an SCAudio output `AudioStreamBasicDescription` by calling `QTSetComponentProperty` using the `kQTSCAudioPropertyID_BasicDescription` property but it always returns a `badFormat` (-206) error. Setting the output format ID (`mFormatID` in the ASBD) as either `k16BitBigEndianFormat` or `kFloat64Format` fails.

A: The property call fails because you are using Sound Manager format types with the Standard Audio Compression Component.

The Standard Audio Compression Component does not understand these formats and therefore returns `badFormatErr`.

The __Standard Audio Compression Component__ (also known as StdAudio, Standard Audio, SCAudio) was added in QuickTime 7.0 and has the component SubType `StandardCompressionSubTypeAudio`. This component supports high-resolution audio output formats, is built on top of Core Audio and has a full set of component properties to make configuration easier.

APIs such as `SCAudioFillBuffer` (added in QuickTime 7.1) are available when using this component.

__Standard Audio__ replaces __Standard Sound__ which has the component SubType `StandardCompressionSubTypeSound`. Standard Sound uses the Sound Manager (deprecated) and is therefore limited to a maximum of 2 channels and sample rates of 64 kHz or less. Use of Standard Sound is no longer recommended.

As stated above, Standard Audio is built on top of Core Audio and therefore uses Format IDs (the four character code IDs used to identify individual formats of audio data) found in `CoreAudioTypes.h` while `k16BitBigEndianFormat` and `kFloat64Format` are Sound Manager Format Types found in `Sound.h`.

__Listing 1__  Correctly describing a 16-bit Big Endian PCM format.

```
mFormatID = kAudioFormatLinearPCM;
mFormatFlags = kAudioFormatFlagIsBigEndian |
               kAudioFormatFlagIsSignedInteger |
               kAudioFormatFlagIsPacked;
mBitsPerChannel = 16;
```


__Listing 2__  Correctly describing a 64-bit Big Endian PCM format.

```
mFormatID = kAudioFormatLinearPCM;
mFormatFlags = kAudioFormatFlagIsBigEndian |
               kLinearPCMFormatFlagIsFloat |
               kAudioFormatFlagIsPacked;
mBitsPerChannel = 64;
```


- [QuickTime 7 Audio Enhancements](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter02/chapter_2_section_6.html)
- [QuickTime 7.1 Audio Enhancements and Changes](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7-1_Update_Guide/Content/2NewFeaturesChangesa.html)
- [Audio Stream Basic Description](https://developer.apple.com/documentation/MusicAudio/Reference/CoreAudio/core_audio_types/chapter_6_section_4.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-15 | New document that discusses why badFormatErr may be returned from Standard Audio |

