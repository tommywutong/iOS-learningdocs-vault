---
title: Audio Queue Services Programming Guide
apple_id: TP40005343
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-12-19'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioQueueProgrammingGuide/Introduction/Introduction.html
archived_at: '2026-07-15T08:17:14.003992Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Audio%20Queues.md)

# Introduction

This document describes how to use Audio Queue Services, a C programming interface in Core Audio’s Audio Toolbox framework.

Audio Queue Services provides a straightforward, low overhead way to record and play audio in iOS and Mac OS X. It is the recommended technology to use for adding basic recording or playback features to your iOS or Mac OS X application.

Audio Queue Services lets you record and play audio in any of the following formats:

- Linear PCM.
- Any compressed format supported natively on the Apple platform you are developing for.
- Any other format for which a user has an installed codec.

Audio Queue Services is high level. It lets your application use hardware recording and playback devices (such as microphones and loudspeakers) without knowledge of the hardware interface. It also lets you use sophisticated codecs without knowledge of how the codecs work.

At the same time, Audio Queue Services supports some advanced features. It provides fine-grained timing control to support scheduled playback and synchronization. You can use it to synchronize playback of multiple audio queues and to synchronize audio with video.

Audio Queue Services is a pure C interface that you can use in Cocoa applications as well as in Mac OS X command-line tools. To help keep the focus on Audio Queue Services, the code examples in this document are sometimes simplified by using C++ classes from the Core Audio SDK. However, neither the SDK nor the C++ language is necessary to use Audio Queue Services.

_Audio Queue Services Programming Guide_ is useful to all iOS and Mac OS X developers who want a streamlined, straightforward way to record or play audio. To get the most from this document, you should be familiar with:

- The C programming language
- Using Xcode to build iOS or Mac OS X applications
- The terminology described in _[Core Audio Glossary](../Core%20Audio%20Glossary/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjt)_

This guide contains the following chapters:

- [About Audio Queues](About%20Audio%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnjnknltc) describes the capabilities, architecture, and internal workings of audio queues.
- [Recording Audio](Recording%20Audio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqnbnknltc) describes how to record audio.
- [Playing Audio](Playing%20Audio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbtfvbuqmznknltc) describes how to play audio.

You may find the following documents helpful:

- The companion document _[Audio Queue Services Reference](https://developer.apple.com/documentation/audiotoolbox/audio_queue_services)_ provides descriptions of the functions, callbacks, constants, and data types in Audio Queue Services.
- _[Core Audio Data Types Reference](https://developer.apple.com/documentation/coreaudio/core_audio_data_types)_ describes data types essential for using Audio Queue Services.
- _[Core Audio Overview](../Core%20Audio%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzx)_ provides a summary of the Core Audio frameworks, and includes an appendix on [Supported Audio File and Data Formats in OS X](https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/CoreAudioOverview/SupportedAudioFormatsMacOSX/SupportedAudioFormatsMacOSX.html#//apple_ref/doc/uid/TP40003577-CH7).
- _[Core Audio Glossary](../Core%20Audio%20Glossary/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjt)_ defines key terms used in the Core Audio documentation.
[Next](About%20Audio%20Queues.md)

