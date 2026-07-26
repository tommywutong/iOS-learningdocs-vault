---
title: client
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotocol/client
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/client'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/client.json'
content_hash: 'sha256:674b66b0839ebeb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# client

<sub>Instance Property</sub>

The object the protocol uses to communicate with the URL loading system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var client: (any URLProtocolClient)? { get }
```

## See Also

### Getting protocol attributes

- [cachedResponse](cachedresponse.md) — The protocol’s cached response.
- [URLProtocolClient](../urlprotocolclient.md) — The interface used by [URLProtocol](../urlprotocol.md) subclasses to communicate with the URL Loading System.
- [request](request.md) — The protocol’s request.
- [task](task.md) — The protocol’s task.
