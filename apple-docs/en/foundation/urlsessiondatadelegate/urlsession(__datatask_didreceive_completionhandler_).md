---
title: 'urlSession(_:dataTask:didReceive:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondatadelegate/urlsession%28_%3Adatatask%3Adidreceive%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:8f5f35889c9ad48a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDataDelegate](../urlsessiondatadelegate.md)

# urlSession(_:dataTask:didReceive:completionHandler:)

<sub>Instance Method</sub>

Tells the delegate that the data task received the initial reply (headers) from the server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive response: URLResponse, completionHandler: @escaping @Sendable (URLSession.ResponseDisposition) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive response: URLResponse) async -> URLSession.ResponseDisposition
```

## Parameters

- `session` — The session containing the data task that received an initial reply.

- `dataTask` — The data task that received an initial reply.

- `response` — A URL response object populated with headers.

- `completionHandler` — A completion handler that your code calls to continue a transfer, passing a [ResponseDisposition](../urlsession/responsedisposition.md) constant to indicate whether the transfer should continue as a data task or should become a download task. - If you pass [NSURLSessionResponseAllow](../urlsession/responsedisposition/allow.md), the task continues as a data task. - If you pass [NSURLSessionResponseCancel](../urlsession/responsedisposition/cancel.md), the task is canceled. - If you pass [NSURLSessionResponseBecomeDownload](../urlsession/responsedisposition/becomedownload.md), your delegate’s [- URLSession:dataTask:didBecomeDownloadTask:](<urlsession(__datatask_didbecome_)-60op5.md>) method is called to provide the new download task that supersedes the current task.

## Discussion

Implementing this method is optional unless you need to cancel the transfer or convert it to a download task when the response headers are first received. If you don’t provide this delegate method, the session always allows the task to continue.

You also implement this method if you need to support the fairly obscure `multipart/x-mixed-replace` content type. With that content type, the server sends a series of parts, each of which is intended to replace the previous part. The session calls this method at the beginning of each part, followed by one or more calls to [- URLSession:dataTask:didReceiveData:](<urlsession(__datatask_didreceive_).md>) with the contents of that part.

Each time the [- URLSession:dataTask:didReceiveResponse:completionHandler:](<urlsession(__datatask_didreceive_completionhandler_).md>) method is called for a part, collect the data received for the previous part (if any) and process the data as needed for your application. This processing can include storing the data to the filesystem, parsing it into custom types, or displaying it to the user. Next, begin receiving the next part by calling the completion handler with the [NSURLSessionResponseAllow](../urlsession/responsedisposition/allow.md) constant. Finally, if you have also implemented [- URLSession:task:didCompleteWithError:](<../urlsessiontaskdelegate/urlsession(__task_didcompletewitherror_).md>), the session will call it after sending all the data for the last part.

## See Also

### Handling task life cycle changes

- [ResponseDisposition](../urlsession/responsedisposition.md) — Constants indicating how a data or upload session should proceed after receiving the initial headers.
- [- URLSession:dataTask:didBecomeDownloadTask:](<urlsession(__datatask_didbecome_)-60op5.md>) — Tells the delegate that the data task was changed to a download task.
- [- URLSession:dataTask:didBecomeStreamTask:](<urlsession(__datatask_didbecome_)-7nqzu.md>) — Tells the delegate that the data task was changed to a stream task.
