---
title: Error Subdomains
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/error-subdomains
source_url: 'https://developer.apple.com/documentation/corefoundation/error-subdomains'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/error-subdomains.json'
content_hash: 'sha256:fca85017500c88b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFStream](cfstream.md)

# Error Subdomains

Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.

## Overview

Error codes in the `kCFStreamErrorDomainSOCKS` domain can come from multiple parts of the protocol stack, many of which define their own error values as part of outside specifications such as the HTTP specification.

To avoid confusion from conflicting error numbers, error codes in the `kCFStreamErrorDomainSOCKS` domain contain two parts: a subdomain, which tells which part of the protocol stack generated the error, and the error code itself.

Calling [CFSocketStreamSOCKSGetErrorSubdomain(_:)](<../cfnetwork/cfsocketstreamsocksgeterrorsubdomain(__).md>) returns an identifier that tells which layer of the protocol stack produced the error. This list of constants contains the possible values that this function will return.

Calling [CFSocketStreamSOCKSGetError(_:)](<../cfnetwork/cfsocketstreamsocksgeterror(__).md>) returns the actual error code that the subdomain describes.

## Topics

### Constants

- [kCFStreamErrorSOCKSSubDomainNone](../cfnetwork/kcfstreamerrorsockssubdomainnone.md) — A general SOCKS error.
- [kCFStreamErrorSOCKSSubDomainVersionCode](../cfnetwork/kcfstreamerrorsockssubdomainversioncode.md) — The version of SOCKS that the server wants to use.
- [kCFStreamErrorSOCKS4SubDomainResponse](../cfnetwork/kcfstreamerrorsocks4subdomainresponse.md) — The SOCKS4 status code returned by the server.
- [kCFStreamErrorSOCKS5SubDomainUserPass](../cfnetwork/kcfstreamerrorsocks5subdomainuserpass.md) — The status code that the server returned during authentication.
- [kCFStreamErrorSOCKS5SubDomainMethod](../cfnetwork/kcfstreamerrorsocks5subdomainmethod.md) — The server’s desired negotiation method.
- [kCFStreamErrorSOCKS5SubDomainResponse](../cfnetwork/kcfstreamerrorsocks5subdomainresponse.md) — The response code that the server returned in reply to the connection request.

## See Also

### Constants

- [CFStreamStatus](cfstreamstatus.md) — Constants that describe the status of a stream.
- [CFStreamErrorDomain](cfstreamerrordomain.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Secure Sockets (SOCKS) Errors](../cfnetwork/1518266-secure-sockets-socks-errors.md) — Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [CFStreamEventType](cfstreameventtype.md) — Defines constants for stream-related events.
- [Stream Properties](stream-properties.md) — Stream property names that can be set or copied.
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md) — Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md) — Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md) — Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md) — String constants that specify the service type of a stream.
