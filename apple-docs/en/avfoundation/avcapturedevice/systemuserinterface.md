---
title: AVCaptureDevice.SystemUserInterface
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systemuserinterface
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systemuserinterface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systemuserinterface.json'
content_hash: 'sha256:a18c27d9cb806740'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.SystemUserInterface

<sub>Enumeration</sub>

Constants that describe the capture device configuration user interfaces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum SystemUserInterface
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### User interfaces

- [AVCaptureSystemUserInterfaceVideoEffects](systemuserinterface/videoeffects.md) — The system user interface for changing the state of video effects.
- [AVCaptureSystemUserInterfaceMicrophoneModes](systemuserinterface/microphonemodes.md) — The system user interface for selecting microphone modes.

### Initializers

- [init(rawValue:)](<systemuserinterface/init(rawvalue_).md>)

## See Also

### Presenting the configuration user interface

- [+ showSystemUserInterface:](<showsystemuserinterface(__).md>) — Displays the system’s user interface to configure video effects or microphone modes.
