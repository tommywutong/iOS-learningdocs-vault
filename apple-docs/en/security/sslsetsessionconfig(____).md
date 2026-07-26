---
title: 'SSLSetSessionConfig(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+（13.0 起废弃）, iPadOS 10.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.12+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetsessionconfig(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetsessionconfig(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetsessionconfig%28_%3A_%3A%29.json'
content_hash: 'sha256:3b667fdcbf331876'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetSessionConfig(_:_:)

<sub>Function</sub>

Sets a predefined configuration for the Secure Sockets Layer (SSL) session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetSessionConfig(_ context: SSLContext, _ config: CFString) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `config` — The predefined configuration you want to apply to the SSL session. You can configure enabled protocol versions, enabled cipher suites, and the [kSSLSessionOptionFallback](sslsessionoption/fallback.md) session option.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
