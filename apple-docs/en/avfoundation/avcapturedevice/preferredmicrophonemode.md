---
title: preferredMicrophoneMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/preferredmicrophonemode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/preferredmicrophonemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/preferredmicrophonemode.json'
content_hash: 'sha256:256e061fe7b4c052'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# preferredMicrophoneMode

<sub>Type Property</sub>

The microphone mode that the user selects in Control Center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var preferredMicrophoneMode: AVCaptureDevice.MicrophoneMode { get }
```

## Discussion

Use key-value observing to monitor the user’s microphone mode selection.

## See Also

### Inspecting the microphone mode

- [activeMicrophoneMode](activemicrophonemode.md) — The device’s active microphone mode.
- [MicrophoneMode](microphonemode.md) — Constants that define the available microphone modes.
