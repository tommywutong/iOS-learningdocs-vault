---
title: isRangingAvailable()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/israngingavailable()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/israngingavailable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/israngingavailable%28%29.json'
content_hash: 'sha256:5feff52cdda60c78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# isRangingAvailable()

<sub>Type Method</sub>

Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class func isRangingAvailable() -> Bool
```

## Return Value

[true](../../swift/true.md) if the device supports ranging or [false](../../swift/false.md) if it does not.

## See Also

### Determining the availability of services

- [+ significantLocationChangeMonitoringAvailable](<significantlocationchangemonitoringavailable().md>) — Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [+ headingAvailable](<headingavailable().md>) — Returns a Boolean value indicating whether the location manager is able to generate heading-related events.
- [authorizedForWidgetUpdates](isauthorizedforwidgetupdates.md) — A Boolean value that indicates whether a widget is eligible to receive location updates.
- [accuracyAuthorization](accuracyauthorization.md) — A value that indicates the level of location accuracy the app has permission to use.
- [+ isMonitoringAvailableForClass:](<ismonitoringavailable(for_).md>) — Returns a Boolean value indicating whether the device supports region monitoring using the specified class.
- [+ locationServicesEnabled](<locationservicesenabled().md>) — Returns a Boolean value indicating whether location services are enabled on the device.
