---
title: 'setBadgeTextAttributes(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbaritem/setbadgetextattributes(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/setbadgetextattributes(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/setbadgetextattributes%28_%3Afor%3A%29.json'
content_hash: 'sha256:7273c5e4699d0b1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# setBadgeTextAttributes(_:for:)

<sub>Instance Method</sub>

Registers text attributes that the badge uses for the specified state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBadgeTextAttributes(_ textAttributes: [NSAttributedString.Key : Any]?, for state: UIControl.State)
```

## Parameters

- `textAttributes` — A dictionary of text attributes. For a list of possible attributes, see [NSAttributedString.Key](../../foundation/nsattributedstring/key.md).

- `state` — The item’s state. For possible values, see [State](../uicontrol/state-swift.struct.md).

## Discussion

The [- setTitleTextAttributes:forState:](<../uibaritem/settitletextattributes(__for_).md>) method allows you to customize the appearance of the item’s title. Use this method to apply similar customizations to the badge’s value to achieve a consistent appearance.

## See Also

### Configuring the item’s badge

- [badgeValue](badgevalue.md) — The text that the item’s badge displays.
- [badgeColor](badgecolor.md) — The background color of the item’s badge.
- [- badgeTextAttributesForState:](<badgetextattributes(for_).md>) — Returns the badge’s text attributes for the specified state.
