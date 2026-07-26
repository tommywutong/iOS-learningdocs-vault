---
title: sourceDevicePosition
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureinput/port/sourcedeviceposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/sourcedeviceposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureinput/port/sourcedeviceposition.json'
content_hash: 'sha256:0031bf33965ff5e2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureInput](../../avcaptureinput.md) · [Port](../port.md)

# sourceDevicePosition

<sub>Instance Property</sub>

The position of the source device providing input through this port.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var sourceDevicePosition: AVCaptureDevice.Position { get }
```

## Discussion

All ports contained in an [AVCaptureInput](../../avcaptureinput.md) object’s [ports](../ports.md) array have the same [sourceDevicePosition](sourcedeviceposition.md) value.

When working with a microphone input in an [AVCaptureMultiCamSession](../../avcapturemulticamsession.md), it’s possible to record multiple microphone directions simultaneously. For example, you can record audio from the front microphone input to pair with video from the front camera, and record audio from the back microphone input to pair with video from the back camera.

By calling the input’s [- portsWithMediaType:sourceDeviceType:sourceDevicePosition:](<../../avcapturedeviceinput/ports(for_sourcedevicetype_sourcedeviceposition_).md>) method, you may discover additional hidden ports originating from the source audio device. These ports represent individual microphones positioned to pick up audio from one particular direction.

```swift
// Find the audio port that captures omnidirectional audio.
let omniAudioPort = audioDeviceInput.ports(for: .audio,
                                           sourceDeviceType: .builtInMicrophone,
                                           sourceDevicePosition: .unspecified).first

// Find the audio port that captures front audio.
let frontAudioPort = audioDeviceInput.ports(for: .audio,
                                            sourceDeviceType: .builtInMicrophone,
                                            sourceDevicePosition: .front).first

// Find the audio port that captures back audio.
let backAudioPort = audioDeviceInput.ports(for: .audio,
                                           sourceDeviceType: .builtInMicrophone,
                                           sourceDevicePosition: .back).first
```

## See Also

### Inspecting an input port

- [enabled](isenabled.md) — A Boolean value that indicates whether the port is in an enabled state.
- [mediaType](mediatype.md) — The media type of the port.
- [formatDescription](formatdescription.md) — A description of the port format.
- [sourceDeviceType](sourcedevicetype.md) — The device type of the source camera that provides data to the port.
- [clock](clock.md) — An object that represents the capture device’s clock.
