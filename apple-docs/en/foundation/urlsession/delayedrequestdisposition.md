---
title: URLSession.DelayedRequestDisposition
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/delayedrequestdisposition
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/delayedrequestdisposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/delayedrequestdisposition.json'
content_hash: 'sha256:4c1548df300c1ba0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# URLSession.DelayedRequestDisposition

<sub>Enumeration</sub>

The action to take on a delayed URL session task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DelayedRequestDisposition
```

## Overview

The values of this enumeration indicate how to handle a task with a delayed start time (as set with the [earliestBeginDate](../urlsessiontask/earliestbegindate.md) property). When the task is ready to start, it calls the [- URLSession:task:willBeginDelayedRequest:completionHandler:](<../urlsessiontaskdelegate/urlsession(__task_willbegindelayedrequest_completionhandler_).md>) method of [URLSessionTaskDelegate](../urlsessiontaskdelegate.md). The implementation of this method must call the provided completion handler, passing in one case of this enumeration as the first argument. If the [NSURLSessionDelayedRequestUseNewRequest](delayedrequestdisposition/usenewrequest.md) disposition is used for the first argument, the caller must also provide a new [NSURLRequest](../nsurlrequest.md) as the second argument.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Dispositions

- [NSURLSessionDelayedRequestCancel](delayedrequestdisposition/cancel.md) — A disposition indicating that the task should be canceled.
- [NSURLSessionDelayedRequestContinueLoading](delayedrequestdisposition/continueloading.md) — A disposition indicating that the task should proceed with the original request.
- [NSURLSessionDelayedRequestUseNewRequest](delayedrequestdisposition/usenewrequest.md) — A disposition indicating that the task should use a new request to perform the network load.

### Initializers

- [init(rawValue:)](<delayedrequestdisposition/init(rawvalue_).md>)

## See Also

### Handling delayed and waiting tasks

- [- URLSession:task:willBeginDelayedRequest:completionHandler:](<../urlsessiontaskdelegate/urlsession(__task_willbegindelayedrequest_completionhandler_).md>) — Tells the delegate that a delayed URL session task will now begin loading.
- [- URLSession:taskIsWaitingForConnectivity:](<../urlsessiontaskdelegate/urlsession(__taskiswaitingforconnectivity_).md>) — Tells the delegate that the task is waiting until suitable connectivity is available before beginning the network load.
