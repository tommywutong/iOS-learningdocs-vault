---
title: 'urlSession(_:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didsendbodydata:totalbytessent:totalbytesexpectedtosend:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didsendbodydata:totalbytessent:totalbytesexpectedtosend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate/urlsession%28_%3Atask%3Adidsendbodydata%3Atotalbytessent%3Atotalbytesexpectedtosend%3A%29.json'
content_hash: 'sha256:79b90d11372ec46f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskDelegate](../urlsessiontaskdelegate.md)

# urlSession(_:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:)

<sub>Instance Method</sub>

Periodically informs the delegate of the progress of sending body content to the server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, didSendBodyData bytesSent: Int64, totalBytesSent: Int64, totalBytesExpectedToSend: Int64)
```

## Parameters

- `session` — The session containing the data task.

- `task` — The data task.

- `bytesSent` — The number of bytes sent since the last time this delegate method was called.

- `totalBytesSent` — The total number of bytes sent so far.

- `totalBytesExpectedToSend` — The expected length of the body data. The URL loading system can determine the length of the upload data in three ways: - From the length of the `NSData` object provided as the upload body. - From the length of the file on disk provided as the upload body of an upload task (_not_ a download task). - From the `Content-Length` in the request object, if you explicitly set it. Otherwise, the value is [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) (`-1`) if you provided a stream or body data object, or zero (`0`) if you did not.

## Discussion

The `totalBytesSent` and `totalBytesExpectedToSend` parameters are also available as [URLSessionTask](../urlsessiontask.md) properties [countOfBytesSent](../urlsessiontask/countofbytessent.md) and [countOfBytesExpectedToSend](../urlsessiontask/countofbytesexpectedtosend.md). Or, since [URLSessionTask](../urlsessiontask.md) supports [ProgressReporting](../progressreporting.md), you can use the task’s [progress](../urlsessiontask/progress.md) property instead, which may be more convenient.

## See Also

### Working with upload tasks

- [- URLSession:task:needNewBodyStream:](<urlsession(__task_neednewbodystream_).md>) — Tells the delegate when a task requires a new request body stream to send to the remote server.
