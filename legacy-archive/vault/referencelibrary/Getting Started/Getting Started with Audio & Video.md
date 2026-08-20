---
title: Getting Started with Audio & Video
apple_id: TP30001095
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2009-05-27'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_MusicAudio/_index.html
archived_at: '2026-07-18T02:39:24.873301Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

Whether your multimedia needs are basic or advanced, OS X brings world-class support for adding professional-grade audio and video features to your application.

For audio recording, playback, and synchronization, Audio Queue Services offers a flexible, high-level API. For even more control, look at Extended Audio File Services and audio units—OS X’s audio plug-in architecture.

Audio units provide digital signal processing for filtering, effects, format conversion, I/O, and MIDI-based music synthesis. Use one of the many system-supplied audio units or develop your own. Other OS X interfaces support audio streaming, surround sound, custom codec development, hardware access for driver development and disc recording, and MIDI control.

If your application needs to play video, including content purchased through iTunes, you can take advantage of the new, lightweight, and more efficient media playback capability provided in QuickTime X. You gain access to this capability through the QTKit framework, a feature-rich Objective-C API for manipulating and rendering time-based media such as movies, audio files, animations, and streaming content.

### Start Here

Before you embark on adding OS X audio technologies to your application, become familiar with Core Audio’s features and architecture by reading [Core Audio Overview](../../documentation/Music%20Audio/Core%20Audio%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzx). Learn about OS X video support by reading [QTKit Application Tutorial](../../documentation/Cocoa/QTKit%20Application%20Tutorial/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjv).

#### Want to get familiar with the fundamentals?

- [Audio Queue Services Programming Guide](../../documentation/Music%20Audio/Audio%20Queue%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbt) explains how to add audio recording, playback, and synchronization to your application. Audio Queue Services can work with any OS X audio format.
- [Sound Programming Topics for Cocoa](../../documentation/Cocoa/Sound%20Programming%20Topics%20for%20Cocoa/Introduction%20to%20Sound%20Programming%20Topics%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydi2i) describes a simple playback interface suitable for playing uncompressed audio.
- [Audio Unit Programming Guide](../../documentation/Music%20Audio/Audio%20Unit%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzy) explains how to create audio processing plug-ins.
- [Getting Started with Hardware and Drivers](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_HardwareDrivers/_index.html#//apple_ref/doc/uid/TP40003522) provides orientation for supporting or developing audio peripheral devices.
- You can also review presentations from past Worldwide Developer Conferences on [ADC on iTunes](https://developer.apple.com/adconitunes/), including [Understanding the Core Audio Architecture](https://deimos.apple.com/WebObjects/Core.woa/BrowsePrivately/adc.apple.com.1670040666.01688079091.1912327130?i=1132016387)

#### Prefer to learn by example?

For audio:

- [AudioQueueTools](../../samplecode/AudioQueueTools/AudioQueueTools.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzyga) demonstrates how to record to an audio file and play it back using Audio Queue Services.
- [RecordAudioToFile](../../samplecode/RecordAudioToFile/RecordAudioToFile.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojygy) shows how to perform low-latency audio recording using the AUHAL audio unit and Extended Audio File Services.
- [PlayFile](../../samplecode/PlayFile/PlayFile.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnrvge) demonstrates audio file playback using Audio File Services, the Audio File Player audio unit, and the Default Output audio unit.
- [PlaySoftMIDI](../../samplecode/PlaySoftMIDI/PlaySoftMIDI.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnrtgu) shows how to play back a MIDI file using system-supplied audio units.
- [StarterAudioUnitExample](../../samplecode/StarterAudioUnitExample/StarterAudioUnitExample.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimjrhe) is a simple effect audio unit that corresponds to the tutorial in [Audio Unit Programming Guide](../../documentation/Music%20Audio/Audio%20Unit%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzy).
- [Audio Toolbox Convert File](../../samplecode/Audio%20Toolbox%20Convert%20File/Audio%20Toolbox%20Convert%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnruhe) provides examples of audio format conversion using Extended Audio File Services and Audio Converter Services.
- [OpenALExample](../../samplecode/OpenALExample/OpenALExample.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnjyg4) demonstrates how to bind OpenAL audio sources to OpenGL objects to create an immersive audio environment.

For video, [QTKit Application Tutorial](../../documentation/Cocoa/QTKit%20Application%20Tutorial/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjv) explains how to build three different Cocoa applications for playing, editing, and recording audio and video media:

- MyMediaPlayer demonstrates how to build a media player using Cocoa bindings. You can extend the media player by adding new capabilities for movie editing and custom movie playback.
- MyMediaRecorder builds an application for capturing and recording audio and video, and then outputting that media to QuickTime movies.
- StopMotion lets you construct a stop-motion application to capture single frames of video and assemble those frames into an animated QuickTime movie for playback.

### Go In Depth

- To perform spatial manipulation of sound in your application, especially if you are a games developer, use the OS X OpenAL framework. Learn more about OpenAL on the [OpenAL](http://www.openal.org/) website. The AU Lab application (Apple’s reference audio unit host, included with Xcode Tools) supports working with surround sound.
- To add recording capability to your application, use Audio Queue Services. Read [Audio Queue Services Programming Guide](../../documentation/Music%20Audio/Audio%20Queue%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbt) to learn how to record linear PCM or compressed audio.
- To parse an audio file stream, use Audio File Stream Services, part of the Audio Toolbox framework. Read [Audio File Stream Services Reference](https://developer.apple.com/documentation/audiotoolbox/audio_file_stream_services) and [Audio File Services Reference](https://developer.apple.com/documentation/audiotoolbox/audio_file_services), which describe the C interfaces you need.
- To support MIDI interfacing, play MIDI data from a file, or record incoming MIDI data, read [Core MIDI Services and MIDI Server Services](../../documentation/Music%20Audio/Core%20Audio%20Overview/Core%20Audio%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqnbnknltcmi) in [Core Audio Overview](../../documentation/Music%20Audio/Core%20Audio%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzx). Look at MIDI File Formats to learn how to use MIDI data in QuickTime.
- If you are a hardware vendor, you may need to supply drivers to allow your product to interact with Mac apps. Core Audio supports driver development. Consult [Audio Device Driver Programming Guide](../../documentation/Device%20Drivers/Audio%20Device%20Driver%20Programming%20Guide/Introduction%20to%20Audio%20Device%20Driver%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomrz).
- If your application offers disc recording capability, refer to Disc Recording Framework Reference and Disc Recording UI Framework Reference for comprehensive descriptions of these interfaces.

### Ready for More?

The OS X [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) contains many additional resources to make your job easier. Browse by topic, framework, or resource type (such as guides or sample code). Set filters to focus on what you are looking for.

