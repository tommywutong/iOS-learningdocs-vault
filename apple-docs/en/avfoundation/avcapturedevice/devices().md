---
title: devices()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturedevice/devices()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devices()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devices%28%29.json'
content_hash: 'sha256:adbe74bf095d191e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# devices()

<sub>Type Method</sub>

Returns all available capture devices on the system.

> [!warning] Deprecated
> Use the [DiscoverySession](discoverysession.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class func devices() -> [AVCaptureDevice]
```

## Return Value

An array of available devices.

## See Also

### Finding and monitoring devices

- [DiscoverySession](discoverysession.md) — An object that finds capture devices that match specific search criteria.
- [+ defaultDeviceWithDeviceType:mediaType:position:](<default(__for_position_).md>) — Returns the default device for the specified device type, media type, and position.
- [+ defaultDeviceWithMediaType:](<default(for_).md>) — Returns the default device that captures the specified media type.
- [+ deviceWithUniqueID:](<init(uniqueid_).md>) — Creates an object that represents a device with the specified identifier.
- [AVCaptureDeviceWasConnectedNotification](wasconnectednotification.md) — A notification the system posts when a new capture device becomes available.
- [AVCaptureDeviceWasDisconnectedNotification](wasdisconnectednotification.md) — A notification the system posts when an existing device becomes unavailable.
- [+ devicesWithMediaType:](<devices(for_).md>) — Returns devices capable of capturing media of the specified type. _(deprecated)_
