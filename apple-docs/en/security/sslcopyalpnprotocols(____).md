---
title: 'SSLCopyALPNProtocols(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.13+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslcopyalpnprotocols(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslcopyalpnprotocols(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcopyalpnprotocols%28_%3A_%3A%29.json'
content_hash: 'sha256:aa9423db7b241c6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLCopyALPNProtocols(_:_:)

<sub>Function</sub>

Gets the list of supported application layer protocols.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLCopyALPNProtocols(_ context: SSLContext, _ protocols: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

## Parameters

- `context` — The session context.

- `protocols` — A pointer the function uses to return an array of ASCII-encoded strings representing the supported protocols, such as http/1.1. See [RFC 7301](https://tools.ietf.org/html/rfc7301) for more details.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You must set the `protocols` parameter to `NULL` on input, or the operation fails. If the function has data to provide, it allocates memory for an array and returns it using `protocols`. Otherwise, `protocols` remains `NULL` on output.
