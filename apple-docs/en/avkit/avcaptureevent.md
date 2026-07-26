---
title: AVCaptureEvent
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureevent
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureevent.json'
content_hash: 'sha256:b9319a88a78a5c2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVCaptureEvent

<sub>Class</sub>

An object that describes a user interaction with a system hardware button.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class AVCaptureEvent
```

## Overview

Inspect a capture event’s [phase](avcaptureevent/phase.md) to determine whether the event begins, ends, or is in a canceled state.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting the event

- [phase](avcaptureevent/phase.md) — The current phase of a capture event.
- [AVCaptureEventPhase](avcaptureeventphase.md) — Constants that indicate the phase of a system capture event.

### Playing a sound

- [shouldPlaySound](avcaptureevent/shouldplaysound.md) — A Boolean value that indicates whether you must play a sound manually.
- [- playSound:](<avcaptureevent/play(__).md>) — Plays the specified capture sound through AirPods.

## See Also

### iOS playback and capture

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md) — Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [AVPlayerViewController](avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVCaptureEventInteraction](avcaptureeventinteraction.md) — An object that registers handlers to respond to capture events from system hardware buttons.
- [AVCaptureEventSound](avcaptureeventsound.md) — A sound object for a capture event.
- [AVInputPickerInteraction](avinputpickerinteraction.md) — Use `AVInputPickerInteraction` to present an input picker.
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
