---
title: 'init(padding:softEdgeRadius:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/featheredglassbackgroundeffect/init(padding:softedgeradius:)'
source_url: 'https://developer.apple.com/documentation/swiftui/featheredglassbackgroundeffect/init(padding:softedgeradius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/featheredglassbackgroundeffect/init%28padding%3Asoftedgeradius%3A%29.json'
content_hash: 'sha256:50d7443253989004'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FeatheredGlassBackgroundEffect](../featheredglassbackgroundeffect.md)

# init(padding:softEdgeRadius:)

<sub>Initializer</sub>

Creates a feathered glassBackground effect.

<sub>visionOS</sub>

```swift
init(padding length: CGFloat, softEdgeRadius: CGFloat? = nil)
```

## Parameters

- `softEdgeRadius` — When a blur is clipped, the radial size of the blur’s edge. If you set the value to `nil`, SwiftUI uses a default amount. The default value of this parameter is `nil`.

## Return Value

A feathered background effect.
