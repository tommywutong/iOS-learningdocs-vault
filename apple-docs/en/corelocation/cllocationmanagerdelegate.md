---
title: CLLocationManagerDelegate
framework: Core Location
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanagerdelegate
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate.json'
content_hash: 'sha256:9b61fde81f64cf1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationManagerDelegate

<sub>Protocol</sub>

The methods you use to receive events from an associated location-manager object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CLLocationManagerDelegate : NSObjectProtocol
```

## Overview

The location manager calls its delegate’s methods to report location-related events to your app. Implement this protocol in an app-specific object and use the methods to update your app. For example, you might use the current location to update the user’s position on a map or you might return search results relevant only to the user’s current location.

> [!important] Important
> Always implement the methods for handling any potential failures in addition to the methods for receiving location-related data.

Assign your delegate object to the [delegate](cllocationmanager/delegate.md) property of the [CLLocationManager](cllocationmanager.md) object before starting any services. Core Location may report a cached value to your delegate immediately after you start the service, followed by a more current value later. Check the time stamp of any data objects you receive before using them.

Core Location calls the methods of your delegate object on the runloop from the thread on which you initialized [CLLocationManager](cllocationmanager.md). That thread must itself have an active run loop, like the one found in your app’s main thread.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to authorization changes

- [- locationManagerDidChangeAuthorization:](<cllocationmanagerdelegate/locationmanagerdidchangeauthorization(__).md>) — Tells the delegate when the app creates the location manager and when the authorization status changes.
- [- locationManager:didChangeAuthorizationStatus:](<cllocationmanagerdelegate/locationmanager(__didchangeauthorization_).md>) — Tells the delegate its authorization status when the app creates the location manager and when the authorization status changes. _(deprecated)_

### Handling errors

- [- locationManager:didFailWithError:](<cllocationmanagerdelegate/locationmanager(__didfailwitherror_).md>) — Tells the delegate that the location manager was unable to retrieve a location value.

### Receiving location updates

- [- locationManager:didUpdateLocations:](<cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) — Tells the delegate that new location data is available.
- [- locationManager:didUpdateToLocation:fromLocation:](<cllocationmanagerdelegate/locationmanager(__didupdateto_from_).md>) — Tells the delegate that a new location value is available. _(deprecated)_
- [- locationManager:didFinishDeferredUpdatesWithError:](<cllocationmanagerdelegate/locationmanager(__didfinishdeferredupdateswitherror_).md>) — Tells the delegate that updates will no longer be deferred.

### Pausing location updates

- [- locationManagerDidPauseLocationUpdates:](<cllocationmanagerdelegate/locationmanagerdidpauselocationupdates(__).md>) — Tells the delegate that location updates were paused.
- [- locationManagerDidResumeLocationUpdates:](<cllocationmanagerdelegate/locationmanagerdidresumelocationupdates(__).md>) — Tells the delegate that the delivery of location updates has resumed.

### Receiving visit updates

- [- locationManager:didVisit:](<cllocationmanagerdelegate/locationmanager(__didvisit_).md>) — Tells the delegate that a new visit-related event was received.

### Receiving heading updates

- [- locationManager:didUpdateHeading:](<cllocationmanagerdelegate/locationmanager(__didupdateheading_).md>) — Tells the delegate that the location manager received updated heading information.
- [- locationManagerShouldDisplayHeadingCalibration:](<cllocationmanagerdelegate/locationmanagershoulddisplayheadingcalibration(__).md>) — Asks the delegate whether the heading calibration alert should be displayed.

### Receiving region-related updates

- [- locationManager:didEnterRegion:](<cllocationmanagerdelegate/locationmanager(__didenterregion_).md>) — Tells the delegate that the user entered the specified region.
- [- locationManager:didExitRegion:](<cllocationmanagerdelegate/locationmanager(__didexitregion_).md>) — Tells the delegate that the user left the specified region.
- [- locationManager:didDetermineState:forRegion:](<cllocationmanagerdelegate/locationmanager(__diddeterminestate_for_).md>) — Tells the delegate about the state of the specified region.
- [- locationManager:monitoringDidFailForRegion:withError:](<cllocationmanagerdelegate/locationmanager(__monitoringdidfailfor_witherror_).md>) — Tells the delegate that a region monitoring error occurred.
- [- locationManager:didStartMonitoringForRegion:](<cllocationmanagerdelegate/locationmanager(__didstartmonitoringfor_).md>) — Tells the delegate that a new region is being monitored.
- [CLRegionState](clregionstate.md) — Constants that reflect the relationship of the current location to the region boundaries.

### Receiving beacon-related updates

- [- locationManager:didRangeBeacons:satisfyingConstraint:](<cllocationmanagerdelegate/locationmanager(__didrange_satisfying_).md>) — Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [- locationManager:didFailRangingBeaconsForConstraint:error:](<cllocationmanagerdelegate/locationmanager(__didfailrangingfor_error_).md>) — Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.
- [- locationManager:didRangeBeacons:inRegion:](<cllocationmanagerdelegate/locationmanager(__didrangebeacons_in_).md>) — Tells the delegate that one or more beacons are in range. _(deprecated)_
- [- locationManager:rangingBeaconsDidFailForRegion:withError:](<cllocationmanagerdelegate/locationmanager(__rangingbeaconsdidfailfor_witherror_).md>) — Tells the delegate that an error occurred while gathering ranging information for a set of beacons. _(deprecated)_

## See Also

### Receiving data from location services

- [delegate](cllocationmanager/delegate.md) — The delegate object to receive update events.
