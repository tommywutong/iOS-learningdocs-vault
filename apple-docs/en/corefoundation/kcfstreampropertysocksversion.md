---
title: kCFStreamPropertySOCKSVersion
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfstreampropertysocksversion
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocksversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstreampropertysocksversion.json'
content_hash: 'sha256:3bc115d749950912'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStreamPropertySOCKSVersion

<sub>Global Variable</sub>

Constant for the SOCKS version key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFStreamPropertySOCKSVersion: CFString
```

## Discussion

Its value must be `kCFStreamSocketSOCKSVersion4` or `kCFStreamSocketSOCKSVersion5` to set SOCKS4 or SOCKS5, respectively. If this key is not present, SOCKS5 is used by default.

## See Also

### Constants

- [kCFStreamPropertySOCKSProxyHost](kcfstreampropertysocksproxyhost.md) — Constant for the SOCKS proxy host key.
- [kCFStreamPropertySOCKSProxyPort](kcfstreampropertysocksproxyport.md) — Constant for the SOCKS proxy host port key.
- [kCFStreamSocketSOCKSVersion4](kcfstreamsocketsocksversion4.md) — Constant used in the `kCFStreamSockerSOCKSVersion` key to specify SOCKS4 as the SOCKS version for the stream.
- [kCFStreamSocketSOCKSVersion5](kcfstreamsocketsocksversion5.md) — Constant used in the `kCFStreamSOCKSVersion` key to specify SOCKS5 as the SOCKS version for the stream.
- [kCFStreamPropertySOCKSUser](kcfstreampropertysocksuser.md) — Constant for the key required to set a user name.
- [kCFStreamPropertySOCKSPassword](kcfstreampropertysockspassword.md) — Constant for the key required to set a user’s password.
