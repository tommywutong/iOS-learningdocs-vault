---
title: kCLHeadingFilterNone
framework: Core Location
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/kclheadingfilternone
source_url: 'https://developer.apple.com/documentation/corelocation/kclheadingfilternone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/kclheadingfilternone.json'
content_hash: 'sha256:f8b43ddd70581775'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# kCLHeadingFilterNone

<sub>Global Variable</sub>

A constant indicating that all header values should be reported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCLHeadingFilterNone: CLLocationDegrees
```

## Discussion

Use this constant to indicate that any change to the heading, regardless of how small, should be reported.

## See Also

### Running the heading service

- [- startUpdatingHeading](<cllocationmanager/startupdatingheading().md>) — Starts the generation of updates that report the user’s current heading.
- [- stopUpdatingHeading](<cllocationmanager/stopupdatingheading().md>) — Stops the generation of heading updates.
- [- dismissHeadingCalibrationDisplay](<cllocationmanager/dismissheadingcalibrationdisplay().md>) — Dismisses the heading calibration view from the screen immediately.
- [headingFilter](cllocationmanager/headingfilter.md) — The minimum angular change in degrees required to generate new heading events.
- [CLLocationDegrees](cllocationdegrees.md) — A latitude or longitude value specified in degrees.
- [headingOrientation](cllocationmanager/headingorientation.md) — The device orientation to use when computing heading values. _(deprecated)_
- [CLDeviceOrientation](cldeviceorientation.md) — Constants indicating the physical orientation of the device.
