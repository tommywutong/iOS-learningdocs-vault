---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysession/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/delegate.json'
content_hash: 'sha256:16073544b2773a15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# delegate

<sub>Instance Property</sub>

The content key session’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any AVContentKeySessionDelegate)? { get }
```

## Discussion

Set the session’s delegate using the [- setDelegate:queue:](<setdelegate(__queue_).md>) method.

## See Also

### Managing the delegate object

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the session’s delegate object and the dispatch queue on which to call the delegate’s methods.
- [delegateQueue](delegatequeue.md) — The dispatch queue the session uses to invoke delegate callbacks.
