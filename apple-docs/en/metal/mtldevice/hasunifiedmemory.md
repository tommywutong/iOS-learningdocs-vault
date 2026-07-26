---
title: hasUnifiedMemory
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/hasunifiedmemory
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/hasunifiedmemory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/hasunifiedmemory.json'
content_hash: 'sha256:658a49ae9ea4b5e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# hasUnifiedMemory

<sub>Instance Property</sub>

A Boolean value that indicates whether the GPU shares all of its memory with the CPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var hasUnifiedMemory: Bool { get }
```

## Discussion

A GPU with unified memory ([true](../../swift/true.md)) is typically an integrated GPU. A GPU with dedicated memory ([false](../../swift/false.md)) may take additional time to synchronize managed resources or copy data into private GPU resources.

## See Also

### Checking a GPU device’s memory

- [currentAllocatedSize](currentallocatedsize.md) — The total amount of memory, in bytes, the GPU device is using for all of its resources.
- [recommendedMaxWorkingSetSize](recommendedmaxworkingsetsize.md) — An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.
- [maxTransferRate](maxtransferrate.md) — The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM). _(deprecated)_
