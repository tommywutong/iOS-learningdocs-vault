---
title: MTLCommandBufferStatus
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferstatus
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferstatus.json'
content_hash: 'sha256:8e9e932426b2a746'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandBufferStatus

<sub>Enumeration</sub>

The discrete states for a command buffer that represent its life cycle stages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLCommandBufferStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Command buffer states

- [MTLCommandBufferStatusNotEnqueued](mtlcommandbufferstatus/notenqueued.md) — A command buffer’s initial state, which indicates its command queue isn’t reserving a place for it.
- [MTLCommandBufferStatusEnqueued](mtlcommandbufferstatus/enqueued.md) — A command buffer’s second state, which indicates its command queue is reserving a place for it.
- [MTLCommandBufferStatusCommitted](mtlcommandbufferstatus/committed.md) — A command buffer’s third state, which indicates the command queue is preparing to schedule the command buffer by resolving its dependencies.
- [MTLCommandBufferStatusScheduled](mtlcommandbufferstatus/scheduled.md) — A command buffer’s fourth state, which indicates the command buffer has its resources ready and is waiting for the GPU to run its commands.
- [MTLCommandBufferStatusCompleted](mtlcommandbufferstatus/completed.md) — A command buffer’s successful, final state, which indicates the GPU finished running the command buffer’s commands without any problems.
- [MTLCommandBufferStatusError](mtlcommandbufferstatus/error.md) — A command buffer’s unsuccessful, final state, which indicates the GPU stopped running the buffer’s commands because of a runtime issue.

### Initializers

- [init(rawValue:)](<mtlcommandbufferstatus/init(rawvalue_).md>)

## See Also

### Troubleshooting a command buffer

- [status](mtlcommandbuffer/status.md) — The command buffer’s current state.
- [Command buffer debugging](command-buffer-debugging.md) — Properties and methods for programmatically debugging runtime issues with a command buffer.
