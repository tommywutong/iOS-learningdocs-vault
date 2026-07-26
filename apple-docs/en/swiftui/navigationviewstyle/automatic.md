---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/navigationviewstyle/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/navigationviewstyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationviewstyle/automatic.json'
content_hash: 'sha256:6339a4455922de3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationViewStyle](../navigationviewstyle.md)

# automatic

<sub>Type Property</sub>

The default navigation view style in the current context of the view being styled.

> [!warning] Deprecated
> Replace a styled [NavigationView](../navigationview.md) with a [NavigationStack](../navigationstack.md) or [NavigationSplitView](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var automatic: DefaultNavigationViewStyle { get }
```

## See Also

### Getting built-in navigation view styles

- [columns](columns.md) — A navigation view style represented by a series of views in columns. _(deprecated)_
- [stack](stack.md) — A navigation view style represented by a view stack that only shows a single top view at a time. _(deprecated)_
