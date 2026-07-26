---
title: startUpdatingLocation()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/startupdatinglocation()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/startupdatinglocation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/startupdatinglocation%28%29.json'
content_hash: 'sha256:6529c1542398ac3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# startUpdatingLocation()

<sub>Instance Method</sub>

Starts the generation of updates that report the user’s current location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func startUpdatingLocation()
```

## Discussion

This method returns immediately. Calling this method causes the location manager to obtain an initial location fix (which may take several seconds) and notify your delegate by calling its [- locationManager:didUpdateLocations:](<../cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) method. After that, the receiver generates update events primarily when the value in the [distanceFilter](distancefilter.md) property is exceeded. Updates may be delivered in other situations though. For example, the receiver may send another notification if the hardware gathers a more accurate location reading.

Calling this method several times in succession does not automatically result in new events being generated. Calling [- stopUpdatingLocation](<stopupdatinglocation().md>) in between, however, does cause a new initial event to be sent the next time you call this method.

If you start this service and your app is suspended, the system stops the delivery of events until your app starts running again (either in the foreground or background). If your app is terminated, the delivery of new location events stops altogether. Therefore, if your app needs to receive location events while in the background, it must include the `UIBackgroundModes` key (with the `location` value) in its `Info.plist` file.

In addition to your delegate object implementing the [- locationManager:didUpdateLocations:](<../cllocationmanagerdelegate/locationmanager(__didupdatelocations_).md>) method, it should also implement the [- locationManager:didFailWithError:](<../cllocationmanagerdelegate/locationmanager(__didfailwitherror_).md>) method to respond to potential errors.

## See Also

### Running the standard location service

- [- stopUpdatingLocation](<stopupdatinglocation().md>) — Stops the generation of location updates.
- [- requestLocation](<requestlocation().md>) — Requests the one-time delivery of the user’s current location.
- [pausesLocationUpdatesAutomatically](pauseslocationupdatesautomatically.md) — A Boolean value that indicates whether the location-manager object may pause location updates.
- [allowsBackgroundLocationUpdates](allowsbackgroundlocationupdates.md) — A Boolean value that indicates whether the app receives location updates when running in the background.
- [showsBackgroundLocationIndicator](showsbackgroundlocationindicator.md) — A Boolean value that indicates whether the status bar changes its appearance when an app uses location services in the background.
- [activityType](activitytype.md) — The type of activity the app expects the user to typically perform while in the app’s location session.
- [CLActivityType](../clactivitytype.md) — Constants that indicate the type of activity associated with location updates.
