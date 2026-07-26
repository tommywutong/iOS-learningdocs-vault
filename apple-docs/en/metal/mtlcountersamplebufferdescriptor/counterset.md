---
title: counterSet
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebufferdescriptor/counterset
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor/counterset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebufferdescriptor/counterset.json'
content_hash: 'sha256:8d458a107e7e5acd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBufferDescriptor](../mtlcountersamplebufferdescriptor.md)

# counterSet

<sub>Instance Property</sub>

A GPU device’s counter set instance that you want to sample.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var counterSet: (any MTLCounterSet)? { get set }
```

## Discussion

Assign this property to one of the counter sets in an [MTLDevice](../mtldevice.md) instance’s [counterSets](../mtldevice/countersets.md) property.

## See Also

### Configuring a descriptor for a counter sample buffer

- [label](label.md) — The name for the counter sample buffer you create with the descriptor.
- [sampleCount](samplecount.md) — The number of instances of a counter set’s data that a counter sample buffer can store.
- [storageMode](storagemode.md) — The memory storage mode for the counter sample buffers you create with the descriptor.
