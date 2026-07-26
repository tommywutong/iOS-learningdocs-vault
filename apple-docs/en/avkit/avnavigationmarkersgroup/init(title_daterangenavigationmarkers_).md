---
title: 'init(title:dateRangeNavigationMarkers:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avnavigationmarkersgroup/init(title:daterangenavigationmarkers:)'
source_url: 'https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup/init(title:daterangenavigationmarkers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avnavigationmarkersgroup/init%28title%3Adaterangenavigationmarkers%3A%29.json'
content_hash: 'sha256:9f21adfc739d0b0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVNavigationMarkersGroup](../avnavigationmarkersgroup.md)

# init(title:dateRangeNavigationMarkers:)

<sub>Initializer</sub>

Initializes a navigation markers group with the specified title and array of date range navigation markers.

<sub>tvOS</sub>

```swift
init(title: String?, dateRangeNavigationMarkers navigationMarkers: [AVDateRangeMetadataGroup])
```

## Parameters

- `title` — The title to present for the markers group.

- `navigationMarkers` — The array of date range navigation markers for which the group provides navigation.

## Return Value

A new navigation markers group.

## Discussion

To associate marker groups with an asset for playback, use the [navigationMarkerGroups](../../avfoundation/avplayeritem/navigationmarkergroups.md) property of an [AVPlayerItem](../../avfoundation/avplayeritem.md) object.

To create a chapter list, pass `nil` for the `title` parameter and set the group as the first item in the player item’s [navigationMarkerGroups](../../avfoundation/avplayeritem/navigationmarkergroups.md) array. To provide additional options for navigating media (such as a “Goals Scored” group for a recorded sporting event), provide a unique `title` value for each marker group in the array.

## See Also

### Creating a Navigation Marker Group

- [- initWithTitle:timedNavigationMarkers:](<init(title_timednavigationmarkers_).md>) — Initializes a navigation markers group with the specified title and array of timed navigation markers.
