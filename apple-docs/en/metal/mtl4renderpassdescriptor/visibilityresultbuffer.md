---
title: visibilityResultBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpassdescriptor/visibilityresultbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/visibilityresultbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpassdescriptor/visibilityresultbuffer.json'
content_hash: 'sha256:a9aa7edb1a80ef8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPassDescriptor](../mtl4renderpassdescriptor.md)

# visibilityResultBuffer

<sub>Instance Property</sub>

Configures a buffer into which Metal writes counts of fragments (pixels) passing the depth and stencil tests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var visibilityResultBuffer: (any MTLBuffer)? { get set }
```
