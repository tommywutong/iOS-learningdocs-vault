---
title: CFStream Socket Security Level Constants
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstream-socket-security-level-constants
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstream-socket-security-level-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstream-socket-security-level-constants.json'
content_hash: 'sha256:57f3fcf1dde30d0b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFStream](cfstream.md)

# CFStream Socket Security Level Constants

<sub>API Collection</sub>

Constants for setting the security level of a socket stream.

## Overview

This enumeration defines the preferred constants for setting the security protocol for a socket stream pair when calling [CFReadStreamSetProperty](<cfreadstreamsetproperty(______).md>) or [CFWriteStreamSetProperty](<cfwritestreamsetproperty(______).md>).

## Topics

### Constants

- [kCFStreamSocketSecurityLevelNone](kcfstreamsocketsecuritylevelnone.md) — Specifies that no security level be set.
- [kCFStreamSocketSecurityLevelSSLv2](kcfstreamsocketsecuritylevelsslv2.md) — Specifies that SSL version 2 be set as the security protocol for a socket stream. _(deprecated)_
- [kCFStreamSocketSecurityLevelSSLv3](kcfstreamsocketsecuritylevelsslv3.md) — Specifies that SSL version 3 be set as the security protocol for a socket stream pair. _(deprecated)_
- [kCFStreamSocketSecurityLevelTLSv1](kcfstreamsocketsecurityleveltlsv1.md) — Specifies that TLS version 1 be set as the security protocol for a socket stream.
- [kCFStreamSocketSecurityLevelNegotiatedSSL](kcfstreamsocketsecuritylevelnegotiatedssl.md) — Specifies that the highest level security protocol that can be negotiated be set as the security protocol for a socket stream.

## See Also

### Setting the Security Protocol

- [CFReadStreamSetProperty](<cfreadstreamsetproperty(______).md>) — Sets the value of a property for a stream.
- [CFWriteStreamSetProperty](<cfwritestreamsetproperty(______).md>) — Sets the value of a property for a stream.
