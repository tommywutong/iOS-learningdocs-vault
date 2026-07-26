---
title: CMSCertificateChainMode
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/cmscertificatechainmode
source_url: 'https://developer.apple.com/documentation/security/cmscertificatechainmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmscertificatechainmode.json'
content_hash: 'sha256:bcd1ec4043565931'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSCertificateChainMode

<sub>Enumeration</sub>

Constants that can be set to specify what certificates to include in a signed message.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CMSCertificateChainMode
```

## Overview

Use these with the [CMSEncoderSetCertificateChainMode](<cmsencodersetcertificatechainmode(____).md>) function.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCMSCertificateNone](cmscertificatechainmode/none.md) — Don’t include any certificates.
- [kCMSCertificateSignerOnly](cmscertificatechainmode/signeronly.md) — Only include signer certificates.
- [kCMSCertificateChain](cmscertificatechainmode/chain.md) — Include the signer certificate chain up to but not including the root certificate.
- [kCMSCertificateChainWithRoot](cmscertificatechainmode/chainwithroot.md) — Include the entire signer certificate chain, including the root certificate.

### Enumeration Cases

- [kCMSCertificateChainWithRootOrFail](cmscertificatechainmode/chainwithrootorfail.md)

### Initializers

- [init(rawValue:)](<cmscertificatechainmode/init(rawvalue_).md>)
