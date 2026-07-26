---
title: SecCSFlags
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccsflags
source_url: 'https://developer.apple.com/documentation/security/seccsflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccsflags.json'
content_hash: 'sha256:4bb1c8ce723d853d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCSFlags

<sub>Structure</sub>

Values that can be used in the `flags` parameter to most code signing functions.

<sub>Mac Catalyst, macOS</sub>

```swift
struct SecCSFlags
```

## Overview

All of the bits in the [SecCSFlags](seccsflags.md) enumeration are reserved by Apple. If you set any bits not defined here, the behavior is undefined.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<seccsflags/init(rawvalue_).md>)

### Constants

- [kSecCSConsiderExpiration](seccsflags/considerexpiration.md) — Consider expired certificates invalid.
- [kSecCSEnforceRevocationChecks](seccsflags/enforcerevocationchecks.md)
- [kSecCSCheckTrustedAnchors](seccsflags/checktrustedanchors.md)
- [kSecCSNoNetworkAccess](seccsflags/nonetworkaccess.md)
- [kSecCSReportProgress](seccsflags/reportprogress.md)
- [kSecCSQuickCheck](seccsflags/quickcheck.md)

### Type Properties

- [kSecCSApplyEmbeddedPolicy](seccsflags/applyembeddedpolicy.md)
- [kSecCSMatchGuestRequirementInKernel](seccsflags/matchguestrequirementinkernel.md)
- [kSecCSStripDisallowedXattrs](seccsflags/stripdisallowedxattrs.md)
- [kSecCSUseSignature1](seccsflags/usesignature1.md)
- [kSecCSUseSignature2](seccsflags/usesignature2.md)
