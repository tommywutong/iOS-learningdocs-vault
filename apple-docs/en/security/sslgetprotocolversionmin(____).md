---
title: 'SSLGetProtocolVersionMin(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.8+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetprotocolversionmin(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetprotocolversionmin(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetprotocolversionmin%28_%3A_%3A%29.json'
content_hash: 'sha256:e4ec4c7bc03bfaf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetProtocolVersionMin(_:_:)

<sub>Function</sub>

Gets the minimum protocol version allowed by the application for a given SSL context.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetProtocolVersionMin(_ context: SSLContext, _ minVersion: UnsafeMutablePointer<SSLProtocol>) -> OSStatus
```

## Parameters

- `context` — The SSL context associated with the connection.

- `minVersion` — The address of an [SSLProtocol](sslprotocol.md) integer where the minimum version should be stored. See [SSLProtocol](sslprotocol.md) for a list of possible values.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
