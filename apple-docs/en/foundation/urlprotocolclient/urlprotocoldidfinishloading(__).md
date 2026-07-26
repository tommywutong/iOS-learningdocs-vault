---
title: 'urlProtocolDidFinishLoading(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocolclient/urlprotocoldidfinishloading(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocoldidfinishloading(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocolclient/urlprotocoldidfinishloading%28_%3A%29.json'
content_hash: 'sha256:a08936c2accbc7a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocolClient](../urlprotocolclient.md)

# urlProtocolDidFinishLoading(_:)

<sub>Instance Method</sub>

Tells the client that the protocol implementation has finished loading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urlProtocolDidFinishLoading(_ protocol: URLProtocol)
```

## Parameters

- `protocol` — The URL protocol object sending the message.

## See Also

### Indicating loading progress or failure

- [- URLProtocol:didFailWithError:](<urlprotocol(__didfailwitherror_).md>) — Tells the client that the load request failed due to an error.
- [- URLProtocol:didLoadData:](<urlprotocol(__didload_).md>) — Tells the client that the protocol implementation has loaded some data.
