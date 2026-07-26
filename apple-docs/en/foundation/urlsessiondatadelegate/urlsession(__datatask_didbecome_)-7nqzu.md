---
title: 'urlSession(_:dataTask:didBecome:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-7nqzu'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-7nqzu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondatadelegate/urlsession%28_%3Adatatask%3Adidbecome%3A%29-7nqzu.json'
content_hash: 'sha256:5f6db43559a4b1fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDataDelegate](../urlsessiondatadelegate.md)

# urlSession(_:dataTask:didBecome:)

<sub>Instance Method</sub>

Tells the delegate that the data task was changed to a stream task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didBecome streamTask: URLSessionStreamTask)
```

## Parameters

- `session` — The session containing the task that was replaced by a stream task.

- `dataTask` — The data task that was replaced by a stream task.

- `streamTask` — The new stream task that replaced the data task.

## Discussion

When your [- URLSession:dataTask:didReceiveResponse:completionHandler:](<urlsession(__datatask_didreceive_completionhandler_).md>) delegate method uses the [NSURLSessionResponseBecomeStream](../urlsession/responsedisposition/becomestream.md) disposition to convert the request to use a stream, the session calls this delegate method to provide you with the new stream task. After this call, the session delegate receives no further delegate method calls related to the original data task.

For requests that were pipelined, the stream task allows only reading, and the object  immediately sends the delegate message [- URLSession:writeClosedForStreamTask:](<../urlsessionstreamdelegate/urlsession(__writeclosedfor_).md>). You can disable pipelining for all requests in a session by setting the [HTTPShouldUsePipelining](../urlsessionconfiguration/httpshouldusepipelining.md) property on its [URLSessionConfiguration](../urlsessionconfiguration.md) object, or for individual requests  by setting the [HTTPShouldUsePipelining](../nsurlrequest/httpshouldusepipelining.md) property on an [NSURLRequest](../nsurlrequest.md) object.

## See Also

### Handling task life cycle changes

- [- URLSession:dataTask:didReceiveResponse:completionHandler:](<urlsession(__datatask_didreceive_completionhandler_).md>) — Tells the delegate that the data task received the initial reply (headers) from the server.
- [ResponseDisposition](../urlsession/responsedisposition.md) — Constants indicating how a data or upload session should proceed after receiving the initial headers.
- [- URLSession:dataTask:didBecomeDownloadTask:](<urlsession(__datatask_didbecome_)-60op5.md>) — Tells the delegate that the data task was changed to a download task.
