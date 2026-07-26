---
title: UITabBarItemAppearance.Style
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbaritemappearance/style
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritemappearance/style'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritemappearance/style.json'
content_hash: 'sha256:3f96f4bb99a295d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItemAppearance](../uitabbaritemappearance.md)

# UITabBarItemAppearance.Style

<sub>Enumeration</sub>

Constants indicating the layout of a tab bar item’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Style
```

## Overview

A tab bar adjusts the layout of each item’s icon and title string based on the current trait environment and other factors.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Item layout

- [UITabBarItemAppearanceStyleStacked](style/stacked.md) — A vertically stacked icon and title.
- [UITabBarItemAppearanceStyleInline](style/inline.md) — A side-by-side layout of the icon and title, suitable for use in regular-width environments.
- [UITabBarItemAppearanceStyleCompactInline](style/compactinline.md) — A side-by-side layout of the icon and title, suitable for use in compact-width environments.

### Initializers

- [init(rawValue:)](<style/init(rawvalue_).md>)

## See Also

### Resetting the appearance properties

- [- configureWithDefaultForStyle:](<configurewithdefault(for_).md>) — Configures the tab bar item appearance object with appropriate values for the specified style.
