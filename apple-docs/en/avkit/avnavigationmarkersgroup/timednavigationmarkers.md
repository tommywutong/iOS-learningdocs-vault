---
title: timedNavigationMarkers
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avnavigationmarkersgroup/timednavigationmarkers
source_url: 'https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup/timednavigationmarkers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avnavigationmarkersgroup/timednavigationmarkers.json'
content_hash: 'sha256:bffea3856791328e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVNavigationMarkersGroup](../avnavigationmarkersgroup.md)

# timedNavigationMarkers

<sub>Instance Property</sub>

The array of timed navigation markers for which the group provides navigation.

<sub>tvOS</sub>

```swift
var timedNavigationMarkers: [AVTimedMetadataGroup]? { get }
```

## Discussion

Returns the array of [AVTimedMetadataGroup](../../avfoundation/avtimedmetadatagroup.md) objects managed by this group. This value may be `nil`.

## See Also

### Inspecting Navigation Metadata

- [title](title.md) — The title of the marker group.
- [dateRangeNavigationMarkers](daterangenavigationmarkers.md) — The array of date range navigation markers for which the group provides navigation.
