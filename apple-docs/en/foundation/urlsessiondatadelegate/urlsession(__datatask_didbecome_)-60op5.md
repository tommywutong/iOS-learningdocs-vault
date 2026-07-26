---
title: 'urlSession(_:dataTask:didBecome:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-60op5'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-60op5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondatadelegate/urlsession%28_%3Adatatask%3Adidbecome%3A%29-60op5.json'
content_hash: 'sha256:4a4bbf22e03ab801'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDataDelegate](../urlsessiondatadelegate.md)

# urlSession(_:dataTask:didBecome:)

<sub>Instance Method</sub>

Tells the delegate that the data task was changed to a download task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didBecome downloadTask: URLSessionDownloadTask)
```

## Parameters

- `session` — The session containing the task that was replaced by a download task.

- `dataTask` — The data task that was replaced by a download task.

- `downloadTask` — The new download task that replaced the data task.

## Discussion

When your [- URLSession:dataTask:didReceiveResponse:completionHandler:](<urlsession(__datatask_didreceive_completionhandler_).md>) delegate method uses the [NSURLSessionResponseBecomeDownload](../urlsession/responsedisposition/becomedownload.md) disposition to convert the request to use a download, the session calls this delegate method to provide you with the new download task. After this call, the session delegate receives no further delegate method calls related to the original data task.

## See Also

### Handling task life cycle changes

- [- URLSession:dataTask:didReceiveResponse:completionHandler:](<urlsession(__datatask_didreceive_completionhandler_).md>) — Tells the delegate that the data task received the initial reply (headers) from the server.
- [ResponseDisposition](../urlsession/responsedisposition.md) — Constants indicating how a data or upload session should proceed after receiving the initial headers.
- [- URLSession:dataTask:didBecomeStreamTask:](<urlsession(__datatask_didbecome_)-7nqzu.md>) — Tells the delegate that the data task was changed to a stream task.
