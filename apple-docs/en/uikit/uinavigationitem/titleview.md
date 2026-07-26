---
title: titleView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/titleview
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/titleview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/titleview.json'
content_hash: 'sha256:992d5da55b1c5353'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# titleView

<sub>Instance Property</sub>

A custom view that displays in the center of the navigation bar when the receiver is the top item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var titleView: UIView? { get set }
```

## Discussion

If this property value is `nil`, the navigation item’s title is displayed in the center of the navigation bar when the receiver is the top item. If you set this property to a custom title, it is displayed instead of the title.

Custom views can contain buttons. Use the [+ buttonWithType:](<../uibutton/init(type_).md>) method in [UIButton](../uibutton.md) class to add buttons to your custom view in the style of the navigation bar. Custom title views are centered on the navigation bar and may be resized to fit.

The default value is `nil`.

## See Also

### Specifying custom views

- [centerItemGroups](centeritemgroups.md) — Customizable item groups to display in the center section of the navigation bar.
- [leadingItemGroups](leadingitemgroups.md) — Item groups to display in the leading section of the navigation bar.
- [trailingItemGroups](trailingitemgroups.md) — Item groups to display in the trailing section of the navigation bar.
- [pinnedTrailingGroup](pinnedtrailinggroup.md) — The item group to display on the trailing edge of the navigation bar, on the trailing side of the overflow and search items.
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
