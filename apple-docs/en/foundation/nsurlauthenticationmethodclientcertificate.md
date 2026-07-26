---
title: NSURLAuthenticationMethodClientCertificate
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlauthenticationmethodclientcertificate
source_url: 'https://developer.apple.com/documentation/foundation/nsurlauthenticationmethodclientcertificate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlauthenticationmethodclientcertificate.json'
content_hash: 'sha256:85f9295933151377'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLAuthenticationMethodClientCertificate

<sub>Global Variable</sub>

Use client certificate authentication for this protection space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSURLAuthenticationMethodClientCertificate: String
```

## Discussion

This authentication method can apply to any protocol.

## See Also

### Session-wide authentication challenges

- [NSURLAuthenticationMethodNegotiate](nsurlauthenticationmethodnegotiate.md) — Negotiate whether to use Kerberos or NTLM authentication for this protection space.
- [NSURLAuthenticationMethodNTLM](nsurlauthenticationmethodntlm.md) — Use NTLM authentication for this protection space.
- [NSURLAuthenticationMethodServerTrust](nsurlauthenticationmethodservertrust.md) — Perform server trust authentication (certificate validation) for this protection space.
