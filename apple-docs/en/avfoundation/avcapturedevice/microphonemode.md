---
title: AVCaptureDevice.MicrophoneMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/microphonemode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/microphonemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/microphonemode.json'
content_hash: 'sha256:d50a9b072722edcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.MicrophoneMode

<sub>Enumeration</sub>

Constants that define the available microphone modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum MicrophoneMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Microphone modes

- [AVCaptureMicrophoneModeStandard](microphonemode/standard.md) — A mode that processes microphone audio with standard voice DSP.
- [AVCaptureMicrophoneModeWideSpectrum](microphonemode/widespectrum.md) — A mode that minimizes microphone audio processing to capture all sounds in the room.
- [AVCaptureMicrophoneModeVoiceIsolation](microphonemode/voiceisolation.md) — A mode that processes microphone audio to isolate the voice and attenuate other signals.

### Initializers

- [init(rawValue:)](<microphonemode/init(rawvalue_).md>)

## See Also

### Inspecting the microphone mode

- [activeMicrophoneMode](activemicrophonemode.md) — The device’s active microphone mode.
- [preferredMicrophoneMode](preferredmicrophonemode.md) — The microphone mode that the user selects in Control Center.
