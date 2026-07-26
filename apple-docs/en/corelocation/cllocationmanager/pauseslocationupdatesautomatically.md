---
title: pausesLocationUpdatesAutomatically
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/pauseslocationupdatesautomatically
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/pauseslocationupdatesautomatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/pauseslocationupdatesautomatically.json'
content_hash: 'sha256:55bc8beee2c2a8ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# pausesLocationUpdatesAutomatically

<sub>Instance Property</sub>

A Boolean value that indicates whether the location-manager object may pause location updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var pausesLocationUpdatesAutomatically: Bool { get set }
```

## Discussion

Allowing the location manager to pause updates can improve battery life on the target device without sacrificing location data. Setting this property to [true](../../swift/true.md) causes the location manager to pause updates (and powers down the appropriate hardware) at times when the location data is unlikely to change. For example, if the user stops for food while using a navigation app, the location manager might pause updates for a period of time. You can help the determination of when to pause location updates by assigning a value to the [activityType](activitytype.md) property.

After a pause occurs, it’s your responsibility to restart location services again when you determine that they’re needed. Core Location calls the [- locationManagerDidPauseLocationUpdates:](<../cllocationmanagerdelegate/locationmanagerdidpauselocationupdates(__).md>) method of your location manager’s delegate to let you know that a pause has occurred. In that method configure a local notification that has a [UNLocationNotificationTrigger](../../usernotifications/unlocationnotificationtrigger.md) to notify when the user exits the current region. The message for the local notification should prompt the user to launch your app again so that it can resume updates.

> [!important] Important
> For apps that have in-use authorization, a pause to location updates ends access to location changes until the app launches again and is able to restart those updates. To prevent location updates from stopping entirely, consider disabling this property and changing location accuracy to [kCLLocationAccuracyThreeKilometers](../kcllocationaccuracythreekilometers.md) when your app moves to the background. This allows your app to continue receiving location updates in a power-friendly manner.

On supported platforms the default value of this property is [true](../../swift/true.md); otherwise the default value is [false](../../swift/false.md) and is immutable.

## See Also

### Running the standard location service

- [- startUpdatingLocation](<startupdatinglocation().md>) — Starts the generation of updates that report the user’s current location.
- [- stopUpdatingLocation](<stopupdatinglocation().md>) — Stops the generation of location updates.
- [- requestLocation](<requestlocation().md>) — Requests the one-time delivery of the user’s current location.
- [allowsBackgroundLocationUpdates](allowsbackgroundlocationupdates.md) — A Boolean value that indicates whether the app receives location updates when running in the background.
- [showsBackgroundLocationIndicator](showsbackgroundlocationindicator.md) — A Boolean value that indicates whether the status bar changes its appearance when an app uses location services in the background.
- [activityType](activitytype.md) — The type of activity the app expects the user to typically perform while in the app’s location session.
- [CLActivityType](../clactivitytype.md) — Constants that indicate the type of activity associated with location updates.
