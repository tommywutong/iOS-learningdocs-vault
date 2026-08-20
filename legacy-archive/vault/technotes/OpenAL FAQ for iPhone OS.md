---
title: OpenAL FAQ for iPhone OS
apple_id: DTS40007999
resource_type: Technical Note
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/technotes/tn2199/_index.html
archived_at: '2026-07-26T19:54:09.567904Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2199

# OpenAL FAQ for iPhone OS

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Common questions and answers about using OpenAL to add positional audio to your iPhone OS application.

OpenAL is a cross-platform, positional audio API included in iPhone OS. It is the recommended technology for adding audio to games and is well suited for adding audio features to many other types of applications. OpenAL provides an environmental context for audio, enabling you to build applications that immerse users in directional sound. Built upon Core Audio, OpenAL in iPhone OS provides high performance and excellent audio quality.

__1. Which version of the OpenAL specification does iPhone OS implement?__

The OpenAL framework in iPhone OS 2.1 implements the OpenAL 1.1 specification.

__2. What are the supported Apple platforms for OpenAL?__

OpenAL is available in the OpenAL framework (`OpenAL.framework`) in iPhone OS 2.0 and later. It is also available in Mac OS X v10.4 and later.

__3. Which audio formats can I play using OpenAL on the iPhone and iPod touch?__

To use OpenAL for playback, your application typically reads audio data from disk using Extended Audio File Services. In this process you convert the on-disk format, as needed, into one of the OpenAL playback formats. As part of this conversion, you must ensure that the samples you pass to OpenAL have iPhone-native endianness. Use the `kAudioFormatFlagsNativeEndian` constant from the `CoreAudioTypes.h` header file when calling Extended Audio File Services.

The on-disk audio format that your application reads must be PCM (uncompressed) or a compressed format that does not use hardware decompression, such as IMA-4.

The supported playback formats for OpenAL in iPhone OS are identical to those for OpenAL in Mac OS X. You can play the following linear PCM variants: mono 8-bit, mono 16-bit, stereo 8-bit, and stereo 16-bit.

__4. How does OpenAL on the iPhone/iPod touch differ from OpenAL on the desktop?__

The iPhone OS implementation of OpenAL does not include the effect extensions found on the desktop. Specifically, the Roger Beep, Distortion, Reverb, Obstruction, and Occlusion effects are not available in iPhone OS.

The OpenAL capture APIs, which you would use for OpenAL recording, are also not available in this version of the OS.

__5. What are the best practices for optimizing performance and efficiency when using OpenAL on iPhone and iPod touch?__

- Use the `alBufferDataStatic` API, found in the `oalStaticBufferExtension.h` header file, instead of the standard `alBufferData` function. This eliminates extra buffer copies by allowing your application to own the audio data memory used by the buffer objects.
- If your application renders several audio buffers simultaneously, you should typically use a lower sample rate, such as 22kHz. When rendering a single source, a 44.1kHz sample rate may be most efficient. Experiment and analyze the performance of your application. Individual circumstances determine the best tradeoff between sample rate and the number of audio sources being rendered.

__6. Where can I get support for OpenAL development?__

Apple actively participates in the OpenAL mailing lists, where you can post questions or issues. Visit [OpenAL.org](http://openal.org) to subscribe to these lists.

For Apple-specific audio technology discussions, join the [Core Audio mailing list](http://lists.apple.com/mailman/listinfo/coreaudio-api).

__7. Where can I get detailed information about OpenAL?__

Visit the [OpenAL](http://openal.org/) website for detailed information about the technology, including features, specifications, documentation, mailing lists, licensing, shipping titles, and more.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-03-09 | Moved to Retired Documents Library. |
| 2008-11-14 | Corrected a typographical error. |
|  | Corrected a typographical error. |
| 2008-09-18 | First Version |

