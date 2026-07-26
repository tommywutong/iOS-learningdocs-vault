---
title: Deprecated symbols
framework: Core Location
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/deprecated-symbols
source_url: 'https://developer.apple.com/documentation/corelocation/deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/deprecated-symbols.json'
content_hash: 'sha256:2a6e423f100d16d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md) · [CLLocationManager](cllocationmanager.md)

# Deprecated symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Topics

### Properties

- [headingAvailable](cllocationmanager/headingavailable-swift.property.md) — A Boolean value indicating whether the location manager is able to generate heading-related events. _(deprecated)_
- [locationServicesEnabled](cllocationmanager/locationservicesenabled-swift.property.md) — A Boolean value indicating whether location services are enabled on the device. _(deprecated)_
- [purpose](cllocationmanager/purpose.md) — An app-provided string that describes the reason for using location services. _(deprecated)_
- [rangedRegions](cllocationmanager/rangedregions.md) — The set of regions currently being tracked using ranging. _(deprecated)_

### Methods

- [- startMonitoringForRegion:](<cllocationmanager/startmonitoring(for_).md>) — Starts monitoring the specified region. _(deprecated)_
- [- stopMonitoringForRegion:](<cllocationmanager/stopmonitoring(for_).md>) — Stops monitoring the specified region. _(deprecated)_
- [+ regionMonitoringAvailable](<cllocationmanager/regionmonitoringavailable().md>) — Returns a Boolean value indicating whether region monitoring is supported on the current device. _(deprecated)_
- [+ regionMonitoringEnabled](<cllocationmanager/regionmonitoringenabled().md>) — Returns a Boolean value indicating whether region monitoring is currently enabled. _(deprecated)_
- [+ authorizationStatus](<cllocationmanager/authorizationstatus().md>) — Returns the app’s authorization status for using location services. _(deprecated)_
- [- startMonitoringForRegion:desiredAccuracy:](<cllocationmanager/startmonitoring(for_desiredaccuracy_).md>) — Starts monitoring the specified region for boundary crossings. _(deprecated)_
- [- requestStateForRegion:](<cllocationmanager/requeststate(for_).md>) — Retrieves the state of a region asynchronously. _(deprecated)_
- [- startRangingBeaconsInRegion:](<cllocationmanager/startrangingbeacons(in_).md>) — Starts the delivery of notifications for the specified beacon region. _(deprecated)_
- [- stopRangingBeaconsInRegion:](<cllocationmanager/stoprangingbeacons(in_).md>) — Stops the delivery of notifications for the specified beacon region. _(deprecated)_
- [+ deferredLocationUpdatesAvailable](<cllocationmanager/deferredlocationupdatesavailable().md>) — Returns a Boolean value indicating whether the device supports deferred location updates. _(deprecated)_
- [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<cllocationmanager/allowdeferredlocationupdates(untiltraveled_timeout_).md>) — Asks the location manager to defer the delivery of location updates until the specified criteria are met. _(deprecated)_
- [- disallowDeferredLocationUpdates](<cllocationmanager/disallowdeferredlocationupdates().md>) — Cancels the deferral of location updates for this app. _(deprecated)_
