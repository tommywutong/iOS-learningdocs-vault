---
title: AVExternalStorageDevice
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalstoragedevice
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalstoragedevice.json'
content_hash: 'sha256:c000822f5e57b587'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVExternalStorageDevice

<sub>Class</sub>

Represents a physical external storage device that stores media assets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVExternalStorageDevice
```

## Overview

Each storage device instance corresponds to a physical external storage device where the system can media assets. You can access all of the currently available external storage devices with the [AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md) object’s [externalStorageDevices](avexternalstoragedevicediscoverysession/externalstoragedevices.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Checking permission to generate URLs

- [authorizationStatus](avexternalstoragedevice/authorizationstatus.md) — Your app’s authorization status for the external storage device.

### Requesting permission to generate URLs

- [+ requestAccessWithCompletionHandler:](<avexternalstoragedevice/requestaccess(completionhandler_).md>) — Requests access to an external storage device on behalf of your app, which can present a dialog to a person on their device’s display.

### Generating URLs for image assets

- [- nextAvailableURLsWithPathExtensions:error:](<avexternalstoragedevice/nextavailableurls(withpathextensions_).md>) — Generates an array of security scoped URLs that are compliant for digital camera formats, where each element has a different path extension.

### Inspecting a storage device

- [connected](avexternalstoragedevice/isconnected.md) — A Boolean value that indicates whether the system has a connection to the external storage device.
- [displayName](avexternalstoragedevice/displayname.md) — The name of an external storage device that’s appropriate for a user interface.
- [uuid](avexternalstoragedevice/uuid.md) — The external storage device’s unique identifier.
- [freeSize](avexternalstoragedevice/freesize.md) — The amount of free storage space, in bytes, that’s available on the external storage device.
- [totalSize](avexternalstoragedevice/totalsize.md) — The total amount of storage space, in bytes, that’s available on the external storage device.
- [notRecommendedForCaptureUse](avexternalstoragedevice/isnotrecommendedforcaptureuse.md) — A Boolean value that indicates whether the external storage device is suitable for camera capture. _(deprecated)_
- [reasonsNotRecommendedForCaptureUse](avexternalstoragedevice/reasonsnotrecommendedforcaptureuse.md) _(beta)_
- [ReasonNotRecommendedForCaptureUse](avexternalstoragedevice/reasonnotrecommendedforcaptureuse.md) _(beta)_

## See Also

### Capture devices

- [Choosing a capture device](choosing-a-capture-device.md) — Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md) — Capture the optimal shot by providing automatic framing recommendations.
- [AVCaptureDevice](avcapturedevice.md) — An object that represents a hardware or virtual capture device like a camera or microphone.
- [AVCaptureDeviceInput](avcapturedeviceinput.md) — An object that provides media input from a capture device to a capture session.
- [AVContinuityDevice](avcontinuitydevice.md) — A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md) — Informs your app when the external storage devices connect to and disconnect from the system.
