---
title: 'SSLGetNegotiatedCipher(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetnegotiatedcipher(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetnegotiatedcipher(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetnegotiatedcipher%28_%3A_%3A%29.json'
content_hash: 'sha256:eb8e437854ecd6c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetNegotiatedCipher(_:_:)

<sub>Function</sub>

Retrieves the cipher suite negotiated for this session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetNegotiatedCipher(_ context: SSLContext, _ cipherSuite: UnsafeMutablePointer<SSLCipherSuite>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `cipherSuite` — On return, points to the cipher suite that was negotiated for this session.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You should call this function only when a session is active.
