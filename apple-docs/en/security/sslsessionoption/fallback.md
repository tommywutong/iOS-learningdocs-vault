---
title: SSLSessionOption.fallback
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsessionoption/fallback
source_url: 'https://developer.apple.com/documentation/security/sslsessionoption/fallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsessionoption/fallback.json'
content_hash: 'sha256:599cfa2529e1f52a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SSLSessionOption](../sslsessionoption.md)

# SSLSessionOption.fallback

<sub>Case</sub>

Enable fallback countermeasures.

<sub>Mac Catalyst, macOS</sub>

```swift
case fallback
```

## Discussion

Use this option when retyring an SSL connection with a lower protocol version because of failure to connect.
