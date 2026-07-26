---
title: SecTrustOptionFlags
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustoptionflags
source_url: 'https://developer.apple.com/documentation/security/sectrustoptionflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustoptionflags.json'
content_hash: 'sha256:a2f153dee94f3818'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustOptionFlags

<sub>Structure</sub>

The option flags used to condition a trust evaluation.

<sub>macOS</sub>

```swift
struct SecTrustOptionFlags
```

## Overview

Use these flags in calls to the [SecTrustSetOptions](<sectrustsetoptions(____).md>) function.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<sectrustoptionflags/init(rawvalue_).md>) — Initializes a trust option flags structure.

### Flags

- [kSecTrustOptionAllowExpired](sectrustoptionflags/allowexpired.md) — Allow expired certificates (except for the root certificate).
- [kSecTrustOptionLeafIsCA](sectrustoptionflags/leafisca.md) — Allow CA certificates as leaf certificates.
- [kSecTrustOptionFetchIssuerFromNet](sectrustoptionflags/fetchissuerfromnet.md) — Allow network downloads of CA certificates.
- [kSecTrustOptionAllowExpiredRoot](sectrustoptionflags/allowexpiredroot.md) — Allow expired root certificates.
- [kSecTrustOptionRequireRevPerCert](sectrustoptionflags/requirerevpercert.md) — Require a positive revocation check for each certificate.
- [kSecTrustOptionUseTrustSettings](sectrustoptionflags/usetrustsettings.md) — Use TrustSettings instead of anchors.
- [kSecTrustOptionImplicitAnchors](sectrustoptionflags/implicitanchors.md) — Treat properly self-signed certificates as anchors implicitly.
