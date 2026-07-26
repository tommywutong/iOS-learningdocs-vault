---
title: 'urlSession(_:task:needNewBodyStream:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:neednewbodystream:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:neednewbodystream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate/urlsession%28_%3Atask%3Aneednewbodystream%3A%29.json'
content_hash: 'sha256:ef51d2da8bfd379d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskDelegate](../urlsessiontaskdelegate.md)

# urlSession(_:task:needNewBodyStream:)

<sub>Instance Method</sub>

Tells the delegate when a task requires a new request body stream to send to the remote server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, needNewBodyStream completionHandler: @escaping @Sendable (InputStream?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, needNewBodyStreamForTask task: URLSessionTask) async -> InputStream?
```

## Parameters

- `session` — The session containing the task that needs a new body stream.

- `task` — The task that needs a new body stream.

- `completionHandler` — A completion handler that your delegate method should call with the new body stream.

## Discussion

The task calls this delegate method under two circumstances:

- To provide the initial request body stream if the task was created with [- uploadTaskWithStreamedRequest:](<../urlsession/uploadtask(withstreamedrequest_).md>)
- To provide a replacement request body stream if the task needs to resend a request that has a body stream because of an authentication challenge or other recoverable server error.

> [!note] Note
> You don’t need to implement this method if your code provides the request body using a file URL or a data object.

## See Also

### Working with upload tasks

- [- URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:](<urlsession(__task_didsendbodydata_totalbytessent_totalbytesexpectedtosend_).md>) — Periodically informs the delegate of the progress of sending body content to the server.
