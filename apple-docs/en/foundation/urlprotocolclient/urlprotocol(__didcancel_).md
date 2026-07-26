---
title: 'urlProtocol(_:didCancel:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocolclient/urlprotocol(_:didcancel:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didcancel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocolclient/urlprotocol%28_%3Adidcancel%3A%29.json'
content_hash: 'sha256:18c81a894dceab2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocolClient](../urlprotocolclient.md)

# urlProtocol(_:didCancel:)

<sub>Instance Method</sub>

Tells the client that an authentication challenge has been canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urlProtocol(_ protocol: URLProtocol, didCancel challenge: URLAuthenticationChallenge)
```

## Parameters

- `protocol` — The URL protocol object sending the message.

- `challenge` — The authentication challenge that was canceled.

## See Also

### Handling authentication challenges

- [- URLProtocol:didReceiveAuthenticationChallenge:](<urlprotocol(__didreceive_).md>) — Tells the client that the URL Loading System received an authentication challenge.
