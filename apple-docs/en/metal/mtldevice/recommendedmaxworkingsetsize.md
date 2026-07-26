---
title: recommendedMaxWorkingSetSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 13.0+, macOS 10.12+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/recommendedmaxworkingsetsize
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/recommendedmaxworkingsetsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/recommendedmaxworkingsetsize.json'
content_hash: 'sha256:66c06153fb00d35f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# recommendedMaxWorkingSetSize

<sub>Instance Property</sub>

An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var recommendedMaxWorkingSetSize: UInt64 { get }
```

## Discussion

You can help the GPU maintain its performance by keeping the total memory footprint of its resources and heaps less than this threshold value.

## See Also

### Checking a GPU device’s memory

- [currentAllocatedSize](currentallocatedsize.md) — The total amount of memory, in bytes, the GPU device is using for all of its resources.
- [hasUnifiedMemory](hasunifiedmemory.md) — A Boolean value that indicates whether the GPU shares all of its memory with the CPU.
- [maxTransferRate](maxtransferrate.md) — The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM). _(deprecated)_
