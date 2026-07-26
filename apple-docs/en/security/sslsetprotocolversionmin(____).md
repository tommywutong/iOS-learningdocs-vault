---
title: 'SSLSetProtocolVersionMin(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.8+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetprotocolversionmin(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetprotocolversionmin(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetprotocolversionmin%28_%3A_%3A%29.json'
content_hash: 'sha256:1de2e3d0b7db6461'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetProtocolVersionMin(_:_:)

<sub>Function</sub>

Sets the minimum protocol version allowed by the application for a given SSL context.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetProtocolVersionMin(_ context: SSLContext, _ minVersion: SSLProtocol) -> OSStatus
```

## Parameters

- `context` — The SSL context associated with the connection.

- `minVersion` — The new minimum version ([kTLSProtocol1](sslprotocol/tlsprotocol1.md), for example). See [SSLProtocol](sslprotocol.md) for a complete list.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
