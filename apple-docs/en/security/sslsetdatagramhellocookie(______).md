---
title: 'SSLSetDatagramHelloCookie(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.8+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetdatagramhellocookie(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetdatagramhellocookie(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetdatagramhellocookie%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8e448caf90dadda9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetDatagramHelloCookie(_:_:_:)

<sub>Function</sub>

Sets the cookie value used in the Datagram Transport Layer Security (DTLS) hello message.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetDatagramHelloCookie(_ dtlsContext: SSLContext, _ cookie: UnsafeRawPointer?, _ cookieLen: Int) -> OSStatus
```

## Parameters

- `dtlsContext` — The SSL context associated with the connection.

- `cookie` — The cookie value.

- `cookieLen` — The length of the cookie (up to 32 bytes).

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function should be called only on the server side, and is optional. The default cookie is a zero-length cookie.
