---
title: Audio Engine
framework: AVFAudio
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/audio-engine
source_url: 'https://developer.apple.com/documentation/avfaudio/audio-engine'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/audio-engine.json'
content_hash: 'sha256:e65eedfac68d154e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# Audio Engine

<sub>API Collection</sub>

Perform advanced real-time and offline audio processing, implement 3D spatialization, and work with MIDI and samplers.

## Overview

The audio engine provides a powerful, feature-rich API to simplify audio generation, processing, and input/output tasks. The engine contains a group of nodes that connect to form an audio signal processing chain. These nodes perform a variety of tasks on a signal before rendering to an output destination.

Audio Engine helps you achieve simple, as well as complex, audio processing tasks. With Audio Engine, your apps can:

- Play audio using files and buffers
- Capture audio at any point during the processing chain
- Add built-in effects like reverb, delay, distortion, and your custom effects
- Perform stereo and 3D mixing
- Provide MIDI playback and control over sampler instruments

## Topics

### Essentials

- [AVAudioEngine](avaudioengine.md) — An object that manages a graph of audio nodes, controls playback, and configures real-time rendering constraints.

### Nodes

- [AVAudioNode](avaudionode.md) — An object you use for audio generation, processing, or an I/O block.
- [AVAudioInputNode](avaudioinputnode.md) — An object that connects to the system’s audio input.
- [AVAudioOutputNode](avaudiooutputnode.md) — An object that connects to the system’s audio output.
- [AVAudioIONode](avaudioionode.md) — An object that performs audio input or output in the engine.

### Playback

- [Building an audio sequencer to arrange and play clips](building-an-audio-sequencer-to-arrange-and-play-clips.md) — Synchronize audio loops with a main tempo by creating a real-time clip launcher.
- [Playing custom audio with your own player](playing-custom-audio-with-your-own-player.md) — Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [Using voice processing](using-voice-processing.md) — Add voice-processing capabilities to your app by using audio engine.
- [AVAudioPlayerNode](avaudioplayernode.md) — An object for scheduling the playback of buffers or segments of audio files.

### MIDI

- [AVAudioSequencer](avaudiosequencer.md) — An object that plays audio from a collection of MIDI events the system organizes into music tracks.
- [AVAudioUnitSampler](avaudiounitsampler.md) — An object that you configure with one or more instrument samples, based on Apple’s Sampler audio unit.
- [AVMIDIEventListBlock](avmidieventlistblock.md) _(beta)_

### Mixing

- [AVAudioMixerNode](avaudiomixernode.md) — An object that takes any number of inputs and converts them into a single output.
- [AVAudioMixing](avaudiomixing.md) — A collection of properties that are applicable to the input bus of a mixer node.

### Effects

- [Creating custom audio effects](creating-custom-audio-effects.md) — Add custom audio-effect processing to apps like Logic Pro X and GarageBand by creating Audio Unit (AU) plug-ins.
- [Audio Units](audio-units.md) — The data type for a plug-in component that provides audio processing or audio data generation.

### Rendering

- [Building a signal generator](building-a-signal-generator.md) — Generate audio signals using an audio source node and a custom render callback.
- [Performing offline audio processing](performing-offline-audio-processing.md) — Add offline audio processing features to your app by enabling offline manual rendering mode.
- [AVAudioSourceNode](avaudiosourcenode.md) — An object that supplies audio data.
- [AVAudioSinkNode](avaudiosinknode.md) — An object that receives audio data.

### Conversion

- [AVAudioConverter](avaudioconverter.md) — An object that converts streams of audio between formats.

### Spatial audio

- [AVAudioEnvironmentNode](avaudioenvironmentnode.md) — An object that simulates a 3D audio environment.
- [AVAudioEnvironmentDistanceAttenuationParameters](avaudioenvironmentdistanceattenuationparameters.md) — An object that specifies the amount of attenuation distance, the gradual loss in audio intensity, and other characteristics.
- [AVAudioEnvironmentReverbParameters](avaudioenvironmentreverbparameters.md) — A class that encapsulates the parameters that you use to control the reverb of the environment node class.
- [AVAudio3DMixing](avaudio3dmixing.md) — A collection of properties that define 3D mixing properties.
- [AVAudio3DPoint](avaudio3dpoint.md) — A structure that represents a point in 3D space.
- [AVAudio3DVectorOrientation](avaudio3dvectororientation.md) — A structure that represents two orthogonal vectors that describe the orientation of the listener in 3D space.
- [AVAudio3DAngularOrientation](avaudio3dangularorientation.md) — A structure that represents the angular orientation of the listener in 3D space.
- [AVAudio3DMixingSourceMode](avaudio3dmixingsourcemode.md) — The source modes for the input bus of the audio environment node.
- [AVAudio3DMixingRenderingAlgorithm](avaudio3dmixingrenderingalgorithm.md) — The types of rendering algorithms available per input bus of the environment node.
- [AVAudioEnvironmentOutputType](avaudioenvironmentoutputtype.md) — The output types for using with the automatic 3D mixing rendering algorithm.
- [AVAudio3DMixingPointSourceInHeadMode](avaudio3dmixingpointsourceinheadmode.md) — The in-head modes for a point source.
- [AVAudio3DVector](avaudio3dvector.md) — A structure that represents a vector in 3D space, in degrees.

### Supporting data types

- [AVAudioBuffer](avaudiobuffer.md) — An object that represents a buffer of audio data with a format.
- [AVAudioPCMBuffer](avaudiopcmbuffer.md) — An object that represents an audio buffer you use with PCM audio formats.
- [AVReadOnlyAudioPCMBuffer](avreadonlyaudiopcmbuffer.md) — A read-only, Sendable audio buffer for safe concurrent access.
- [AVAudioFile](avaudiofile.md) — An object that represents an audio file that the system can open for reading or writing.
- [AVAudioTime](avaudiotime.md) — An object you use to represent a moment in time.
- [Audio settings](audio-settings.md) — Configure audio processing settings using standard key and value constants.
