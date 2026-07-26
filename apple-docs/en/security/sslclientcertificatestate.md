---
title: SSLClientCertificateState
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslclientcertificatestate
source_url: 'https://developer.apple.com/documentation/security/sslclientcertificatestate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslclientcertificatestate.json'
content_hash: 'sha256:bde368f23544bd70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLClientCertificateState

<sub>Enumeration</sub>

An enumeration of the states of client certificate exchange.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SSLClientCertificateState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSSLClientCertNone](sslclientcertificatestate/certnone.md) — Indicates that the server hasn’t asked for a certificate and that the client hasn’t sent one. _(deprecated)_
- [kSSLClientCertRequested](sslclientcertificatestate/certrequested.md) — Indicates that the server has asked for a certificate, but the client has not sent it. _(deprecated)_
- [kSSLClientCertSent](sslclientcertificatestate/certsent.md) — Indicates that the server asked for a certificate, the client sent one, and the server validated it. The application can inspect the certificate using the function `SSLGetPeerCertificates`. _(deprecated)_
- [kSSLClientCertRejected](sslclientcertificatestate/certrejected.md) — Indicates that the client sent a certificate but the certificate failed validation. This value is seen only on the server side. The server application can inspect the certificate using the function `SSLGetPeerCertificates`. _(deprecated)_

### Initializers

- [init(rawValue:)](<sslclientcertificatestate/init(rawvalue_).md>)
