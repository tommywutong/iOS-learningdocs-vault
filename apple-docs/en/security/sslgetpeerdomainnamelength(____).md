---
title: 'SSLGetPeerDomainNameLength(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetpeerdomainnamelength(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetpeerdomainnamelength(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetpeerdomainnamelength%28_%3A_%3A%29.json'
content_hash: 'sha256:b61393f8db1e470a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetPeerDomainNameLength(_:_:)

<sub>Function</sub>

Determines the length of a previously set peer domain name.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetPeerDomainNameLength(_ context: SSLContext, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `peerNameLen` — On return, points to the length of the peer domain name.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

If you previously called the [SSLSetPeerDomainName](<sslsetpeerdomainname(______).md>) function to specify a fully qualified domain name for the peer certificate, you can use the [SSLGetPeerDomainName](<sslgetpeerdomainname(______).md>) function to retrieve the peer domain name. Before doing so, you must call the [SSLGetPeerDomainNameLength](<sslgetpeerdomainnamelength(____).md>) function to retrieve the buffer size needed for the domain name.
