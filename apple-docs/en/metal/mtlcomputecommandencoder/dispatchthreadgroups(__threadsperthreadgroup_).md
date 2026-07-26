---
title: 'dispatchThreadgroups(_:threadsPerThreadgroup:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/dispatchthreadgroups(_:threadsperthreadgroup:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/dispatchthreadgroups(_:threadsperthreadgroup:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/dispatchthreadgroups%28_%3Athreadsperthreadgroup%3A%29.json'
content_hash: 'sha256:c61241be61d20ccd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# dispatchThreadgroups(_:threadsPerThreadgroup:)

<sub>Instance Method</sub>

Encodes a compute dispatch command using a grid aligned to threadgroup boundaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dispatchThreadgroups(_ threadgroupsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)
```

## Parameters

- `threadgroupsPerGrid` — An [MTLSize](../mtlsize.md) instance that represents the number of threads for each grid dimension.

- `threadsPerThreadgroup` — An [MTLSize](../mtlsize.md) instance that represents the number of threads in a threadgroup.

## Discussion

> [!tip] Tip
> Prefer using dispatchThreads for your kernel calls on `Apple4` and later Apple GPUs. See [Metal Feature Set Tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on hardware support.

Metal calculates the number of threads in a grid by multiplying `threadsPerThreadgroup` by `threadgroupsPerGrid`.

If the size of your data doesn’t match the size of the grid, perform boundary checks in your compute function to avoid accessing data out of bounds. See [Calculating threadgroup and grid sizes](../calculating-threadgroup-and-grid-sizes.md) for an example.

## See Also

### Dispatching kernel calls directly

- [- dispatchThreads:threadsPerThreadgroup:](<dispatchthreads(__threadsperthreadgroup_).md>) — Encodes a compute command using an arbitrarily sized grid.
