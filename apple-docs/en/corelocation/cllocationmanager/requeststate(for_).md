---
title: 'requestState(for:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocationmanager/requeststate(for:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/requeststate(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/requeststate%28for%3A%29.json'
content_hash: 'sha256:ee8460cbe1a18daf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# requestState(for:)

<sub>Instance Method</sub>

Retrieves the state of a region asynchronously.

> [!warning] Deprecated
> Use [CLMonitor](../clmonitor-2r51v.md) to track and query the state for monitored constraints.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func requestState(for region: CLRegion)
```

## Parameters

- `region` — The region with the state you want to know. This object needs to be an instance of one of the standard region subclasses that [Core Location](../../corelocation.md) provides, such as [CLCircularRegion](../clcircularregion.md) or [CLBeaconRegion](../clbeaconregion.md). You can’t use this method to determine the state of custom regions you define yourself.

## Discussion

This method performs the request asynchronously and delivers the results to the location manager’s delegate. You must implement the [- locationManager:didDetermineState:forRegion:](<../cllocationmanagerdelegate/locationmanager(__diddeterminestate_for_).md>) method in the delegate to receive the results.

If the `region` parameter contains an unknown type of region object, this method does nothing. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Methods

- [- startMonitoringForRegion:](<startmonitoring(for_).md>) — Starts monitoring the specified region. _(deprecated)_
- [- stopMonitoringForRegion:](<stopmonitoring(for_).md>) — Stops monitoring the specified region. _(deprecated)_
- [+ regionMonitoringAvailable](<regionmonitoringavailable().md>) — Returns a Boolean value indicating whether region monitoring is supported on the current device. _(deprecated)_
- [+ regionMonitoringEnabled](<regionmonitoringenabled().md>) — Returns a Boolean value indicating whether region monitoring is currently enabled. _(deprecated)_
- [+ authorizationStatus](<authorizationstatus().md>) — Returns the app’s authorization status for using location services. _(deprecated)_
- [- startMonitoringForRegion:desiredAccuracy:](<startmonitoring(for_desiredaccuracy_).md>) — Starts monitoring the specified region for boundary crossings. _(deprecated)_
- [- startRangingBeaconsInRegion:](<startrangingbeacons(in_).md>) — Starts the delivery of notifications for the specified beacon region. _(deprecated)_
- [- stopRangingBeaconsInRegion:](<stoprangingbeacons(in_).md>) — Stops the delivery of notifications for the specified beacon region. _(deprecated)_
- [+ deferredLocationUpdatesAvailable](<deferredlocationupdatesavailable().md>) — Returns a Boolean value indicating whether the device supports deferred location updates. _(deprecated)_
- [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<allowdeferredlocationupdates(untiltraveled_timeout_).md>) — Asks the location manager to defer the delivery of location updates until the specified criteria are met. _(deprecated)_
- [- disallowDeferredLocationUpdates](<disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
