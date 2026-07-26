---
title: renderTargetHeight
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpassdescriptor/rendertargetheight
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/rendertargetheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpassdescriptor/rendertargetheight.json'
content_hash: 'sha256:c036539159d65676'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPassDescriptor](../mtl4renderpassdescriptor.md)

# renderTargetHeight

<sub>Instance Property</sub>

Sets the height, in pixels, to which Metal constrains the render target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var renderTargetHeight: Int { get set }
```

## Discussion

When this value is non-zero, you need to assign it to be smaller than or equal to the minimum height of all attachments.

The default value of this property is `0`.
