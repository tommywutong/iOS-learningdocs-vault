---
title: UINavigationItem.BackButtonDisplayMode.default
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum/default
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum/default.json'
content_hash: 'sha256:c1cded49cf992386'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UINavigationItem](../../uinavigationitem.md) · [BackButtonDisplayMode](../backbuttondisplaymode-swift.enum.md)

# UINavigationItem.BackButtonDisplayMode.default

<sub>Case</sub>

The navigation item attempts to display a specific title, a generic title, or no title for the Back button, depending on the space available.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case `default`
```

## Discussion

When you set the [backButtonDisplayMode](../backbuttondisplaymode-swift.property.md) property to this value, the navigation item attempts to display these titles for its Back button in the following order:

- [backButtonTitle](../backbuttontitle.md)
- [title](../title.md)
- A generic title, such as _Back_
- No title

The navigation item selects the most appropriate title for the Back button according to the available space.

## See Also

### Constants

- [UINavigationItemBackButtonDisplayModeGeneric](generic.md) — The navigation item attempts to display a generic title or no title for the Back button, depending on the space available.
- [UINavigationItemBackButtonDisplayModeMinimal](minimal.md) — The navigation item displays the Back button indicator instead of a title.
