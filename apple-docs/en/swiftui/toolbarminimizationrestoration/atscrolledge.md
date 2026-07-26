---
title: atScrollEdge
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/toolbarminimizationrestoration/atscrolledge
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarminimizationrestoration/atscrolledge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarminimizationrestoration/atscrolledge.json'
content_hash: 'sha256:9726eea2dea74c90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarMinimizationRestoration](../toolbarminimizationrestoration.md)

# atScrollEdge

<sub>Type Property</sub>

The toolbar restores only when the scroll view’s content reaches the scroll edge.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static let atScrollEdge: ToolbarMinimizationRestoration
```

## Discussion

Mid-scroll reversals do not restore the toolbar. Currently this is only honored alongside [onScrollDown](../toolbarminimizationbehavior/onscrolldown.md) and only for [navigationBar](../toolbarplacement/navigationbar.md).

## See Also

### Getting restoration options

- [automatic](automatic.md) — The system determines the restoration behavior. _(beta)_
