---
title: 'SSLSetPeerDomainName(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetpeerdomainname(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetpeerdomainname(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetpeerdomainname%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:893ba57da3143db3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetPeerDomainName(_:_:_:)

<sub>Function</sub>

Specifies the fully qualified domain name of the peer.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetPeerDomainName(_ context: SSLContext, _ peerName: UnsafePointer<CChar>?, _ peerNameLen: Int) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `peerName` — The fully qualified domain name of the peer—for example, `store.apple.com`. The name is in the form of a C string, except that `NULL` termination is optional.

- `peerNameLen` — The number of bytes passed in the `peerName` parameter.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You can use this function to verify the common name field in the peer’s certificate. If you call this function and the common name in the certificate does not match the value you specify in the `peerName` parameter, then handshake fails and returns `errSSLXCertChainInvalid`. Use of this function is optional.

This function can be called only when no session is active.
