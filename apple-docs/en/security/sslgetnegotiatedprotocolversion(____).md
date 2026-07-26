---
title: 'SSLGetNegotiatedProtocolVersion(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetnegotiatedprotocolversion(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetnegotiatedprotocolversion(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetnegotiatedprotocolversion%28_%3A_%3A%29.json'
content_hash: 'sha256:75a0e1f3afb22220'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetNegotiatedProtocolVersion(_:_:)

<sub>Function</sub>

Obtains the negotiated protocol version of the active session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetNegotiatedProtocolVersion(_ context: SSLContext, _ protocol: UnsafeMutablePointer<SSLProtocol>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `protocol` — On return, points to the negotiated protocol version of the active session. The value is set to [kSSLProtocolUnknown](sslprotocol/sslprotocolunknown.md) if no SSL session is in progress.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function retrieves the version of the Secure Sockets Layer (SSL) or Transport Layer Security (TLS) protocol negotiated for the session. Note that the negotiated protocol may not be the same as your preferred protocol, depending on which protocol versions you enabled with the [SSLSetProtocolVersionEnabled](sslsetprotocolversionenabled.md) function. This function can return any of the following values:

- `kSSLProtocol2`
- `kSSLProtocol3`
- `kTLSProtocol1`
- `kSSLProtocolUnknown`
