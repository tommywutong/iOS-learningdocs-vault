---
title: CFStream SOCKS Proxy Key Constants
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstream-socks-proxy-key-constants
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstream-socks-proxy-key-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstream-socks-proxy-key-constants.json'
content_hash: 'sha256:7a383eb801e4e708'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFStream](cfstream.md)

# CFStream SOCKS Proxy Key Constants

<sub>API Collection</sub>

Constants for SOCKS Proxy `CFDictionary` keys.

## Overview

When setting the stream’s SOCKS Proxy property, the property’s value is a `CFDictionary` object containing at minimum the kCFStreamPropertySOCKSProxyHost and kCFStreamPropertySOCKSProxyPort keys. The dictionary may also contain the other keys described in this section.

## Topics

### Constants

- [kCFStreamPropertySOCKSProxyHost](kcfstreampropertysocksproxyhost.md) — Constant for the SOCKS proxy host key.
- [kCFStreamPropertySOCKSProxyPort](kcfstreampropertysocksproxyport.md) — Constant for the SOCKS proxy host port key.
- [kCFStreamPropertySOCKSVersion](kcfstreampropertysocksversion.md) — Constant for the SOCKS version key.
- [kCFStreamSocketSOCKSVersion4](kcfstreamsocketsocksversion4.md) — Constant used in the `kCFStreamSockerSOCKSVersion` key to specify SOCKS4 as the SOCKS version for the stream.
- [kCFStreamSocketSOCKSVersion5](kcfstreamsocketsocksversion5.md) — Constant used in the `kCFStreamSOCKSVersion` key to specify SOCKS5 as the SOCKS version for the stream.
- [kCFStreamPropertySOCKSUser](kcfstreampropertysocksuser.md) — Constant for the key required to set a user name.
- [kCFStreamPropertySOCKSPassword](kcfstreampropertysockspassword.md) — Constant for the key required to set a user’s password.

## See Also

### Constants

- [CFStreamStatus](cfstreamstatus.md) — Constants that describe the status of a stream.
- [CFStreamErrorDomain](cfstreamerrordomain.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Error Subdomains](error-subdomains.md) — Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.
- [Secure Sockets (SOCKS) Errors](../cfnetwork/1518266-secure-sockets-socks-errors.md) — Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [CFStreamEventType](cfstreameventtype.md) — Defines constants for stream-related events.
- [Stream Properties](stream-properties.md) — Stream property names that can be set or copied.
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md) — Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md) — Constants for setting the security level of a socket stream.
- [Stream Service Types](stream-service-types.md) — String constants that specify the service type of a stream.
