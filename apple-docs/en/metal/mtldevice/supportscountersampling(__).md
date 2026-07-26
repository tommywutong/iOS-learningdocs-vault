---
title: 'supportsCounterSampling(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/supportscountersampling(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportscountersampling(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportscountersampling%28_%3A%29.json'
content_hash: 'sha256:c3d631dcf85e51fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsCounterSampling(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func supportsCounterSampling(_ samplingPoint: MTLCounterSamplingPoint) -> Bool
```

## Parameters

- `samplingPoint` — The command boundary to test.

## See Also

### Sampling a GPU device’s counters

- [counterSets](countersets.md) — The counter sets supported by the device object.
- [MTLCounterSamplingPoint](../mtlcountersamplingpoint.md) — Options for different times when you can sample GPU counters.
- [- newCounterSampleBufferWithDescriptor:error:](<makecountersamplebuffer(descriptor_).md>) — Creates a counter sample buffer.
