---
title: URLSession.DataTaskPublisher
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/datataskpublisher
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/datataskpublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/datataskpublisher.json'
content_hash: 'sha256:fff203545b5da12a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# URLSession.DataTaskPublisher

<sub>Structure</sub>

A publisher that delivers the results of performing URL session data tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DataTaskPublisher
```

## Relationships

- **Conforms To**: [Publisher](../../combine/publisher.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Declaring publisher topography

- [Output](datataskpublisher/output.md) — The kind of values published by this publisher.
- [Failure](datataskpublisher/failure.md) — The kind of errors this publisher might publish.

### Creating a data task publisher

- [init(request:session:)](<datataskpublisher/init(request_session_).md>) — Creates a data task publisher from the provided URL request and URL session.

### Inspecting data task properties

- [request](datataskpublisher/request.md) — The URL request performed by the data task associated with this publisher.
- [session](datataskpublisher/session.md) — The URL session that performs the data task associated with this publisher.

## See Also

### Performing tasks as a Combine Publisher

- [Processing URL session data task results with Combine](../processing-url-session-data-task-results-with-combine.md) — Use a chain of asynchronous operators to receive and process data fetched from a URL.
- [dataTaskPublisher(for:)](<datataskpublisher(for_)-61v3e.md>) — Returns a publisher that wraps a URL session data task for a given URL request.
- [dataTaskPublisher(for:)](<datataskpublisher(for_)-5kiir.md>) — Returns a publisher that wraps a URL session data task for a given URL.
