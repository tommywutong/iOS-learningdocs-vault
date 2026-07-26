---
title: wasDisconnectedNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/wasdisconnectednotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/wasdisconnectednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/wasdisconnectednotification.json'
content_hash: 'sha256:ef8975436cabf74b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# wasDisconnectedNotification

<sub>Type Property</sub>

A notification the system posts when an existing device becomes unavailable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let wasDisconnectedNotification: NSNotification.Name
```

## Discussion

The notification’s [object](../../foundation/notification/object.md) property contains the capture device that disconnected.

## See Also

### Finding and monitoring devices

- [DiscoverySession](discoverysession.md) — An object that finds capture devices that match specific search criteria.
- [+ defaultDeviceWithDeviceType:mediaType:position:](<default(__for_position_).md>) — Returns the default device for the specified device type, media type, and position.
- [+ defaultDeviceWithMediaType:](<default(for_).md>) — Returns the default device that captures the specified media type.
- [+ deviceWithUniqueID:](<init(uniqueid_).md>) — Creates an object that represents a device with the specified identifier.
- [AVCaptureDeviceWasConnectedNotification](wasconnectednotification.md) — A notification the system posts when a new capture device becomes available.
- [+ devicesWithMediaType:](<devices(for_).md>) — Returns devices capable of capturing media of the specified type. _(deprecated)_
- [+ devices](<devices().md>) — Returns all available capture devices on the system. _(deprecated)_
