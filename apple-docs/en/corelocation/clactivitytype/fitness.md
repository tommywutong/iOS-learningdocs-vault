---
title: CLActivityType.fitness
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clactivitytype/fitness
source_url: 'https://developer.apple.com/documentation/corelocation/clactivitytype/fitness'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clactivitytype/fitness.json'
content_hash: 'sha256:2f2bf8932f2e42a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLActivityType](../clactivitytype.md)

# CLActivityType.fitness

<sub>Case</sub>

The value that indicates positioning during dedicated fitness sessions, such as walking workouts, running workouts, cycling workouts, and so on.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case fitness
```

## Discussion

For other positioning sessions that aren’t workouts, use [CLActivityTypeOtherNavigation](othernavigation.md) or [CLActivityTypeOther](other.md). This activity might cause the system to pause location updates when the user doesn’t move a significant distance over a period of time.

When [activityType](../cllocationmanager/activitytype.md) is [CLActivityTypeFitness](fitness.md), the system disables indoor positioning.

## See Also

### Activity types

- [CLActivityTypeOther](other.md) — The value that indicates the app is using location manager for an unspecified activity.
- [CLActivityTypeAutomotiveNavigation](automotivenavigation.md) — The value that indicates positioning in an automobile following a road network.
- [CLActivityTypeOtherNavigation](othernavigation.md) — The value that indicates positioning for activities that don’t or may not adhere to roads such as cycling, scooters, trains, boats and off-road vehicles.
- [CLActivityTypeAirborne](airborne.md) — The value that indicates activities in the air.
