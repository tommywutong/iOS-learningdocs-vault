---
title: 'SSLGetPeerID(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetpeerid(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetpeerid(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetpeerid%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1799e56968833643'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetPeerID(_:_:_:)

<sub>Function</sub>

Retrieves the current peer ID data.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetPeerID(_ context: SSLContext, _ peerID: UnsafeMutablePointer<UnsafeRawPointer?>, _ peerIDLen: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `peerID` — On return, points to a buffer containing the peer ID data.

- `peerIDLen` — On return, the length of the peer ID data buffer.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

If the peer ID data for this context was not set by calling the [SSLSetPeerID](<sslsetpeerid(______).md>) function, this function returns a `NULL` pointer in the `peerID` parameter, and `0` in the `peerIDLen` parameter.
