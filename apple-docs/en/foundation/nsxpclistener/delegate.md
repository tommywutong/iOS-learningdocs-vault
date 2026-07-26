---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistener/delegate
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener/delegate.json'
content_hash: 'sha256:dda55e6b484c3f77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListener](../nsxpclistener.md)

# delegate

<sub>Instance Property</sub>

The delegate for the listener.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any NSXPCListenerDelegate)? { get set }
```

## Discussion

If no delegate is set, all new connections are rejected. See the documentation for [NSXPCListenerDelegate](../nsxpclistenerdelegate.md) for implementation details.
