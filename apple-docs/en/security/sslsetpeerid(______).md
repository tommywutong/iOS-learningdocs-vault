---
title: 'SSLSetPeerID(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetpeerid(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetpeerid(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetpeerid%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c1dabeeb2cb2aade'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetPeerID(_:_:_:)

<sub>Function</sub>

Specifies data that is sufficient to uniquely identify the peer of the current session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetPeerID(_ context: SSLContext, _ peerID: UnsafeRawPointer?, _ peerIDLen: Int) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `peerID` — A pointer to a buffer containing the peer ID data to set.

- `peerIDLen` — The length of the peer ID data buffer.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Secure Transport uses the peer ID to match the peer of an SSL session with the peer of a previous session in order to resume an interrupted session. If the peer IDs match, Secure Transport attempts to resume the session with the same parameters as used in the previous session with the same peer.

The data you provide to this function is treated as an opaque blob by Secure Transport but is compared byte for byte with previous peer ID data values set by the current application. An example of peer ID data is an IP address and port, stored in some caller-private manner. Calling this function is optional but is required if you want the session to be resumable. If you do call this function, you must call it prior to the handshake for the current session.

You can use the [SSLGetPeerID](<sslgetpeerid(______).md>) function to retrieve the peer ID data for the current session.
