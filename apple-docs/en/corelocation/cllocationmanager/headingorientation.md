---
title: headingOrientation
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/cllocationmanager/headingorientation
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/headingorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/headingorientation.json'
content_hash: 'sha256:3410e244fec12978'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# headingOrientation

<sub>Instance Property</sub>

The device orientation to use when computing heading values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
var headingOrientation: CLDeviceOrientation { get set }
```

## Discussion

When computing heading values, the location manager assumes that the top of the device in portrait mode represents due north (0 degrees) by default. For apps that run in other orientations, this may not always be the most convenient orientation. This property allows you to specify which device orientation you want the location manager to use as the reference point for due north.

Although you can set the value of this property to [CLDeviceOrientationUnknown](../cldeviceorientation/unknown.md), [CLDeviceOrientationFaceUp](../cldeviceorientation/faceup.md), or [CLDeviceOrientationFaceDown](../cldeviceorientation/facedown.md), doing so has no effect on the orientation reference point. The original reference point is retained instead.

Changing the value in this property affects only those heading values reported after the change is made.

## See Also

### Running the heading service

- [- startUpdatingHeading](<startupdatingheading().md>) — Starts the generation of updates that report the user’s current heading.
- [- stopUpdatingHeading](<stopupdatingheading().md>) — Stops the generation of heading updates.
- [- dismissHeadingCalibrationDisplay](<dismissheadingcalibrationdisplay().md>) — Dismisses the heading calibration view from the screen immediately.
- [headingFilter](headingfilter.md) — The minimum angular change in degrees required to generate new heading events.
- [kCLHeadingFilterNone](../kclheadingfilternone.md) — A constant indicating that all header values should be reported.
- [CLLocationDegrees](../cllocationdegrees.md) — A latitude or longitude value specified in degrees.
- [CLDeviceOrientation](../cldeviceorientation.md) — Constants indicating the physical orientation of the device.
