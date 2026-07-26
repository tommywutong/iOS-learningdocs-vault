---
title: URLSessionTask.State
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/state-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/state-swift.enum.json'
content_hash: 'sha256:56a80d4431ebaccc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# URLSessionTask.State

<sub>Enumeration</sub>

Constants for determining the current state of a task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Task states

- [NSURLSessionTaskStateRunning](state-swift.enum/running.md) — The task is currently being serviced by the session.
- [NSURLSessionTaskStateSuspended](state-swift.enum/suspended.md) — The task was suspended by the app.
- [NSURLSessionTaskStateCanceling](state-swift.enum/canceling.md) — The task has received a `cancel` message.
- [NSURLSessionTaskStateCompleted](state-swift.enum/completed.md) — The task has completed (without being canceled), and the task’s delegate receives no further callbacks.

### Initializers

- [init(rawValue:)](<state-swift.enum/init(rawvalue_).md>)

## See Also

### Controlling the task state

- [- cancel](<cancel().md>) — Cancels the task.
- [- resume](<resume().md>) — Resumes the task, if it is suspended.
- [- suspend](<suspend().md>) — Temporarily suspends a task.
- [state](state-swift.property.md) — The current state of the task—active, suspended, in the process of being canceled, or completed.
- [priority](priority.md) — The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).
- [URL session task priority](../url-session-task-priority.md) — Constants for providing task priority hints to a host, used with the [priority](priority.md) property.
