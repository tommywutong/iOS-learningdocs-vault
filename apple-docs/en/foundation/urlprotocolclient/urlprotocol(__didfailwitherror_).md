---
title: 'urlProtocol(_:didFailWithError:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocolclient/urlprotocol(_:didfailwitherror:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didfailwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocolclient/urlprotocol%28_%3Adidfailwitherror%3A%29.json'
content_hash: 'sha256:a7f441bddb7d7165'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocolClient](../urlprotocolclient.md)

# urlProtocol(_:didFailWithError:)

<sub>Instance Method</sub>

Tells the client that the load request failed due to an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urlProtocol(_ protocol: URLProtocol, didFailWithError error: any Error)
```

## Parameters

- `protocol` — The URL protocol object sending the message.

- `error` — The error that caused the failure of the load request.

## See Also

### Indicating loading progress or failure

- [- URLProtocol:didLoadData:](<urlprotocol(__didload_).md>) — Tells the client that the protocol implementation has loaded some data.
- [- URLProtocolDidFinishLoading:](<urlprotocoldidfinishloading(__).md>) — Tells the client that the protocol implementation has finished loading.
