---
title: 'urlProtocol(_:didReceive:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocolclient/urlprotocol(_:didreceive:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didreceive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocolclient/urlprotocol%28_%3Adidreceive%3A%29.json'
content_hash: 'sha256:db23f33a0b4601c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocolClient](../urlprotocolclient.md)

# urlProtocol(_:didReceive:)

<sub>Instance Method</sub>

Tells the client that the URL Loading System received an authentication challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urlProtocol(_ protocol: URLProtocol, didReceive challenge: URLAuthenticationChallenge)
```

## Parameters

- `protocol` — The URL protocol object sending the message.

- `challenge` — The authentication challenge that has been received.

## Discussion

The protocol client guarantees that it will answer the request on the same thread that called this method. The client may add a default credential to the challenge it issues to the connection delegate, if `protocol` did not provide one.

## See Also

### Handling authentication challenges

- [- URLProtocol:didCancelAuthenticationChallenge:](<urlprotocol(__didcancel_).md>) — Tells the client that an authentication challenge has been canceled.
