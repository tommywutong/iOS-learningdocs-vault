---
title: significantLocationChangeMonitoringAvailable()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/significantlocationchangemonitoringavailable()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/significantlocationchangemonitoringavailable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/significantlocationchangemonitoringavailable%28%29.json'
content_hash: 'sha256:6e7950ca6620a140'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# significantLocationChangeMonitoringAvailable()

<sub>Type Method</sub>

Returns a Boolean value indicating whether the significant-change location service is available on the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class func significantLocationChangeMonitoringAvailable() -> Bool
```

## Return Value

[true](../../swift/true.md) if location change monitoring is available; [false](../../swift/false.md) if it is not.

## Discussion

This method indicates whether the device is able to report updates based on significant location changes only. This capability provides tremendous power savings for apps that want to track a user’s approximate location and don’t need highly accurate position information.

## See Also

### Determining the availability of services

- [+ headingAvailable](<headingavailable().md>) — Returns a Boolean value indicating whether the location manager is able to generate heading-related events.
- [authorizedForWidgetUpdates](isauthorizedforwidgetupdates.md) — A Boolean value that indicates whether a widget is eligible to receive location updates.
- [accuracyAuthorization](accuracyauthorization.md) — A value that indicates the level of location accuracy the app has permission to use.
- [+ isMonitoringAvailableForClass:](<ismonitoringavailable(for_).md>) — Returns a Boolean value indicating whether the device supports region monitoring using the specified class.
- [+ isRangingAvailable](<israngingavailable().md>) — Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.
- [+ locationServicesEnabled](<locationservicesenabled().md>) — Returns a Boolean value indicating whether location services are enabled on the device.
