---
title: CFStream Property SSL Settings Constants
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstream-property-ssl-settings-constants
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstream-property-ssl-settings-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstream-property-ssl-settings-constants.json'
content_hash: 'sha256:1eb81d9af036d1b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFStream](cfstream.md)

# CFStream Property SSL Settings Constants

Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.

## Overview

This enumeration defines the constants for keys in a `CFDictionary` object that is the value of the kCFStreamPropertySSLSettings key.

## Topics

### Constants

- [kCFStreamSSLLevel](../cfnetwork/kcfstreamssllevel.md) — Security property key whose value specifies the stream’s security level.
- [kCFStreamSSLAllowsExpiredCertificates](../cfnetwork/kcfstreamsslallowsexpiredcertificates.md) — Security property key whose value indicates whether expired certificates are allowed. _(deprecated)_
- [kCFStreamSSLAllowsExpiredRoots](../cfnetwork/kcfstreamsslallowsexpiredroots.md) — Security property whose value indicates whether expired root certificates are allowed. _(deprecated)_
- [kCFStreamSSLAllowsAnyRoot](../cfnetwork/kcfstreamsslallowsanyroot.md) — Security property key whose value indicates whether root certificates should be allowed. _(deprecated)_
- [kCFStreamSSLValidatesCertificateChain](../cfnetwork/kcfstreamsslvalidatescertificatechain.md) — Security property key whose value indicates whether the certificate chain should be validated.
- [kCFStreamSSLPeerName](../cfnetwork/kcfstreamsslpeername.md) — Security property key whose value overrides the name used for certificate verification.
- [kCFStreamSSLCertificates](../cfnetwork/kcfstreamsslcertificates.md) — Security property key whose value is a CFArray of SecCertificateRefs except for the first element in the array, which is a SecIdentityRef.
- [kCFStreamSSLIsServer](../cfnetwork/kcfstreamsslisserver.md) — Security property key whose value indicates whether the connection is to act as a server in the SSL process.

## See Also

### Constants

- [CFStreamStatus](cfstreamstatus.md) — Constants that describe the status of a stream.
- [CFStreamErrorDomain](cfstreamerrordomain.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Error Subdomains](error-subdomains.md) — Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.
- [Secure Sockets (SOCKS) Errors](../cfnetwork/1518266-secure-sockets-socks-errors.md) — Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [CFStreamEventType](cfstreameventtype.md) — Defines constants for stream-related events.
- [Stream Properties](stream-properties.md) — Stream property names that can be set or copied.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md) — Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md) — Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md) — String constants that specify the service type of a stream.
