---
title: 'responds(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsproxy/responds(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsproxy/responds(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsproxy/responds%28to%3A%29.json'
content_hash: 'sha256:9addf5e118126cb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSProxy](../nsproxy.md)

# responds(to:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the receiving class responds to a given selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func responds(to aSelector: Selector) -> Bool
```

## Parameters

- `aSelector` — A selector.

## Return Value

[true](../../swift/true.md) if the receiving class responds to `aSelector` messages, otherwise [false](../../swift/false.md).
