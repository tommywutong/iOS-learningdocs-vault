---
title: delegateQueue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/delegatequeue
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/delegatequeue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/delegatequeue.json'
content_hash: 'sha256:7e1d03d8c37a5b3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# delegateQueue

<sub>Instance Property</sub>

The operation queue provided when this object was created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var delegateQueue: OperationQueue { get }
```

## Discussion

All delegate method calls and completion handlers related to the session are performed on this queue. The session object keeps a strong reference to this queue until your app exits or the session object is deallocated. If you do not invalidate the session, your app leaks memory until it exits.

> [!note] Note
> This queue must be set at object creation time and may not be changed.

## See Also

### Working with a delegate

- [delegate](delegate.md) — The delegate assigned when this object was created.
- [URLSessionDelegate](../urlsessiondelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle session-level events, like session life cycle changes.
- [URLSessionTaskDelegate](../urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
