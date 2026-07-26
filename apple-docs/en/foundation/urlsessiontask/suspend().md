---
title: suspend()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/suspend()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/suspend()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/suspend%28%29.json'
content_hash: 'sha256:d0b517029434917e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# suspend()

<sub>Instance Method</sub>

Temporarily suspends a task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func suspend()
```

## Discussion

A task, while suspended, produces no network traffic and isn’t subject to timeouts. Call [- resume](<resume().md>) to resume data transfer.

## See Also

### Related Documentation

- [- cancelByProducingResumeData:](<../urlsessiondownloadtask/cancel(byproducingresumedata_).md>) — Cancels a download and calls a callback with resume data for later use.

### Controlling the task state

- [- cancel](<cancel().md>) — Cancels the task.
- [- resume](<resume().md>) — Resumes the task, if it is suspended.
- [state](state-swift.property.md) — The current state of the task—active, suspended, in the process of being canceled, or completed.
- [State](state-swift.enum.md) — Constants for determining the current state of a task.
- [priority](priority.md) — The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).
- [URL session task priority](../url-session-task-priority.md) — Constants for providing task priority hints to a host, used with the [priority](priority.md) property.
