---
title: 'SSLCopyRequestedPeerNameLength(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.11+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslcopyrequestedpeernamelength(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslcopyrequestedpeernamelength(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcopyrequestedpeernamelength%28_%3A_%3A%29.json'
content_hash: 'sha256:5b02f51b87fdb985'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLCopyRequestedPeerNameLength(_:_:)

<sub>Function</sub>

Obtains the hostname specified by the client in the ServerName extension (SNI). Server only.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLCopyRequestedPeerNameLength(_ ctx: SSLContext, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `ctx` — An SSL session context reference.

- `peerNameLen` — The length of the peer name, as retrieved by calling the [SSLCopyRequestedPeerName](<sslcopyrequestedpeername(______).md>) function.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
