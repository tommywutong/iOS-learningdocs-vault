---
title: 'makeCounterSampleBuffer(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makecountersamplebuffer(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecountersamplebuffer(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecountersamplebuffer%28descriptor%3A%29.json'
content_hash: 'sha256:79e6ae99fa9b0a98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeCounterSampleBuffer(descriptor:)

<sub>Instance Method</sub>

Creates a counter sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCounterSampleBuffer(descriptor: MTLCounterSampleBufferDescriptor) throws -> any MTLCounterSampleBuffer
```

## Parameters

- `descriptor` — An [MTLCounterSampleBufferDescriptor](../mtlcountersamplebufferdescriptor.md) instance.

## Return Value

A new [MTLCounterSampleBuffer](../mtlcountersamplebuffer.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

The method may produce an error if the GPU driver has exhausted its underlying resources for counter sample buffers.

## See Also

### Sampling a GPU device’s counters

- [counterSets](countersets.md) — The counter sets supported by the device object.
- [- supportsCounterSampling:](<supportscountersampling(__).md>) — Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.
- [MTLCounterSamplingPoint](../mtlcountersamplingpoint.md) — Options for different times when you can sample GPU counters.
