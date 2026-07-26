---
title: CLLocationDegrees
framework: Core Location
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationdegrees
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationdegrees'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationdegrees.json'
content_hash: 'sha256:37efd5297806877c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationDegrees

<sub>Type Alias</sub>

A latitude or longitude value specified in degrees.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CLLocationDegrees = Double
```

## See Also

### Running the heading service

- [- startUpdatingHeading](<cllocationmanager/startupdatingheading().md>) — Starts the generation of updates that report the user’s current heading.
- [- stopUpdatingHeading](<cllocationmanager/stopupdatingheading().md>) — Stops the generation of heading updates.
- [- dismissHeadingCalibrationDisplay](<cllocationmanager/dismissheadingcalibrationdisplay().md>) — Dismisses the heading calibration view from the screen immediately.
- [headingFilter](cllocationmanager/headingfilter.md) — The minimum angular change in degrees required to generate new heading events.
- [kCLHeadingFilterNone](kclheadingfilternone.md) — A constant indicating that all header values should be reported.
- [headingOrientation](cllocationmanager/headingorientation.md) — The device orientation to use when computing heading values. _(deprecated)_
- [CLDeviceOrientation](cldeviceorientation.md) — Constants indicating the physical orientation of the device.
