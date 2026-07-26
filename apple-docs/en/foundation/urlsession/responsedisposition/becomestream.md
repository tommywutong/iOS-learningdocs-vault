---
title: URLSession.ResponseDisposition.becomeStream
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/responsedisposition/becomestream
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/responsedisposition/becomestream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/responsedisposition/becomestream.json'
content_hash: 'sha256:ccccec681e2c2c4b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSession](../../urlsession.md) · [ResponseDisposition](../responsedisposition.md)

# URLSession.ResponseDisposition.becomeStream

<sub>Case</sub>

Convert the response for this request to use a [URLSessionStreamTask](../../urlsessionstreamtask.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case becomeStream
```

## Discussion

When used with the completion handler from [- URLSession:dataTask:didReceiveResponse:completionHandler:](<../../urlsessiondatadelegate/urlsession(__datatask_didreceive_completionhandler_).md>), this disposition converts the task to a stream task. This will result in your delegate’s [- URLSession:dataTask:didBecomeStreamTask:](<../../urlsessiondatadelegate/urlsession(__datatask_didbecome_)-7nqzu.md>) being called to provide you with the new stream task that supersedes the current task.

## See Also

### Task dispositions

- [NSURLSessionResponseCancel](cancel.md) — Cancel the load.
- [NSURLSessionResponseAllow](allow.md) — Allow the load operation to continue.
- [NSURLSessionResponseBecomeDownload](becomedownload.md) — Convert the response for this request to use a [URLSessionDownloadTask](../../urlsessiondownloadtask.md).
