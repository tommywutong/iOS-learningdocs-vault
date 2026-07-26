---
title: AVCaptureEventSound
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureeventsound
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureeventsound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureeventsound.json'
content_hash: 'sha256:6bd6484dc9499686'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVCaptureEventSound

<sub>Class</sub>

A sound object for a capture event.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class AVCaptureEventSound
```

## Overview

> [!important] Important
> To use AirPods Camera Control, it must be available in your country or region. AirPods Camera Control is not currently available in the European Union.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a sound

- [- initWithURL:error:](<avcaptureeventsound/init(url_)-2a6o4.md>) — Creates a sound object for a capture event.

### Accessing default sounds

- [cameraShutterSound](avcaptureeventsound/camerashutter.md) — The default sound for photo capture.
- [beginVideoRecordingSound](avcaptureeventsound/beginvideorecording.md) — The default sound for starting a video recording.
- [endVideoRecordingSound](avcaptureeventsound/endvideorecording.md) — The default sound for ending a video recording.

### Initializers

- [init(URL:)](<avcaptureeventsound/init(url_)-3e9o9.md>)

## See Also

### iOS playback and capture

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md) — Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [AVPlayerViewController](avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVCaptureEventInteraction](avcaptureeventinteraction.md) — An object that registers handlers to respond to capture events from system hardware buttons.
- [AVCaptureEvent](avcaptureevent.md) — An object that describes a user interaction with a system hardware button.
- [AVInputPickerInteraction](avinputpickerinteraction.md) — Use `AVInputPickerInteraction` to present an input picker.
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
