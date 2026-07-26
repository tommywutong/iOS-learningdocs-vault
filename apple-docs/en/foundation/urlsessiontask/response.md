---
title: response
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/response
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/response'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/response.json'
content_hash: 'sha256:d7936831fbb2f9a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# response

<sub>Instance Property</sub>

The server’s response to the currently active request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var response: URLResponse? { get }
```

## Discussion

This object provides information about the request as provided by the server. This information always includes the original URL. It may also include an expected length, MIME type information, encoding information, a suggested filename, or a combination of these.

## See Also

### Obtaining general task information

- [currentRequest](currentrequest.md) — The URL request object currently being handled by the task.
- [originalRequest](originalrequest.md) — The original request object passed when the task was created.
- [taskDescription](taskdescription.md) — An app-provided string value for the current task.
- [taskIdentifier](taskidentifier.md) — An identifier uniquely identifying the task within a given session.
- [error](error.md) — An error object that indicates why the task failed.
