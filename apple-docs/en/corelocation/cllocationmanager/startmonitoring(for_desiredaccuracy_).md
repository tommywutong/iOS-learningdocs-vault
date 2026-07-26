---
title: 'startMonitoring(for:desiredAccuracy:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocationmanager/startmonitoring(for:desiredaccuracy:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoring(for:desiredaccuracy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/startmonitoring%28for%3Adesiredaccuracy%3A%29.json'
content_hash: 'sha256:58afeae3b43ed012'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# startMonitoring(for:desiredAccuracy:)

<sub>Instance Method</sub>

Starts monitoring the specified region for boundary crossings.

> [!warning] Deprecated
> Use [- startMonitoringForRegion:](<startmonitoring(for_).md>) instead.

<sub>macOS</sub>

```swift
func startMonitoring(for region: CLRegion, desiredAccuracy accuracy: CLLocationAccuracy)
```

## Parameters

- `region` — The region object that defines the boundary to monitor. This parameter must not be `nil`.

- `accuracy` — The distance past the border (measured in meters) at which to generate notifications. You can use this value to prevent the delivery of multiple notifications when the user is close to the border’s edge.

## Discussion

You must call this method separately for each region you want to monitor. If an existing region with the same identifier is already being monitored by the app, the old region is replaced by the new one. The regions you add using this method are shared by all location manager objects in your app and stored in the [monitoredRegions](monitoredregions.md) property.

If you begin monitoring a region and your app is subsequently terminated, the system automatically relaunches it into the background if the region boundary is crossed. In such a case, the options dictionary passed to the [application(_:didFinishLaunchingWithOptions:)](<../../uikit/uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) method of your app delegate contains the key [location](../../uikit/uiapplication/launchoptionskey/location.md) to indicate that your app was launched because of a location-related event. In addition, creating a new location manager and assigning a delegate results in the delivery of the corresponding region messages. The newly created location manager’s [location](location.md) property also contains the current location even if location services are not enabled.

Region events are delivered to the [- locationManager:didEnterRegion:](<../cllocationmanagerdelegate/locationmanager(__didenterregion_).md>) and [- locationManager:didExitRegion:](<../cllocationmanagerdelegate/locationmanager(__didexitregion_).md>) methods of your delegate. If there is an error, the location manager calls the [- locationManager:monitoringDidFailForRegion:withError:](<../cllocationmanagerdelegate/locationmanager(__monitoringdidfailfor_witherror_).md>) method of your delegate instead.

## See Also

### Methods

- [- startMonitoringForRegion:](<startmonitoring(for_).md>) — Starts monitoring the specified region. _(deprecated)_
- [- stopMonitoringForRegion:](<stopmonitoring(for_).md>) — Stops monitoring the specified region. _(deprecated)_
- [+ regionMonitoringAvailable](<regionmonitoringavailable().md>) — Returns a Boolean value indicating whether region monitoring is supported on the current device. _(deprecated)_
- [+ regionMonitoringEnabled](<regionmonitoringenabled().md>) — Returns a Boolean value indicating whether region monitoring is currently enabled. _(deprecated)_
- [+ authorizationStatus](<authorizationstatus().md>) — Returns the app’s authorization status for using location services. _(deprecated)_
- [- requestStateForRegion:](<requeststate(for_).md>) — Retrieves the state of a region asynchronously. _(deprecated)_
- [- startRangingBeaconsInRegion:](<startrangingbeacons(in_).md>) — Starts the delivery of notifications for the specified beacon region. _(deprecated)_
- [- stopRangingBeaconsInRegion:](<stoprangingbeacons(in_).md>) — Stops the delivery of notifications for the specified beacon region. _(deprecated)_
- [+ deferredLocationUpdatesAvailable](<deferredlocationupdatesavailable().md>) — Returns a Boolean value indicating whether the device supports deferred location updates. _(deprecated)_
- [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<allowdeferredlocationupdates(untiltraveled_timeout_).md>) — Asks the location manager to defer the delivery of location updates until the specified criteria are met. _(deprecated)_
- [- disallowDeferredLocationUpdates](<disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
