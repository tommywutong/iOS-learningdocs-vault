---
title: navigationMarkerGroups
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/navigationmarkergroups
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/navigationmarkergroups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/navigationmarkergroups.json'
content_hash: 'sha256:ec874a4b25b410c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# navigationMarkerGroups

<sub>Instance Property</sub>

The time marker groups that provide ways to navigate the player item’s content.

<sub>tvOS</sub>

```swift
var navigationMarkerGroups: [AVNavigationMarkersGroup] { get set }
```

## Discussion

A navigation marker group provides a set of time markers for navigating playback. The most common form of navigation marker group is a chapter list; however, you can also provide other sets of markers to allow a user to jump to significant events in the presentation. For example, a “Goals Scored” marker group might summarize key moments in a recorded sporting event. When you present a player item containing marker groups with the [AVPlayerViewController](../../avkit/avplayerviewcontroller.md) class, the user interface provides options for navigating each group.

To provide a chapter list, use the first item in the [navigationMarkerGroups](navigationmarkergroups.md) array and set its title property to `nil`. To provide additional or alternate means of navigating content, use a unique title value for each navigation marker group in the array.

## See Also

### Configuring player items for AVKit

- [nextContentProposal](nextcontentproposal.md) — The item proposed to follow the current content.
