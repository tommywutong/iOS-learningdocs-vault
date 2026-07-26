---
title: MTLCommandBufferHandler
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferhandler
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferhandler.json'
content_hash: 'sha256:d3739d3e7005b6a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandBufferHandler

<sub>Type Alias</sub>

A completion handler signature a GPU device calls when it finishes scheduling a command buffer, or when the GPU finishes running it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLCommandBufferHandler = @Sendable (any MTLCommandBuffer) -> Void
```

## Parameters

- `commandBuffer` — The [MTLCommandBuffer](mtlcommandbuffer.md) instance that’s invoking the completion handler.

## Discussion

The [MTLCommandBuffer](mtlcommandbuffer.md) type uses this signature in its methods that register your completion handlers, including [- addScheduledHandler:](<mtlcommandbuffer/addscheduledhandler(__).md>) and [- addCompletedHandler:](<mtlcommandbuffer/addcompletedhandler(__).md>).

## See Also

### Registering state change handlers

- [- addScheduledHandler:](<mtlcommandbuffer/addscheduledhandler(__).md>) — Registers a completion handler the GPU device calls immediately after it schedules the command buffer to run on the GPU.
- [- addCompletedHandler:](<mtlcommandbuffer/addcompletedhandler(__).md>) — Registers a completion handler the GPU device calls immediately after the GPU finishes running the commands in the command buffer.
