---
title: MTLStageInRegionIndirectArguments
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstageinregionindirectarguments
source_url: 'https://developer.apple.com/documentation/metal/mtlstageinregionindirectarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstageinregionindirectarguments.json'
content_hash: 'sha256:c0992434a6e3cffd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStageInRegionIndirectArguments

<sub>Structure</sub>

The data layout required for the arguments needed to specify the stage-in region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLStageInRegionIndirectArguments
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtlstageinregionindirectarguments/init().md>)
- [init(stageInOrigin:stageInSize:)](<mtlstageinregionindirectarguments/init(stageinorigin_stageinsize_).md>)

### Instance Properties

- [stageInOrigin](mtlstageinregionindirectarguments/stageinorigin.md) — The location of the upper-left corner of the block.
- [stageInSize](mtlstageinregionindirectarguments/stageinsize.md) — The size of the block.

## See Also

### Indirect compute commands

- [MTLIndirectComputeCommand](mtlindirectcomputecommand.md) — A compute command in an indirect command buffer.
- [MTLRegion](mtlregion.md) — The bounds for a subset of an instance’s elements.
- [MTLSize](mtlsize.md) — A type that represents one, two, or three dimensions of a type instance, such as an array or texture.
- [MTLOrigin](mtlorigin.md) — The coordinates for the front upper-left corner of a region.
- [MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md) — The data layout required for arguments needed to specify the size of threadgroups.
