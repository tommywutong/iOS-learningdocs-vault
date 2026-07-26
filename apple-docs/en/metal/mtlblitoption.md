---
title: MTLBlitOption
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblitoption
source_url: 'https://developer.apple.com/documentation/metal/mtlblitoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitoption.json'
content_hash: 'sha256:ca8fd166dc1e1965'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBlitOption

<sub>Structure</sub>

The options that enable behavior for some blit operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLBlitOption
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Depth and stencil buffer options

- [MTLBlitOptionDepthFromDepthStencil](mtlblitoption/depthfromdepthstencil.md) — A blit option that copies the depth portion of a combined depth and stencil texture to or from a buffer.
- [MTLBlitOptionStencilFromDepthStencil](mtlblitoption/stencilfromdepthstencil.md) — A blit option that copies the stencil portion of a combined depth and stencil texture to or from a buffer.

### Texture compression options

- [MTLBlitOptionRowLinearPVRTC](mtlblitoption/rowlinearpvrtc.md) — A blit option that copies PVRTC data between a texture and a buffer.

### Swift support

- [init(rawValue:)](<mtlblitoption/init(rawvalue_).md>) — Creates a blit option from a raw value.

## See Also

### Encoding a blit pass

- [MTLBlitCommandEncoder](mtlblitcommandencoder.md) — Encodes commands that copy and modify resources for a single blit pass.
