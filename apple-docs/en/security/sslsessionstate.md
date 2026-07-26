---
title: SSLSessionState
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslsessionstate
source_url: 'https://developer.apple.com/documentation/security/sslsessionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsessionstate.json'
content_hash: 'sha256:8f9a7fb9eef6fc7e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSessionState

<sub>Enumeration</sub>

The flags that represent the state of an SSL session.

<sub>Mac Catalyst, macOS</sub>

```swift
@frozen enum SSLSessionState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSSLIdle](sslsessionstate/idle.md) — No I/O has been performed yet. _(deprecated)_
- [kSSLHandshake](sslsessionstate/handshake.md) — The SSL handshake is in progress. _(deprecated)_
- [kSSLConnected](sslsessionstate/connected.md) — The SSL handshake is complete; the connection is ready for normal I/O. _(deprecated)_
- [kSSLClosed](sslsessionstate/closed.md) — The connection closed normally. _(deprecated)_
- [kSSLAborted](sslsessionstate/aborted.md) — The connection aborted. _(deprecated)_

### Initializers

- [init(rawValue:)](<sslsessionstate/init(rawvalue_).md>)
