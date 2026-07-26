---
title: authorizationStatus()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.2+（14.0 起废弃）, iPadOS 4.2+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.7+（11.0 起废弃）, tvOS 9.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（7.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/cllocationmanager/authorizationstatus()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/authorizationstatus()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/authorizationstatus%28%29.json'
content_hash: 'sha256:655f2514dbb31119'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# authorizationStatus()

<sub>Type Method</sub>

Returns the app’s authorization status for using location services.

> [!warning] Deprecated
> Use the [authorizationStatus](authorizationstatus-swift.property.md) instance property with [- locationManagerDidChangeAuthorization:](<../cllocationmanagerdelegate/locationmanagerdidchangeauthorization(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func authorizationStatus() -> CLAuthorizationStatus
```

## Return Value

A value indicating whether the app is authorized to use location services.

## Discussion

The system is guaranteed to call the delegate method with the app’s initial authorization state and all authorization status changes.

The system manages the authorization status of a given app according to several factors. Users must authorize the app to use location services explicitly, and location services must be enabled in Settings \> Privacy. See [Choosing the  Location Services Authorization to Request](../../bundleresources/choosing-the-location-services-authorization-to-request.md) for more information.

## See Also

### Methods

- [- startMonitoringForRegion:](<startmonitoring(for_).md>) — Starts monitoring the specified region. _(deprecated)_
- [- stopMonitoringForRegion:](<stopmonitoring(for_).md>) — Stops monitoring the specified region. _(deprecated)_
- [+ regionMonitoringAvailable](<regionmonitoringavailable().md>) — Returns a Boolean value indicating whether region monitoring is supported on the current device. _(deprecated)_
- [+ regionMonitoringEnabled](<regionmonitoringenabled().md>) — Returns a Boolean value indicating whether region monitoring is currently enabled. _(deprecated)_
- [- startMonitoringForRegion:desiredAccuracy:](<startmonitoring(for_desiredaccuracy_).md>) — Starts monitoring the specified region for boundary crossings. _(deprecated)_
- [- requestStateForRegion:](<requeststate(for_).md>) — Retrieves the state of a region asynchronously. _(deprecated)_
- [- startRangingBeaconsInRegion:](<startrangingbeacons(in_).md>) — Starts the delivery of notifications for the specified beacon region. _(deprecated)_
- [- stopRangingBeaconsInRegion:](<stoprangingbeacons(in_).md>) — Stops the delivery of notifications for the specified beacon region. _(deprecated)_
- [+ deferredLocationUpdatesAvailable](<deferredlocationupdatesavailable().md>) — Returns a Boolean value indicating whether the device supports deferred location updates. _(deprecated)_
- [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<allowdeferredlocationupdates(untiltraveled_timeout_).md>) — Asks the location manager to defer the delivery of location updates until the specified criteria are met. _(deprecated)_
- [- disallowDeferredLocationUpdates](<disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
