---
title: endCommandBuffer()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandbuffer/endcommandbuffer()
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/endcommandbuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/endcommandbuffer%28%29.json'
content_hash: 'sha256:2e9a4ea53ef541aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# endCommandBuffer()

<sub>Instance Method</sub>

Closes a command buffer to prepare it for submission to a command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func endCommandBuffer()
```

## Discussion

Explicitly ending the command buffer allows you to reuse the [MTL4CommandAllocator](../mtl4commandallocator.md) to start servicing other command buffers. It is an error to call `commit` on a command buffer previously recording before calling this method.
