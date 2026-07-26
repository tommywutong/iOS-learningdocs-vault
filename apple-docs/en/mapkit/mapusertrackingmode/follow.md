---
title: MapUserTrackingMode.follow
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+（17.0 起废弃）, iPadOS 14.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 11.0+（14.0 起废弃）, tvOS 14.0+（17.0 起废弃）, visionOS, watchOS 7.0+（10.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mapusertrackingmode/follow
source_url: 'https://developer.apple.com/documentation/mapkit/mapusertrackingmode/follow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapusertrackingmode/follow.json'
content_hash: 'sha256:165337f4d80b320d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapUserTrackingMode](../mapusertrackingmode.md)

# MapUserTrackingMode.follow

<sub>Case</sub>

The map updates by following a person’s location.

> [!warning] Deprecated
> Use Map initializers that take a `position` parameter along with\\nMapCameraPosition.userLocation to configure the user location\\ntracking behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case follow
```

## See Also

### Setting the user tracking mode

- [MapUserTrackingMode.none](none.md) — The map doesn’t update based on the person’s location. _(deprecated)_
- [MapUserTrackingMode.followWithHeading](followwithheading.md) — The map updates by following the person’s heading.
