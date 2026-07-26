---
title: URLSessionTask.State.suspended
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/state-swift.enum/suspended
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.enum/suspended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/state-swift.enum/suspended.json'
content_hash: 'sha256:6f8e8c0166e217cf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSessionTask](../../urlsessiontask.md) · [State](../state-swift.enum.md)

# URLSessionTask.State.suspended

<sub>Case</sub>

The task was suspended by the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case suspended
```

## Discussion

No further processing takes place until the task is resumed. A task in this state is not subject to timeouts.

## See Also

### Task states

- [NSURLSessionTaskStateRunning](running.md) — The task is currently being serviced by the session.
- [NSURLSessionTaskStateCanceling](canceling.md) — The task has received a `cancel` message.
- [NSURLSessionTaskStateCompleted](completed.md) — The task has completed (without being canceled), and the task’s delegate receives no further callbacks.
