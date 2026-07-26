---
title: SSLSessionOption
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslsessionoption
source_url: 'https://developer.apple.com/documentation/security/sslsessionoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsessionoption.json'
content_hash: 'sha256:65d72b6b2310c11a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSessionOption

<sub>Enumeration</sub>

The options that can be set for an SSL session.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SSLSessionOption
```

## Overview

Use these flags with calls to the [SSLSetSessionOption](<sslsetsessionoption(______).md>) function.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSSLSessionOptionBreakOnServerAuth](sslsessionoption/breakonserverauth.md) — Enables returning from [SSLHandshake](<sslhandshake(__).md>) (with a result of `errSSLServerAuthCompleted`) when the server authentication portion of the handshake is complete to allow your application to perform its own certificate verification. _(deprecated)_
- [kSSLSessionOptionBreakOnCertRequested](sslsessionoption/breakoncertrequested.md) — Enables returning from [SSLHandshake](<sslhandshake(__).md>) (with a result of `errSSLClientCertRequested`) when the server requests a client certificate. _(deprecated)_
- [kSSLSessionOptionBreakOnClientAuth](sslsessionoption/breakonclientauth.md) — Enables returning from [SSLHandshake](<sslhandshake(__).md>) (with a result of `errSSLClientAuthCompleted`) when the client authentication portion of the handshake is complete to allow your application to perform its own certificate verification. _(deprecated)_
- [kSSLSessionOptionFalseStart](sslsessionoption/falsestart.md) — When enabled, TLS False Start is used if an adequate cipher-suite is negotiated. _(deprecated)_
- [kSSLSessionOptionSendOneByteRecord](sslsessionoption/sendonebyterecord.md) — Enables `1/n-1` record splitting for BEAST attack mitigation. _(deprecated)_
- [kSSLSessionOptionAllowServerIdentityChange](sslsessionoption/allowserveridentitychange.md) — Allow server identity change on renegotiation. _(deprecated)_
- [kSSLSessionOptionFallback](sslsessionoption/fallback.md) — Enable fallback countermeasures. _(deprecated)_
- [kSSLSessionOptionBreakOnClientHello](sslsessionoption/breakonclienthello.md) — Break from a client hello in order to check for SNI. _(deprecated)_
- [kSSLSessionOptionAllowRenegotiation](sslsessionoption/allowrenegotiation.md) — Allow renegotiation. _(deprecated)_
- [kSSLSessionOptionEnableSessionTickets](sslsessionoption/enablesessiontickets.md) — Enable session tickets. _(deprecated)_

### Initializers

- [init(rawValue:)](<sslsessionoption/init(rawvalue_).md>)
