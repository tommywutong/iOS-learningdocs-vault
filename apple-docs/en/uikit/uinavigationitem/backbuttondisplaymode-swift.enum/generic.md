---
title: UINavigationItem.BackButtonDisplayMode.generic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum/generic
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum/generic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum/generic.json'
content_hash: 'sha256:a19c881cefeae692'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UINavigationItem](../../uinavigationitem.md) · [BackButtonDisplayMode](../backbuttondisplaymode-swift.enum.md)

# UINavigationItem.BackButtonDisplayMode.generic

<sub>Case</sub>

The navigation item attempts to display a generic title or no title for the Back button, depending on the space available.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case generic
```

## Discussion

When you set the [backButtonDisplayMode](../backbuttondisplaymode-swift.property.md) property to this value, the navigation item attempts to display these titles for its Back button in the following order:

- A generic title, such as _Back_
- No title

The navigation item selects the most appropriate title for the Back button according to the available space. This display mode ignores the values of the [title](../title.md) and [backButtonTitle](../backbuttontitle.md) properties.

## See Also

### Constants

- [UINavigationItemBackButtonDisplayModeDefault](default.md) — The navigation item attempts to display a specific title, a generic title, or no title for the Back button, depending on the space available.
- [UINavigationItemBackButtonDisplayModeMinimal](minimal.md) — The navigation item displays the Back button indicator instead of a title.
