---
title: 'cancel(byProducingResumeData:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionuploadtask/cancel(byproducingresumedata:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionuploadtask/cancel(byproducingresumedata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionuploadtask/cancel%28byproducingresumedata%3A%29.json'
content_hash: 'sha256:f2b9d02bf1023370'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionUploadTask](../urlsessionuploadtask.md)

# cancel(byProducingResumeData:)

<sub>Instance Method</sub>

Cancels an upload and calls the completion handler with resume data for later use. resumeData will be nil if the server does not support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel(byProducingResumeData completionHandler: @escaping @Sendable (Data?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelByProducingResumeData() async -> Data?
```

## Parameters

- `completionHandler` — The completion handler to call when the upload has been successfully canceled.
