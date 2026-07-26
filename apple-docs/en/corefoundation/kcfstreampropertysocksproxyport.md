---
title: kCFStreamPropertySOCKSProxyPort
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfstreampropertysocksproxyport
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocksproxyport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstreampropertysocksproxyport.json'
content_hash: 'sha256:dd664acc4a9596ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStreamPropertySOCKSProxyPort

<sub>Global Variable</sub>

Constant for the SOCKS proxy host port key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFStreamPropertySOCKSProxyPort: CFString
```

## Discussion

This key contains a `CFNumberRef` object of type `kCFNumberSInt32Type` whose value represents the port on which the proxy listens.

## See Also

### Constants

- [kCFStreamPropertySOCKSProxyHost](kcfstreampropertysocksproxyhost.md) — Constant for the SOCKS proxy host key.
- [kCFStreamPropertySOCKSVersion](kcfstreampropertysocksversion.md) — Constant for the SOCKS version key.
- [kCFStreamSocketSOCKSVersion4](kcfstreamsocketsocksversion4.md) — Constant used in the `kCFStreamSockerSOCKSVersion` key to specify SOCKS4 as the SOCKS version for the stream.
- [kCFStreamSocketSOCKSVersion5](kcfstreamsocketsocksversion5.md) — Constant used in the `kCFStreamSOCKSVersion` key to specify SOCKS5 as the SOCKS version for the stream.
- [kCFStreamPropertySOCKSUser](kcfstreampropertysocksuser.md) — Constant for the key required to set a user name.
- [kCFStreamPropertySOCKSPassword](kcfstreampropertysockspassword.md) — Constant for the key required to set a user’s password.
