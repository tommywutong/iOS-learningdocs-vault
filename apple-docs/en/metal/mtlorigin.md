---
title: MTLOrigin
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlorigin
source_url: 'https://developer.apple.com/documentation/metal/mtlorigin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlorigin.json'
content_hash: 'sha256:cd52576a9b1e7471'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLOrigin

<sub>Structure</sub>

The coordinates for the front upper-left corner of a region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLOrigin
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating origin points

- [init()](<mtlorigin/init().md>) — Initializes a new origin.
- [init(x:y:z:)](<mtlorigin/init(x_y_z_).md>) — Initializes a new origin with the specified coordinates.
- [MTLOriginMake](<mtloriginmake(______).md>) — Returns a new origin with the specified coordinates.

### Getting and setting coordinate values

- [x](mtlorigin/x.md) — The x coordinate of the origin.
- [y](mtlorigin/y.md) — The y coordinate of the origin.
- [z](mtlorigin/z.md) — The z coordinate of the origin.

## See Also

### Indirect compute commands

- [MTLIndirectComputeCommand](mtlindirectcomputecommand.md) — A compute command in an indirect command buffer.
- [MTLRegion](mtlregion.md) — The bounds for a subset of an instance’s elements.
- [MTLSize](mtlsize.md) — A type that represents one, two, or three dimensions of a type instance, such as an array or texture.
- [MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md) — The data layout required for the arguments needed to specify the stage-in region.
- [MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md) — The data layout required for arguments needed to specify the size of threadgroups.
