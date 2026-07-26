---
title: title
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/title
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/title.json'
content_hash: 'sha256:d31b6c8120fe445a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# title

<sub>Instance Property</sub>

The navigation item’s title that displays in the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var title: String? { get set }
```

## Discussion

The default value is `nil`.

When the navigation item is on the navigation item stack and is second from the top — in other words, its view controller manages the views that the user would navigate back to — the value in this property is used for the back button on the top-most navigation bar. If the value of this property is `nil`, the system uses the string “Back” as the text of the back button. In iOS 11 and later, the size and position of the title is determined by the [prefersLargeTitles](../uinavigationbar/preferslargetitles.md) property of the navigation bar and the [largeTitleDisplayMode](largetitledisplaymode-swift.property.md) property of the navigation item.

## See Also

### Related Documentation

- [- initWithTitle:](<init(title_).md>) — Creates a navigation item with the specified title.
- [titleView](titleview.md) — A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [UINavigationItem](../uinavigationitem.md) — The items that a navigation bar displays when the associated view controller is visible.

### Configuring the title

- [attributedTitle](attributedtitle-25fxb.md)
- [largeTitle](largetitle.md) — String to be used as the large title.
- [largeTitleDisplayMode](largetitledisplaymode-swift.property.md) — The mode for displaying the title of the navigation bar.
- [LargeTitleDisplayMode](largetitledisplaymode-swift.enum.md) — Constants that indicate how to size the title of this item.
