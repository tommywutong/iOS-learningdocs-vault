---
title: AVContinuityDevice
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontinuitydevice
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontinuitydevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontinuitydevice.json'
content_hash: 'sha256:f42c941768b5481c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContinuityDevice

<sub>Class</sub>

A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.

<sub>tvOS</sub>

```swift
class AVContinuityDevice
```

## Overview

Each continuity device instance represents another iOS device that’s nearby. Your app can access the other device’s cameras and microphones with its [videoDevices](avcontinuitydevice/videodevices.md) and [audioSessionInputs](avcontinuitydevice/audiosessioninputs.md) properties, respectively.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Checking a continuity device’s availability

- [connected](avcontinuitydevice/isconnected.md) — A Boolean value that indicates whether you can use the continuity device because it’s connected to the system.

### Retrieving video devices from a continuity device

- [videoDevices](avcontinuitydevice/videodevices.md) — An array of the continuity device’s video-capture devices available to your app.

### Retrieving audio ports from a continuity device

- [audioSessionInputs](avcontinuitydevice/audiosessioninputs.md) — An array of the continuity device’s audio session port descriptions that’s available to your app.

### Identifying a continuity device

- [connectionID](avcontinuitydevice/connectionid.md) — A universally unique value that identifies a specific continuity device.

## See Also

### Capture devices

- [Choosing a capture device](choosing-a-capture-device.md) — Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md) — Capture the optimal shot by providing automatic framing recommendations.
- [AVCaptureDevice](avcapturedevice.md) — An object that represents a hardware or virtual capture device like a camera or microphone.
- [AVCaptureDeviceInput](avcapturedeviceinput.md) — An object that provides media input from a capture device to a capture session.
- [AVExternalStorageDevice](avexternalstoragedevice.md) — Represents a physical external storage device that stores media assets.
- [AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md) — Informs your app when the external storage devices connect to and disconnect from the system.
