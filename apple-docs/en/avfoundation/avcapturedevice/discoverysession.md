---
title: AVCaptureDevice.DiscoverySession
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/discoverysession
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/discoverysession.json'
content_hash: 'sha256:1613d526b9ce99b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.DiscoverySession

<sub>Class</sub>

An object that finds capture devices that match specific search criteria.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class DiscoverySession
```

## Overview

After creating a device discovery session, query its [devices](discoverysession/devices.md) property to find a device to use for capture. You can also key-value observe this property to monitor changes to the list of available devices.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Creating a session

- [+ discoverySessionWithDeviceTypes:mediaType:position:](<discoverysession/init(devicetypes_mediatype_position_).md>) — Creates a discovery session that finds devices that match the specified criteria.

### Finding devices

- [devices](discoverysession/devices.md) — A list of devices that match the search criteria of the discovery session.
- [supportedMultiCamDeviceSets](discoverysession/supportedmulticamdevicesets.md) — Sets of capture devices that you can use simultaneously in a multi-camera session.

## See Also

### Finding and monitoring devices

- [+ defaultDeviceWithDeviceType:mediaType:position:](<default(__for_position_).md>) — Returns the default device for the specified device type, media type, and position.
- [+ defaultDeviceWithMediaType:](<default(for_).md>) — Returns the default device that captures the specified media type.
- [+ deviceWithUniqueID:](<init(uniqueid_).md>) — Creates an object that represents a device with the specified identifier.
- [AVCaptureDeviceWasConnectedNotification](wasconnectednotification.md) — A notification the system posts when a new capture device becomes available.
- [AVCaptureDeviceWasDisconnectedNotification](wasdisconnectednotification.md) — A notification the system posts when an existing device becomes unavailable.
- [+ devicesWithMediaType:](<devices(for_).md>) — Returns devices capable of capturing media of the specified type. _(deprecated)_
- [+ devices](<devices().md>) — Returns all available capture devices on the system. _(deprecated)_
