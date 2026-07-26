---
title: 'init(style:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbaritemappearance/init(style:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritemappearance/init(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritemappearance/init%28style%3A%29.json'
content_hash: 'sha256:a87fb362a8e15cea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItemAppearance](../uitabbaritemappearance.md)

# init(style:)

<sub>Initializer</sub>

Creates an appearance object with appropriate default values for a tab bar, displaying its items with the specified layout style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(style: UITabBarItemAppearance.Style)
```

## Parameters

- `style` — The layout style for the appearance attributes. UIKit uses this value to configure the default appearance attributes. For a list of possible values, see [Style](style.md).

## Return Value

A new appearance object containing appropriate default values for the specified layout style.

## See Also

### Creating a tab bar item appearance object

- [- init](<init().md>) — Creates an appearance object with default values for a stacked tab bar item.
- [- initWithCoder:](<init(coder_).md>) — Creates an appearance object from data in an unarchiver.
