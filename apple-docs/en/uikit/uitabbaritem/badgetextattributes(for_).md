---
title: 'badgeTextAttributes(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbaritem/badgetextattributes(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/badgetextattributes(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/badgetextattributes%28for%3A%29.json'
content_hash: 'sha256:41878a3915db2e95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# badgeTextAttributes(for:)

<sub>Instance Method</sub>

Returns the badge’s text attributes for the specified state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func badgeTextAttributes(for state: UIControl.State) -> [NSAttributedString.Key : Any]?
```

## Parameters

- `state` — The item’s state. For possible values, see [State](../uicontrol/state-swift.struct.md).

## Discussion

Use this method to retrieve the attributes the item applies to its badge’s value for the specified state. For a list of attributes, see [NSAttributedString.Key](../../foundation/nsattributedstring/key.md).

## See Also

### Configuring the item’s badge

- [badgeValue](badgevalue.md) — The text that the item’s badge displays.
- [badgeColor](badgecolor.md) — The background color of the item’s badge.
- [- setBadgeTextAttributes:forState:](<setbadgetextattributes(__for_).md>) — Registers text attributes that the badge uses for the specified state.
