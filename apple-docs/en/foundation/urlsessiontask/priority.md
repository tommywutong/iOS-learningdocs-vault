---
title: priority
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/priority
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/priority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/priority.json'
content_hash: 'sha256:655d4baaac1deda9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# priority

<sub>Instance Property</sub>

The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var priority: Float { get set }
```

## Discussion

To provide hints to a host on how to prioritize URL session tasks from your app, specify a priority for each task. Specifying a priority provides only a hint and does not guarantee performance. If you don’t specify a priority, a URL session task has a priority of [NSURLSessionTaskPriorityDefault](defaultpriority.md), with a value of `0.5`.

There are three named priorities you can employ, described in [URL session task priority](../url-session-task-priority.md).

You can specify or change a task’s priority at any time, but not all networking protocols respond to changes after a task has started. There is no API to let you determine the effective priority for a task from a host’s perspective.

## See Also

### Controlling the task state

- [- cancel](<cancel().md>) — Cancels the task.
- [- resume](<resume().md>) — Resumes the task, if it is suspended.
- [- suspend](<suspend().md>) — Temporarily suspends a task.
- [state](state-swift.property.md) — The current state of the task—active, suspended, in the process of being canceled, or completed.
- [State](state-swift.enum.md) — Constants for determining the current state of a task.
- [URL session task priority](../url-session-task-priority.md) — Constants for providing task priority hints to a host, used with the [priority](priority.md) property.
