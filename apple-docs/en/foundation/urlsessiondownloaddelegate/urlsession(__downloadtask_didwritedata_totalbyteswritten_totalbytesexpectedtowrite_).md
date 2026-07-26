---
title: 'urlSession(_:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondownloaddelegate/urlsession(_:downloadtask:didwritedata:totalbyteswritten:totalbytesexpectedtowrite:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/urlsession(_:downloadtask:didwritedata:totalbyteswritten:totalbytesexpectedtowrite:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondownloaddelegate/urlsession%28_%3Adownloadtask%3Adidwritedata%3Atotalbyteswritten%3Atotalbytesexpectedtowrite%3A%29.json'
content_hash: 'sha256:ad90c3ff529c887d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDownloadDelegate](../urlsessiondownloaddelegate.md)

# urlSession(_:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:)

<sub>Instance Method</sub>

Periodically informs the delegate about the download’s progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didWriteData bytesWritten: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)
```

## Parameters

- `session` — The session containing the download task.

- `downloadTask` — The download task.

- `bytesWritten` — The number of bytes transferred since the last time this delegate method was called.

- `totalBytesWritten` — The total number of bytes transferred so far.

- `totalBytesExpectedToWrite` — The expected length of the file, as provided by the `Content-Length` header. If this header was not provided, the value is [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md).
