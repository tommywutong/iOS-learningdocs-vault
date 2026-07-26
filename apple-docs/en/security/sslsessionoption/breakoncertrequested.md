---
title: SSLSessionOption.breakOnCertRequested
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsessionoption/breakoncertrequested
source_url: 'https://developer.apple.com/documentation/security/sslsessionoption/breakoncertrequested'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsessionoption/breakoncertrequested.json'
content_hash: 'sha256:3566abbd670cc781'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SSLSessionOption](../sslsessionoption.md)

# SSLSessionOption.breakOnCertRequested

<sub>Case</sub>

Enables returning from [SSLHandshake](<../sslhandshake(__).md>) (with a result of `errSSLClientCertRequested`) when the server requests a client certificate.

<sub>Mac Catalyst, macOS</sub>

```swift
case breakOnCertRequested
```
