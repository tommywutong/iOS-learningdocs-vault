---
title: AVCaptureDeviceInput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput.json'
content_hash: 'sha256:450a71f0ae83e613'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureDeviceInput

<sub>Class</sub>

An object that provides media input from a capture device to a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVCaptureDeviceInput
```

## Overview

This class is a concrete subclass of [AVCaptureInput](avcaptureinput.md) that you use to connect a capture device to a capture session.

## Relationships

- **Inherits From**: [AVCaptureInput](avcaptureinput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an input

- [- initWithDevice:error:](<avcapturedeviceinput/init(device_).md>) — Creates an input for the specified capture device.

### Configuring video properties

- [unifiedAutoExposureDefaultsEnabled](avcapturedeviceinput/unifiedautoexposuredefaultsenabled.md) — A Boolean value that indicates whether the input enables unified auto-exposure defaults.
- [videoMinFrameDurationOverride](avcapturedeviceinput/videominframedurationoverride.md) — A time value that acts as a modifier to a capture device’s active video minimum frame duration.

### Configuring audio properties

- [- isMultichannelAudioModeSupported:](<avcapturedeviceinput/ismultichannelaudiomodesupported(__).md>) — A Boolean value that indicates whether the input supports the specified multichannel audio mode.
- [multichannelAudioMode](avcapturedeviceinput/multichannelaudiomode.md) — The multichannel audio mode to apply when recording audio.
- [AVCaptureMultichannelAudioMode](avcapturemultichannelaudiomode.md) — Constants that indicate the modes of multichannel audio.
- [windNoiseRemovalSupported](avcapturedeviceinput/iswindnoiseremovalsupported.md)
- [windNoiseRemovalEnabled](avcapturedeviceinput/iswindnoiseremovalenabled.md)

### Configuring Cinematic video capture

- [cinematicVideoCaptureSupported](avcapturedeviceinput/iscinematicvideocapturesupported.md) — A BOOL value specifying whether Cinematic Video capture is supported.
- [cinematicVideoCaptureEnabled](avcapturedeviceinput/iscinematicvideocaptureenabled.md) — A BOOL value specifying whether the Cinematic Video effect is being applied to any movie file output, video data output, metadata output, or video preview layer added to the capture session.
- [simulatedAperture](avcapturedeviceinput/simulatedaperture.md) — Shallow depth of field simulated aperture.

### Locking frame duration

- [activeLockedVideoFrameDuration](avcapturedeviceinput/activelockedvideoframeduration.md) — The receiver’s locked frame duration (the reciprocal of its frame rate). Setting this property guarantees the intra-frame duration delivered by the device input is precisely the frame duration you request.
- [lockedVideoFrameDurationSupported](avcapturedeviceinput/islockedvideoframedurationsupported.md) — Indicates whether the device input supports locked frame durations.

### Synchronizing with external devices

- [externalSyncSupported](avcapturedeviceinput/isexternalsyncsupported.md) — Indicates whether the device input supports being configured to follow an external sync device.
- [- followExternalSyncDevice:videoFrameDuration:delegate:](<avcapturedeviceinput/follow(__videoframeduration_delegate_).md>) — Configures the the device input to follow an external sync device at the given frame duration.
- [- unfollowExternalSyncDevice](<avcapturedeviceinput/unfollowexternalsyncdevice().md>) — Discontinues external sync.
- [activeExternalSyncVideoFrameDuration](avcapturedeviceinput/activeexternalsyncvideoframeduration.md) — The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
- [externalSyncDevice](avcapturedeviceinput/externalsyncdevice.md) — The external sync device currently being followed by this input.

### Accessing the device

- [device](avcapturedeviceinput/device.md) — A capture device associated with this input.
- [- portsWithMediaType:sourceDeviceType:sourceDevicePosition:](<avcapturedeviceinput/ports(for_sourcedevicetype_sourcedeviceposition_).md>) — Retrieves a virtual device’s constituent device ports for use in a multi-camera session.

### Instance Properties

- [audioZoomEnabled](avcapturedeviceinput/isaudiozoomenabled.md) — Whether or not audio zoom is enabled.
- [audioZoomSupported](avcapturedeviceinput/isaudiozoomsupported.md) — Whether or not audio zoom is supported.

## See Also

### Capture devices

- [Choosing a capture device](choosing-a-capture-device.md) — Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md) — Capture the optimal shot by providing automatic framing recommendations.
- [AVCaptureDevice](avcapturedevice.md) — An object that represents a hardware or virtual capture device like a camera or microphone.
- [AVContinuityDevice](avcontinuitydevice.md) — A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [AVExternalStorageDevice](avexternalstoragedevice.md) — Represents a physical external storage device that stores media assets.
- [AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md) — Informs your app when the external storage devices connect to and disconnect from the system.
