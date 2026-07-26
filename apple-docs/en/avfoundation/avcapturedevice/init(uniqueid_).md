---
title: 'init(uniqueID:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/init(uniqueid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/init(uniqueid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/init%28uniqueid%3A%29.json'
content_hash: 'sha256:52b967eb0aab425d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# init(uniqueID:)

<sub>Initializer</sub>

Creates an object that represents a device with the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(uniqueID deviceUniqueID: String)
```

## Parameters

- `deviceUniqueID` — An identifier that uniquely identifies the device.

## Return Value

A capture device, or `nil` if no device with the specified identifier exists.

## Discussion

Every capture device has a unique identifier that persists on a system across device connections, app restarts, and reboots of the system itself.

## See Also

### Finding and monitoring devices

- [DiscoverySession](discoverysession.md) — An object that finds capture devices that match specific search criteria.
- [+ defaultDeviceWithDeviceType:mediaType:position:](<default(__for_position_).md>) — Returns the default device for the specified device type, media type, and position.
- [+ defaultDeviceWithMediaType:](<default(for_).md>) — Returns the default device that captures the specified media type.
- [AVCaptureDeviceWasConnectedNotification](wasconnectednotification.md) — A notification the system posts when a new capture device becomes available.
- [AVCaptureDeviceWasDisconnectedNotification](wasdisconnectednotification.md) — A notification the system posts when an existing device becomes unavailable.
- [+ devicesWithMediaType:](<devices(for_).md>) — Returns devices capable of capturing media of the specified type. _(deprecated)_
- [+ devices](<devices().md>) — Returns all available capture devices on the system. _(deprecated)_
