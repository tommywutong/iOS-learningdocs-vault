---
title: 'isMonitoringAvailable(for:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanager/ismonitoringavailable(for:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/ismonitoringavailable(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/ismonitoringavailable%28for%3A%29.json'
content_hash: 'sha256:c7344d71fdfcb4bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# isMonitoringAvailable(for:)

<sub>Type Method</sub>

Returns a Boolean value indicating whether the device supports region monitoring using the specified class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class func isMonitoringAvailable(for regionClass: AnyClass) -> Bool
```

## Parameters

- `regionClass` — A region monitoring class from the MapKit framework. This class must descend from the [CLRegion](../clregion.md) class.

## Return Value

[true](../../swift/true.md) if the device is capable of monitoring regions using the specified class or [false](../../swift/false.md) if it is not.

## Discussion

The availability of region monitoring support is dependent on the hardware present on the device. This method does not take into account the availability of location services or the fact that the user might have disabled them for the app or system; you must determine your app’s authorization status separately.

## See Also

### Determining the availability of services

- [+ significantLocationChangeMonitoringAvailable](<significantlocationchangemonitoringavailable().md>) — Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [+ headingAvailable](<headingavailable().md>) — Returns a Boolean value indicating whether the location manager is able to generate heading-related events.
- [authorizedForWidgetUpdates](isauthorizedforwidgetupdates.md) — A Boolean value that indicates whether a widget is eligible to receive location updates.
- [accuracyAuthorization](accuracyauthorization.md) — A value that indicates the level of location accuracy the app has permission to use.
- [+ isRangingAvailable](<israngingavailable().md>) — Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.
- [+ locationServicesEnabled](<locationservicesenabled().md>) — Returns a Boolean value indicating whether location services are enabled on the device.
