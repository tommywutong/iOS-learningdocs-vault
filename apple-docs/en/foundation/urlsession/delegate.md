---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/delegate
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/delegate.json'
content_hash: 'sha256:acbd7efbad31aeab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# delegate

<sub>Instance Property</sub>

The delegate assigned when this object was created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var delegate: (any URLSessionDelegate)? { get }
```

## Discussion

This delegate object is responsible for handling authentication challenges, for making caching decisions, and for handling other session-related events. The session object keeps a strong reference to this delegate until your app exits or explicitly invalidates the session. If you do not invalidate the session, your app leaks memory until it exits.

> [!note] Note
> This delegate object must be set at object creation time and may not be changed.

## See Also

### Working with a delegate

- [URLSessionDelegate](../urlsessiondelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle session-level events, like session life cycle changes.
- [URLSessionTaskDelegate](../urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
- [delegateQueue](delegatequeue.md) — The operation queue provided when this object was created.
