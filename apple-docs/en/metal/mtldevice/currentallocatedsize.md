---
title: currentAllocatedSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/currentallocatedsize
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/currentallocatedsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/currentallocatedsize.json'
content_hash: 'sha256:0c92b0e7d9bfab70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# currentAllocatedSize

<sub>Instance Property</sub>

The total amount of memory, in bytes, the GPU device is using for all of its resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var currentAllocatedSize: Int { get }
```

## See Also

### Checking a GPU device’s memory

- [recommendedMaxWorkingSetSize](recommendedmaxworkingsetsize.md) — An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.
- [hasUnifiedMemory](hasunifiedmemory.md) — A Boolean value that indicates whether the GPU shares all of its memory with the CPU.
- [maxTransferRate](maxtransferrate.md) — The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM). _(deprecated)_
