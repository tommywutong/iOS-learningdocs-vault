---
title: isAuthorizedForWidgetUpdates
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/isauthorizedforwidgetupdates
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/isauthorizedforwidgetupdates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/isauthorizedforwidgetupdates.json'
content_hash: 'sha256:b5101767fa064d75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# isAuthorizedForWidgetUpdates

<sub>Instance Property</sub>

A Boolean value that indicates whether a widget is eligible to receive location updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var isAuthorizedForWidgetUpdates: Bool { get }
```

## Discussion

This property is `true` when either of the following is true:

- The app’s authorization status is [kCLAuthorizationStatusAuthorizedAlways](../clauthorizationstatus/authorizedalways.md).
- The app’s authorization status is [kCLAuthorizationStatusAuthorizedWhenInUse](../clauthorizationstatus/authorizedwheninuse.md) and the user agrees to extend the app’s authorization status to widgets.

> [!note] Note
> For apps that use [kCLAuthorizationStatusAuthorizedWhenInUse](../clauthorizationstatus/authorizedwheninuse.md), after the user agrees to extend an app’s authorization status to widgets, the app’s Location Services settings indicate While Using the App or Widgets as the active access level.

For details about using location information in widgets with [kCLAuthorizationStatusAuthorizedWhenInUse](../clauthorizationstatus/authorizedwheninuse.md), see [Accessing location information in widgets](../../widgetkit/accessing-location-information-in-widgets.md).

## See Also

### Determining the availability of services

- [+ significantLocationChangeMonitoringAvailable](<significantlocationchangemonitoringavailable().md>) — Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [+ headingAvailable](<headingavailable().md>) — Returns a Boolean value indicating whether the location manager is able to generate heading-related events.
- [accuracyAuthorization](accuracyauthorization.md) — A value that indicates the level of location accuracy the app has permission to use.
- [+ isMonitoringAvailableForClass:](<ismonitoringavailable(for_).md>) — Returns a Boolean value indicating whether the device supports region monitoring using the specified class.
- [+ isRangingAvailable](<israngingavailable().md>) — Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.
- [+ locationServicesEnabled](<locationservicesenabled().md>) — Returns a Boolean value indicating whether location services are enabled on the device.
