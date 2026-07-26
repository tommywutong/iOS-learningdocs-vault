---
title: regionMonitoringAvailable()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, macOS 10.8+（10.10 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/cllocationmanager/regionmonitoringavailable()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/regionmonitoringavailable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/regionmonitoringavailable%28%29.json'
content_hash: 'sha256:37bfba4c91f480d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# regionMonitoringAvailable()

<sub>Type Method</sub>

Returns a Boolean value indicating whether region monitoring is supported on the current device.

> [!warning] Deprecated
> Use [+ isMonitoringAvailableForClass:](<ismonitoringavailable(for_).md>) instead.

<sub>macOS, visionOS</sub>

```swift
class func regionMonitoringAvailable() -> Bool
```

## Return Value

[true](../../swift/true.md) if region monitoring is available; [false](../../swift/false.md) if it is not.

## Discussion

Support for region monitoring may not be available on all devices and models. You should check the value of this property before attempting to set up any regions or initiate region monitoring.

Even if region monitoring support is present on a device, it may still be unavailable because the user disabled it for the current app or for all apps.

### Special Considerations

This class is deprecated in iOS 7 and later but is still supported in macOS.

## See Also

### Methods

- [- startMonitoringForRegion:](<startmonitoring(for_).md>) — Starts monitoring the specified region. _(deprecated)_
- [- stopMonitoringForRegion:](<stopmonitoring(for_).md>) — Stops monitoring the specified region. _(deprecated)_
- [+ regionMonitoringEnabled](<regionmonitoringenabled().md>) — Returns a Boolean value indicating whether region monitoring is currently enabled. _(deprecated)_
- [+ authorizationStatus](<authorizationstatus().md>) — Returns the app’s authorization status for using location services. _(deprecated)_
- [- startMonitoringForRegion:desiredAccuracy:](<startmonitoring(for_desiredaccuracy_).md>) — Starts monitoring the specified region for boundary crossings. _(deprecated)_
- [- requestStateForRegion:](<requeststate(for_).md>) — Retrieves the state of a region asynchronously. _(deprecated)_
- [- startRangingBeaconsInRegion:](<startrangingbeacons(in_).md>) — Starts the delivery of notifications for the specified beacon region. _(deprecated)_
- [- stopRangingBeaconsInRegion:](<stoprangingbeacons(in_).md>) — Stops the delivery of notifications for the specified beacon region. _(deprecated)_
- [+ deferredLocationUpdatesAvailable](<deferredlocationupdatesavailable().md>) — Returns a Boolean value indicating whether the device supports deferred location updates. _(deprecated)_
- [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<allowdeferredlocationupdates(untiltraveled_timeout_).md>) — Asks the location manager to defer the delivery of location updates until the specified criteria are met. _(deprecated)_
- [- disallowDeferredLocationUpdates](<disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
