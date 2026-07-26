---
title: render
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensorusage/render
source_url: 'https://developer.apple.com/documentation/metal/mtltensorusage/render'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorusage/render.json'
content_hash: 'sha256:219823878378e3e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorUsage](../mtltensorusage.md)

# render

<sub>Type Property</sub>

A tensor context that applies to render encoders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var render: MTLTensorUsage { get }
```

## Discussion

You can use tensors with this context in [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md) or [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instances.
