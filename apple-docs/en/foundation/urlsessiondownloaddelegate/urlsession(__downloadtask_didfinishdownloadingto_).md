---
title: 'urlSession(_:downloadTask:didFinishDownloadingTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondownloaddelegate/urlsession(_:downloadtask:didfinishdownloadingto:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/urlsession(_:downloadtask:didfinishdownloadingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondownloaddelegate/urlsession%28_%3Adownloadtask%3Adidfinishdownloadingto%3A%29.json'
content_hash: 'sha256:673b7653ed9df60f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDownloadDelegate](../urlsessiondownloaddelegate.md)

# urlSession(_:downloadTask:didFinishDownloadingTo:)

<sub>Instance Method</sub>

Tells the delegate that a download task has finished downloading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didFinishDownloadingTo location: URL)
```

## Parameters

- `session` — The session containing the download task that finished.

- `downloadTask` — The download task that finished.

- `location` — A file URL for the temporary file. Because the file is temporary, you must either open the file for reading or move it to a permanent location in your app’s sandbox container directory before returning from this delegate method. If you choose to open the file for reading, you should do the actual reading in another thread to avoid blocking the delegate queue.
