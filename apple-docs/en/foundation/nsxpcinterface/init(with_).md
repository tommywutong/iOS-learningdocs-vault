---
title: 'init(with:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcinterface/init(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcinterface/init(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcinterface/init%28with%3A%29.json'
content_hash: 'sha256:2ecc950bf4121f9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCInterface](../nsxpcinterface.md)

# init(with:)

<sub>Initializer</sub>

Returns an NSXPCInterface instance for a given protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(with protocol: Protocol)
```

## Discussion

Most interfaces do not need any further configuration. Interfaces with collection classes or additional proxy objects should be configured using the other methods in this class.
