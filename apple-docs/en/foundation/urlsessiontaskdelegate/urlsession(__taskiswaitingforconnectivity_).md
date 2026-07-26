---
title: 'urlSession(_:taskIsWaitingForConnectivity:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiontaskdelegate/urlsession(_:taskiswaitingforconnectivity:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:taskiswaitingforconnectivity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate/urlsession%28_%3Ataskiswaitingforconnectivity%3A%29.json'
content_hash: 'sha256:6574a2802c8034c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskDelegate](../urlsessiontaskdelegate.md)

# urlSession(_:taskIsWaitingForConnectivity:)

<sub>Instance Method</sub>

Tells the delegate that the task is waiting until suitable connectivity is available before beginning the network load.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, taskIsWaitingForConnectivity task: URLSessionTask)
```

## Parameters

- `session` — The session that contains the waiting task.

- `task` — The task that is waiting for a change in connectivity.

## Discussion

This method is called if the  [waitsForConnectivity](../urlsessionconfiguration/waitsforconnectivity.md) property of [URLSessionConfiguration](../urlsessionconfiguration.md) is `true`, and sufficient connectivity is unavailable. The delegate can use this opportunity to update the user interface; for example, by presenting an offline mode or a cellular-only mode.

This method is called, at most, once per task, and only if connectivity is initially unavailable. It is never called for background sessions because `waitsForConnectivity` is ignored for those sessions.

## See Also

### Handling delayed and waiting tasks

- [- URLSession:task:willBeginDelayedRequest:completionHandler:](<urlsession(__task_willbegindelayedrequest_completionhandler_).md>) — Tells the delegate that a delayed URL session task will now begin loading.
- [DelayedRequestDisposition](../urlsession/delayedrequestdisposition.md) — The action to take on a delayed URL session task.
