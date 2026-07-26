---
title: UITabBarAppearance
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarappearance.json'
content_hash: 'sha256:ef40726b7dac9435'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITabBarAppearance

<sub>Class</sub>

An object for customizing the appearance of a tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITabBarAppearance
```

## Overview

After creating a [UITabBarAppearance](uitabbarappearance.md) object, use the methods and properties of this class to specify the appearance of items in the tab bar. Use the inherited properties from [UIBarAppearance](uibarappearance.md) to configure the background and shadow attributes of the tab bar itself.

## Relationships

- **Inherits From**: [UIBarAppearance](uibarappearance.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring stacked item appearances

- [stackedLayoutAppearance](uitabbarappearance/stackedlayoutappearance.md) — The appearance attributes for items with a stacked layout.
- [stackedItemPositioning](uitabbarappearance/stackeditempositioning.md) — The scheme to use when positioning stacked items within the tab bar.
- [stackedItemSpacing](uitabbarappearance/stackeditemspacing.md) — The amount of space to insert between stacked tab bar items.
- [stackedItemWidth](uitabbarappearance/stackeditemwidth.md) — The width of stacked items in the tab bar.

### Configuring inline item appearances

- [inlineLayoutAppearance](uitabbarappearance/inlinelayoutappearance.md) — The appearance attributes for items displayed with an inline style.
- [compactInlineLayoutAppearance](uitabbarappearance/compactinlinelayoutappearance.md) — The appearance attributes for items displayed with an inline style in a compact environment.

### Specifying the selection appearance

- [selectionIndicatorTintColor](uitabbarappearance/selectionindicatortintcolor.md) — The tint color to apply to the selection indicator image.
- [selectionIndicatorImage](uitabbarappearance/selectionindicatorimage.md) — The image to draw for the selected item.

## See Also

### Tab bar appearance

- [UITabBarItemAppearance](uitabbaritemappearance.md) — An object for customizing the appearance of tab bar items.
- [UITabBarItemStateAppearance](uitabbaritemstateappearance.md) — A data object containing the specific customizations for tab bar items in a particular state.
