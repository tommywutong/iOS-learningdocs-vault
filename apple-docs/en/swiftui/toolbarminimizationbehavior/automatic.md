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
doc_path: /documentation/swiftui/toolbarminimizationbehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarminimizationbehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarminimizationbehavior/automatic.json'
content_hash: 'sha256:e9dbde4093179623'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarMinimizationBehavior](../toolbarminimizationbehavior.md)

# automatic

<sub>Type Property</sub>

The system determines the minimize behavior. By default, navigation bars on iOS will minimize when the view has a searchable using the [toolbarPrincipal](../searchfieldplacement/toolbarprincipal.md) placement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: ToolbarMinimizationBehavior { get }
```

## See Also

### Getting behaviors

- [never](never.md) — The toolbar cannot be minimized. _(beta)_
- [onScrollDown](onscrolldown.md) — Minimize when scrolling down. _(beta)_
- [onScrollUp](onscrollup.md) — Minimize when scrolling up. _(beta)_
