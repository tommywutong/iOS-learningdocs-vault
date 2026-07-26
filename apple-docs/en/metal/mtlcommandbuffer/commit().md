---
title: commit()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/commit()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/commit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/commit%28%29.json'
content_hash: 'sha256:2790d4244d45b869'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# commit()

<sub>Instance Method</sub>

Submits the command buffer to run on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func commit()
```

## Discussion

The [- commit](<commit().md>) method sends the command buffer to the [MTLCommandQueue](../mtlcommandqueue.md) instance that owns it, which then schedules it to run on the GPU. If your app calls [- commit](<commit().md>) for a command buffer that isn’t enqueued, the method effectively calls [- enqueue](<enqueue().md>) for you.

The [- commit](<commit().md>) method has several restrictions, including:

- You can commit a command buffer to its command queue only one time.
- You can only commit a command buffer when it doesn’t have an active encoder (see [MTLCommandBuffer](../mtlcommandbuffer.md) and [MTLCommandEncoder](../mtlcommandencoder.md)).
- You can’t encode additional commands to a command buffer after you commit it.
- You can’t call the [- addScheduledHandler:](<addscheduledhandler(__).md>) or [- addCompletedHandler:](<addcompletedhandler(__).md>) methods after you commit a command buffer.

The GPU starts the command buffer after it starts any command buffers that are ahead of it in the same command queue.

## See Also

### Submitting a command buffer

- [- enqueue](<enqueue().md>) — Reserves the next available place for the command buffer in its command queue.
