---
title: UIBarButtonItemStateAppearance
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitemstateappearance
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemstateappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemstateappearance.json'
content_hash: 'sha256:ec0097944e4c21a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBarButtonItemStateAppearance

<sub>Class</sub>

A data object containing the specific customizations for a bar button item in a particular state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIBarButtonItemStateAppearance
```

## Overview

Use a [UIBarButtonItemStateAppearance](uibarbuttonitemstateappearance.md) object to customize the title and background image of your bar button items. Don’t create [UIBarButtonItemStateAppearance](uibarbuttonitemstateappearance.md) objects yourself. Instead, create a [UIBarButtonItemAppearance](uibarbuttonitemappearance.md) object and use its properties to fetch the appearance attributes for the button in a particular state. For example, to set the button’s attributes when it’s in the normal state, configure the object in the [normal](uibarbuttonitemappearance/normal.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Configuring the title

- [titleTextAttributes](uibarbuttonitemstateappearance/titletextattributes.md) — String attributes to apply to the text of the bar button item’s title.
- [titlePositionAdjustment](uibarbuttonitemstateappearance/titlepositionadjustment.md) — The additional amount by which to offset the title horizontally and vertically.

### Configuring the background appearance

- [backgroundImage](uibarbuttonitemstateappearance/backgroundimage.md) — A background image to display around the button.
- [backgroundImagePositionAdjustment](uibarbuttonitemstateappearance/backgroundimagepositionadjustment.md) — The distance, in points, by which to offset the background image horizontally and vertically.

## See Also

### Shared appearance

- [UIBarAppearance](uibarappearance.md) — An object for customizing the basic appearance of system bars.
- [UIBarButtonItemAppearance](uibarbuttonitemappearance.md) — An object for customizing the appearance of bar button items.
