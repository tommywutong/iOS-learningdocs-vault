---
title: 'urlSession(_:streamTask:didBecome:outputStream:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionstreamdelegate/urlsession(_:streamtask:didbecome:outputstream:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate/urlsession(_:streamtask:didbecome:outputstream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamdelegate/urlsession%28_%3Astreamtask%3Adidbecome%3Aoutputstream%3A%29.json'
content_hash: 'sha256:2a2d480def2cd5c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamDelegate](../urlsessionstreamdelegate.md)

# urlSession(_:streamTask:didBecome:outputStream:)

<sub>Instance Method</sub>

Tells the delegate that the stream task has been completed as a result of the stream task calling the [- captureStreams](<../urlsessionstreamtask/capturestreams().md>) method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, streamTask: URLSessionStreamTask, didBecome inputStream: InputStream, outputStream: OutputStream)
```

## Parameters

- `session` — The session of the stream task that has been completed.

- `streamTask` — The stream task that has been completed.

- `inputStream` — The created input stream. This [InputStream](../inputstream.md) object is unopened.

- `outputStream` — The created output stream. This [OutputStream](../outputstream.md) object is unopened

## Discussion

This delegate method will only be called after all enqueued reads and writes for the stream task have been completed.
