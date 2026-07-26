---
title: UITabBarItemStateAppearance
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritemstateappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritemstateappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritemstateappearance.json'
content_hash: 'sha256:bcd185683fed4c76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITabBarItemStateAppearance

<sub>Class</sub>

A data object containing the specific customizations for tab bar items in a particular state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITabBarItemStateAppearance
```

## Overview

Use a [UITabBarItemStateAppearance](uitabbaritemstateappearance.md) object to customize the appearance of your tab bar items and the badges they display. Don’t create [UITabBarItemStateAppearance](uitabbaritemstateappearance.md) objects yourself. Instead, create a [UITabBarItemAppearance](uitabbaritemappearance.md) object and use its properties to fetch the appearance attributes for tab bar items in a particular state. For example, to set the attributes for items in the normal state, configure the object in the [normal](uitabbaritemappearance/normal.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Configuring the item’s title

- [titleTextAttributes](uitabbaritemstateappearance/titletextattributes.md) — String attributes to apply to the text of the tab bar item’s title.
- [titlePositionAdjustment](uitabbaritemstateappearance/titlepositionadjustment.md) — The additional amount by which to offset the title horizontally and vertically.

### Tinting the item’s icon

- [iconColor](uitabbaritemstateappearance/iconcolor.md) — The color of item icons.

### Configuring the badge appearance

- [badgeTextAttributes](uitabbaritemstateappearance/badgetextattributes.md) — String attributes to apply to the text of the item’s badge.
- [badgeBackgroundColor](uitabbaritemstateappearance/badgebackgroundcolor.md) — The background color of the badge.
- [badgeTitlePositionAdjustment](uitabbaritemstateappearance/badgetitlepositionadjustment.md) — The additional amount by which to offset the badge’s title horizontally and vertically.
- [badgePositionAdjustment](uitabbaritemstateappearance/badgepositionadjustment.md) — The additional amount by which to offset the badge horizontally and vertically.

## See Also

### Tab bar appearance

- [UITabBarAppearance](uitabbarappearance.md) — An object for customizing the appearance of a tab bar.
- [UITabBarItemAppearance](uitabbaritemappearance.md) — An object for customizing the appearance of tab bar items.
