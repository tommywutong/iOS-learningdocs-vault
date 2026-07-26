---
title: ColumnNavigationViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+（27.0 起废弃）, iPadOS 15.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/columnnavigationviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/columnnavigationviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/columnnavigationviewstyle.json'
content_hash: 'sha256:ec03de57372b43e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ColumnNavigationViewStyle

<sub>Structure</sub>

A navigation view style represented by a series of views in columns.

> [!warning] Deprecated
> Replace a styled [NavigationView](navigationview.md) with a [NavigationStack](navigationstack.md) or [NavigationSplitView](navigationsplitview.md). For more information, see [Migrating to new navigation types](migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct ColumnNavigationViewStyle
```

## Overview

Use [columns](navigationviewstyle/columns.md) to construct this style.

## Relationships

- **Conforms To**: [NavigationViewStyle](navigationviewstyle.md)

## See Also

### Supporting types

- [DefaultNavigationViewStyle](defaultnavigationviewstyle.md) — The default navigation view style. _(deprecated)_
- [StackNavigationViewStyle](stacknavigationviewstyle.md) — A navigation view style represented by a view stack that only shows a single top view at a time. _(deprecated)_
- [DoubleColumnNavigationViewStyle](doublecolumnnavigationviewstyle.md) — A navigation view style represented by a primary view stack that navigates to a detail view. _(deprecated)_
