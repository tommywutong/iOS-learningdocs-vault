---
title: 'urlSession(_:downloadTask:didResumeAtOffset:expectedTotalBytes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondownloaddelegate/urlsession(_:downloadtask:didresumeatoffset:expectedtotalbytes:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/urlsession(_:downloadtask:didresumeatoffset:expectedtotalbytes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondownloaddelegate/urlsession%28_%3Adownloadtask%3Adidresumeatoffset%3Aexpectedtotalbytes%3A%29.json'
content_hash: 'sha256:a369a90812c1af0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDownloadDelegate](../urlsessiondownloaddelegate.md)

# urlSession(_:downloadTask:didResumeAtOffset:expectedTotalBytes:)

<sub>Instance Method</sub>

Tells the delegate that the download task has resumed downloading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didResumeAtOffset fileOffset: Int64, expectedTotalBytes: Int64)
```

## Parameters

- `session` — The session containing the download task that finished.

- `downloadTask` — The download task that resumed. See explanation in the discussion.

- `fileOffset` — If the file’s cache policy or last modified date prevents reuse of the existing content, then this value is zero. Otherwise, this value is an integer representing the number of bytes on disk that do not need to be retrieved again. > [!note] Note > In some situations, it may be possible for the transfer to resume earlier in the file than where the previous transfer ended.

- `expectedTotalBytes` — The expected length of the file, as provided by the `Content-Length` header. If this header was not provided, the value is [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md).

## Discussion

If a resumable download task is canceled or fails, you can request a `resumeData` object that provides enough information to restart the download in the future. Later, you can call [- downloadTaskWithResumeData:](<../urlsession/downloadtask(withresumedata_).md>) or [- downloadTaskWithResumeData:completionHandler:](<../urlsession/downloadtask(withresumedata_completionhandler_).md>) with that data.

When you call those methods, you get a new download task. As soon as you resume that task, the session calls this method with that new task to indicate that the download is resumed.
