---
title: headingFilter
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.15+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/headingfilter
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/headingfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/headingfilter.json'
content_hash: 'sha256:83d98a359f52978a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# headingFilter

<sub>Instance Property</sub>

The minimum angular change in degrees required to generate new heading events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
var headingFilter: CLLocationDegrees { get set }
```

## Discussion

The angular distance is measured relative to the last delivered heading event. Use the value [kCLHeadingFilterNone](../kclheadingfilternone.md) to be notified of all movements. The default value of this property is `1` degree.

## See Also

### Running the heading service

- [- startUpdatingHeading](<startupdatingheading().md>) — Starts the generation of updates that report the user’s current heading.
- [- stopUpdatingHeading](<stopupdatingheading().md>) — Stops the generation of heading updates.
- [- dismissHeadingCalibrationDisplay](<dismissheadingcalibrationdisplay().md>) — Dismisses the heading calibration view from the screen immediately.
- [kCLHeadingFilterNone](../kclheadingfilternone.md) — A constant indicating that all header values should be reported.
- [CLLocationDegrees](../cllocationdegrees.md) — A latitude or longitude value specified in degrees.
- [headingOrientation](headingorientation.md) — The device orientation to use when computing heading values. _(deprecated)_
- [CLDeviceOrientation](../cldeviceorientation.md) — Constants indicating the physical orientation of the device.
