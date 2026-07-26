---
title: MTLRegion
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlregion
source_url: 'https://developer.apple.com/documentation/metal/mtlregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlregion.json'
content_hash: 'sha256:c07b0f71f2a5ec65'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRegion

<sub>Structure</sub>

The bounds for a subset of an instance’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLRegion
```

## Overview

Metal has many instance types that represent arrays of discrete elements. For example, a texture has an array of pixel elements, and a thread grid has an array of computational threads. Use [MTLRegion](mtlregion.md) instances to describe subsets of these instances.

The origin is the front upper-left corner of the region, and its extents go towards the back lower-right corner. Conceptually, when using an [MTLRegion](mtlregion.md) instance to describe a subset of an instance, treat the instance as a 3D array of elements, even if it has fewer dimensions. For a 2D instance, set the z coordinate of the origin to `0` and the depth to `1`. For a 1D instance, set the y and z coordinates of the origin to `0` and the height and depth to `1`.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating regions

- [init()](<mtlregion/init().md>) — Initializes a new region.
- [init(origin:size:)](<mtlregion/init(origin_size_).md>) — Initializes a new region with the specified origin and size.
- [MTLRegionMake1D](<mtlregionmake1d(____).md>) — Creates a 3D representation of a 1D region.
- [MTLRegionMake2D](<mtlregionmake2d(________).md>) — Creates a 3D representation of a 2D region.
- [MTLRegionMake3D](<mtlregionmake3d(____________).md>) — Creates a 3D region.

### Getting and setting region information

- [origin](mtlregion/origin.md) — The coordinates of the front upper-left corner of the region.
- [size](mtlregion/size.md) — The dimensions of the region.

## See Also

### Indirect compute commands

- [MTLIndirectComputeCommand](mtlindirectcomputecommand.md) — A compute command in an indirect command buffer.
- [MTLSize](mtlsize.md) — A type that represents one, two, or three dimensions of a type instance, such as an array or texture.
- [MTLOrigin](mtlorigin.md) — The coordinates for the front upper-left corner of a region.
- [MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md) — The data layout required for the arguments needed to specify the stage-in region.
- [MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md) — The data layout required for arguments needed to specify the size of threadgroups.
