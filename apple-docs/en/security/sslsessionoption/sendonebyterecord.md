---
title: SSLSessionOption.sendOneByteRecord
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsessionoption/sendonebyterecord
source_url: 'https://developer.apple.com/documentation/security/sslsessionoption/sendonebyterecord'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsessionoption/sendonebyterecord.json'
content_hash: 'sha256:fff1e3530981cd28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SSLSessionOption](../sslsessionoption.md)

# SSLSessionOption.sendOneByteRecord

<sub>Case</sub>

Enables `1/n-1` record splitting for BEAST attack mitigation.

<sub>Mac Catalyst, macOS</sub>

```swift
case sendOneByteRecord
```

## Discussion

When enabled, record splitting is performed only for TLS 1.0 connections based on a block cipher.
