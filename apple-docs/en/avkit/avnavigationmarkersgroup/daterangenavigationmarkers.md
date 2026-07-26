---
title: dateRangeNavigationMarkers
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avnavigationmarkersgroup/daterangenavigationmarkers
source_url: 'https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup/daterangenavigationmarkers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avnavigationmarkersgroup/daterangenavigationmarkers.json'
content_hash: 'sha256:ccd2a66fea2f2eda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVNavigationMarkersGroup](../avnavigationmarkersgroup.md)

# dateRangeNavigationMarkers

<sub>Instance Property</sub>

The array of date range navigation markers for which the group provides navigation.

<sub>tvOS</sub>

```swift
var dateRangeNavigationMarkers: [AVDateRangeMetadataGroup]? { get }
```

## Discussion

Returns the array of [AVDateRangeMetadataGroup](../../avfoundation/avdaterangemetadatagroup.md) objects managed by this group. This value may be `nil`.

## See Also

### Inspecting Navigation Metadata

- [title](title.md) — The title of the marker group.
- [timedNavigationMarkers](timednavigationmarkers.md) — The array of timed navigation markers for which the group provides navigation.
