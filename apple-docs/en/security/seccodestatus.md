---
title: SecCodeStatus
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodestatus
source_url: 'https://developer.apple.com/documentation/security/seccodestatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodestatus.json'
content_hash: 'sha256:1e65123a9eeaedb5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeStatus

<sub>Structure</sub>

Operational flags attached by code signing services to running code.

<sub>Mac Catalyst, macOS</sub>

```swift
struct SecCodeStatus
```

## Overview

These flags are maintained by the code’s host, and can be read by anyone. Running code may change its own flags, and root may change anyone’s flags. However, each of these flags can change in only one direction and never back, for the lifetime of the code. Not even root can violate this restriction.

All of the bits in the [SecCodeStatus](seccodestatus.md) enumeration are reserved by Apple. If you set any bits not defined here, the behavior is undefined.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<seccodestatus/init(rawvalue_).md>)

### Constants

- [kSecCodeStatusValid](seccodestatus/valid.md) — The code is dynamically valid.
- [kSecCodeStatusHard](seccodestatus/hard.md) — The code prefers to be denied access to resources if gaining access would invalidate it.
- [kSecCodeStatusKill](seccodestatus/kill.md) — The code wants to be terminated if it ever loses its validity.
- [kSecCodeStatusDebugged](seccodestatus/debugged.md) — The code has been debugged by another process that was allowed to do so.
- [kSecCodeStatusPlatform](seccodestatus/platform.md) — The code ships with the operating system and is signed by Apple.
