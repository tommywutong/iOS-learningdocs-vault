---
title: enqueue()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/enqueue()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/enqueue()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/enqueue%28%29.json'
content_hash: 'sha256:90cb80523fb60e5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# enqueue()

<sub>Instance Method</sub>

Reserves the next available place for the command buffer in its command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func enqueue()
```

## Discussion

The [- enqueue](<enqueue().md>) method adds the command buffer to the [MTLCommandQueue](../mtlcommandqueue.md) instance that owns it, but doesn’t commit the command buffer to run on the GPU. You can call the command buffer’s [- commit](<commit().md>) method at a later time when it’s ready to run on the GPU. You can call a command buffer’s [- enqueue](<enqueue().md>) method any time before you call [- commit](<commit().md>), including before, after, or as you encode commands to it.

> [!note] Note
> The command buffer can only reserve a place in its queue a single time; all subsequent [- enqueue](<enqueue().md>) calls have no effect.

Enqueuing your command buffers first gives you the flexibility to arrange their relative order of execution before encoding commands to any of them. This approach lets you potentially encode each command buffer on a thread, in parallel, instead of encoding them one by one on a single thread. The order in which each worker thread finishes encoding and commits its command buffer doesn’t matter when you enqueue them in order before committing.

## See Also

### Submitting a command buffer

- [- commit](<commit().md>) — Submits the command buffer to run on the GPU.
