---
title: StackNavigationViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/stacknavigationviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/stacknavigationviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/stacknavigationviewstyle.json'
content_hash: 'sha256:1001568945f43320'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# StackNavigationViewStyle

<sub>Structure</sub>

A navigation view style represented by a view stack that only shows a single top view at a time.

> [!warning] Deprecated
> Replace a styled [NavigationView](navigationview.md) with a [NavigationStack](navigationstack.md) or [NavigationSplitView](navigationsplitview.md). For more information, see [Migrating to new navigation types](migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct StackNavigationViewStyle
```

## Overview

Use [stack](navigationviewstyle/stack.md) to construct this style.

## Relationships

- **Conforms To**: [NavigationViewStyle](navigationviewstyle.md)

## Topics

### Creating a stack navigation view style

- [init()](<stacknavigationviewstyle/init().md>) — Creates a navigation view style represented by a view stack that only shows a single top view at a time. _(deprecated)_

## See Also

### Supporting types

- [DefaultNavigationViewStyle](defaultnavigationviewstyle.md) — The default navigation view style. _(deprecated)_
- [ColumnNavigationViewStyle](columnnavigationviewstyle.md) — A navigation view style represented by a series of views in columns. _(deprecated)_
- [DoubleColumnNavigationViewStyle](doublecolumnnavigationviewstyle.md) — A navigation view style represented by a primary view stack that navigates to a detail view. _(deprecated)_
