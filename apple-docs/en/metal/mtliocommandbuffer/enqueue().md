---
title: enqueue()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandbuffer/enqueue()
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/enqueue()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/enqueue%28%29.json'
content_hash: 'sha256:a3b3d8189a05ac89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# enqueue()

<sub>Instance Method</sub>

Reserves a place for the input/output command buffer in the input/output command queue without committing the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func enqueue()
```

## Discussion

The method saves the next position for the command buffer in the input/output command queue. You can call [- enqueue](<enqueue().md>) at any time relative to encoding commands, but you can only enqueue a command buffer once. To submit a command buffer to GPU for execution, call its [- commit](<commit().md>) method.

For example, to fill multiple command buffers asynchronously that execute in a specific order:

1. Call each command buffer’s [- enqueue](<enqueue().md>) method in order.
2. Encode commands into each command buffer on its own, separate thread.
3. Call each command buffer’s [- commit](<commit().md>) in any order.

## See Also

### Submitting a command buffer

- [- commit](<commit().md>) — Submits the command buffer to the queue for execution on the GPU.
