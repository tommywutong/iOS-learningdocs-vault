---
title: taskIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/taskidentifier
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/taskidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/taskidentifier.json'
content_hash: 'sha256:f3ff15885668d0a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# taskIdentifier

<sub>Instance Property</sub>

An identifier uniquely identifying the task within a given session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var taskIdentifier: Int { get }
```

## Discussion

This value is unique only within the context of a single session; tasks in other sessions may have the same [taskIdentifier](taskidentifier.md) value.

## See Also

### Obtaining general task information

- [currentRequest](currentrequest.md) — The URL request object currently being handled by the task.
- [originalRequest](originalrequest.md) — The original request object passed when the task was created.
- [response](response.md) — The server’s response to the currently active request.
- [taskDescription](taskdescription.md) — An app-provided string value for the current task.
- [error](error.md) — An error object that indicates why the task failed.
