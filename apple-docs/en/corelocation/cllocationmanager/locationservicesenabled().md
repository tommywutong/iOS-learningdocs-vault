---
title: locationServicesEnabled()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/locationservicesenabled()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/locationservicesenabled()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/locationservicesenabled%28%29.json'
content_hash: 'sha256:8a21c0eafaa971ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# locationServicesEnabled()

<sub>Type Method</sub>

Returns a Boolean value indicating whether location services are enabled on the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func locationServicesEnabled() -> Bool
```

## Return Value

[true](../../swift/true.md) if location services are enabled on the device; [false](../../swift/false.md) if they are not.

## Discussion

Users can enable or disable location services by toggling the Location Services switch in Settings \> Privacy.

- When users disable the switch, the system calls your delegate’s [- locationManager:didChangeAuthorizationStatus:](<../cllocationmanagerdelegate/locationmanager(__didchangeauthorization_).md>) method with a denied authorization status ([kCLAuthorizationStatusDenied](../clauthorizationstatus/denied.md)).
- When users enable the switch, the system returns your app’s authorization to its previous state and calls your delegate’s [- locationManager:didChangeAuthorizationStatus:](<../cllocationmanagerdelegate/locationmanager(__didchangeauthorization_).md>) method.

You are not required to call [+ locationServicesEnabled](<locationservicesenabled().md>). However, If you wish to display instructions about enabling location services, you may check the return value of this method to find out if the services are disabled for the entire device, or just for your app.  If the result is `true`, provide instructions for enabling services for your app; otherwise, provide instructions for enabling the Location Services switch in Settings \> Privacy.

If users disable or deny location services and you attempt to start location updates anyway, the location manager reports an error to its delegate. See [- locationManager:didFailWithError:](<../cllocationmanagerdelegate/locationmanager(__didfailwitherror_).md>) and [- locationManager:monitoringDidFailForRegion:withError:](<../cllocationmanagerdelegate/locationmanager(__monitoringdidfailfor_witherror_).md>) for more information.

## Topics

### Related Documentation

- [- locationManager:didFailWithError:](<../cllocationmanagerdelegate/locationmanager(__didfailwitherror_).md>) — Tells the delegate that the location manager was unable to retrieve a location value.
- [- locationManager:monitoringDidFailForRegion:withError:](<../cllocationmanagerdelegate/locationmanager(__monitoringdidfailfor_witherror_).md>) — Tells the delegate that a region monitoring error occurred.

## See Also

### Determining the availability of services

- [+ significantLocationChangeMonitoringAvailable](<significantlocationchangemonitoringavailable().md>) — Returns a Boolean value indicating whether the significant-change location service is available on the device.
- [+ headingAvailable](<headingavailable().md>) — Returns a Boolean value indicating whether the location manager is able to generate heading-related events.
- [authorizedForWidgetUpdates](isauthorizedforwidgetupdates.md) — A Boolean value that indicates whether a widget is eligible to receive location updates.
- [accuracyAuthorization](accuracyauthorization.md) — A value that indicates the level of location accuracy the app has permission to use.
- [+ isMonitoringAvailableForClass:](<ismonitoringavailable(for_).md>) — Returns a Boolean value indicating whether the device supports region monitoring using the specified class.
- [+ isRangingAvailable](<israngingavailable().md>) — Returns a Boolean value indicating whether the device supports ranging of beacons that use the iBeacon protocol.
