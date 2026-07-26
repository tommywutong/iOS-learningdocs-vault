---
title: microphone
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct/microphone
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/microphone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/microphone.json'
content_hash: 'sha256:ecdfe9784d2b4a39'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DeviceType](../devicetype-swift.struct.md)

# microphone

<sub>Type Property</sub>

A microphone device type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
static let microphone: AVCaptureDevice.DeviceType
```

## Discussion

In iOS and tvOS, the system only exposes one capture device of this type. The audio routing subsystem decides which physical microphone to use, be it a built-in microphone, a wired headset, or an external microphone. The microphone device’s [localizedName](../localizedname.md) changes as the audio subsystem switches to a different physical device.

## See Also

### Microphones

- [AVCaptureDeviceTypeBuiltInMicrophone](builtinmicrophone.md) — A built-in microphone. _(deprecated)_
