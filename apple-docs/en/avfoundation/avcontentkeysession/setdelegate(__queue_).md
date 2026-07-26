---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:732e89da46c28e70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the session’s delegate object and the dispatch queue on which to call the delegate’s methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setDelegate(_ delegate: (any AVContentKeySessionDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — An object that conforms to the [AVContentKeySessionDelegate](../avcontentkeysessiondelegate.md) protocol.

- `delegateQueue` — The dispatch queue on which the session calls the delegate object.

## See Also

### Managing the delegate object

- [delegate](delegate.md) — The content key session’s delegate object.
- [delegateQueue](delegatequeue.md) — The dispatch queue the session uses to invoke delegate callbacks.
