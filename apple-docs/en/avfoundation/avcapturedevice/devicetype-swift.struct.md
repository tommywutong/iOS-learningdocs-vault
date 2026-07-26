---
title: AVCaptureDevice.DeviceType
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct.json'
content_hash: 'sha256:5ab9432a67f9b672'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.DeviceType

<sub>Structure</sub>

A structure that defines the device types the framework supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct DeviceType
```

## Discussion

Use the device type constants to retrieve devices using an [DiscoverySession](discoverysession.md) object, or when calling the [+ defaultDeviceWithDeviceType:mediaType:position:](<default(__for_position_).md>) method.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Cameras

- [AVCaptureDeviceTypeBuiltInWideAngleCamera](devicetype-swift.struct/builtinwideanglecamera.md) — A built-in wide-angle camera device type.
- [AVCaptureDeviceTypeBuiltInUltraWideCamera](devicetype-swift.struct/builtinultrawidecamera.md) — A built-in camera device type with a shorter focal length than a wide-angle camera.
- [AVCaptureDeviceTypeBuiltInTelephotoCamera](devicetype-swift.struct/builtintelephotocamera.md) — A built-in camera device type with a longer focal length than a wide-angle camera.
- [AVCaptureDeviceTypeBuiltInDualCamera](devicetype-swift.struct/builtindualcamera.md) — A built-in camera device type that consists of a wide-angle and telephoto camera.
- [AVCaptureDeviceTypeBuiltInDualWideCamera](devicetype-swift.struct/builtindualwidecamera.md) — A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [AVCaptureDeviceTypeBuiltInTripleCamera](devicetype-swift.struct/builtintriplecamera.md) — A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [AVCaptureDeviceTypeContinuityCamera](devicetype-swift.struct/continuitycamera.md) — A Continuity Camera device type.
- [AVCaptureDeviceTypeBuiltInDuoCamera](devicetype-swift.struct/builtinduocamera.md) — A built-in dual camera device type. _(deprecated)_

### Microphones

- [AVCaptureDeviceTypeMicrophone](devicetype-swift.struct/microphone.md) — A microphone device type.
- [AVCaptureDeviceTypeBuiltInMicrophone](devicetype-swift.struct/builtinmicrophone.md) — A built-in microphone. _(deprecated)_

### External devices

- [AVCaptureDeviceTypeExternal](devicetype-swift.struct/external.md) — An external device type.
- [AVCaptureDeviceTypeExternalUnknown](devicetype-swift.struct/externalunknown.md) — An unknown external device type. _(deprecated)_

### Desk View

- [AVCaptureDeviceTypeDeskViewCamera](devicetype-swift.struct/deskviewcamera.md) — A virtual overhead camera that captures a user’s desk.

### Depth sensing

- [AVCaptureDeviceTypeBuiltInLiDARDepthCamera](devicetype-swift.struct/builtinlidardepthcamera.md) — A device that consists of two cameras, one LiDAR and one YUV.
- [AVCaptureDeviceTypeBuiltInTrueDepthCamera](devicetype-swift.struct/builtintruedepthcamera.md) — A device that consists of two cameras, one Infrared and one YUV.

### Initializers

- [init(rawValue:)](<devicetype-swift.struct/init(rawvalue_).md>) — Creates a capture device type with a string value.

## See Also

### Identifying a device

- [uniqueID](uniqueid.md) — An identifier that uniquely identifies the device.
- [modelID](modelid.md) — A model identifier for the device.
- [localizedName](localizedname.md) — A localized device name for display in the user interface.
- [manufacturer](manufacturer.md) — A human-readable string for the manufacturer of the device.
- [deviceType](devicetype-swift.property.md) — The type of device, such as a built-in microphone or wide-angle camera.
- [position](position-swift.property.md) — The physical position of the capture device hardware.
- [Position](position-swift.enum.md) — Constants that indicate the physical position of a capture device.
