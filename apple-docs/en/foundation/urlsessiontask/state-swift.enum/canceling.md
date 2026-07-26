---
title: URLSessionTask.State.canceling
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/state-swift.enum/canceling
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.enum/canceling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/state-swift.enum/canceling.json'
content_hash: 'sha256:c8c76943ebd4fe47'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSessionTask](../../urlsessiontask.md) · [State](../state-swift.enum.md)

# URLSessionTask.State.canceling

<sub>Case</sub>

The task has received a `cancel` message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case canceling
```

## Discussion

The delegate may or may not have received a [- URLSession:task:didCompleteWithError:](<../../urlsessiontaskdelegate/urlsession(__task_didcompletewitherror_).md>) message yet. A task in this state is not subject to timeouts.

## See Also

### Task states

- [NSURLSessionTaskStateRunning](running.md) — The task is currently being serviced by the session.
- [NSURLSessionTaskStateSuspended](suspended.md) — The task was suspended by the app.
- [NSURLSessionTaskStateCompleted](completed.md) — The task has completed (without being canceled), and the task’s delegate receives no further callbacks.
