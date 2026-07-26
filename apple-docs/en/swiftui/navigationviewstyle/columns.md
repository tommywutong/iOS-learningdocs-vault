---
title: columns
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+（27.0 起废弃）, iPadOS 15.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/navigationviewstyle/columns
source_url: 'https://developer.apple.com/documentation/swiftui/navigationviewstyle/columns'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationviewstyle/columns.json'
content_hash: 'sha256:06b56080d4601492'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationViewStyle](../navigationviewstyle.md)

# columns

<sub>Type Property</sub>

A navigation view style represented by a series of views in columns.

> [!warning] Deprecated
> Replace a styled [NavigationView](../navigationview.md) with a [NavigationStack](../navigationstack.md) or [NavigationSplitView](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static var columns: ColumnNavigationViewStyle { get }
```

## See Also

### Getting built-in navigation view styles

- [automatic](automatic.md) — The default navigation view style in the current context of the view being styled. _(deprecated)_
- [stack](stack.md) — A navigation view style represented by a view stack that only shows a single top view at a time. _(deprecated)_
