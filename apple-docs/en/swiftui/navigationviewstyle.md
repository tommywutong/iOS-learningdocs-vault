---
title: NavigationViewStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/navigationviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/navigationviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationviewstyle.json'
content_hash: 'sha256:818d49ca6ed38ce9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NavigationViewStyle

<sub>Protocol</sub>

A specification for the appearance and interaction of a navigation view.

> [!warning] Deprecated
> Replace a styled [NavigationView](navigationview.md) with a [NavigationStack](navigationstack.md) or [NavigationSplitView](navigationsplitview.md). For more information, see [Migrating to new navigation types](migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NavigationViewStyle
```

## Relationships

- **Conforming Types**: [ColumnNavigationViewStyle](columnnavigationviewstyle.md), [DefaultNavigationViewStyle](defaultnavigationviewstyle.md), [DoubleColumnNavigationViewStyle](doublecolumnnavigationviewstyle.md), [StackNavigationViewStyle](stacknavigationviewstyle.md)

## Topics

### Getting built-in navigation view styles

- [automatic](navigationviewstyle/automatic.md) — The default navigation view style in the current context of the view being styled. _(deprecated)_
- [columns](navigationviewstyle/columns.md) — A navigation view style represented by a series of views in columns. _(deprecated)_
- [stack](navigationviewstyle/stack.md) — A navigation view style represented by a view stack that only shows a single top view at a time. _(deprecated)_

### Supporting types

- [DefaultNavigationViewStyle](defaultnavigationviewstyle.md) — The default navigation view style. _(deprecated)_
- [ColumnNavigationViewStyle](columnnavigationviewstyle.md) — A navigation view style represented by a series of views in columns. _(deprecated)_
- [StackNavigationViewStyle](stacknavigationviewstyle.md) — A navigation view style represented by a view stack that only shows a single top view at a time. _(deprecated)_
- [DoubleColumnNavigationViewStyle](doublecolumnnavigationviewstyle.md) — A navigation view style represented by a primary view stack that navigates to a detail view. _(deprecated)_

## See Also

### Styling navigation views

- [navigationViewStyle(_:)](<view/navigationviewstyle(__).md>) — Sets the style for navigation views within this view. _(deprecated)_
