---
title: MTLPatchType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpatchtype
source_url: 'https://developer.apple.com/documentation/metal/mtlpatchtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpatchtype.json'
content_hash: 'sha256:19f86280b5a724c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPatchType

<sub>Enumeration</sub>

Types of tessellation patches that can be inputs of a post-tessellation vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLPatchType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Patch types

- [MTLPatchTypeNone](mtlpatchtype/none.md) — An option that indicates that this isn’t a post-tessellation vertex function.
- [MTLPatchTypeTriangle](mtlpatchtype/triangle.md) — A triangle patch.
- [MTLPatchTypeQuad](mtlpatchtype/quad.md) — A quad patch.

### Initializers

- [init(rawValue:)](<mtlpatchtype/init(rawvalue_).md>)

## See Also

### Identifying the tessellation patch

- [patchType](mtlfunction/patchtype.md) — The tessellation patch type of a post-tessellation vertex function.
- [patchControlPointCount](mtlfunction/patchcontrolpointcount.md) — The number of patch control points in the post-tessellation vertex function.
