---
title: 'configureWithDefault(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbaritemappearance/configurewithdefault(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritemappearance/configurewithdefault(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritemappearance/configurewithdefault%28for%3A%29.json'
content_hash: 'sha256:a548ec612e3aa5c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItemAppearance](../uitabbaritemappearance.md)

# configureWithDefault(for:)

<sub>Instance Method</sub>

Configures the tab bar item appearance object with appropriate values for the specified style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func configureWithDefault(for style: UITabBarItemAppearance.Style)
```

## Parameters

- `style` — The layout style for the appearance attributes. UIKit configures the object with the default appearance attributes for the specified style. For a list of possible values, see [Style](style.md).

## See Also

### Resetting the appearance properties

- [Style](style.md) — Constants indicating the layout of a tab bar item’s content.
