---
title: 'urlProtocol(_:wasRedirectedTo:redirectResponse:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocolclient/urlprotocol(_:wasredirectedto:redirectresponse:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:wasredirectedto:redirectresponse:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocolclient/urlprotocol%28_%3Awasredirectedto%3Aredirectresponse%3A%29.json'
content_hash: 'sha256:fa1b804dd2395823'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocolClient](../urlprotocolclient.md)

# urlProtocol(_:wasRedirectedTo:redirectResponse:)

<sub>Instance Method</sub>

Tells the client that the protocol implementation has been redirected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urlProtocol(_ protocol: URLProtocol, wasRedirectedTo request: URLRequest, redirectResponse: URLResponse)
```

## Parameters

- `protocol` — The URL protocol object sending the message.

- `request` — The new request that the original request was redirected to.

- `redirectResponse` — The response from the original request that caused the redirect.
