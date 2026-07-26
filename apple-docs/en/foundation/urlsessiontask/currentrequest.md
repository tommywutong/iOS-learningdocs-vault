---
title: currentRequest
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/currentrequest
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/currentrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/currentrequest.json'
content_hash: 'sha256:56d68c2429d0154b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# currentRequest

<sub>Instance Property</sub>

The URL request object currently being handled by the task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentRequest: URLRequest? { get }
```

## Discussion

This value is typically the same as the initial request ([originalRequest](originalrequest.md)) except when the server has responded to the initial request with a redirect to a different URL.

## See Also

### Obtaining general task information

- [originalRequest](originalrequest.md) — The original request object passed when the task was created.
- [response](response.md) — The server’s response to the currently active request.
- [taskDescription](taskdescription.md) — An app-provided string value for the current task.
- [taskIdentifier](taskidentifier.md) — An identifier uniquely identifying the task within a given session.
- [error](error.md) — An error object that indicates why the task failed.
