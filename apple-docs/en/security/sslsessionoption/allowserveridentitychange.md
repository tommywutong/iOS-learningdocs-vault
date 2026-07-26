---
title: SSLSessionOption.allowServerIdentityChange
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsessionoption/allowserveridentitychange
source_url: 'https://developer.apple.com/documentation/security/sslsessionoption/allowserveridentitychange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsessionoption/allowserveridentitychange.json'
content_hash: 'sha256:c4abae018de78fdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SSLSessionOption](../sslsessionoption.md)

# SSLSessionOption.allowServerIdentityChange

<sub>Case</sub>

Allow server identity change on renegotiation.

<sub>Mac Catalyst, macOS</sub>

```swift
case allowServerIdentityChange
```

## Discussion

Disallow by default to avoid the Triple Handshake attack.
