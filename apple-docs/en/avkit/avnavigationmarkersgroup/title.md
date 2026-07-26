---
title: title
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avnavigationmarkersgroup/title
source_url: 'https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avnavigationmarkersgroup/title.json'
content_hash: 'sha256:f4c64ec8c7806327'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVNavigationMarkersGroup](../avnavigationmarkersgroup.md)

# title

<sub>Instance Property</sub>

The title of the marker group.

<sub>tvOS</sub>

```swift
var title: String? { get }
```

## Discussion

You set a marker group’s title with the [AVNavigationMarkersGroup](../avnavigationmarkersgroup.md) initializer. Each marker group in the [navigationMarkerGroups](../../avfoundation/avplayeritem/navigationmarkergroups.md) array of an [AVPlayerItem](../../avfoundation/avplayeritem.md) object must have a unique title. To use the marker group as a chapter list, set its title to `nil`.

## See Also

### Inspecting Navigation Metadata

- [timedNavigationMarkers](timednavigationmarkers.md) — The array of timed navigation markers for which the group provides navigation.
- [dateRangeNavigationMarkers](daterangenavigationmarkers.md) — The array of date range navigation markers for which the group provides navigation.
