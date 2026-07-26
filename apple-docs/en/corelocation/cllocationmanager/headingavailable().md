---
title: headingAvailable()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/headingavailable()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/headingavailable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/headingavailable%28%29.json'
content_hash: 'sha256:23369964d66b7296'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# headingAvailable()

<sub>Type Method</sub>

Returns a Boolean value indicating whether the location manager is able to generate heading-related events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class func headingAvailable() -> Bool
```

## Return Value

[true](../../swift/true.md) if heading data is available; [false](../../swift/false.md) if it is not.

## Discussion

Heading data may not be available on all iOS-based devices. You should check the value returned by this method before asking the location manager to deliver heading-related events.

## See Also

### Determining the availability of services

- [+ significantLocationChangeMonitoringAvailable](<significantlocationchangemonitoringavailable().md>) — Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [authorizedForWidgetUpdates](isauthorizedforwidgetupdates.md) — A Boolean value that indicates whether a widget is eligible to receive location updates.
- [accuracyAuthorization](accuracyauthorization.md) — A value that indicates the level of location accuracy the app has permission to use.
- [+ isMonitoringAvailableForClass:](<ismonitoringavailable(for_).md>) — Returns a Boolean value indicating whether the device supports region monitoring using the specified class.
- [+ isRangingAvailable](<israngingavailable().md>) — Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.
- [+ locationServicesEnabled](<locationservicesenabled().md>) — Returns a Boolean value indicating whether location services are enabled on the device.
