---
title: leftBarButtonItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/leftbarbuttonitem
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/leftbarbuttonitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/leftbarbuttonitem.json'
content_hash: 'sha256:3af486d4f478a34c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# leftBarButtonItem

<sub>Instance Property</sub>

A custom bar button item that displays on the left (or leading) edge of the navigation bar when the navigation item is the top item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var leftBarButtonItem: UIBarButtonItem? { get set }
```

## Discussion

The contents of this property always refer to the first bar button item in the [leftBarButtonItems](leftbarbuttonitems.md) array. Assigning a new value to this property replaces the first item in the [leftBarButtonItems](leftbarbuttonitems.md) array with the new value. Setting this property to `nil` removes the first item in the array. If the bar button item is already in the array, it is moved from its current location to the front of the array.

In a right-to-left user interface, the position of the left bar button item is automatically flipped.

## See Also

### Specifying custom views

- [centerItemGroups](centeritemgroups.md) — Customizable item groups to display in the center section of the navigation bar.
- [leadingItemGroups](leadingitemgroups.md) — Item groups to display in the leading section of the navigation bar.
- [trailingItemGroups](trailingitemgroups.md) — Item groups to display in the trailing section of the navigation bar.
- [pinnedTrailingGroup](pinnedtrailinggroup.md) — The item group to display on the trailing edge of the navigation bar, on the trailing side of the overflow and search items.
- [titleView](titleview.md) — A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [subtitleView](subtitleview.md) — A custom view to display below the title in the navigation bar.
- [largeSubtitleView](largesubtitleview.md) — A custom view to display below the large title.
- [leftBarButtonItems](leftbarbuttonitems.md) — An array of custom bar button items to display on the left (or leading) side of the navigation bar when the navigation item is the top item.
- [rightBarButtonItems](rightbarbuttonitems.md) — An array of custom bar button items to display on the right (or trailing) side of the navigation bar when the navigation item is the top item.
- [rightBarButtonItem](rightbarbuttonitem.md) — A custom bar button item that displays on the right (or trailing) edge of the navigation bar when the navigation item is the top item.
- [- setLeftBarButtonItems:animated:](<setleftbarbuttonitems(__animated_).md>) — Sets the left bar button items, optionally animating the transition to the new items.
- [- setLeftBarButtonItem:animated:](<setleftbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the new item.
- [- setRightBarButtonItems:animated:](<setrightbarbuttonitems(__animated_).md>) — Sets the right bar button items, optionally animating the transition to the new items.
- [- setRightBarButtonItem:animated:](<setrightbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the view.
