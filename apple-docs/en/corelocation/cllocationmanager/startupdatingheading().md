---
title: startUpdatingHeading()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.15+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/startupdatingheading()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/startupdatingheading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/startupdatingheading%28%29.json'
content_hash: 'sha256:2141a1d2552638e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# startUpdatingHeading()

<sub>Instance Method</sub>

Starts the generation of updates that report the user’s current heading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
func startUpdatingHeading()
```

## Discussion

This method returns immediately. Calling this method when the receiver is stopped causes it to obtain an initial heading and notify your delegate. After that, the receiver generates update events when the value in the [headingFilter](headingfilter.md) property is exceeded.

Before calling this method, you should always check the [headingAvailable](headingavailable-swift.property.md) property to see whether heading information is supported on the current device. If heading information is not supported, calling this method has no effect and does not result in the delivery of events to your delegate.

Calling this method several times in succession does not automatically result in new events being generated. Calling [- stopUpdatingHeading](<stopupdatingheading().md>) in between, however, does cause a new initial event to be sent the next time you call this method.

If you start this service and your app is suspended, the system stops the delivery of events until your app starts running again (either in the foreground or background). If your app is terminated, the delivery of new heading events stops altogether and must be restarted by your code when the app is relaunched.

Heading events are delivered to the [- locationManager:didUpdateHeading:](<../cllocationmanagerdelegate/locationmanager(__didupdateheading_).md>) method of your delegate. If there is an error, the location manager calls the [- locationManager:didFailWithError:](<../cllocationmanagerdelegate/locationmanager(__didfailwitherror_).md>) method of your delegate instead.

If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## Topics

### Related Documentation

- [headingAvailable](headingavailable-swift.property.md) — A Boolean value indicating whether the location manager is able to generate heading-related events. _(deprecated)_

## See Also

### Running the heading service

- [- stopUpdatingHeading](<stopupdatingheading().md>) — Stops the generation of heading updates.
- [- dismissHeadingCalibrationDisplay](<dismissheadingcalibrationdisplay().md>) — Dismisses the heading calibration view from the screen immediately.
- [headingFilter](headingfilter.md) — The minimum angular change in degrees required to generate new heading events.
- [kCLHeadingFilterNone](../kclheadingfilternone.md) — A constant indicating that all header values should be reported.
- [CLLocationDegrees](../cllocationdegrees.md) — A latitude or longitude value specified in degrees.
- [headingOrientation](headingorientation.md) — The device orientation to use when computing heading values. _(deprecated)_
- [CLDeviceOrientation](../cldeviceorientation.md) — Constants indicating the physical orientation of the device.
