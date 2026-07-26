---
title: SSLSessionOption.breakOnServerAuth
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsessionoption/breakonserverauth
source_url: 'https://developer.apple.com/documentation/security/sslsessionoption/breakonserverauth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsessionoption/breakonserverauth.json'
content_hash: 'sha256:433ab9d1253ce13f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SSLSessionOption](../sslsessionoption.md)

# SSLSessionOption.breakOnServerAuth

<sub>Case</sub>

Enables returning from [SSLHandshake](<../sslhandshake(__).md>) (with a result of `errSSLServerAuthCompleted`) when the server authentication portion of the handshake is complete to allow your application to perform its own certificate verification.

<sub>Mac Catalyst, macOS</sub>

```swift
case breakOnServerAuth
```

## Discussion

Note that in iOS (all versions) and macOS 10.8 and later, setting this option disables Secure Transport’s automatic verification of server certificates.

If you set this option, your application should perform its own certificate verification when `errSSLServerAuthCompleted` is returned before continuing with the handshake.
