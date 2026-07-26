---
title: DefaultNavigationViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/defaultnavigationviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/defaultnavigationviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/defaultnavigationviewstyle.json'
content_hash: 'sha256:884c395948633fd4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DefaultNavigationViewStyle

<sub>Structure</sub>

The default navigation view style.

> [!warning] Deprecated
> Replace a styled [NavigationView](navigationview.md) with a [NavigationStack](navigationstack.md) or [NavigationSplitView](navigationsplitview.md). For more information, see [Migrating to new navigation types](migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DefaultNavigationViewStyle
```

## Overview

Use [automatic](navigationviewstyle/automatic.md) to construct this style.

## Relationships

- **Conforms To**: [NavigationViewStyle](navigationviewstyle.md)

## Topics

### Creating a default navigation view style

- [init()](<defaultnavigationviewstyle/init().md>) — Creates the default navigation view style. _(deprecated)_

## See Also

### Supporting types

- [ColumnNavigationViewStyle](columnnavigationviewstyle.md) — A navigation view style represented by a series of views in columns. _(deprecated)_
- [StackNavigationViewStyle](stacknavigationviewstyle.md) — A navigation view style represented by a view stack that only shows a single top view at a time. _(deprecated)_
- [DoubleColumnNavigationViewStyle](doublecolumnnavigationviewstyle.md) — A navigation view style represented by a primary view stack that navigates to a detail view. _(deprecated)_
