---
title: accuracyAuthorization
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/accuracyauthorization
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/accuracyauthorization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/accuracyauthorization.json'
content_hash: 'sha256:d75c85704084405d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# accuracyAuthorization

<sub>Instance Property</sub>

A value that indicates the level of location accuracy the app has permission to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var accuracyAuthorization: CLAccuracyAuthorization { get }
```

## Discussion

If the value of this property is [CLAccuracyAuthorizationFullAccuracy](../claccuracyauthorization/fullaccuracy.md), you can set the [desiredAccuracy](desiredaccuracy.md) property to any value. If the value is [CLAccuracyAuthorizationReducedAccuracy](../claccuracyauthorization/reducedaccuracy.md), setting [desiredAccuracy](desiredaccuracy.md) to a value other than [kCLLocationAccuracyReduced](../kcllocationaccuracyreduced.md) has no effect on the location information, and your app can’t use region monitoring or beacon ranging.

> [!note] Note
> Because reduced accuracy isn’t available prior to watchOS 7, when the user chooses reduced accuracy on the paired iPhone, watch apps running with this older software don’t receive any location data. This occurs because watchOS apps must adhere to the permissions granted on the paired iPhone.

## See Also

### Determining the availability of services

- [+ significantLocationChangeMonitoringAvailable](<significantlocationchangemonitoringavailable().md>) — Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [+ headingAvailable](<headingavailable().md>) — Returns a Boolean value indicating whether the location manager is able to generate heading-related events.
- [authorizedForWidgetUpdates](isauthorizedforwidgetupdates.md) — A Boolean value that indicates whether a widget is eligible to receive location updates.
- [+ isMonitoringAvailableForClass:](<ismonitoringavailable(for_).md>) — Returns a Boolean value indicating whether the device supports region monitoring using the specified class.
- [+ isRangingAvailable](<israngingavailable().md>) — Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.
- [+ locationServicesEnabled](<locationservicesenabled().md>) — Returns a Boolean value indicating whether location services are enabled on the device.
