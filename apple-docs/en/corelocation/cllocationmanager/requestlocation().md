---
title: requestLocation()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/requestlocation()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/requestlocation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/requestlocation%28%29.json'
content_hash: 'sha256:145591a84352f15f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# requestLocation()

<sub>Instance Method</sub>

Requests the one-time delivery of the user’s current location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func requestLocation()
```

## Discussion

This method returns immediately. Calling it causes the location manager to obtain a location fix (which may take several seconds) and call the delegate’s [- locationManager:didUpdateLocations:](<../cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) method with the result. The location fix is obtained at the accuracy level indicated by the [desiredAccuracy](desiredaccuracy.md) property. Only one location fix is reported to the delegate, after which location services are stopped. If a location fix cannot be determined in a timely manner, the location manager calls the delegate’s [- locationManager:didFailWithError:](<../cllocationmanagerdelegate/locationmanager(__didfailwitherror_).md>) method instead and reports a [kCLErrorLocationUnknown](../clerror-swift.struct/code/locationunknown.md) error.

Use this method when you want the user’s current location but do not need to leave location services running. This method starts location services long enough to return a result or report an error and then stops them again. Calling the [- startUpdatingLocation](<startupdatinglocation().md>) or  [- allowDeferredLocationUpdatesUntilTraveled:timeout:](<allowdeferredlocationupdates(untiltraveled_timeout_).md>) method cancels any pending request made using this method. Calling this method while location services are already running does nothing. To cancel a pending request, call the [- stopUpdatingLocation](<stopupdatinglocation().md>) method.

If obtaining the desired accuracy would take too long, the location manager delivers a less accurate location value rather than reporting an error.

When using this method, the associated delegate must implement the [- locationManager:didUpdateLocations:](<../cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) and [- locationManager:didFailWithError:](<../cllocationmanagerdelegate/locationmanager(__didfailwitherror_).md>) methods. Failure to do so is a programmer error.

## See Also

### Running the standard location service

- [- startUpdatingLocation](<startupdatinglocation().md>) — Starts the generation of updates that report the user’s current location.
- [- stopUpdatingLocation](<stopupdatinglocation().md>) — Stops the generation of location updates.
- [pausesLocationUpdatesAutomatically](pauseslocationupdatesautomatically.md) — A Boolean value that indicates whether the location-manager object may pause location updates.
- [allowsBackgroundLocationUpdates](allowsbackgroundlocationupdates.md) — A Boolean value that indicates whether the app receives location updates when running in the background.
- [showsBackgroundLocationIndicator](showsbackgroundlocationindicator.md) — A Boolean value that indicates whether the status bar changes its appearance when an app uses location services in the background.
- [activityType](activitytype.md) — The type of activity the app expects the user to typically perform while in the app’s location session.
- [CLActivityType](../clactivitytype.md) — Constants that indicate the type of activity associated with location updates.
