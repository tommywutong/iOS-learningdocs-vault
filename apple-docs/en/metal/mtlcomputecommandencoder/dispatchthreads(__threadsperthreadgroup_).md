---
title: 'dispatchThreads(_:threadsPerThreadgroup:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/dispatchthreads(_:threadsperthreadgroup:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/dispatchthreads(_:threadsperthreadgroup:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/dispatchthreads%28_%3Athreadsperthreadgroup%3A%29.json'
content_hash: 'sha256:e8b987137ef77d4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# dispatchThreads(_:threadsPerThreadgroup:)

<sub>Instance Method</sub>

Encodes a compute command using an arbitrarily sized grid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dispatchThreads(_ threadsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)
```

## Parameters

- `threadsPerGrid` — The number of threads in the grid, in each dimension.

- `threadsPerThreadgroup` — The number of threads in one threadgroup, in each dimension.

## Discussion

> [!warning] Warning
> Use this method only if the device your app is running on supports nonuniform threadgroup sizes. Check for device capabilities with [- supportsFamily:](<../mtldevice/supportsfamily(__).md>) on the device providing your compute command encoder. See [Metal Feature Set Tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for device support information.

This method encodes a call that uses an arbitrary number of threads in its execution grid. Metal calculates the number of threadgroups needed, providing partial threadgroups if necessary. Prefer this method to [- dispatchThreadgroups:threadsPerThreadgroup:](<dispatchthreadgroups(__threadsperthreadgroup_).md>) if your app requires bounds checking or you need extra data allocations to saturate a uniform grid.

## See Also

### Dispatching kernel calls directly

- [- dispatchThreadgroups:threadsPerThreadgroup:](<dispatchthreadgroups(__threadsperthreadgroup_).md>) — Encodes a compute dispatch command using a grid aligned to threadgroup boundaries.
