---
title: URLSession.ResponseDisposition.becomeDownload
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/responsedisposition/becomedownload
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/responsedisposition/becomedownload'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/responsedisposition/becomedownload.json'
content_hash: 'sha256:ea6c3feb002553f4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSession](../../urlsession.md) · [ResponseDisposition](../responsedisposition.md)

# URLSession.ResponseDisposition.becomeDownload

<sub>Case</sub>

Convert the response for this request to use a [URLSessionDownloadTask](../../urlsessiondownloadtask.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case becomeDownload
```

## Discussion

When used with the completion handler from [- URLSession:dataTask:didReceiveResponse:completionHandler:](<../../urlsessiondatadelegate/urlsession(__datatask_didreceive_completionhandler_).md>), this disposition converts the data task to a download task. This will result in your delegate’s [- URLSession:dataTask:didBecomeDownloadTask:](<../../urlsessiondatadelegate/urlsession(__datatask_didbecome_)-60op5.md>) being called to provide you with the new download task that supersedes the current task.

## See Also

### Task dispositions

- [NSURLSessionResponseCancel](cancel.md) — Cancel the load.
- [NSURLSessionResponseAllow](allow.md) — Allow the load operation to continue.
- [NSURLSessionResponseBecomeStream](becomestream.md) — Convert the response for this request to use a [URLSessionStreamTask](../../urlsessionstreamtask.md).
