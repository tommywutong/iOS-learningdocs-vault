---
title: 'requestIsCacheEquivalent(_:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/requestiscacheequivalent(_:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/requestiscacheequivalent(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/requestiscacheequivalent%28_%3Ato%3A%29.json'
content_hash: 'sha256:6a7840914669fab9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# requestIsCacheEquivalent(_:to:)

<sub>Type Method</sub>

A Boolean value indicating whether two requests are equivalent for cache purposes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func requestIsCacheEquivalent(_ a: URLRequest, to b: URLRequest) -> Bool
```

## Parameters

- `a` — The request to compare with `bRequest`.

- `b` — The request to compare with `aRequest`.

## Return Value

[true](../../swift/true.md) if `aRequest` and `bRequest` are equivalent for cache purposes, [false](../../swift/false.md) otherwise.

## Discussion

Requests are considered equivalent for cache purposes if and only if they would be handled by the same protocol and that protocol declares them equivalent after performing implementation-specific checks.

The [URLProtocol](../urlprotocol.md) implementation of this method compares the URLs of the requests to determine if the requests should be considered equivalent. Subclasses can override this method to provide protocol-specific comparisons.
