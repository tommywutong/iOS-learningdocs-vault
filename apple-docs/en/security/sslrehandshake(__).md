---
title: 'SSLReHandshake(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+（13.0 起废弃）, iPadOS 10.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.12+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslrehandshake(_:)'
source_url: 'https://developer.apple.com/documentation/security/sslrehandshake(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslrehandshake%28_%3A%29.json'
content_hash: 'sha256:837ff3c06e6a15cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLReHandshake(_:)

<sub>Function</sub>

Requests renegotiation of the SSL handshake. Server only.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLReHandshake(_ context: SSLContext) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

On success, call the [SSLHandshake](<sslhandshake(__).md>) function or the [SSLRead](<sslread(________).md>) function, or both, as appropriate, as you would for the original handshake.
