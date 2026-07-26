---
title: URLSessionTask.State.running
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/state-swift.enum/running
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.enum/running'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/state-swift.enum/running.json'
content_hash: 'sha256:0b6405d86a10495a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSessionTask](../../urlsessiontask.md) · [State](../state-swift.enum.md)

# URLSessionTask.State.running

<sub>Case</sub>

The task is currently being serviced by the session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case running
```

## Discussion

A task in this state is subject to the request and resource timeouts specified in the session configuration object.

## See Also

### Task states

- [NSURLSessionTaskStateSuspended](suspended.md) — The task was suspended by the app.
- [NSURLSessionTaskStateCanceling](canceling.md) — The task has received a `cancel` message.
- [NSURLSessionTaskStateCompleted](completed.md) — The task has completed (without being canceled), and the task’s delegate receives no further callbacks.
