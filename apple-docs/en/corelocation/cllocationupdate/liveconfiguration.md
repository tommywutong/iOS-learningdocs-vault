---
title: CLLocationUpdate.LiveConfiguration
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationupdate/liveconfiguration
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationupdate/liveconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationupdate/liveconfiguration.json'
content_hash: 'sha256:58a502b783b025c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationUpdate](../cllocationupdate.md)

# CLLocationUpdate.LiveConfiguration

<sub>Enumeration</sub>

Values for indicating the kind of updates the framework delivers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum LiveConfiguration
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### Location types

- [CLLocationUpdate.LiveConfiguration.default](liveconfiguration/default.md) — The value that configures positioning for activities that one of the other activity types doesn’t cover.
- [CLLocationUpdate.LiveConfiguration.airborne](liveconfiguration/airborne.md) — The value that configures positioning for activities in the air.
- [CLLocationUpdate.LiveConfiguration.automotiveNavigation](liveconfiguration/automotivenavigation.md) — The value that configures positioning for an automobile following a road network.
- [CLLocationUpdate.LiveConfiguration.fitness](liveconfiguration/fitness.md) — The value that configures positioning for dedicated fitness sessions.
- [CLLocationUpdate.LiveConfiguration.otherNavigation](liveconfiguration/othernavigation.md) — The value that configures positioning for transportation that doesn’t, or may not, adhere to roads, such as cycling, scooters, trains, boats, and off-road vehicles.

### Enumeration Cases

- [CLLocationUpdate.LiveConfiguration.maritime](liveconfiguration/maritime.md)

## See Also

### Receiving location updates

- [liveUpdates(_:)](<liveupdates(__).md>) — Tells Core Location to start delivering the location updates it produces for the configuration you specify.
- [Updates](updates.md) — A structure that represents an asynchronous sequence of location updates.
