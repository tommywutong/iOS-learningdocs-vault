---
title: SSLClientCertificateState.certSent
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslclientcertificatestate/certsent
source_url: 'https://developer.apple.com/documentation/security/sslclientcertificatestate/certsent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslclientcertificatestate/certsent.json'
content_hash: 'sha256:3d0c83076aa04a0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SSLClientCertificateState](../sslclientcertificatestate.md)

# SSLClientCertificateState.certSent

<sub>Case</sub>

Indicates that the server asked for a certificate, the client sent one, and the server validated it. The application can inspect the certificate using the function `SSLGetPeerCertificates`.

<sub>Mac Catalyst, macOS</sub>

```swift
case certSent
```
