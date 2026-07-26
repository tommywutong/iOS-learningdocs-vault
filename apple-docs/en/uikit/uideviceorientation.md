---
title: UIDeviceOrientation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uideviceorientation
source_url: 'https://developer.apple.com/documentation/uikit/uideviceorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uideviceorientation.json'
content_hash: 'sha256:5d59a61d1ef6c117'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDeviceOrientation

<sub>Enumeration</sub>

Constants that describe the physical orientation of the device.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIDeviceOrientation
```

## Overview

The [orientation](uidevice/orientation.md) property uses these constants to identify the device orientation. These constants identify the physical orientation of the device and aren’t tied to the orientation of your app’s user interface.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Device orientations

- [UIDeviceOrientationUnknown](uideviceorientation/unknown.md) — The orientation of the device can’t be determined.
- [UIDeviceOrientationPortrait](uideviceorientation/portrait.md) — The device is in portrait mode, with the device held upright and the front-facing camera at the top.
- [UIDeviceOrientationPortraitUpsideDown](uideviceorientation/portraitupsidedown.md) — The device is in portrait mode but upside down, with the device held upright and the front-facing camera at the bottom.
- [UIDeviceOrientationLandscapeLeft](uideviceorientation/landscapeleft.md) — The device is in landscape mode, with the device held upright and the front-facing camera on the left side.
- [UIDeviceOrientationLandscapeRight](uideviceorientation/landscaperight.md) — The device is in landscape mode, with the device held upright and the front-facing camera on the right side.
- [UIDeviceOrientationFaceUp](uideviceorientation/faceup.md) — The device is held parallel to the ground with the screen facing upwards.
- [UIDeviceOrientationFaceDown](uideviceorientation/facedown.md) — The device is held parallel to the ground with the screen facing downwards.

### Orientation testing

- [UIDeviceOrientationIsPortrait](uideviceorientation/isportrait.md) — A Boolean value that indicates whether the device is in a portrait orientation.
- [UIDeviceOrientationIsLandscape](uideviceorientation/islandscape.md) — A Boolean value that indicates whether the device is in a landscape orientation.
- [UIDeviceOrientationIsFlat](uideviceorientation/isflat.md) — A Boolean value that indicates whether the specified orientation is face up or face down.
- [UIDeviceOrientationIsValidInterfaceOrientation](uideviceorientation/isvalidinterfaceorientation.md) — A Boolean value that indicates whether the specified orientation is one of the portrait or landscape orientations.

### Initializers

- [init(rawValue:)](<uideviceorientation/init(rawvalue_).md>)

## See Also

### Tracking the device orientation

- [orientation](uidevice/orientation.md) — The physical orientation of the device.
- [generatesDeviceOrientationNotifications](uidevice/isgeneratingdeviceorientationnotifications.md) — A Boolean value that indicates whether the device generates orientation notifications.
- [- beginGeneratingDeviceOrientationNotifications](<uidevice/begingeneratingdeviceorientationnotifications().md>) — Begins the generation of notifications of device orientation changes.
- [- endGeneratingDeviceOrientationNotifications](<uidevice/endgeneratingdeviceorientationnotifications().md>) — Ends the generation of notifications of device orientation changes.
