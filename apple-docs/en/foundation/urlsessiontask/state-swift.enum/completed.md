---
title: URLSessionTask.State.completed
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/state-swift.enum/completed
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.enum/completed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/state-swift.enum/completed.json'
content_hash: 'sha256:cfb95574f8581f5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSessionTask](../../urlsessiontask.md) · [State](../state-swift.enum.md)

# URLSessionTask.State.completed

<sub>Case</sub>

The task has completed (without being canceled), and the task’s delegate receives no further callbacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case completed
```

## Discussion

If the task completed successfully, the task’s [error](../error.md) property is `nil`. Otherwise, it provides an error object that tells what went wrong. A task in this state is not subject to timeouts.

## See Also

### Task states

- [NSURLSessionTaskStateRunning](running.md) — The task is currently being serviced by the session.
- [NSURLSessionTaskStateSuspended](suspended.md) — The task was suspended by the app.
- [NSURLSessionTaskStateCanceling](canceling.md) — The task has received a `cancel` message.
