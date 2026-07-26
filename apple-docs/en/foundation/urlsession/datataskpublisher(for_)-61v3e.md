---
title: 'dataTaskPublisher(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/datataskpublisher(for:)-61v3e'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/datataskpublisher(for:)-61v3e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/datataskpublisher%28for%3A%29-61v3e.json'
content_hash: 'sha256:4ff5b9781fffbd5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# dataTaskPublisher(for:)

<sub>Instance Method</sub>

Returns a publisher that wraps a URL session data task for a given URL request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dataTaskPublisher(for request: URLRequest) -> URLSession.DataTaskPublisher
```

## Parameters

- `request` — The URL request for which to create a data task.

## Discussion

The publisher publishes data when the task completes, or terminates if the task fails with an error.

## See Also

### Performing tasks as a Combine Publisher

- [Processing URL session data task results with Combine](../processing-url-session-data-task-results-with-combine.md) — Use a chain of asynchronous operators to receive and process data fetched from a URL.
- [dataTaskPublisher(for:)](<datataskpublisher(for_)-5kiir.md>) — Returns a publisher that wraps a URL session data task for a given URL.
- [DataTaskPublisher](datataskpublisher.md) — A publisher that delivers the results of performing URL session data tasks.
