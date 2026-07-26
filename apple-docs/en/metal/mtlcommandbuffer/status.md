---
title: status
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/status
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/status'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/status.json'
content_hash: 'sha256:0b95ff9b2e22110c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# status

<sub>Instance Property</sub>

The command buffer’s current state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var status: MTLCommandBufferStatus { get }
```

## Discussion

Each command buffer can be in any one of the following states:

| State | Meaning |
|---|---|
| [MTLCommandBufferStatusNotEnqueued](../mtlcommandbufferstatus/notenqueued.md) | A command buffer’s initial state, which indicates its command queue isn’t reserving a place for it. ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You can modify a command buffer in this state by encoding commands to it, or by adding a state change handler. |
| [MTLCommandBufferStatusEnqueued](../mtlcommandbufferstatus/enqueued.md) | A command buffer’s second state, which indicates its command queue is reserving a place for it. ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You can modify a command buffer in this state by encoding commands to it, or by adding a state change handler. |
| [MTLCommandBufferStatusCommitted](../mtlcommandbufferstatus/committed.md) | A command buffer’s third state, which indicates the command queue is preparing to schedule the command buffer by resolving its dependencies. ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You can’t modify a command buffer in this state. |
| [MTLCommandBufferStatusScheduled](../mtlcommandbufferstatus/scheduled.md) | A command buffer’s fourth state, which indicates the command buffer has its resources ready and is waiting for the GPU to run its commands. ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You can’t modify a command buffer in this state. |
| [MTLCommandBufferStatusCompleted](../mtlcommandbufferstatus/completed.md) | A command buffer’s successful, final state, which indicates the GPU finished running the command buffer’s commands without any problems. |
| [MTLCommandBufferStatusError](../mtlcommandbufferstatus/error.md) | A command buffer’s unsuccessful, final state, which indicates the GPU stopped running the buffer’s commands because of a runtime issue. |

The first two states ([MTLCommandBufferStatusNotEnqueued](../mtlcommandbufferstatus/notenqueued.md) and [MTLCommandBufferStatusEnqueued](../mtlcommandbufferstatus/enqueued.md)) both indicate that you can encode commands to the command buffer. You do this by creating an encoder that indirectly adds commands for a pass (see [Command encoder factory methods](../command-encoder-factory-methods.md)) to the command buffer. Command buffers also have some methods that directly encode commands between passes, such as [- encodeSignalEvent:value:](<encodesignalevent(__value_).md>) and [- presentDrawable:](<present(__).md>).

Each command buffer’s state can only change to a state below it in the table, and ends its life cycle at either [MTLCommandBufferStatusCompleted](../mtlcommandbufferstatus/completed.md) or [MTLCommandBufferStatusError](../mtlcommandbufferstatus/error.md).

## See Also

### Troubleshooting a command buffer

- [MTLCommandBufferStatus](../mtlcommandbufferstatus.md) — The discrete states for a command buffer that represent its life cycle stages.
- [Command buffer debugging](../command-buffer-debugging.md) — Properties and methods for programmatically debugging runtime issues with a command buffer.
