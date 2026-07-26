---
title: storageMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebufferdescriptor/storagemode
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor/storagemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebufferdescriptor/storagemode.json'
content_hash: 'sha256:d8c4f73fc05568bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBufferDescriptor](../mtlcountersamplebufferdescriptor.md)

# storageMode

<sub>Instance Property</sub>

The memory storage mode for the counter sample buffers you create with the descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var storageMode: MTLStorageMode { get set }
```

## Discussion

To access a counter sample buffer with the CPU, set this property to [MTLStorageModeShared](../mtlstoragemode/shared.md), otherwise [MTLStorageModePrivate](../mtlstoragemode/private.md).

## See Also

### Configuring a descriptor for a counter sample buffer

- [counterSet](counterset.md) — A GPU device’s counter set instance that you want to sample.
- [label](label.md) — The name for the counter sample buffer you create with the descriptor.
- [sampleCount](samplecount.md) — The number of instances of a counter set’s data that a counter sample buffer can store.
