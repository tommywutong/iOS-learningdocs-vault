---
title: makeCommandBuffer()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/makecommandbuffer()
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecommandbuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecommandbuffer%28%29.json'
content_hash: 'sha256:b789d6f37e0aba2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeCommandBuffer()

<sub>Instance Method</sub>

Creates a new command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandBuffer() -> (any MTL4CommandBuffer)?
```

## Return Value

A [MTL4CommandBuffer](../mtl4commandbuffer.md) instance, or `nil` if the function failed.
