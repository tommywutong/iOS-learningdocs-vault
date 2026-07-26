---
title: kCFStreamSocketSecurityLevelSSLv3
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（10.0 起废弃）, iPadOS 2.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.12 起废弃）, tvOS（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/kcfstreamsocketsecuritylevelsslv3
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstreamsocketsecuritylevelsslv3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstreamsocketsecuritylevelsslv3.json'
content_hash: 'sha256:5705ae0b33ac14de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStreamSocketSecurityLevelSSLv3

<sub>Global Variable</sub>

Specifies that SSL version 3 be set as the security protocol for a socket stream pair.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFStreamSocketSecurityLevelSSLv3: CFString
```

## Discussion

If SSL version 3 is not available, specifies that SSL version 2 be set as the security protocol for a socket stream.

## See Also

### Constants

- [kCFStreamSocketSecurityLevelNone](kcfstreamsocketsecuritylevelnone.md) — Specifies that no security level be set.
- [kCFStreamSocketSecurityLevelSSLv2](kcfstreamsocketsecuritylevelsslv2.md) — Specifies that SSL version 2 be set as the security protocol for a socket stream. _(deprecated)_
- [kCFStreamSocketSecurityLevelTLSv1](kcfstreamsocketsecurityleveltlsv1.md) — Specifies that TLS version 1 be set as the security protocol for a socket stream.
- [kCFStreamSocketSecurityLevelNegotiatedSSL](kcfstreamsocketsecuritylevelnegotiatedssl.md) — Specifies that the highest level security protocol that can be negotiated be set as the security protocol for a socket stream.
