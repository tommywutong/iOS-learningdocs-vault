---
title: Audio Unit Programming Guide
apple_id: TP40003278
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioUnitProgrammingGuide/AQuickTouroftheCoreAudioSDK/AQuickTouroftheCoreAudioSDK.html
archived_at: '2026-07-15T08:17:21.124061Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Unit Programming Guide](Introduction.md)


[Next](Tutorial-%20Building%20a%20Simple%20Effect%20Unit%20with%20a%20Generic%20View.md)[Previous](The%20Audio%20Unit%20View.md)

# A Quick Tour of the Core Audio SDK

You can build an audio unit from scratch using the Core Audio frameworks directly. However, as described throughout this document, Apple strongly encourages you to begin with the freely downloadable Core Audio software development kit, or SDK. Apple builds all of the audio units that ship in OS X using the SDK.

The SDK offers many advantages to audio unit developers. The SDK:

- Insulates you from almost all the complexity in dealing with the OS X Component Manager
- Greatly simplifies development effort with a rich C++ class hierarchy. In many cases, you can create audio units with a few method overrides. This lets you build full-featured, commercial quality audio units without directly calling any of the APIs in the Core Audio frameworks.
- Provides a straightforward starting point with Xcode audio unit project templates.

Install the most recent Core Audio SDK. It is part of the Xcode Tools installation on the OS X DVD. You can also download it from Apple’s developer website at this location:

[http://developer.apple.com/sdk/](https://developer.apple.com/sdk/)

The Core Audio team updates the SDK frequently so be sure that you’re using the most current version.

The installer package places the SDK in a folder named `CoreAudio` at the path:

`/Developer/Examples/CoreAudio/` on your startup volume.

The Core Audio SDK contains materials for working with audio units, audio files, codecs, MIDI, and the HAL. The `ReadMe.rtf` file within the `CoreAudio` folder helps you get oriented. It includes a commented listing of the folders in the SDK, pointers to related resources from the Core Audio team, and release notes.

For audio unit development, the most important parts of the SDK are in the following folders:

- `AudioUnits`
- `PublicUtility`
- `Services`

This section describes each of these folders in turn.

The `AudioUnits` folder contains the C++ class hierarchy that you use to build audio units. This is in the `AudioUnits/AUPublic` folder. The audio unit Xcode templates depend on this class hierarchy.

The `AudioUnits/CarbonGenericView` folder contains the source files for the Carbon generic view.

Host developers find the interfaces for Apple’s Cocoa generic view not in the Core Audio SDK but in OS X’s `CoreAudioKit` framework.

In addition to the `AUPublic` and `CarbonGenericView` source folders, the `AudioUnits` folder contains several complete example Xcode projects for audio units. You can use these projects in a variety of ways:

- Directly using the the audio units built by these projects
- Studying the source code to gain insight into how to design and implement audio units
- Using the projects as starting points for your own audio units

The SDK includes the following example audio unit projects:

- The DiagnosticAUs project builds three audio units that you may find useful for troubleshooting and analysis as you’re developing your audio units:

  - AUValidSamples detects samples passing through it that are out of range or otherwise invalid. You can choose this audio unit from the Apple_DEBUG group in an audio unit host such as AU Lab.
  - AUDebugDispatcher facilitates audio unit debugging. You can choose this audio unit from the Acme Inc group in an audio unit host such as AU Lab.
  - AUPulseDetector measures latency in host applications
- The FilterDemo project builds a basic resonant low-pass filter with a custom view.
- The MultitapDelayAU project builds a multi-tap delay with a custom view.
- The SampleAUs project builds a pass-through audio unit that includes presets and a variety of parameter types.
- The SinSynth project builds a simple instrument unit that you can use in a host application like GarageBand.

This folder contains a miscellaneous collection of C++ and Objective-C source files used by the Core Audio SDK’s audio unit class hierarchy and by the sample projects in the SDK. You may want to examine these files to gain insight into how the class hierarchy works.

This folder contains several Core Audio Xcode projects that build tools, audio units, and audio unit host applications. As with the projects in the `AudioUnits` folder, you can make use of these projects during audio unit development in a variety of ways:

- Directly using the the tools, audio units, and host applications built by these projects
- Studying the source code to gain insight into how Core Audio works, as well as insight into how to design and implement tools, audio units, and host applications
- Using the projects as starting points for your own tools, audio units, and host applications

The Services folder contains the following Xcode projects:

**AudioFileTools**
: A project that builds a set of eight command-line tools for playing, recording, examining, and manipulating audio files.

**AudioUnitHosting**
: A project that builds a Carbon-based audio unit host application. Useful in terms of sample code for host developers but deprecated as a host for testing your audio units. (For audio unit testing, use AU Lab.)

**AUMixer3DTest**
: A project that builds an application that uses a 3D mixer audio unit.

**AUViewTest**
: A project that builds a windowless application based on an audio processing graph. The graph includes an instrument unit, an effect unit, and an output unit. There’s a menu item to open a view for the effect unit. The AUViewTest application uses a music player object to play a repeating sequence through the instrument unit.

**CocoaAUHost**
: A project that builds a Cocoa-based audio unit host application. This project is useful in terms of sample code for host developers but deprecated as a host for testing your audio units. (For audio unit testing, use AU Lab.)

**MatrixMixerTest**
: A project that builds an example mixer unit with a custom Cocoa view.

**OpenALExample**
: A project that builds an application based on the OpenAL API with Apple extensions. The application demonstrates control of listener position and orientation within a two-dimensional layout of audio sources.

[Next](Tutorial-%20Building%20a%20Simple%20Effect%20Unit%20with%20a%20Generic%20View.md)[Previous](The%20Audio%20Unit%20View.md)

