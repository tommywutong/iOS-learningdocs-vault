---
title: UITabBarItemAppearance
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritemappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritemappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritemappearance.json'
content_hash: 'sha256:16783be779640873'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITabBarItemAppearance

<sub>Class</sub>

An object for customizing the appearance of tab bar items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITabBarItemAppearance
```

## Overview

Use a [UITabBarItemAppearance](uitabbaritemappearance.md) object to customize the appearance of a tab bar item in each of its possible states. You can customize the appearance differently for each state. For example, you might apply different colors to the tab bar item’s icon in the [normal](uitabbaritemappearance/normal.md) and [selected](uitabbaritemappearance/selected.md) states.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a tab bar item appearance object

- [- initWithStyle:](<uitabbaritemappearance/init(style_).md>) — Creates an appearance object with appropriate default values for a tab bar, displaying its items with the specified layout style.
- [- init](<uitabbaritemappearance/init().md>) — Creates an appearance object with default values for a stacked tab bar item.
- [- initWithCoder:](<uitabbaritemappearance/init(coder_).md>) — Creates an appearance object from data in an unarchiver.

### Copying a tab bar item appearance object

- [- copy](<uitabbaritemappearance/copy().md>) — Creates a copy of the appearance object.

### Resetting the appearance properties

- [- configureWithDefaultForStyle:](<uitabbaritemappearance/configurewithdefault(for_).md>) — Configures the tab bar item appearance object with appropriate values for the specified style.
- [Style](uitabbaritemappearance/style.md) — Constants indicating the layout of a tab bar item’s content.

### Configuring attributes for different item states

- [normal](uitabbaritemappearance/normal.md) — The appearance data to apply to the tab bar item when it’s enabled, unselected, and not the focused item.
- [selected](uitabbaritemappearance/selected.md) — The appearance data to apply to the tab bar item when it’s selected.
- [disabled](uitabbaritemappearance/disabled.md) — The appearance data to apply to the tab bar item when it’s disabled.
- [focused](uitabbaritemappearance/focused.md) — The appearance data to apply to the tab bar item when it’s focused.

## See Also

### Tab bar appearance

- [UITabBarAppearance](uitabbarappearance.md) — An object for customizing the appearance of a tab bar.
- [UITabBarItemStateAppearance](uitabbaritemstateappearance.md) — A data object containing the specific customizations for tab bar items in a particular state.
