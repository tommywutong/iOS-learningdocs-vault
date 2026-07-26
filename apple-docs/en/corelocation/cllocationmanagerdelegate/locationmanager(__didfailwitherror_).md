---
title: 'locationManager(_:didFailWithError:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfailwitherror:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfailwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanager%28_%3Adidfailwitherror%3A%29.json'
content_hash: 'sha256:f4121aa7a6a217fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManager(_:didFailWithError:)

<sub>Instance Method</sub>

Tells the delegate that the location manager was unable to retrieve a location value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func locationManager(_ manager: CLLocationManager, didFailWithError error: any Error)
```

## Parameters

- `manager` — The location manager object that was unable to retrieve the location.

- `error` — The error object containing the reason the location or heading could not be retrieved.

## Discussion

If you do not implement this method, Core Location throws an exception when attempting to use location services.

The location manager calls this method when it encounters an error trying to get the location or heading data. If the location service is unable to retrieve a location right away, it reports a [kCLErrorLocationUnknown](../clerror-swift.struct/code/locationunknown.md) error and keeps trying. In such a situation, you can simply ignore the error and wait for a new event. If a heading could not be determined because of strong interference from nearby magnetic fields, this method returns [kCLErrorHeadingFailure](../clerror-swift.struct/code/headingfailure.md).

If the user denies your app’s use of the location service, this method reports a [kCLErrorDenied](../clerror-swift.struct/code/denied.md) error. Upon receiving such an error, you should stop the location service.

## See Also

### Related Documentation

- [- locationManager:monitoringDidFailForRegion:withError:](<locationmanager(__monitoringdidfailfor_witherror_).md>) — Tells the delegate that a region monitoring error occurred.
