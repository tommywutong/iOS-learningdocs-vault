---
title: pinnedTrailingGroup
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/pinnedtrailinggroup
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/pinnedtrailinggroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/pinnedtrailinggroup.json'
content_hash: 'sha256:4143227785e3d04d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# pinnedTrailingGroup

<sub>Instance Property</sub>

The item group to display on the trailing edge of the navigation bar, on the trailing side of the overflow and search items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var pinnedTrailingGroup: UIBarButtonItemGroup? { get set }
```

## Discussion

This group can’t move to the overflow menu. If there’s more than one item in this group, assign a [representativeItem](../uibarbuttonitemgroup/representativeitem.md) for the group to avoid overflowing the contents of the navigation bar.

## See Also

### Specifying custom views

- [centerItemGroups](centeritemgroups.md) — Customizable item groups to display in the center section of the navigation bar.
- [leadingItemGroups](leadingitemgroups.md) — Item groups to display in the leading section of the navigation bar.
- [trailingItemGroups](trailingitemgroups.md) — Item groups to display in the trailing section of the navigation bar.
- [titleView](titleview.md) — A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [subtitleView](subtitleview.md) — A custom view to display below the title in the navigation bar.
- [largeSubtitleView](largesubtitleview.md) — A custom view to display below the large title.
- [leftBarButtonItems](leftbarbuttonitems.md) — An array of custom bar button items to display on the left (or leading) side of the navigation bar when the navigation item is the top item.
- [leftBarButtonItem](leftbarbuttonitem.md) — A custom bar button item that displays on the left (or leading) edge of the navigation bar when the navigation item is the top item.
- [rightBarButtonItems](rightbarbuttonitems.md) — An array of custom bar button items to display on the right (or trailing) side of the navigation bar when the navigation item is the top item.
- [rightBarButtonItem](rightbarbuttonitem.md) — A custom bar button item that displays on the right (or trailing) edge of the navigation bar when the navigation item is the top item.
- [- setLeftBarButtonItems:animated:](<setleftbarbuttonitems(__animated_).md>) — Sets the left bar button items, optionally animating the transition to the new items.
- [- setLeftBarButtonItem:animated:](<setleftbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the new item.
- [- setRightBarButtonItems:animated:](<setrightbarbuttonitems(__animated_).md>) — Sets the right bar button items, optionally animating the transition to the new items.
- [- setRightBarButtonItem:animated:](<setrightbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the view.
