---
title: 'urlProtocol(_:didLoad:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocolclient/urlprotocol(_:didload:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didload:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocolclient/urlprotocol%28_%3Adidload%3A%29.json'
content_hash: 'sha256:e7b23782682ffcbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocolClient](../urlprotocolclient.md)

# urlProtocol(_:didLoad:)

<sub>Instance Method</sub>

Tells the client that the protocol implementation has loaded some data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urlProtocol(_ protocol: URLProtocol, didLoad data: Data)
```

## Parameters

- `protocol` — The URL protocol object sending the message.

- `data` — The data being made available.

## Discussion

The data object must contain only new data loaded since the previous invocation of this method.

## See Also

### Indicating loading progress or failure

- [- URLProtocol:didFailWithError:](<urlprotocol(__didfailwitherror_).md>) — Tells the client that the load request failed due to an error.
- [- URLProtocolDidFinishLoading:](<urlprotocoldidfinishloading(__).md>) — Tells the client that the protocol implementation has finished loading.
