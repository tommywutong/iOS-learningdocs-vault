---
title: 'canonicalRequest(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/canonicalrequest(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/canonicalrequest(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/canonicalrequest%28for%3A%29.json'
content_hash: 'sha256:b210e56b3770a0c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# canonicalRequest(for:)

<sub>Type Method</sub>

Returns a canonical version of the specified request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func canonicalRequest(for request: URLRequest) -> URLRequest
```

## Parameters

- `request` — The request whose canonical version is desired.

## Return Value

The canonical form of `request`.

## Discussion

It is up to each concrete protocol implementation to define what “canonical” means. A protocol should guarantee that the same input request always yields the same canonical form.

Special consideration should be given when implementing this method, because the canonical form of a request is used to lookup objects in the URL cache, a process which performs equality checks between [URLRequest](../urlrequest.md) instances.

This is an abstract method and subclasses must provide an implementation.
