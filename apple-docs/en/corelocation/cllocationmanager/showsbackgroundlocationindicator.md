---
title: showsBackgroundLocationIndicator
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/showsbackgroundlocationindicator
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/showsbackgroundlocationindicator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/showsbackgroundlocationindicator.json'
content_hash: 'sha256:73a40326b0f44433'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# showsBackgroundLocationIndicator

<sub>Instance Property</sub>

A Boolean value that indicates whether the status bar changes its appearance when an app uses location services in the background.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var showsBackgroundLocationIndicator: Bool { get set }
```

## Discussion

The default value of this property is `false`. The background location usage indicator is a blue bar or a blue pill in the status bar on iOS; on watchOS the indicator is a small icon. Users can tap the indicator to return to your app.

This property affects only apps that received Always authorization. When such an app moves to the background, the system uses this property to determine whether to change the status bar appearance to indicate that location services are in use. Set this value to `true` to maintain transparency with the user.

For apps with When In Use authorization, the system changes the appearance of the status bar when the app uses location services in the background.

For more information, see [Handling location updates in the background](../handling-location-updates-in-the-background.md).

## See Also

### Running the standard location service

- [- startUpdatingLocation](<startupdatinglocation().md>) — Starts the generation of updates that report the user’s current location.
- [- stopUpdatingLocation](<stopupdatinglocation().md>) — Stops the generation of location updates.
- [- requestLocation](<requestlocation().md>) — Requests the one-time delivery of the user’s current location.
- [pausesLocationUpdatesAutomatically](pauseslocationupdatesautomatically.md) — A Boolean value that indicates whether the location-manager object may pause location updates.
- [allowsBackgroundLocationUpdates](allowsbackgroundlocationupdates.md) — A Boolean value that indicates whether the app receives location updates when running in the background.
- [activityType](activitytype.md) — The type of activity the app expects the user to typically perform while in the app’s location session.
- [CLActivityType](../clactivitytype.md) — Constants that indicate the type of activity associated with location updates.
