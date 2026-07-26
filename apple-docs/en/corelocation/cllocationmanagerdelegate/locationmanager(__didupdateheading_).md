---
title: 'locationManager(_:didUpdateHeading:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.15+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didupdateheading:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didupdateheading:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidupdateheading%3A%29.json'
content_hash: 'sha256:4103c30a122b446b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didUpdateHeading:)

<sub>Instance Method</sub>

Tells the delegate that the location manager received updated heading information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didUpdateHeading newHeading: CLHeading)
```

## Parameters

- `manager` — The location manager object that generated the update event.

- `newHeading` — The new heading data.

## Discussion

Implementation of this method is optional but expected if you start heading updates using the [- startUpdatingHeading](<../cllocationmanager/startupdatingheading().md>) method.

The location manager object calls this method after you initially start the heading service. Subsequent events are delivered when the previously reported value changes by more than the value specified in the [headingFilter](../cllocationmanager/headingfilter.md) property of the location manager object.

## See Also

### Receiving heading updates

- [- locationManagerShouldDisplayHeadingCalibration:](<locationmanagershoulddisplayheadingcalibration(__).md>) — Asks the delegate whether the heading calibration alert should be displayed.
