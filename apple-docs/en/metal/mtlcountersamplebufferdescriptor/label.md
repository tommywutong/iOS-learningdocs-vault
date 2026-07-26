---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebufferdescriptor/label
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebufferdescriptor/label.json'
content_hash: 'sha256:f503d8f105ea173f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBufferDescriptor](../mtlcountersamplebufferdescriptor.md)

# label

<sub>Instance Property</sub>

The name for the counter sample buffer you create with the descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String { get set }
```

## See Also

### Configuring a descriptor for a counter sample buffer

- [counterSet](counterset.md) — A GPU device’s counter set instance that you want to sample.
- [sampleCount](samplecount.md) — The number of instances of a counter set’s data that a counter sample buffer can store.
- [storageMode](storagemode.md) — The memory storage mode for the counter sample buffers you create with the descriptor.
