---
title: stopUpdatingHeading()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/stopupdatingheading()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/stopupdatingheading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/stopupdatingheading%28%29.json'
content_hash: 'sha256:f51135923eefa1a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# stopUpdatingHeading()

<sub>Instance Method</sub>

Stops the generation of heading updates.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
func stopUpdatingHeading()
```

## Discussion

Call this method whenever your code no longer needs to receive heading-related events. Disabling event delivery gives the receiver the option of disabling the appropriate hardware (and thereby saving power) when no clients need location data. You can always restart the generation of heading updates by calling the [- startUpdatingHeading](<startupdatingheading().md>) method again.

If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Running the heading service

- [- startUpdatingHeading](<startupdatingheading().md>) — Starts the generation of updates that report the user’s current heading.
- [- dismissHeadingCalibrationDisplay](<dismissheadingcalibrationdisplay().md>) — Dismisses the heading calibration view from the screen immediately.
- [headingFilter](headingfilter.md) — The minimum angular change in degrees required to generate new heading events.
- [kCLHeadingFilterNone](../kclheadingfilternone.md) — A constant indicating that all header values should be reported.
- [CLLocationDegrees](../cllocationdegrees.md) — A latitude or longitude value specified in degrees.
- [headingOrientation](headingorientation.md) — The device orientation to use when computing heading values. _(deprecated)_
- [CLDeviceOrientation](../cldeviceorientation.md) — Constants indicating the physical orientation of the device.
