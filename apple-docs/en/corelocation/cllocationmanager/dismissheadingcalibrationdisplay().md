---
title: dismissHeadingCalibrationDisplay()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.15+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/dismissheadingcalibrationdisplay()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/dismissheadingcalibrationdisplay()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/dismissheadingcalibrationdisplay%28%29.json'
content_hash: 'sha256:a8cebce88e4ce6a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# dismissHeadingCalibrationDisplay()

<sub>Instance Method</sub>

Dismisses the heading calibration view from the screen immediately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
func dismissHeadingCalibrationDisplay()
```

## Discussion

Core Location uses the heading calibration alert to calibrate the available heading hardware as needed. The display of this view is automatic, assuming your delegate supports displaying the view at all. If the view is displayed, you can use this method to dismiss it after an appropriate amount of time to ensure that your app’s user interface is not unduly disrupted.

## See Also

### Running the heading service

- [- startUpdatingHeading](<startupdatingheading().md>) — Starts the generation of updates that report the user’s current heading.
- [- stopUpdatingHeading](<stopupdatingheading().md>) — Stops the generation of heading updates.
- [headingFilter](headingfilter.md) — The minimum angular change in degrees required to generate new heading events.
- [kCLHeadingFilterNone](../kclheadingfilternone.md) — A constant indicating that all header values should be reported.
- [CLLocationDegrees](../cllocationdegrees.md) — A latitude or longitude value specified in degrees.
- [headingOrientation](headingorientation.md) — The device orientation to use when computing heading values. _(deprecated)_
- [CLDeviceOrientation](../cldeviceorientation.md) — Constants indicating the physical orientation of the device.
