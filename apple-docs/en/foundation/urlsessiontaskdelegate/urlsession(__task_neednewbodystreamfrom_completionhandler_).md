---
title: 'urlSession(_:task:needNewBodyStreamFrom:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:neednewbodystreamfrom:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:neednewbodystreamfrom:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate/urlsession%28_%3Atask%3Aneednewbodystreamfrom%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:77537b40e7b72b8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskDelegate](../urlsessiontaskdelegate.md)

# urlSession(_:task:needNewBodyStreamFrom:completionHandler:)

<sub>Instance Method</sub>

Tells the delegate if a task requires a new body stream starting from the given offset. This may be necessary when resuming a failed upload task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, needNewBodyStreamFrom offset: Int64, completionHandler: @escaping @Sendable (InputStream?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, needNewBodyStreamForTask task: URLSessionTask, from offset: Int64) async -> InputStream?
```

## Parameters

- `session` — The session containing the task that needs a new body stream from the given offset.

- `task` — The task that needs a new body stream.

- `offset` — The starting offset required for the body stream.

- `completionHandler` — A completion handler that your delegate method should call with the new body stream.
