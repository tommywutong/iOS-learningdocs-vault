---
title: 'urlSession(_:task:willBeginDelayedRequest:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:willbegindelayedrequest:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:willbegindelayedrequest:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate/urlsession%28_%3Atask%3Awillbegindelayedrequest%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:664edbc7432a8418'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskDelegate](../urlsessiontaskdelegate.md)

# urlSession(_:task:willBeginDelayedRequest:completionHandler:)

<sub>Instance Method</sub>

Tells the delegate that a delayed URL session task will now begin loading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, willBeginDelayedRequest request: URLRequest, completionHandler: @escaping @Sendable (URLSession.DelayedRequestDisposition, URLRequest?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, willBeginDelayedRequest request: URLRequest) async -> (URLSession.DelayedRequestDisposition, URLRequest?)
```

## Parameters

- `session` — The session containing the delayed request.

- `task` — The task handling the delayed request.

- `request` — The request that was delayed.

- `completionHandler` — A completion handler to perform the request. The completion handler takes two parameters: a disposition that tells the task how to proceed, and a new request object that is only used if the disposition is [NSURLSessionDelayedRequestUseNewRequest](../urlsession/delayedrequestdisposition/usenewrequest.md).

## Discussion

This method is called when a background session task with a delayed start time (as set with the [earliestBeginDate](../urlsessiontask/earliestbegindate.md) property) is ready to start. This delegate method should only be implemented if the request might become stale while waiting for the network load and needs to be replaced by a new request.

For loading to continue, the delegate must call the completion handler, passing in a disposition that indicates how the task should proceed. Passing the [NSURLSessionDelayedRequestCancel](../urlsession/delayedrequestdisposition/cancel.md) disposition is equivalent to calling [- cancel](<../urlsessiontask/cancel().md>) on the task directly.

## See Also

### Handling delayed and waiting tasks

- [DelayedRequestDisposition](../urlsession/delayedrequestdisposition.md) — The action to take on a delayed URL session task.
- [- URLSession:taskIsWaitingForConnectivity:](<urlsession(__taskiswaitingforconnectivity_).md>) — Tells the delegate that the task is waiting until suitable connectivity is available before beginning the network load.
