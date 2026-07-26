---
title: SSLSessionOption.breakOnClientAuth
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsessionoption/breakonclientauth
source_url: 'https://developer.apple.com/documentation/security/sslsessionoption/breakonclientauth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsessionoption/breakonclientauth.json'
content_hash: 'sha256:4c5f14e59a320f0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SSLSessionOption](../sslsessionoption.md)

# SSLSessionOption.breakOnClientAuth

<sub>Case</sub>

Enables returning from [SSLHandshake](<../sslhandshake(__).md>) (with a result of `errSSLClientAuthCompleted`) when the client authentication portion of the handshake is complete to allow your application to perform its own certificate verification.

<sub>Mac Catalyst, macOS</sub>

```swift
case breakOnClientAuth
```

## Discussion

Note that in iOS (all versions) and macOS 10.8 and later, setting this option disables Secure Transport’s automatic verification of client certificates.

If you set this option, your application should perform its own certificate verification when `errSSLClientAuthCompleted` is returned before continuing with the handshake.
