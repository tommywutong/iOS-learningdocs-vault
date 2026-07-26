---
title: SessionCreationFlags
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sessioncreationflags
source_url: 'https://developer.apple.com/documentation/security/sessioncreationflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sessioncreationflags.json'
content_hash: 'sha256:0519b865ca5b2caf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SessionCreationFlags

<sub>Structure</sub>

The flags that affect the creation of a security session.

<sub>Mac Catalyst, macOS</sub>

```swift
struct SessionCreationFlags
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<sessioncreationflags/init(rawvalue_).md>) — Initializes a session creation flags value.

### Flags

- [sessionKeepCurrentBootstrap](sessioncreationflags/sessionkeepcurrentbootstrap.md) — The caller has allocated sub-bootstrap.
