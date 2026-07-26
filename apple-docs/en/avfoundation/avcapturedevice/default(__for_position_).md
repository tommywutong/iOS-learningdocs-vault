---
title: 'default(_:for:position:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/default(_:for:position:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/default(_:for:position:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/default%28_%3Afor%3Aposition%3A%29.json'
content_hash: 'sha256:be4e982a80c91da6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# default(_:for:position:)

<sub>Type Method</sub>

Returns the default device for the specified device type, media type, and position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func `default`(_ deviceType: AVCaptureDevice.DeviceType, for mediaType: AVMediaType?, position: AVCaptureDevice.Position) -> AVCaptureDevice?
```

## Parameters

- `deviceType` — The type of capture device to request, such as [AVCaptureDeviceTypeBuiltInWideAngleCamera](devicetype-swift.struct/builtinwideanglecamera.md).

- `mediaType` — The type of media to request capture of, such as [AVMediaTypeVideo](../avmediatype/video.md) or [AVMediaTypeAudio](../avmediatype/audio.md).

- `position` — The position of capture device to request relative to system hardware (front- or back-facing). Pass [AVCaptureDevicePositionUnspecified](position-swift.enum/unspecified.md) to search for devices regardless of position.

## Return Value

The default system device, or `nil` if no device currently exists that satisfies the specified criteria.

## Discussion

Use this method to select the system default capture device for a given scenario. For example, to obtain the dual camera on supported hardware and fall back to the standard wide-angle camera otherwise, call this method twice, as shown below.

```swift
// The app's default camera.
var defaultCamera: AVCaptureDevice? {
    // Find the built-in dual camera, if it exists.
    if let device = AVCaptureDevice.default(.builtInDualCamera,
                                            for: .video,
                                            position: .back) {
        return device
    }
    
    // Find the built-in wide-angle camera, if it exists.
    if let device = AVCaptureDevice.default(.builtInWideAngleCamera,
                                            for: .video,
                                            position: .back) {
        return device
    }
    return nil
}
```

## See Also

### Finding and monitoring devices

- [DiscoverySession](discoverysession.md) — An object that finds capture devices that match specific search criteria.
- [+ defaultDeviceWithMediaType:](<default(for_).md>) — Returns the default device that captures the specified media type.
- [+ deviceWithUniqueID:](<init(uniqueid_).md>) — Creates an object that represents a device with the specified identifier.
- [AVCaptureDeviceWasConnectedNotification](wasconnectednotification.md) — A notification the system posts when a new capture device becomes available.
- [AVCaptureDeviceWasDisconnectedNotification](wasdisconnectednotification.md) — A notification the system posts when an existing device becomes unavailable.
- [+ devicesWithMediaType:](<devices(for_).md>) — Returns devices capable of capturing media of the specified type. _(deprecated)_
- [+ devices](<devices().md>) — Returns all available capture devices on the system. _(deprecated)_
