---
title: leftBarButtonItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/leftbarbuttonitems
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/leftbarbuttonitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/leftbarbuttonitems.json'
content_hash: 'sha256:e2c09ae38934de2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# leftBarButtonItems

<sub>Instance Property</sub>

An array of custom bar button items to display on the left (or leading) side of the navigation bar when the navigation item is the top item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var leftBarButtonItems: [UIBarButtonItem]? { get set }
```

## Discussion

This array can contain 0 or more bar items to display on the left (or leading) side of the navigation bar. Items can include fixed-width and flexible-width spaces. If the [leftItemsSupplementBackButton](leftitemssupplementbackbutton.md) property is [true](../../swift/true.md), the items are displayed to the right (or trailing side) of the Back button, otherwise the items replace the Back button and start at the left (or leading) edge of the bar. Items are displayed left-to-right in the same order as they appear in the array. In a right-to-left user interface, the items are automatically flipped.

If there is not enough room to display all of the items in the array, those that would overlap the title view (if present) or the buttons on the right side of the bar are not displayed.

The first item in the array can also be set using the [leftBarButtonItem](leftbarbuttonitem.md) property.

## See Also

### Specifying custom views

- [centerItemGroups](centeritemgroups.md) — Customizable item groups to display in the center section of the navigation bar.
- [leadingItemGroups](leadingitemgroups.md) — Item groups to display in the leading section of the navigation bar.
- [trailingItemGroups](trailingitemgroups.md) — Item groups to display in the trailing section of the navigation bar.
- [pinnedTrailingGroup](pinnedtrailinggroup.md) — The item group to display on the trailing edge of the navigation bar, on the trailing side of the overflow and search items.
- [titleView](titleview.md) — A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [subtitleView](subtitleview.md) — A custom view to display below the title in the navigation bar.
- [largeSubtitleView](largesubtitleview.md) — A custom view to display below the large title.
- [leftBarButtonItem](leftbarbuttonitem.md) — A custom bar button item that displays on the left (or leading) edge of the navigation bar when the navigation item is the top item.
- [rightBarButtonItems](rightbarbuttonitems.md) — An array of custom bar button items to display on the right (or trailing) side of the navigation bar when the navigation item is the top item.
- [rightBarButtonItem](rightbarbuttonitem.md) — A custom bar button item that displays on the right (or trailing) edge of the navigation bar when the navigation item is the top item.
- [- setLeftBarButtonItems:animated:](<setleftbarbuttonitems(__animated_).md>) — Sets the left bar button items, optionally animating the transition to the new items.
- [- setLeftBarButtonItem:animated:](<setleftbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the new item.
- [- setRightBarButtonItems:animated:](<setrightbarbuttonitems(__animated_).md>) — Sets the right bar button items, optionally animating the transition to the new items.
- [- setRightBarButtonItem:animated:](<setrightbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the view.
