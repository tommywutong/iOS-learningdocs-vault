---
title: doubleColumn
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationsplitviewvisibility/doublecolumn
source_url: 'https://developer.apple.com/documentation/swiftui/navigationsplitviewvisibility/doublecolumn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationsplitviewvisibility/doublecolumn.json'
content_hash: 'sha256:451dc9acaf6a1b69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationSplitViewVisibility](../navigationsplitviewvisibility.md)

# doubleColumn

<sub>Type Property</sub>

Show the content column and detail area of a three-column navigation split view, or the sidebar column and detail area of a two-column navigation split view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var doubleColumn: NavigationSplitViewVisibility { get }
```

## Discussion

For a two-column navigation split view, `doubleColumn` is equivalent to `all`.

## See Also

### Getting visibilities

- [automatic](automatic.md) — Use the default leading column visibility for the current device.
- [all](all.md) — Show all the columns of a three-column navigation split view.
- [detailOnly](detailonly.md) — Hide the leading two columns of a three-column navigation split view, so that just the detail area shows.
