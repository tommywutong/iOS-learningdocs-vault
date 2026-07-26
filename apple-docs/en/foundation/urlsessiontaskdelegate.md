---
title: URLSessionTaskDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontaskdelegate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate.json'
content_hash: 'sha256:d8d9248cbbc4456f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionTaskDelegate

<sub>Protocol</sub>

A protocol that defines methods that URL session instances call on their delegates to handle task-level events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol URLSessionTaskDelegate : URLSessionDelegate
```

## Overview

You use this protocol in one of two ways, depending on how you use a [URLSession](urlsession.md):

- If you create tasks with Swift’s `async`-`await` syntax, using methods like [bytes(for:delegate:)](<urlsession/bytes(for_delegate_).md>) and [data(for:delegate:)](<urlsession/data(for_delegate_).md>), you pass a `delegate` argument of this type. The delegate receives callbacks for things like task progress, while the call point awaits the completion of the task.
- If you add tasks to the session with methods like [- dataTaskWithURL:](<urlsession/datatask(with_)-10dy7.md>) and [- downloadTaskWithURL:](<urlsession/downloadtask(with_)-1onj.md>), then you implement this protocol’s methods in a [delegate](urlsession/delegate.md) you set on the session. This session delegate may also implement other protocols as appropriate, like [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md) and [URLSessionDataDelegate](urlsessiondatadelegate.md). You can also assign a delegate of this type directly to the task to intercept callbacks before the task delivers them to the session’s delegate.

> [!note] Note
> Your [URLSession](urlsession.md) object doesn’t need to have a delegate. If you don’t assign a delegate, the session uses a system-provided delegate. In this case, you must provide a completion callback or use the Swift `async`-`await` methods to obtain the data.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [URLSessionDelegate](urlsessiondelegate.md)

- **Inherited By**: [URLSessionDataDelegate](urlsessiondatadelegate.md), [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md), [URLSessionStreamDelegate](urlsessionstreamdelegate.md), [URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md)

## Topics

### Handling task life cycle changes

- [- URLSession:task:didCompleteWithError:](<urlsessiontaskdelegate/urlsession(__task_didcompletewitherror_).md>) — Tells the delegate that the task finished transferring data.

### Handling redirects

- [- URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:](<urlsessiontaskdelegate/urlsession(__task_willperformhttpredirection_newrequest_completionhandler_).md>) — Tells the delegate that the remote server requested an HTTP redirect.

### Working with upload tasks

- [- URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:](<urlsessiontaskdelegate/urlsession(__task_didsendbodydata_totalbytessent_totalbytesexpectedtosend_).md>) — Periodically informs the delegate of the progress of sending body content to the server.
- [- URLSession:task:needNewBodyStream:](<urlsessiontaskdelegate/urlsession(__task_neednewbodystream_).md>) — Tells the delegate when a task requires a new request body stream to send to the remote server.

### Handling authentication challenges

- [- URLSession:task:didReceiveChallenge:completionHandler:](<urlsessiontaskdelegate/urlsession(__task_didreceive_completionhandler_).md>) — Requests credentials from the delegate in response to an authentication request from the remote server.
- [AuthChallengeDisposition](urlsession/authchallengedisposition.md) — Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.

### Handling delayed and waiting tasks

- [- URLSession:task:willBeginDelayedRequest:completionHandler:](<urlsessiontaskdelegate/urlsession(__task_willbegindelayedrequest_completionhandler_).md>) — Tells the delegate that a delayed URL session task will now begin loading.
- [DelayedRequestDisposition](urlsession/delayedrequestdisposition.md) — The action to take on a delayed URL session task.
- [- URLSession:taskIsWaitingForConnectivity:](<urlsessiontaskdelegate/urlsession(__taskiswaitingforconnectivity_).md>) — Tells the delegate that the task is waiting until suitable connectivity is available before beginning the network load.

### Collecting task metrics

- [- URLSession:task:didFinishCollectingMetrics:](<urlsessiontaskdelegate/urlsession(__task_didfinishcollecting_).md>) — Tells the delegate that the session finished collecting metrics for the task.
- [URLSessionTaskMetrics](urlsessiontaskmetrics.md) — An object encapsulating the metrics for a session task.

### Instance Methods

- [- URLSession:didCreateTask:](<urlsessiontaskdelegate/urlsession(__didcreatetask_).md>)
- [- URLSession:task:didReceiveInformationalResponse:](<urlsessiontaskdelegate/urlsession(__task_didreceiveinformationalresponse_).md>)
- [- URLSession:task:needNewBodyStreamFromOffset:completionHandler:](<urlsessiontaskdelegate/urlsession(__task_neednewbodystreamfrom_completionhandler_).md>) — Tells the delegate if a task requires a new body stream starting from the given offset. This may be necessary when resuming a failed upload task.

## See Also

### Working with a delegate

- [delegate](urlsession/delegate.md) — The delegate assigned when this object was created.
- [URLSessionDelegate](urlsessiondelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle session-level events, like session life cycle changes.
- [delegateQueue](urlsession/delegatequeue.md) — The operation queue provided when this object was created.
