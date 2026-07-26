---
title: activeMicrophoneMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/activemicrophonemode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/activemicrophonemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/activemicrophonemode.json'
content_hash: 'sha256:40018c795e6ea236'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# activeMicrophoneMode

<sub>Type Property</sub>

The device’s active microphone mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var activeMicrophoneMode: AVCaptureDevice.MicrophoneMode { get }
```

## Discussion

The value may differ from the value of the [preferredMicrophoneMode](preferredmicrophonemode.md) property if the app’s active audio route doesn’t support the mode.

This property is key-value observable.

## See Also

### Inspecting the microphone mode

- [preferredMicrophoneMode](preferredmicrophonemode.md) — The microphone mode that the user selects in Control Center.
- [MicrophoneMode](microphonemode.md) — Constants that define the available microphone modes.
