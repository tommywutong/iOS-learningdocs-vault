---
title: 'feathered(padding:softEdgeRadius:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/glassbackgroundeffect/feathered(padding:softedgeradius:)'
source_url: 'https://developer.apple.com/documentation/swiftui/glassbackgroundeffect/feathered(padding:softedgeradius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/glassbackgroundeffect/feathered%28padding%3Asoftedgeradius%3A%29.json'
content_hash: 'sha256:c73202b54b74ed2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GlassBackgroundEffect](../glassbackgroundeffect.md)

# feathered(padding:softEdgeRadius:)

<sub>Type Method</sub>

A feathered background effect with custom padding and soft edge radius.

<sub>visionOS</sub>

```swift
static func feathered(padding length: CGFloat, softEdgeRadius: CGFloat? = nil) -> FeatheredGlassBackgroundEffect
```

## Parameters

- `softEdgeRadius` — When a blur is clipped, the radial size of the blur’s edge. If you set the value to `nil`, SwiftUI uses a default amount. The default value of this parameter is `nil`.

## Return Value

A feathered background effect.
