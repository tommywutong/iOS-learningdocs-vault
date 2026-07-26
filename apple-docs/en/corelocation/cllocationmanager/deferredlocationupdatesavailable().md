---
title: deferredLocationUpdatesAvailable()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+（13.0 起废弃）, iPadOS 6.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/cllocationmanager/deferredlocationupdatesavailable()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/deferredlocationupdatesavailable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/deferredlocationupdatesavailable%28%29.json'
content_hash: 'sha256:ae6b49b493763f6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# deferredLocationUpdatesAvailable()

<sub>Type Method</sub>

Returns a Boolean value indicating whether the device supports deferred location updates.

> [!warning] Deprecated
> You can remove calls to this method

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class func deferredLocationUpdatesAvailable() -> Bool
```

## Return Value

[true](../../swift/true.md) if the device supports deferred location updates or [false](../../swift/false.md) if it does not.

## Discussion

Deferred location updates are a way for the location manager to avoid frequently waking up a background app to deliver location changes. Normally, when an app wants location updates in the background, the app must be woken up whenever a new event arrives. Waking up the app consumes power, which in some situations might be wasted if the app cannot do anything with the location information other than log it and go back to sleep anyway. Deferring location updates gives you the ability to wait until a time when your app can do something useful with the data and then process the updates all at once.

Deferred location updates require the presence of GPS hardware and may not be supported on all iOS devices.

## See Also

### Methods

- [- startMonitoringForRegion:](<startmonitoring(for_).md>) — Starts monitoring the specified region. _(deprecated)_
- [- stopMonitoringForRegion:](<stopmonitoring(for_).md>) — Stops monitoring the specified region. _(deprecated)_
- [+ regionMonitoringAvailable](<regionmonitoringavailable().md>) — Returns a Boolean value indicating whether region monitoring is supported on the current device. _(deprecated)_
- [+ regionMonitoringEnabled](<regionmonitoringenabled().md>) — Returns a Boolean value indicating whether region monitoring is currently enabled. _(deprecated)_
- [+ authorizationStatus](<authorizationstatus().md>) — Returns the app’s authorization status for using location services. _(deprecated)_
- [- startMonitoringForRegion:desiredAccuracy:](<startmonitoring(for_desiredaccuracy_).md>) — Starts monitoring the specified region for boundary crossings. _(deprecated)_
- [- requestStateForRegion:](<requeststate(for_).md>) — Retrieves the state of a region asynchronously. _(deprecated)_
- [- startRangingBeaconsInRegion:](<startrangingbeacons(in_).md>) — Starts the delivery of notifications for the specified beacon region. _(deprecated)_
- [- stopRangingBeaconsInRegion:](<stoprangingbeacons(in_).md>) — Stops the delivery of notifications for the specified beacon region. _(deprecated)_
- [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<allowdeferredlocationupdates(untiltraveled_timeout_).md>) — Asks the location manager to defer the delivery of location updates until the specified criteria are met. _(deprecated)_
- [- disallowDeferredLocationUpdates](<disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
