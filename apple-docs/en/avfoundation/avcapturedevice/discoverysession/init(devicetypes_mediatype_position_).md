---
title: 'init(deviceTypes:mediaType:position:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/discoverysession/init(devicetypes:mediatype:position:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession/init(devicetypes:mediatype:position:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/discoverysession/init%28devicetypes%3Amediatype%3Aposition%3A%29.json'
content_hash: 'sha256:a549da1001cdb5d1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DiscoverySession](../discoverysession.md)

# init(deviceTypes:mediaType:position:)

<sub>Initializer</sub>

Creates a discovery session that finds devices that match the specified criteria.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(deviceTypes: [AVCaptureDevice.DeviceType], mediaType: AVMediaType?, position: AVCaptureDevice.Position)
```

## Parameters

- `deviceTypes` — A list of device types to search for, such as [AVCaptureDeviceTypeBuiltInWideAngleCamera](../devicetype-swift.struct/builtinwideanglecamera.md) and [AVCaptureDeviceTypeBuiltInMicrophone](../devicetype-swift.struct/builtinmicrophone.md). The array must contain at least one valid [DeviceType](../devicetype-swift.struct.md) value.

- `mediaType` — The media type to capture, such as [AVMediaTypeVideo](../../avmediatype/video.md) or [AVMediaTypeAudio](../../avmediatype/audio.md). Pass `nil` to search for devices regardless of supported media types.

- `position` — The position of capture device to search for, relative to system hardware (front- or back-facing). Pass [AVCaptureDevicePositionUnspecified](../position-swift.enum/unspecified.md) to search for devices regardless of position.

## Return Value

A new discovery session.

## Discussion

After creating a discovery session, query its [devices](devices.md) property to examine matching devices and choose one for capture.
