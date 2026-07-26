---
title: CLActivityType.otherNavigation
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clactivitytype/othernavigation
source_url: 'https://developer.apple.com/documentation/corelocation/clactivitytype/othernavigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clactivitytype/othernavigation.json'
content_hash: 'sha256:f14820e2d3f6e77c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLActivityType](../clactivitytype.md)

# CLActivityType.otherNavigation

<sub>Case</sub>

The value that indicates positioning for activities that don’t or may not adhere to roads such as cycling, scooters, trains, boats and off-road vehicles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case otherNavigation
```

## Discussion

Use this activity type to track a positioning session such as by boat, train, or for pedestrian navigation tracking that’s not tied to a road network, paths, or trails. You can also use it for positioning activities indoors and outdoors, such as walking, that isn’t tied to a dedicated fitness session.

This activity might cause the system to pause location updates when the vehicle doesn’t move a significant distance over a period of time.

## See Also

### Activity types

- [CLActivityTypeOther](other.md) — The value that indicates the app is using location manager for an unspecified activity.
- [CLActivityTypeAutomotiveNavigation](automotivenavigation.md) — The value that indicates positioning in an automobile following a road network.
- [CLActivityTypeFitness](fitness.md) — The value that indicates positioning during dedicated fitness sessions, such as walking workouts, running workouts, cycling workouts, and so on.
- [CLActivityTypeAirborne](airborne.md) — The value that indicates activities in the air.
