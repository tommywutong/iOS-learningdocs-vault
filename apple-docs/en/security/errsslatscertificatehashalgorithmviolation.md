---
title: errSSLATSCertificateHashAlgorithmViolation
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errsslatscertificatehashalgorithmviolation
source_url: 'https://developer.apple.com/documentation/security/errsslatscertificatehashalgorithmviolation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errsslatscertificatehashalgorithmviolation.json'
content_hash: 'sha256:82c2b776f53fadff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSSLATSCertificateHashAlgorithmViolation

<sub>Global Variable</sub>

The peer certificate hash algorithm isn’t App Transport Security compliant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var errSSLATSCertificateHashAlgorithmViolation: OSStatus { get }
```

## Discussion

For more information about App Transport Security (ATS) compliance, see [Preventing Insecure Network Connections](preventing-insecure-network-connections.md).
