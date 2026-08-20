---
title: Core Audio Overview
apple_id: TP40003577
resource_type: Guide
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/CoreAudioOverview/WhatsinCoreAudio/WhatsinCoreAudio.html
archived_at: '2026-07-15T08:18:03.355428Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Audio Overview](Introduction.md)


[Next](System-Supplied%20Audio%20Units%20in%20OS%20X.md)[Previous](Core%20Audio%20Frameworks.md)

# Core Audio Services

This chapter lists the services available in Core Audio. In iOS, you find these services arranged into the following frameworks:

- _Audio Toolbox_—Application-level services: files, streams, alerts, playback and recording. In iOS, includes audio session services.
- _Audio Unit_—Audio unit and audio codec services.
- _AVFoundation_—An Objective-C audio playback interface.
- _Core Audio_—Data types and, in OS X, hardware services.
- _OpenAL_—Positional and low-latency audio services.

Core Audio in OS X includes those frameworks and adds three more:

- _Core Audio Kit_—Audio unit user-interface services.
- _Core MIDI_—Application-level MIDI support.
- _Core MIDI Server_—MIDI server and driver support.

For a framework-focused view of the header files in Core Audio, see the Appendix [Core Audio Frameworks](Core%20Audio%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqojnknltc).

The rest of this chapter presents a services-focused view of Core Audio—starting with services available in both iOS and OS X.

The services listed in this section are available in iOS 2.0 and OS X v10.5.

Audio Converter Services allows you to convert data between formats. This interface consists of the functions, data types, and constants declared in the `AudioConverter.h` header file in `AudioToolbox.framework`.

Audio File services lets you read or write audio data to and from a file or buffer. You use it in conjunction with Audio Queue Services to record or play audio. In iOS and OS X, Audio File Services consists of the functions, data types, and constants declared in the `AudioFile.h` header file in `AudioToolbox.framework`.

Audio File Stream services lets you parse audio file streams—that is, audio data for which you don’t necessarily have access to the entire file. You can also use it to parse file data from disk, although Audio File Services is designed for that purpose.

Audio File Stream services returns audio data and metadata to your application via callbacks. which you typically then play back using Audio Queue Services. In iOS and OS X, Audio File Stream Services consists of the functions, data types, and constants declared in the `AudioFileStream.h` header file in `AudioToolbox.framework`.

Audio Format Services lets you work with audio data format information. Other services, such as Audio File Services, have functions for this use as well. You use Audio Format Services when all you want to do is obtain audio data format information. In OS X, you can also use this service to get system characteristics such as the available sample rates for encoding. Audio Format Services consists of the functions, data types, and constants declared in the `AudioFormat.h` header file in `AudioToolbox.framework`.

Audio Processing Graph Services lets you create and manipulate audio processing graphs in your application. In iOS and in OS X, it consists of the functions, data types, and constants declared in `AUGraph.h` header file in `AudioToolbox.framework`.

Audio Queue Services lets you play or record audio. It also lets you pause and resume playback, perform looping, and synchronize multiple channels of audio. In iOS and OS X, Audio Queue Services consists of the functions, data types, and constants declared in the `AudioQueue.h` header file in `AudioToolbox.framework`.

Audio Unit Services lets you load and use audio units in your application.

In iOS, Audio Unit Services comprises the functions, data types, and constants declared in the following header files in `AudioUnit.framework`:

- `AUComponent.h`
- `AudioComponent`.h (iOS only)
- `AudioOutputUnit.h`
- `AudioUnitParameters.h`
- `AudioUnitProperties.h`

OS X adds to these the following header files from `AudioUnit.framework` and `AudioToolbox.framework`:

- `AUCocoaUIView.h`
- `AudioUnitCarbonView.h`
- `AudioUnitUtilities.h` (in `AudioToolbox.framework`)
- `LogicAUProperties`.h
- `MusicDevice.h`

OpenAL is an open-source positional audio technology designed for use in game applications. iOS and OS X have implementations of the OpenAL 1.1 specification. You find its headers in the following header files in the OpenAL framework:

- al.h
- alc.h

In iOS you have these additional header files:

