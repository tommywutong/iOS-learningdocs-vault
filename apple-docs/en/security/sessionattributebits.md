---
title: SessionAttributeBits
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sessionattributebits
source_url: 'https://developer.apple.com/documentation/security/sessionattributebits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sessionattributebits.json'
content_hash: 'sha256:13859d38c2a8a263'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SessionAttributeBits

<sub>Structure</sub>

The attributes of a security session.

<sub>Mac Catalyst, macOS</sub>

```swift
struct SessionAttributeBits
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<sessionattributebits/init(rawvalue_).md>) — Initializes a session attribute bits structure.

### Bits

- [sessionIsRoot](sessionattributebits/sessionisroot.md) — A bit that indicates the session is the root session.
- [sessionHasGraphicAccess](sessionattributebits/sessionhasgraphicaccess.md) — A bit that indicates a graphic subsystem is available.
- [sessionHasTTY](sessionattributebits/sessionhastty.md) — A bit that indicates `/dev/tty` is available.
- [sessionIsRemote](sessionattributebits/sessionisremote.md) — A bit that indicates the session was initiated over the network.
