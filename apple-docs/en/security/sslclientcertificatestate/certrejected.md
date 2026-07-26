---
title: SSLClientCertificateState.certRejected
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslclientcertificatestate/certrejected
source_url: 'https://developer.apple.com/documentation/security/sslclientcertificatestate/certrejected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslclientcertificatestate/certrejected.json'
content_hash: 'sha256:411d48f7ff4baf9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SSLClientCertificateState](../sslclientcertificatestate.md)

# SSLClientCertificateState.certRejected

<sub>Case</sub>

Indicates that the client sent a certificate but the certificate failed validation. This value is seen only on the server side. The server application can inspect the certificate using the function `SSLGetPeerCertificates`.

<sub>Mac Catalyst, macOS</sub>

```swift
case certRejected
```
