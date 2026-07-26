---
title: AVInputPickerInteraction
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinputpickerinteraction
source_url: 'https://developer.apple.com/documentation/avkit/avinputpickerinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinputpickerinteraction.json'
content_hash: 'sha256:b41b075b9a9d00a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVInputPickerInteraction

<sub>Class</sub>

Use `AVInputPickerInteraction` to present an input picker.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class AVInputPickerInteraction
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](../uikit/uiinteraction.md)

## Topics

### Creating an input picker

- [- init](<avinputpickerinteraction/init().md>) — Creates a new instance of AVInputPickerController using a default sharedInstance from `AVAudioSession`.
- [- initWithAudioSession:](<avinputpickerinteraction/init(audiosession_).md>) — Creates a new instance of AVInputPickerInteraction using a specific `AVAudioSession`.

### Managing presentation

- [presented](avinputpickerinteraction/ispresented.md) — A Boolean value that indicates whether the picker is currently visible.
- [- present](<avinputpickerinteraction/present().md>) — Presents the input picker.
- [- dismiss](<avinputpickerinteraction/dismiss().md>) — Dismisses the input picker.

### Setting the delegate

- [delegate](avinputpickerinteraction/delegate-swift.property.md) — The input picker view’s delegate.
- [Delegate](avinputpickerinteraction/delegate-swift.protocol.md) — The `AVInputPickerInteractionDelegate` protocol defines methods you use to receive notifications about transitions in an `AVInputPickerInteraction` object.

### Accessing the audio session

- [audioSession](avinputpickerinteraction/audiosession.md) — The audio session for the picker.

## See Also

### iOS playback and capture

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md) — Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [AVPlayerViewController](avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVCaptureEventInteraction](avcaptureeventinteraction.md) — An object that registers handlers to respond to capture events from system hardware buttons.
- [AVCaptureEvent](avcaptureevent.md) — An object that describes a user interaction with a system hardware button.
- [AVCaptureEventSound](avcaptureeventsound.md) — A sound object for a capture event.
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
