---
title: sampleCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebufferdescriptor/samplecount
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor/samplecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebufferdescriptor/samplecount.json'
content_hash: 'sha256:1914381904bd6f1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBufferDescriptor](../mtlcountersamplebufferdescriptor.md)

# sampleCount

<sub>Instance Property</sub>

The number of instances of a counter set’s data that a counter sample buffer can store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleCount: Int { get set }
```

## Discussion

The counter sample buffer instances you create with the [MTLCounterSampleBufferDescriptor](../mtlcountersamplebufferdescriptor.md) can store [sampleCount](samplecount.md) instances of a counter set.

## See Also

### Configuring a descriptor for a counter sample buffer

- [counterSet](counterset.md) — A GPU device’s counter set instance that you want to sample.
- [label](label.md) — The name for the counter sample buffer you create with the descriptor.
- [storageMode](storagemode.md) — The memory storage mode for the counter sample buffers you create with the descriptor.
