---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabbarminimizebehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/tabbarminimizebehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabbarminimizebehavior/automatic.json'
content_hash: 'sha256:bf4b6064b8560b0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabBarMinimizeBehavior](../tabbarminimizebehavior.md)

# automatic

<sub>Type Property</sub>

Determine the behavior automatically based on the surrounding context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: TabBarMinimizeBehavior
```

## Discussion

The depends on the platform:

- On iOS, iPadOS, tvOS, and watchOS, the tab bar does not minimize.
- On visionOS, the tab bar minimizes when people look away from it.
- On macOS, the tab bar minimizes when the window has reduced space.
