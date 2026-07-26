---
title: CLActivityType.automotiveNavigation
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clactivitytype/automotivenavigation
source_url: 'https://developer.apple.com/documentation/corelocation/clactivitytype/automotivenavigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clactivitytype/automotivenavigation.json'
content_hash: 'sha256:7a4e2c25e2a2a0e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLActivityType](../clactivitytype.md)

# CLActivityType.automotiveNavigation

<sub>Case</sub>

The value that indicates positioning in an automobile following a road network.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case automotiveNavigation
```

## Discussion

Use this activity type when your app is using the location manager specifically during a vehicular positioning session to track location changes to the automobile.

This activity might cause the system to pause location updates when the vehicle doesn’t move for an extended period of time.

## See Also

### Activity types

- [CLActivityTypeOther](other.md) — The value that indicates the app is using location manager for an unspecified activity.
- [CLActivityTypeFitness](fitness.md) — The value that indicates positioning during dedicated fitness sessions, such as walking workouts, running workouts, cycling workouts, and so on.
- [CLActivityTypeOtherNavigation](othernavigation.md) — The value that indicates positioning for activities that don’t or may not adhere to roads such as cycling, scooters, trains, boats and off-road vehicles.
- [CLActivityTypeAirborne](airborne.md) — The value that indicates activities in the air.
