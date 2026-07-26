---
title: NSURLAuthenticationMethodServerTrust
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlauthenticationmethodservertrust
source_url: 'https://developer.apple.com/documentation/foundation/nsurlauthenticationmethodservertrust'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlauthenticationmethodservertrust.json'
content_hash: 'sha256:ec000e6fe1fba6c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLAuthenticationMethodServerTrust

<sub>Global Variable</sub>

Perform server trust authentication (certificate validation) for this protection space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSURLAuthenticationMethodServerTrust: String
```

## Discussion

This authentication method can apply to any protocol, and is most commonly used for overriding SSL and TLS chain validation.

To learn more, read [Overriding TLS Chain Validation Correctly](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingTopics/Articles/OverridingSSLChainValidationCorrectly.html#//apple_ref/doc/uid/TP40012544).

## See Also

### Session-wide authentication challenges

- [NSURLAuthenticationMethodClientCertificate](nsurlauthenticationmethodclientcertificate.md) — Use client certificate authentication for this protection space.
- [NSURLAuthenticationMethodNegotiate](nsurlauthenticationmethodnegotiate.md) — Negotiate whether to use Kerberos or NTLM authentication for this protection space.
- [NSURLAuthenticationMethodNTLM](nsurlauthenticationmethodntlm.md) — Use NTLM authentication for this protection space.
