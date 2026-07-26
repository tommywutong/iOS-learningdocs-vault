---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationsplitviewvisibility/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/navigationsplitviewvisibility/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationsplitviewvisibility/automatic.json'
content_hash: 'sha256:a176ccdbcf0ab518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationSplitViewVisibility](../navigationsplitviewvisibility.md)

# automatic

<sub>Type Property</sub>

Use the default leading column visibility for the current device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: NavigationSplitViewVisibility { get }
```

## Discussion

This computed property returns one of the three concrete cases: [detailOnly](detailonly.md), [doubleColumn](doublecolumn.md), or [all](all.md).

## See Also

### Getting visibilities

- [all](all.md) — Show all the columns of a three-column navigation split view.
- [doubleColumn](doublecolumn.md) — Show the content column and detail area of a three-column navigation split view, or the sidebar column and detail area of a two-column navigation split view.
- [detailOnly](detailonly.md) — Hide the leading two columns of a three-column navigation split view, so that just the detail area shows.
