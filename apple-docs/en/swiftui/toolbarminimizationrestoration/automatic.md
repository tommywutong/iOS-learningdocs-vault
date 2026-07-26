---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/toolbarminimizationrestoration/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarminimizationrestoration/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarminimizationrestoration/automatic.json'
content_hash: 'sha256:123c230d2cc18258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarMinimizationRestoration](../toolbarminimizationrestoration.md)

# automatic

<sub>Type Property</sub>

The system determines the restoration behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: ToolbarMinimizationRestoration
```

## Discussion

By default, the toolbar restores when the user reverses scroll direction.

## See Also

### Getting restoration options

- [atScrollEdge](atscrolledge.md) — The toolbar restores only when the scroll view’s content reaches the scroll edge. _(beta)_
