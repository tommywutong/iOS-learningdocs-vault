---
title: Core Audio Overview
apple_id: TP40003577
resource_type: Guide
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/CoreAudioOverview/Introduction/Introduction.html
archived_at: '2026-07-15T08:18:00.579307Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](What%20Is%20Core%20Audio.md)

# Introduction

Core Audio provides software interfaces for implementing audio features in applications you create for iOS and OS X. Under the hood, it handles all aspects of audio on each of these platforms. In iOS, Core Audio capabilities include recording, playback, sound effects, positioning, format conversion, and file stream parsing, as well as:

- A built-in equalizer and mixer that you can use in your applications
- Automatic access to audio input and output hardware
- APIs to let you manage the audio aspects of your application in the context of a device that can take phone calls
- Optimizations to extend battery life without impacting audio quality

On the Mac, Core Audio encompasses recording, editing, playback, compression and decompression, MIDI, signal processing, file stream parsing, and audio synthesis. You can use it to write standalone applications or modular effects and codec plug-ins that work with existing products.

Core Audio combines C and Objective-C programming interfaces with tight system integration, resulting in a flexible programming environment that maintains low latency through the signal chain.

_Core Audio Overview_ is for all developers interested in creating audio software. Before reading this document you should have basic knowledge of general audio, digital audio, and MIDI terminology. You will also do well to have some familiarity with object-oriented programming concepts and with Apple’s development environment, Xcode. If you are developing for iOS-based devices, you should be familiar with Cocoa Touch development as introduced in _[Start Developing iOS Apps Today (Retired)](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/index.html#//apple_ref/doc/uid/TP40011343)_.

This document is organized into the following chapters:

- [What Is Core Audio?](What%20Is%20Core%20Audio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqmznknltc) describes the features of Core Audio and what you can use it for.
- [Core Audio Essentials](Core%20Audio%20Essentials.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqmjqfvjvomi) describes the architecture of Core Audio, introduces you to its programming patterns and idioms, and shows you the basics of how to use it in your applications.
- [Common Tasks in OS X](Common%20Tasks%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqnrnknltc) outlines how you can use Core Audio to accomplish several audio tasks in OS X.

This document also contains four appendixes:

- [Core Audio Frameworks](Core%20Audio%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqojnknltc) lists the frameworks and headers that define Core Audio.
- [Core Audio Services](Core%20Audio%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqnbnknlti) provides an alternate view of Core Audio, listing the services available in iOS, OS X, and on both platforms.
- [System-Supplied Audio Units in OS X](System-Supplied%20Audio%20Units%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqobnknlte) lists the audio units that ship in OS X v10.5.
- [Supported Audio File and Data Formats in OS X](Supported%20Audio%20File%20and%20Data%20Formats%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqnznknltc) lists the audio file and data formats that Core Audio supports in OS X v10.5.

For more detailed information about audio and Core Audio, see the following resources:

- _[AVAudioPlayer Class Reference](https://developer.apple.com/documentation/avfoundation/avaudioplayer)_, which describes a simple Objective-C interface for audio playback in iOS applications.
- _[Audio Session Programming Guide](../../Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_, which explains how to specify important aspects of audio behavior for iOS applications.
- _[Audio Queue Services Programming Guide](../Audio%20Queue%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbt)_, which explains how to implement recording and playback in your application.
- _[Core Audio Data Types Reference](https://developer.apple.com/documentation/coreaudio/core_audio_data_types)_, which describes the data types used throughout Core Audio.
- _[Audio File Stream Services Reference](https://developer.apple.com/documentation/audiotoolbox/audio_file_stream_services)_, which describes the interfaces you use for working with streamed audio.
- _[Audio Unit Programming Guide](../Audio%20Unit%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzy)_, which contains detailed information about creating audio units for OS X.
- _[Core Audio Glossary](../Core%20Audio%20Glossary/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjt)_, which defines terms used throughout the Core Audio documentation suite.
- _[Apple Core Audio Format Specification 1.0](../Apple%20Core%20Audio%20Format%20Specification%201.0.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnrs)_, which describes Apple’s universal audio container format, the Core Audio File (CAF) format.
- The Core Audio mailing list: [http://lists.apple.com/mailman/listinfo/coreaudio-api](http://lists.apple.com/mailman/listinfo/coreaudio-api)
- The OS X audio developer site: [http://developer.apple.com/audio/](https://developer.apple.com/audio/)
- The Core Audio SDK (software development kit), available at [http://developer.apple.com/sdk/](https://developer.apple.com/sdk/)
[Next](What%20Is%20Core%20Audio.md)

