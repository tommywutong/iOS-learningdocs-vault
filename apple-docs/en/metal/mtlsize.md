---
title: MTLSize
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsize
source_url: 'https://developer.apple.com/documentation/metal/mtlsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsize.json'
content_hash: 'sha256:fbf02c3da883c087'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSize

<sub>Structure</sub>

A type that represents one, two, or three dimensions of a type instance, such as an array or texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLSize
```

## Overview

Metal has many types that represent arrays of discrete elements, such as:

- A texture, which has an array of pixel elements
- A thread grid, which has an array of computational threads

Types and methods that work with these array-like types frequently have an [MTLSize](mtlsize.md) property or parameter that refers to the extents of a specific instance of the type, or a region within the instance.

> [!important] Important
> Treat each size instance as a measure of something in 3D, even if it represents something with only one or two dimensions, by assigning `1` to the irrelevant dimensions.

The following are some examples for setting a size for an instance that has less than three dimentions:

- For a 2D texture that has a height and width of `5`, set a size’s [depth](mtlsize/depth.md) property to `1` so that it represents `[5, 5, 1]`.
- For a 1D array with length `42`, set a size’s [height](mtlsize/height.md), [depth](mtlsize/depth.md) properties to `1`, so that it represents `[42, 1, 1]`.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a size instance

- [init()](<mtlsize/init().md>) — Creates a default size instance by setting the initial values for its width, height, and depth properties to zero.
- [init(width:height:depth:)](<mtlsize/init(width_height_depth_).md>) — Creates a size instance with values for its width, height, and depth properties.
- [MTLSizeMake](<mtlsizemake(______).md>) — Creates a size instance with values for its width, height, and depth properties.

### Accessing a size’s dimensions

- [width](mtlsize/width.md) — A value for the x-axis dimension.
- [height](mtlsize/height.md) — A value for the y-axis dimension.
- [depth](mtlsize/depth.md) — A value for the z-axis dimension.

## See Also

### Indirect compute commands

- [MTLIndirectComputeCommand](mtlindirectcomputecommand.md) — A compute command in an indirect command buffer.
- [MTLRegion](mtlregion.md) — The bounds for a subset of an instance’s elements.
- [MTLOrigin](mtlorigin.md) — The coordinates for the front upper-left corner of a region.
- [MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md) — The data layout required for the arguments needed to specify the stage-in region.
- [MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md) — The data layout required for arguments needed to specify the size of threadgroups.