- `oalMacOSX_OALExtensions.h`
- `oalStaticBufferExtension.h`

In OS X you have this additional header file:

- `MacOSX_OALExtensions.h`

System Sound Services lets you play short sounds and alerts. On the iPhone, it lets you invoke vibration. System Sound Services consists of a subset of the functions, data types, and constants declared in the `AudioServices.h` header file in `AudioToolbox.framework`.

The services listed in this section are available in iOS only.

Audio Session Services lets you manage audio sessions in your application—coordinating the audio behavior in your application with background applications on an iPhone or iPod touch. Audio Session Services consists of a subset of the functions, data types, and constants declared in the `AudioServices.h` header file in `AudioToolbox.framework`.

The `AVAudioPlayer` class provides a simple Objective-C interface for playing sounds. If your application does not require stereo positioning or precise synchronization, and if you are not playing audio captured from a network stream, Apple recommends that you use this class for playback. This class is declared in the `AVAudioPlayer.h` header file in `AVFoundation.framework`.

The services listed in this section are available in OS X only.

Audio Codec Services allows you to convert data between formats. This interface consists of the functions, data types, and constants declared in the `AudioCodec.h` header file in `AudioUnit.framework`.

- `AudioCodec.h` (located in `AudioUnit.framework`).

Audio Hardware Services provides a small, lightweight interface to some of the important features of the Audio HAL (hardware abstraction layer). Audio Hardware Services consists of a subset of the functions, data types, and constants declared in the `AudioServices.h` header file in `AudioToolbox.framework`.

Core Audio Clock Services provides a reference clock that you can use to synchronize applications and devices. This service consists of the functions, data types, and constants declared in the `CoreAudioClock.h` header file in `AudioToolbox.framework`.

Core Audio in OS X supports MIDI through Core MIDI Services, which consists of the functions, data types, and constants declared in the following header files in `CoreMIDI.framework`:

- `MIDIServices.h`
- `MIDISetup.h`
- `MIDIThruConnection.h`
- `MIDIDriver.h`

Core MIDI Server Services lets MIDI drivers communicate with the OS X MIDI server. This interface consists of the functions, data types, and constants declared in the following header files in `CoreMIDIServer.framework`:

- `CoreMIDIServer.h`
- `MIDIDriver.h`

about extended audio file services

In many cases, you use Extended Audio File Services, which provides the simplest interface for reading and writing audio data. Files read using this API are automatically uncompressed and/or converted into linear PCM format, which is the native format for audio units. Similarly, you can use one function call to write linear PCM audio data to a file in a compressed or converted format. [Supported Audio File and Data Formats in OS X](Supported%20Audio%20File%20and%20Data%20Formats%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqnznknltc) lists the file formats that Core Audio supports by default. Some formats have restrictions; for example, by default, Core Audio can read, but not write, MP3 files.

Core Audio in OS X uses a hardware abstraction layer (HAL) to provide a consistent and predictable interface for applications to deal with hardware. Each piece of hardware is represented by an audio device object (type `AudioDevice`) in the HAL. Applications can query the audio device object to obtain timing information that can be used for synchronization or to adjust for latency.

HAL Services consists of the functions, data types, and constants declared in the following header files in `CoreAudio.framework`:

- `AudioDriverPlugin.h`
- `AudioHardware.h`
- `AudioHardwarePlugin.h`
- `CoreAudioTypes.h` (Contains data types and constants used by all Core Audio interfaces)
- `HostTime.h`

Most developers will find that Apple’s AUHAL unit serves their hardware interface needs, so they don’t have to interact directly with the HAL Services. The AUHAL is responsible for transmitting audio data, including any required channel mapping, to the specified audio device object. For more information about using the AUHAL unit and other output units, see [Interfacing with Hardware](Common%20Tasks%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzxfvbuqnrnknltcmq).

Music Player Services, available in OS X, allows you to arrange and play a collection of MIDI music tracks. It consists of the functions, data types, and constants declared in the header file `MusicPlayer.h` in `AudioToolbox.framework`.

[Next](System-Supplied%20Audio%20Units%20in%20OS%20X.md)[Previous](Core%20Audio%20Frameworks.md)

