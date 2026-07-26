---
title: cachedResponse
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotocol/cachedresponse
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/cachedresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/cachedresponse.json'
content_hash: 'sha256:a33d109212d15f32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# cachedResponse

<sub>Instance Property</sub>

The protocol’s cached response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var cachedResponse: CachedURLResponse? { get }
```

## Discussion

If not overridden in a subclass, this method returns the cached response stored at initialization time.

## See Also

### Getting protocol attributes

- [client](client.md) — The object the protocol uses to communicate with the URL loading system.
- [URLProtocolClient](../urlprotocolclient.md) — The interface used by [URLProtocol](../urlprotocol.md) subclasses to communicate with the URL Loading System.
- [request](request.md) — The protocol’s request.
- [task](task.md) — The protocol’s task.
