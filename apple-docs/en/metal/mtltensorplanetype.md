---
title: MTLTensorPlaneType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/metal/mtltensorplanetype
source_url: 'https://developer.apple.com/documentation/metal/mtltensorplanetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorplanetype.json'
content_hash: 'sha256:1c9d389748426462'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorPlaneType

<sub>Enumeration</sub>

The possible tensor plane types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLTensorPlaneType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTLTensorPlaneTypeData](mtltensorplanetype/data.md) — The main data plane, which every tensor has _(beta)_
- [MTLTensorPlaneTypeScales](mtltensorplanetype/scales.md) — The auxiliary plane that stores scale factors for elements in the data plane. _(beta)_

### Initializers

- [init(rawValue:)](<mtltensorplanetype/init(rawvalue_).md>) _(beta)_
