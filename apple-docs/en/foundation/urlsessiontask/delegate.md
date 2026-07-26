---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/delegate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/delegate.json'
content_hash: 'sha256:38ee48981525b93f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# delegate

<sub>Instance Property</sub>

A delegate specific to the task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var delegate: (any URLSessionTaskDelegate)? { get set }
```

## Discussion

This task-specific delegate receives messages from the task before the session’s [delegate](../urlsession/delegate.md) receives them. This is similar to the behavior of the `delegate` parameter used by the asychronous methods in [URLSession](../urlsession.md) like [bytes(for:delegate:)](<../urlsession/bytes(for_delegate_).md>) and [data(for:delegate:)](<../urlsession/data(for_delegate_).md>).

## See Also

### Using a task-specific delegate

- [URLSessionTaskDelegate](../urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
