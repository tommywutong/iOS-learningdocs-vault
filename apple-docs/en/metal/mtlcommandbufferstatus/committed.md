---
title: MTLCommandBufferStatus.committed
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferstatus/committed
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/committed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferstatus/committed.json'
content_hash: 'sha256:1b189526f07d83e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferStatus](../mtlcommandbufferstatus.md)

# MTLCommandBufferStatus.committed

<sub>Case</sub>

A command buffer’s third state, which indicates the command queue is preparing to schedule the command buffer by resolving its dependencies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case committed
```

## Discussion

See the [MTLCommandBuffer](../mtlcommandbuffer.md) protocol’s [status](../mtlcommandbuffer/status.md) property for more information.

## See Also

### Command buffer states

- [MTLCommandBufferStatusNotEnqueued](notenqueued.md) — A command buffer’s initial state, which indicates its command queue isn’t reserving a place for it.
- [MTLCommandBufferStatusEnqueued](enqueued.md) — A command buffer’s second state, which indicates its command queue is reserving a place for it.
- [MTLCommandBufferStatusScheduled](scheduled.md) — A command buffer’s fourth state, which indicates the command buffer has its resources ready and is waiting for the GPU to run its commands.
- [MTLCommandBufferStatusCompleted](completed.md) — A command buffer’s successful, final state, which indicates the GPU finished running the command buffer’s commands without any problems.
- [MTLCommandBufferStatusError](error.md) — A command buffer’s unsuccessful, final state, which indicates the GPU stopped running the buffer’s commands because of a runtime issue.
