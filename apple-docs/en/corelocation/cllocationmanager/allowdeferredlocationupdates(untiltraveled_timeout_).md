---
title: 'allowDeferredLocationUpdates(untilTraveled:timeout:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（13.0 起废弃）, iPadOS 6.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.15+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocationmanager/allowdeferredlocationupdates(untiltraveled:timeout:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/allowdeferredlocationupdates(untiltraveled:timeout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/allowdeferredlocationupdates%28untiltraveled%3Atimeout%3A%29.json'
content_hash: 'sha256:3b955a4e3b8fc7bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# allowDeferredLocationUpdates(untilTraveled:timeout:)

<sub>Instance Method</sub>

Asks the location manager to defer the delivery of location updates until the specified criteria are met.

> [!warning] Deprecated
> You can remove calls to this method

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func allowDeferredLocationUpdates(untilTraveled distance: CLLocationDistance, timeout: TimeInterval)
```

## Parameters

- `distance` — The distance (in meters) from the current location that must be travelled before event delivery resumes. To specify an unlimited distance, pass the [CLLocationDistanceMax](../cllocationdistancemax.md) constant.

- `timeout` — The amount of time (in seconds) from the current time that must pass before event delivery resumes. To specify an unlimited amount of time, pass the [CLTimeIntervalMax](../cltimeintervalmax.md) constant.

## Discussion

Call this method in situations where you want location data with GPS accuracy but do not need to process that data right away. If your app is in the background and the system is able to optimize its power usage, the location manager tells the GPS hardware to store new locations internally until the specified distance or timeout conditions are met. When one or both criteria are met, the location manager ends deferred locations by calling the [- locationManager:didFinishDeferredUpdatesWithError:](<../cllocationmanagerdelegate/locationmanager(__didfinishdeferredupdateswitherror_).md>) method of its delegate and delivers the cached locations to the  [- locationManager:didUpdateLocations:](<../cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) method. If your app is in the foreground, the location manager does not defer the deliver of events but does monitor for the specified criteria. If your app moves to the background before the criteria are met, the location manager may begin deferring the delivery of events.

> [!important] Important
> Because deferred updates use the GPS to track location changes, the location manager allows deferred updates only when GPS hardware is available on the device and when the desired accuracy is set to [kCLLocationAccuracyBest](../kcllocationaccuracybest.md) or [kCLLocationAccuracyBestForNavigation](../kcllocationaccuracybestfornavigation.md). If the GPS hardware is not available, the location manager reports a [kCLErrorDeferredFailed](../clerror-swift.struct/code/deferredfailed.md) error. If the accuracy is not set to one of the supported values, the location manager reports a [kCLErrorDeferredAccuracyTooLow](../clerror-swift.struct/code/deferredaccuracytoolow.md) error.
>
> In addition, the [distanceFilter](distancefilter.md) property of the location manager must be set to [kCLDistanceFilterNone](../kcldistancefilternone.md). If it is set to any other value, the location manager reports a [kCLErrorDeferredDistanceFiltered](../clerror-swift.struct/code/deferreddistancefiltered.md) error.

Start the delivery of location updates before calling this method. The most common place to call this method is in your delegate’s [- locationManager:didUpdateLocations:](<../cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) method. After processing any new locations, call this method if you want to defer future updates until the distance or time criteria are met. If new events arrive and your app is in the background, the events are cached and their delivery is deferred appropriately.

Your delegate’s [- locationManager:didFinishDeferredUpdatesWithError:](<../cllocationmanagerdelegate/locationmanager(__didfinishdeferredupdateswitherror_).md>) method is called exactly once for each time you call this method. If you call this method twice in succession, the location manager cancels the previous deferral before starting the new one. Therefore, you should keep track of whether updates are currently deferred and avoid calling this method multiple times in succession. If you want to change the deferral criteria for any reason, and therefore call this method again, be prepared to receive a [kCLErrorDeferredCanceled](../clerror-swift.struct/code/deferredcanceled.md) error in your delegate’s [- locationManager:didFinishDeferredUpdatesWithError:](<../cllocationmanagerdelegate/locationmanager(__didfinishdeferredupdateswitherror_).md>) method.

After calling this method, the location manager may deliver location updates even if the specified distance and timeout criteria are not met. For example, if the caches used to store deferred samples become full, the location manager may deliver the cached samples so it can collect new ones. The delivery of samples does not automatically end deferred mode for your app. The location manager resumes deferred mode when it is able to do so.

Deferred updates are delivered only when the system enters a low power state. Deferred updates do not occur during debugging because Xcode prevents your app from sleeping and thus prevents the system from entering that low power state.

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
- [+ deferredLocationUpdatesAvailable](<deferredlocationupdatesavailable().md>) — Returns a Boolean value indicating whether the device supports deferred location updates. _(deprecated)_
- [- disallowDeferredLocationUpdates](<disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
