---
title: 'resolveCounters(_:range:destinationBuffer:destinationOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/resolvecounters(_:range:destinationbuffer:destinationoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/resolvecounters(_:range:destinationbuffer:destinationoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/resolvecounters%28_%3Arange%3Adestinationbuffer%3Adestinationoffset%3A%29.json'
content_hash: 'sha256:f5522f81a5be9aec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# resolveCounters(_:range:destinationBuffer:destinationOffset:)

<sub>Instance Method</sub>

Encodes a command that resolves the data from the samples in a sample counter buffer and stores the results into a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func resolveCounters(_ sampleBuffer: any MTLCounterSampleBuffer, range: Range<Int>, destinationBuffer: any MTLBuffer, destinationOffset: Int)
```

## Parameters

- `sampleBuffer` — A counter sample buffer source that contains the sample data.

- `range` — A range that indicates which of the buffer’s samples the command resolves.

- `destinationBuffer` — A destination buffer where the command stores the data it resolves.

- `destinationOffset` — A starting offset, in bytes, within `destinationBuffer` where the blit pass writes the first byte of the data it resolves.

## Discussion

For an example of how and when to use this method, see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md).

> [!note] Note
> The GPU stores [MTLCounterErrorValue](../mtlcountererrorvalue.md) in `destinationBuffer` each time it encounters an error resolving a sample.

## See Also

### Sampling counters

- [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<samplecounters(samplebuffer_sampleindex_barrier_).md>) — Encodes a command that samples the GPU’s hardware counters during a blit pass and stores the data in a counter sample buffer.
