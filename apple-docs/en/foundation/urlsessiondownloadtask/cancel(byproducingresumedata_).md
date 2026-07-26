---
title: 'cancel(byProducingResumeData:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondownloadtask/cancel(byproducingresumedata:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondownloadtask/cancel(byproducingresumedata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondownloadtask/cancel%28byproducingresumedata%3A%29.json'
content_hash: 'sha256:518c67c51ec1e7b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDownloadTask](../urlsessiondownloadtask.md)

# cancel(byProducingResumeData:)

<sub>Instance Method</sub>

Cancels a download and calls a callback with resume data for later use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel(byProducingResumeData completionHandler: @escaping @Sendable (Data?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelByProducingResumeData() async -> Data?
```

## Parameters

- `completionHandler` — A completion handler that is called when the download has been successfully canceled. If the download is resumable, the completion handler is provided with a `resumeData` object. Your app can later pass this object to a session’s [- downloadTaskWithResumeData:](<../urlsession/downloadtask(withresumedata_).md>) or [- downloadTaskWithResumeData:completionHandler:](<../urlsession/downloadtask(withresumedata_completionhandler_).md>) method to create a new task that resumes the download where it left off. This block is not guaranteed to execute in a particular thread context. As such, you may want specify an appropriate dispatch queue in which to perform any work.

## Discussion

A download can be resumed only if the following conditions are met:

- The resource has not changed since you first requested it
- The task is an HTTP or HTTPS `GET` request
- The server provides either the `ETag` or `Last-Modified` header (or both) in its response
- The server supports byte-range requests
- The temporary file hasn’t been deleted by the system in response to disk space pressure
