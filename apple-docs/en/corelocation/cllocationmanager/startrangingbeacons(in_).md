---
title: 'startRangingBeacons(in:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 14.0+（14.0 起废弃）, macOS 11.0+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocationmanager/startrangingbeacons(in:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/startrangingbeacons(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/startrangingbeacons%28in%3A%29.json'
content_hash: 'sha256:7f69667af7136922'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# startRangingBeacons(in:)

<sub>Instance Method</sub>

Starts the delivery of notifications for the specified beacon region.

> [!warning] Deprecated
> Use [- startRangingBeaconsSatisfyingConstraint:](<startrangingbeacons(satisfying_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func startRangingBeacons(in region: CLBeaconRegion)
```

## Parameters

- `region` — The region object that defines the identifying information for the targeted beacons. The number of beacons represented by this region object depends on which identifier values you use to initialize it. Beacons must match all of the identifiers you specify. This method copies the region information it needs from the object you provide.

## Discussion

Once registered, the location manager reports any encountered beacons to its delegate by calling the [- locationManager:didRangeBeacons:inRegion:](<../cllocationmanagerdelegate/locationmanager(__didrangebeacons_in_).md>) method. If there is an error registering the specified beacon region, the location manager calls its delegate’s [- locationManager:rangingBeaconsDidFailForRegion:withError:](<../cllocationmanagerdelegate/locationmanager(__rangingbeaconsdidfailfor_witherror_).md>) method and provides the appropriate error information.

## See Also

### Methods

- [- startMonitoringForRegion:](<startmonitoring(for_).md>) — Starts monitoring the specified region. _(deprecated)_
- [- stopMonitoringForRegion:](<stopmonitoring(for_).md>) — Stops monitoring the specified region. _(deprecated)_
- [+ regionMonitoringAvailable](<regionmonitoringavailable().md>) — Returns a Boolean value indicating whether region monitoring is supported on the current device. _(deprecated)_
- [+ regionMonitoringEnabled](<regionmonitoringenabled().md>) — Returns a Boolean value indicating whether region monitoring is currently enabled. _(deprecated)_
- [+ authorizationStatus](<authorizationstatus().md>) — Returns the app’s authorization status for using location services. _(deprecated)_
- [- startMonitoringForRegion:desiredAccuracy:](<startmonitoring(for_desiredaccuracy_).md>) — Starts monitoring the specified region for boundary crossings. _(deprecated)_
- [- requestStateForRegion:](<requeststate(for_).md>) — Retrieves the state of a region asynchronously. _(deprecated)_
- [- stopRangingBeaconsInRegion:](<stoprangingbeacons(in_).md>) — Stops the delivery of notifications for the specified beacon region. _(deprecated)_
- [+ deferredLocationUpdatesAvailable](<deferredlocationupdatesavailable().md>) — Returns a Boolean value indicating whether the device supports deferred location updates. _(deprecated)_
- [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<allowdeferredlocationupdates(untiltraveled_timeout_).md>) — Asks the location manager to defer the delivery of location updates until the specified criteria are met. _(deprecated)_
- [- disallowDeferredLocationUpdates](<disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
