---
title: AVSpeechSynthesisProviderAudioUnit
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avspeechsynthesisprovideraudiounit
source_url: 'https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovideraudiounit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avspeechsynthesisprovideraudiounit.json'
content_hash: 'sha256:077369b78b69d778'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVSpeechSynthesisProviderAudioUnit

<sub>Class</sub>

An object that generates speech from text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVSpeechSynthesisProviderAudioUnit
```

## Overview

Use a speech synthesizer audio unit to generate audio buffers that contain speech for a given voice and speech markup. The audio unit receives an [AVSpeechSynthesisProviderRequest](avspeechsynthesisproviderrequest.md) as input, and extracts audio buffers through the render block.

Use [speechSynthesisOutputMetadataBlock](avspeechsynthesisprovideraudiounit/speechsynthesisoutputmetadatablock.md) to provide metadata as an array of [AVSpeechSynthesisMarker](avspeechsynthesismarker.md).

The system scans and loads voices for audio unit extensions of this type, and the voices it provides are available for use in [AVSpeechSynthesizer](avspeechsynthesizer.md) and accessibility technologies like VoiceOver and Speak Screen.

> [!important] Important
> Network access isn’t allowed in speech synthesizers.

## Relationships

- **Inherits From**: [AUAudioUnit](../audiotoolbox/auaudiounit.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Rendering speech

- [- synthesizeSpeechRequest:](<avspeechsynthesisprovideraudiounit/synthesizespeechrequest(__).md>) — Sets the text to synthesize and the voice to use.
- [AVSpeechSynthesisProviderRequest](avspeechsynthesisproviderrequest.md) — An object that represents the text to synthesize and the voice to use.

### Supplying metadata

- [AVSpeechSynthesisProviderOutputBlock](avspeechsynthesisprovideroutputblock.md) — A type that represents the method for sending marker information to the host.
- [speechSynthesisOutputMetadataBlock](avspeechsynthesisprovideraudiounit/speechsynthesisoutputmetadatablock.md) — A block that subclasses use to send marker information to the host.
- [AVSpeechSynthesisMarker](avspeechsynthesismarker.md) — An object that contains information about the synthesized audio.

### Getting and setting voices

- [speechVoices](avspeechsynthesisprovideraudiounit/speechvoices.md) — A list of voices the audio unit provides to the system.
- [AVSpeechSynthesisProviderVoice](avspeechsynthesisprovidervoice.md) — An object that represents a voice that an audio unit provides to its host.

### Cancelling a request

- [- cancelSpeechRequest](<avspeechsynthesisprovideraudiounit/cancelspeechrequest().md>) — Informs the audio unit to discard the speech request.
