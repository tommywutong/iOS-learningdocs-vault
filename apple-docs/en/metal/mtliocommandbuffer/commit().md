---
title: commit()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandbuffer/commit()
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/commit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/commit%28%29.json'
content_hash: 'sha256:84a3f277c7de41bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# commit()

<sub>Instance Method</sub>

Submits the command buffer to the queue for execution on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func commit()
```

## Discussion

If you haven’t already called [- enqueue](<enqueue().md>) for the command buffer, the [- commit](<commit().md>) method enqueues it at the next position in the input/output command queue.

You can only commit an input/output command buffer once, after which you can’t encode any additional commands or add more completion handlers to it.

## See Also

### Submitting a command buffer

- [- enqueue](<enqueue().md>) — Reserves a place for the input/output command buffer in the input/output command queue without committing the command buffer.
