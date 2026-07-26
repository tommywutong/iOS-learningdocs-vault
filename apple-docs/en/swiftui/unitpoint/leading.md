---
title: leading
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitpoint/leading
source_url: 'https://developer.apple.com/documentation/swiftui/unitpoint/leading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitpoint/leading.json'
content_hash: 'sha256:cbf580f6e6861389'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitPoint](../unitpoint.md)

# leading

<sub>Type Property</sub>

A point that’s centered vertically on the leading edge of a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let leading: UnitPoint
```

## Discussion

This point occupies the position where the horizontal and vertical alignment guides intersect for [leading](../alignment/leading.md) alignment. The leading edge appears on the left in a left-to-right language environment and on the right in a right-to-left environment.

## See Also

### Getting middle points

- [center](center.md) — A point that’s centered in a view.
- [trailing](trailing.md) — A point that’s centered vertically on the trailing edge of a view.
