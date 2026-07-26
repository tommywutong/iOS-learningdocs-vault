---
title: URL session task priority
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/url-session-task-priority
source_url: 'https://developer.apple.com/documentation/foundation/url-session-task-priority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url-session-task-priority.json'
content_hash: 'sha256:21d270eb10a5754e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLSessionTask](urlsessiontask.md)

# URL session task priority

<sub>API Collection</sub>

Constants for providing task priority hints to a host, used with the [priority](urlsessiontask/priority.md) property.

## Topics

### Priority constants

- [NSURLSessionTaskPriorityDefault](urlsessiontask/defaultpriority.md) — The default URL session task priority, used implicitly for any task you have not prioritized.
- [NSURLSessionTaskPriorityLow](urlsessiontask/lowpriority.md) — A low URL session task priority, with a floating point value above the minimum of `0` and below the default value.
- [NSURLSessionTaskPriorityHigh](urlsessiontask/highpriority.md) — A high URL session task priority, with a floating point value above the default value and below the maximum of `1.0`.

## See Also

### Controlling the task state

- [- cancel](<urlsessiontask/cancel().md>) — Cancels the task.
- [- resume](<urlsessiontask/resume().md>) — Resumes the task, if it is suspended.
- [- suspend](<urlsessiontask/suspend().md>) — Temporarily suspends a task.
- [state](urlsessiontask/state-swift.property.md) — The current state of the task—active, suspended, in the process of being canceled, or completed.
- [State](urlsessiontask/state-swift.enum.md) — Constants for determining the current state of a task.
- [priority](urlsessiontask/priority.md) — The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).
