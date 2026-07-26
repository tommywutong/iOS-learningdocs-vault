---
title: 'SSLGetPeerDomainName(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetpeerdomainname(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetpeerdomainname(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetpeerdomainname%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7dc6f6394db5e210'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetPeerDomainName(_:_:_:)

<sub>Function</sub>

Retrieves the peer domain name specified previously.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetPeerDomainName(_ context: SSLContext, _ peerName: UnsafeMutablePointer<CChar>, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `peerName` — On return, points to the peer domain name.

- `peerNameLen` — A pointer to the length of the peer domain name. Before calling this function, retrieve the peer domain name length by calling the function [SSLGetPeerDomainNameLength](<sslgetpeerdomainnamelength(____).md>).

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

If you previously called the [SSLSetPeerDomainName](<sslsetpeerdomainname(______).md>) function to specify a fully qualified domain name for the peer certificate, you can use the [SSLGetPeerDomainName](<sslgetpeerdomainname(______).md>) function to retrieve the domain name.
