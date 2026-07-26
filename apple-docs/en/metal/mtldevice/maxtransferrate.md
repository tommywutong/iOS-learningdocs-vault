---
title: maxTransferRate
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevice/maxtransferrate
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maxtransferrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maxtransferrate.json'
content_hash: 'sha256:daba81d0cdaaa441'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# maxTransferRate

<sub>Instance Property</sub>

The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM).

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
var maxTransferRate: UInt64 { get }
```

## Discussion

Metal calculates this value from the raw data-clock rate, and the GPU may not be able to reach this speed in real-world conditions.

> [!important] Important
> The maximum transfer rate for built-in GPUs is `0`.

## See Also

### Checking a GPU device’s memory

- [currentAllocatedSize](currentallocatedsize.md) — The total amount of memory, in bytes, the GPU device is using for all of its resources.
- [recommendedMaxWorkingSetSize](recommendedmaxworkingsetsize.md) — An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.
- [hasUnifiedMemory](hasunifiedmemory.md) — A Boolean value that indicates whether the GPU shares all of its memory with the CPU.
