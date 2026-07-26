---
title: CLActivityType
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clactivitytype
source_url: 'https://developer.apple.com/documentation/corelocation/clactivitytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clactivitytype.json'
content_hash: 'sha256:01b7d6a6ffda0073'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLActivityType

<sub>Enumeration</sub>

Constants that indicate the type of activity associated with location updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CLActivityType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Activity types

- [CLActivityTypeOther](clactivitytype/other.md) — The value that indicates the app is using location manager for an unspecified activity.
- [CLActivityTypeAutomotiveNavigation](clactivitytype/automotivenavigation.md) — The value that indicates positioning in an automobile following a road network.
- [CLActivityTypeFitness](clactivitytype/fitness.md) — The value that indicates positioning during dedicated fitness sessions, such as walking workouts, running workouts, cycling workouts, and so on.
- [CLActivityTypeOtherNavigation](clactivitytype/othernavigation.md) — The value that indicates positioning for activities that don’t or may not adhere to roads such as cycling, scooters, trains, boats and off-road vehicles.
- [CLActivityTypeAirborne](clactivitytype/airborne.md) — The value that indicates activities in the air.

### Enumeration Cases

- [CLActivityTypeMaritime](clactivitytype/maritime.md) _(beta)_

### Initializers

- [init(rawValue:)](<clactivitytype/init(rawvalue_).md>)

## See Also

### Running the standard location service

- [- startUpdatingLocation](<cllocationmanager/startupdatinglocation().md>) — Starts the generation of updates that report the user’s current location.
- [- stopUpdatingLocation](<cllocationmanager/stopupdatinglocation().md>) — Stops the generation of location updates.
- [- requestLocation](<cllocationmanager/requestlocation().md>) — Requests the one-time delivery of the user’s current location.
- [pausesLocationUpdatesAutomatically](cllocationmanager/pauseslocationupdatesautomatically.md) — A Boolean value that indicates whether the location-manager object may pause location updates.
- [allowsBackgroundLocationUpdates](cllocationmanager/allowsbackgroundlocationupdates.md) — A Boolean value that indicates whether the app receives location updates when running in the background.
- [showsBackgroundLocationIndicator](cllocationmanager/showsbackgroundlocationindicator.md) — A Boolean value that indicates whether the status bar changes its appearance when an app uses location services in the background.
- [activityType](cllocationmanager/activitytype.md) — The type of activity the app expects the user to typically perform while in the app’s location session.
