---
title: waitUntilScheduled()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/waituntilscheduled()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilscheduled()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/waituntilscheduled%28%29.json'
content_hash: 'sha256:884da690daab6bab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# waitUntilScheduled()

<sub>Instance Method</sub>

Blocks the current thread until the command queue schedules the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func waitUntilScheduled()
```

## Discussion

This method returns after the following events:

- The command queue _schedules_ (see [status](status.md) and [MTLCommandBufferStatusScheduled](../mtlcommandbufferstatus/scheduled.md)) the command buffer to run on the GPU.
- The command buffer invokes all the completion handlers your app submits with [- addScheduledHandler:](<addscheduledhandler(__).md>).

Use the [- waitUntilCompleted](<waituntilcompleted().md>) method to check for completion of the scheduled work.

## See Also

### Waiting for state changes

- [- waitUntilCompleted](<waituntilcompleted().md>) — Blocks the current thread until the GPU finishes executing the command buffer and all of its completion handlers.
