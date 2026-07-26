---
title: 'urlProtocol(_:cachedResponseIsValid:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocolclient/urlprotocol(_:cachedresponseisvalid:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:cachedresponseisvalid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocolclient/urlprotocol%28_%3Acachedresponseisvalid%3A%29.json'
content_hash: 'sha256:e8f6b11d37cd2e2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocolClient](../urlprotocolclient.md)

# urlProtocol(_:cachedResponseIsValid:)

<sub>Instance Method</sub>

Tells the client that a cached response is valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urlProtocol(_ protocol: URLProtocol, cachedResponseIsValid cachedResponse: CachedURLResponse)
```

## Parameters

- `protocol` — The URL protocol object sending the message.

- `cachedResponse` — The cached response whose validity is being communicated.
