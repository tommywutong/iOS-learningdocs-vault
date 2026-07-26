---
title: regionMonitoringEnabled()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+（6.0 起废弃）, iPadOS 4.0+（6.0 起废弃）, macOS 10.8+（10.10 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/cllocationmanager/regionmonitoringenabled()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/regionmonitoringenabled()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/regionmonitoringenabled%28%29.json'
content_hash: 'sha256:7075b0b3ecf0ec46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# regionMonitoringEnabled()

<sub>Type Method</sub>

Returns a Boolean value indicating whether region monitoring is currently enabled.

> [!warning] Deprecated
> Use [+ isMonitoringAvailableForClass:](<ismonitoringavailable(for_).md>) instead.

<sub>macOS, visionOS</sub>

```swift
class func regionMonitoringEnabled() -> Bool
```

## Return Value

[true](../../swift/true.md) if region monitoring is available and is currently enabled; [false](../../swift/false.md) if it is unavailable or not enabled.

## Discussion

In iOS, the user can enable or disable location services (including region monitoring) using the controls in Settings \> Location Services.

You should check the return value of this method before starting region monitoring updates to determine whether the user currently allows location services to be used at all. If this method returns [false](../../swift/false.md) and you start region monitoring updates anyway, the Core Location framework prompts the user to confirm asking whether location services should be reenabled.

This method does not check to see if region monitoring capabilities are actually supported by the device. Therefore, you should also check the return value of the [+ regionMonitoringAvailable](<regionmonitoringavailable().md>) class method before attempting to start region monitoring services.

## See Also

### Methods

- [- startMonitoringForRegion:](<startmonitoring(for_).md>) — Starts monitoring the specified region. _(deprecated)_
- [- stopMonitoringForRegion:](<stopmonitoring(for_).md>) — Stops monitoring the specified region. _(deprecated)_
- [+ regionMonitoringAvailable](<regionmonitoringavailable().md>) — Returns a Boolean value indicating whether region monitoring is supported on the current device. _(deprecated)_
- [+ authorizationStatus](<authorizationstatus().md>) — Returns the app’s authorization status for using location services. _(deprecated)_
- [- startMonitoringForRegion:desiredAccuracy:](<startmonitoring(for_desiredaccuracy_).md>) — Starts monitoring the specified region for boundary crossings. _(deprecated)_
- [- requestStateForRegion:](<requeststate(for_).md>) — Retrieves the state of a region asynchronously. _(deprecated)_
- [- startRangingBeaconsInRegion:](<startrangingbeacons(in_).md>) — Starts the delivery of notifications for the specified beacon region. _(deprecated)_
- [- stopRangingBeaconsInRegion:](<stoprangingbeacons(in_).md>) — Stops the delivery of notifications for the specified beacon region. _(deprecated)_
- [+ deferredLocationUpdatesAvailable](<deferredlocationupdatesavailable().md>) — Returns a Boolean value indicating whether the device supports deferred location updates. _(deprecated)_
- [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<allowdeferredlocationupdates(untiltraveled_timeout_).md>) — Asks the location manager to defer the delivery of location updates until the specified criteria are met. _(deprecated)_
- [- disallowDeferredLocationUpdates](<disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
