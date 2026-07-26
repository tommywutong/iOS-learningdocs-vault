---
title: 'canInit(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/caninit(with:)-76brg'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/caninit(with:)-76brg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/caninit%28with%3A%29-76brg.json'
content_hash: 'sha256:6ac0f2efa68d58e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# canInit(with:)

<sub>Type Method</sub>

Determines whether the protocol subclass can handle the specified request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func canInit(with request: URLRequest) -> Bool
```

## Parameters

- `request` — The request to be handled.

## Return Value

[true](../../swift/true.md) if the protocol subclass can handle `request`, otherwise [false](../../swift/false.md).

## Discussion

A subclass should inspect `request` and determine whether or not the implementation can perform a load with that request.

This is an abstract method and subclasses must provide an implementation.

## See Also

### Determining If a subclass can handle a request

- [+ canInitWithTask:](<caninit(with_)-18gbo.md>) — Determines whether the protocol subclass can handle the specified task.
