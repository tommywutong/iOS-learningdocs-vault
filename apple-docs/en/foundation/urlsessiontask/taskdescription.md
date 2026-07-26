---
title: taskDescription
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/taskdescription
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/taskdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/taskdescription.json'
content_hash: 'sha256:c348a517756d1a35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# taskDescription

<sub>Instance Property</sub>

An app-provided string value for the current task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var taskDescription: String? { get set }
```

## Discussion

The system doesn’t interpret this value; use it for whatever purpose you see fit. For example, you could store a description of the task for debugging purposes, or a key to track the task in your own data structures.

## See Also

### Obtaining general task information

- [currentRequest](currentrequest.md) — The URL request object currently being handled by the task.
- [originalRequest](originalrequest.md) — The original request object passed when the task was created.
- [response](response.md) — The server’s response to the currently active request.
- [taskIdentifier](taskidentifier.md) — An identifier uniquely identifying the task within a given session.
- [error](error.md) — An error object that indicates why the task failed.
