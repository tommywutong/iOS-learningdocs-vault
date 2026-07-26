---
title: error
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/error
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/error.json'
content_hash: 'sha256:79157f4b49f23959'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# error

<sub>Instance Property</sub>

An error object that indicates why the task failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

This value is `nil` if the task is still active or if the transfer completed successfully.

## See Also

### Obtaining general task information

- [currentRequest](currentrequest.md) — The URL request object currently being handled by the task.
- [originalRequest](originalrequest.md) — The original request object passed when the task was created.
- [response](response.md) — The server’s response to the currently active request.
- [taskDescription](taskdescription.md) — An app-provided string value for the current task.
- [taskIdentifier](taskidentifier.md) — An identifier uniquely identifying the task within a given session.
