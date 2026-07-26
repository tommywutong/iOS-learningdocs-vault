---
title: AVExternalStorageDeviceDiscoverySession
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalstoragedevicediscoverysession
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevicediscoverysession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevicediscoverysession.json'
content_hash: 'sha256:93bfc6d2580c779f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVExternalStorageDeviceDiscoverySession

<sub>Class</sub>

Informs your app when the external storage devices connect to and disconnect from the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVExternalStorageDeviceDiscoverySession
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Checking for session support on a device

- [supported](avexternalstoragedevicediscoverysession/issupported.md) — A Boolean value that indicates whether the system supports external storage devices.

### Retrieving the shared device discovery session instance

- [sharedSession](avexternalstoragedevicediscoverysession/shared.md) — The system’s singleton device discovery session instance.

### Monitoring for storage device updates

- [externalStorageDevices](avexternalstoragedevicediscoverysession/externalstoragedevices.md) — An array of external storage devices the session updates as individual devices connect or disconnect from the system.

## See Also

### Capture devices

- [Choosing a capture device](choosing-a-capture-device.md) — Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md) — Capture the optimal shot by providing automatic framing recommendations.
- [AVCaptureDevice](avcapturedevice.md) — An object that represents a hardware or virtual capture device like a camera or microphone.
- [AVCaptureDeviceInput](avcapturedeviceinput.md) — An object that provides media input from a capture device to a capture session.
- [AVContinuityDevice](avcontinuitydevice.md) — A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [AVExternalStorageDevice](avexternalstoragedevice.md) — Represents a physical external storage device that stores media assets.
