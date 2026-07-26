---
title: MapUserTrackingMode
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+（17.0 起废弃）, iPadOS 14.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 11.0+（14.0 起废弃）, tvOS 14.0+（17.0 起废弃）, visionOS, watchOS 7.0+（10.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mapusertrackingmode
source_url: 'https://developer.apple.com/documentation/mapkit/mapusertrackingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapusertrackingmode.json'
content_hash: 'sha256:a83fd1048a56b6ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapUserTrackingMode

<sub>Enumeration</sub>

The modes available for user tracking.

> [!warning] Deprecated
> Use [Map](map.md) initializers that take a `position` parameter along with  `MapCameraPosition.userLocation` to configure how the camera follows the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum MapUserTrackingMode
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Setting the user tracking mode

- [MapUserTrackingMode.none](mapusertrackingmode/none.md) — The map doesn’t update based on the person’s location. _(deprecated)_
- [MapUserTrackingMode.follow](mapusertrackingmode/follow.md) — The map updates by following a person’s location. _(deprecated)_
- [MapUserTrackingMode.followWithHeading](mapusertrackingmode/followwithheading.md) — The map updates by following the person’s heading.
