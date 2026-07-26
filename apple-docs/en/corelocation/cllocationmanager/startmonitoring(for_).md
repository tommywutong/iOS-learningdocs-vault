---
title: 'startMonitoring(for:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocationmanager/startmonitoring(for:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoring(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/startmonitoring%28for%3A%29.json'
content_hash: 'sha256:18efd4d788bdb25c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# startMonitoring(for:)

<sub>Instance Method</sub>

Starts monitoring the specified region.

> [!warning] Deprecated
> Use [addConditionForMonitoring:identifier:](../clmonitor-6ynwz/addconditionformonitoring_identifier_.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func startMonitoring(for region: CLRegion)
```

## Parameters

- `region` — The region object that defines the boundary to monitor. This parameter must not be `nil`.

## Discussion

You must call this method once for each region you want to monitor. If an existing region with the same identifier is already being monitored by the app, the old region is replaced by the new one. The regions you add using this method are shared by all location manager objects in your app and stored in the [monitoredRegions](monitoredregions.md) property.

Region events are delivered to the [- locationManager:didEnterRegion:](<../cllocationmanagerdelegate/locationmanager(__didenterregion_).md>) and [- locationManager:didExitRegion:](<../cllocationmanagerdelegate/locationmanager(__didexitregion_).md>) methods of your delegate. If there is an error, the location manager calls the [- locationManager:monitoringDidFailForRegion:withError:](<../cllocationmanagerdelegate/locationmanager(__monitoringdidfailfor_witherror_).md>) method of your delegate instead.

An app can register up to 20 regions at a time. In order to report region changes in a timely manner, the region monitoring service requires network connectivity.

In iOS 6, regions with a radius between 1 and 400 meters work better on iPhone 4S or later devices. (In iOS 5, regions with a radius between 1 and 150 meters work better on iPhone 4S and later devices.) On these devices, an app can expect to receive the appropriate region entered or region exited notification within 3 to 5 minutes on average, if not sooner.

If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Methods

- [- stopMonitoringForRegion:](<stopmonitoring(for_).md>) — Stops monitoring the specified region. _(deprecated)_
- [+ regionMonitoringAvailable](<regionmonitoringavailable().md>) — Returns a Boolean value indicating whether region monitoring is supported on the current device. _(deprecated)_
- [+ regionMonitoringEnabled](<regionmonitoringenabled().md>) — Returns a Boolean value indicating whether region monitoring is currently enabled. _(deprecated)_
- [+ authorizationStatus](<authorizationstatus().md>) — Returns the app’s authorization status for using location services. _(deprecated)_
- [- startMonitoringForRegion:desiredAccuracy:](<startmonitoring(for_desiredaccuracy_).md>) — Starts monitoring the specified region for boundary crossings. _(deprecated)_
- [- requestStateForRegion:](<requeststate(for_).md>) — Retrieves the state of a region asynchronously. _(deprecated)_
- [- startRangingBeaconsInRegion:](<startrangingbeacons(in_).md>) — Starts the delivery of notifications for the specified beacon region. _(deprecated)_
- [- stopRangingBeaconsInRegion:](<stoprangingbeacons(in_).md>) — Stops the delivery of notifications for the specified beacon region. _(deprecated)_
- [+ deferredLocationUpdatesAvailable](<deferredlocationupdatesavailable().md>) — Returns a Boolean value indicating whether the device supports deferred location updates. _(deprecated)_
- [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<allowdeferredlocationupdates(untiltraveled_timeout_).md>) — Asks the location manager to defer the delivery of location updates until the specified criteria are met. _(deprecated)_
- [- disallowDeferredLocationUpdates](<disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
