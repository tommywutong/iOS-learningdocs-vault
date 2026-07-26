---
title: originalRequest
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/originalrequest
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/originalrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/originalrequest.json'
content_hash: 'sha256:330d898c34a0d6f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# originalRequest

<sub>Instance Property</sub>

The original request object passed when the task was created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var originalRequest: URLRequest? { get }
```

## Discussion

This value is typically the same as the currently active request ([currentRequest](currentrequest.md)) except when the server has responded to the initial request with a redirect to a different URL.

## See Also

### Obtaining general task information

- [currentRequest](currentrequest.md) — The URL request object currently being handled by the task.
- [response](response.md) — The server’s response to the currently active request.
- [taskDescription](taskdescription.md) — An app-provided string value for the current task.
- [taskIdentifier](taskidentifier.md) — An identifier uniquely identifying the task within a given session.
- [error](error.md) — An error object that indicates why the task failed.
