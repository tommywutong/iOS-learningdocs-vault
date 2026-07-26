---
title: 'makeTextureViewPool(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/maketextureviewpool(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maketextureviewpool(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maketextureviewpool%28descriptor%3A%29.json'
content_hash: 'sha256:f1f3028677fe2d09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeTextureViewPool(descriptor:)

<sub>Instance Method</sub>

Creates a new texture view pool from a resource view pool descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTextureViewPool(descriptor: MTLResourceViewPoolDescriptor) throws -> any MTLTextureViewPool
```

## Parameters

- `descriptor` — A [MTLResourceViewPoolDescriptor](../mtlresourceviewpooldescriptor.md) instance that configures the [MTLTextureViewPool](../mtltextureviewpool.md) instance.

## Return Value

A [MTLTextureViewPool](../mtltextureviewpool.md) instance, or `nil` if the function failed.
