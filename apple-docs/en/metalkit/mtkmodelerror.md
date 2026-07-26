---
title: MTKModelError
framework: MetalKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtkmodelerror
source_url: 'https://developer.apple.com/documentation/metalkit/mtkmodelerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtkmodelerror.json'
content_hash: 'sha256:e9f71d86889c19dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetalKit](../metalkit.md)

# MTKModelError

<sub>Structure</sub>

Constants used to declare Model Errors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTKModelError
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a Raw Constant

- [init(rawValue:)](<mtkmodelerror/init(rawvalue_).md>)

### Finding Model Error Constants

- [MTKModelErrorDomain](mtkmodelerror/domain.md) — The error domain used by MetalKit when returning mesh initialization errors.
- [MTKModelErrorKey](mtkmodelerror/key.md) — The key used to retrieve an error string from an error object’s [userInfo](../foundation/nserror/userinfo.md) dictionary.
