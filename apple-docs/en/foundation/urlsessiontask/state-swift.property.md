---
title: state
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/state-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/state-swift.property.json'
content_hash: 'sha256:2790608f21c93fc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# state

<sub>Instance Property</sub>

The current state of the task—active, suspended, in the process of being canceled, or completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var state: URLSessionTask.State { get }
```

## See Also

### Controlling the task state

- [- cancel](<cancel().md>) — Cancels the task.
- [- resume](<resume().md>) — Resumes the task, if it is suspended.
- [- suspend](<suspend().md>) — Temporarily suspends a task.
- [State](state-swift.enum.md) — Constants for determining the current state of a task.
- [priority](priority.md) — The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).
- [URL session task priority](../url-session-task-priority.md) — Constants for providing task priority hints to a host, used with the [priority](priority.md) property.
