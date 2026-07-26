---
title: samplePositions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpassdescriptor/samplepositions
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/samplepositions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpassdescriptor/samplepositions.json'
content_hash: 'sha256:14064e5fa45f4c53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPassDescriptor](../mtl4renderpassdescriptor.md)

# samplePositions

<sub>Instance Property</sub>

Configures the custom sample positions to use in MSAA rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var samplePositions: [MTLSamplePosition] { get set }
```

## Discussion

Set to an empty array to disable custom sample positions.
