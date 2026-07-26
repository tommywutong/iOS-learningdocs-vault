---
title: counterSets
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/countersets
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/countersets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/countersets.json'
content_hash: 'sha256:4d3b8065847fc352'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# counterSets

<sub>Instance Property</sub>

The counter sets supported by the device object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var counterSets: [any MTLCounterSet]? { get }
```

## See Also

### Sampling a GPU device’s counters

- [- supportsCounterSampling:](<supportscountersampling(__).md>) — Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.
- [MTLCounterSamplingPoint](../mtlcountersamplingpoint.md) — Options for different times when you can sample GPU counters.
- [- newCounterSampleBufferWithDescriptor:error:](<makecountersamplebuffer(descriptor_).md>) — Creates a counter sample buffer.
