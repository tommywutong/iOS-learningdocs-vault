---
title: delegateQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysession/delegatequeue
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/delegatequeue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/delegatequeue.json'
content_hash: 'sha256:2c5247f03ae3b6c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# delegateQueue

<sub>Instance Property</sub>

The dispatch queue the session uses to invoke delegate callbacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var delegateQueue: dispatch_queue_t? { get }
```

## See Also

### Managing the delegate object

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the session’s delegate object and the dispatch queue on which to call the delegate’s methods.
- [delegate](delegate.md) — The content key session’s delegate object.
