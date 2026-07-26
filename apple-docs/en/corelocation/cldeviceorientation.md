---
title: CLDeviceOrientation
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cldeviceorientation
source_url: 'https://developer.apple.com/documentation/corelocation/cldeviceorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cldeviceorientation.json'
content_hash: 'sha256:6bdba68963d50f69'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLDeviceOrientation

<sub>Enumeration</sub>

Constants indicating the physical orientation of the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CLDeviceOrientation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Device Orientations

- [CLDeviceOrientationUnknown](cldeviceorientation/unknown.md) — The orientation is currently not known.
- [CLDeviceOrientationPortrait](cldeviceorientation/portrait.md) — The device is in portrait mode, with the device held upright and the home button at the bottom.
- [CLDeviceOrientationPortraitUpsideDown](cldeviceorientation/portraitupsidedown.md) — The device is in portrait mode but upside down, with the device held upright and the home button at the top.
- [CLDeviceOrientationLandscapeLeft](cldeviceorientation/landscapeleft.md) — The device is in landscape mode, with the device held upright and the home button on the right side.
- [CLDeviceOrientationLandscapeRight](cldeviceorientation/landscaperight.md) — The device is in landscape mode, with the device held upright and the home button on the left side.
- [CLDeviceOrientationFaceUp](cldeviceorientation/faceup.md) — The device is held parallel to the ground with the screen facing upwards.
- [CLDeviceOrientationFaceDown](cldeviceorientation/facedown.md) — The device is held parallel to the ground with the screen facing downwards.

### Initializers

- [init(rawValue:)](<cldeviceorientation/init(rawvalue_).md>)

## See Also

### Running the heading service

- [- startUpdatingHeading](<cllocationmanager/startupdatingheading().md>) — Starts the generation of updates that report the user’s current heading.
- [- stopUpdatingHeading](<cllocationmanager/stopupdatingheading().md>) — Stops the generation of heading updates.
- [- dismissHeadingCalibrationDisplay](<cllocationmanager/dismissheadingcalibrationdisplay().md>) — Dismisses the heading calibration view from the screen immediately.
- [headingFilter](cllocationmanager/headingfilter.md) — The minimum angular change in degrees required to generate new heading events.
- [kCLHeadingFilterNone](kclheadingfilternone.md) — A constant indicating that all header values should be reported.
- [CLLocationDegrees](cllocationdegrees.md) — A latitude or longitude value specified in degrees.
- [headingOrientation](cllocationmanager/headingorientation.md) — The device orientation to use when computing heading values. _(deprecated)_
