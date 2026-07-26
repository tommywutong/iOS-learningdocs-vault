---
title: 'SSLCopyRequestedPeerName(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.11+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslcopyrequestedpeername(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslcopyrequestedpeername(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcopyrequestedpeername%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:dd9f22216c8c6874'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLCopyRequestedPeerName(_:_:_:)

<sub>Function</sub>

Determines the buffer size needed for the peer domain name.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLCopyRequestedPeerName(_ context: SSLContext, _ peerName: UnsafeMutablePointer<CChar>, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `peerName` — The fully qualified domain name of the peer—for example, `store.apple.com`. The name is in the form of a C string, except that `NULL` termination is optional.

- `peerNameLen` — On return, points to the length of the peer domain name.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Use the `peerNameLen` returned by this function when calling the [SSLCopyRequestedPeerNameLength](<sslcopyrequestedpeernamelength(____).md>) function.
