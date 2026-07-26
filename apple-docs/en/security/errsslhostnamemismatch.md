---
title: errSSLHostNameMismatch
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errsslhostnamemismatch
source_url: 'https://developer.apple.com/documentation/security/errsslhostnamemismatch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errsslhostnamemismatch.json'
content_hash: 'sha256:cde9dffb267fe390'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSSLHostNameMismatch

<sub>Global Variable</sub>

The host name you connected with does not match any of the host names allowed by the certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var errSSLHostNameMismatch: OSStatus { get }
```

## Discussion

This is commonly caused by an incorrect value for the [kCFStreamSSLPeerName](../cfnetwork/kcfstreamsslpeername.md) property within the dictionary associated with the stream’s [kCFStreamPropertySSLSettings](../cfnetwork/kcfstreampropertysslsettings.md) key.
