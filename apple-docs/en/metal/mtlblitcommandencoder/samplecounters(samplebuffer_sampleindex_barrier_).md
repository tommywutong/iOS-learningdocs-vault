---
title: 'sampleCounters(sampleBuffer:sampleIndex:barrier:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/samplecounters(samplebuffer:sampleindex:barrier:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/samplecounters(samplebuffer:sampleindex:barrier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/samplecounters%28samplebuffer%3Asampleindex%3Abarrier%3A%29.json'
content_hash: 'sha256:7dfa40df77d2132d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# sampleCounters(sampleBuffer:sampleIndex:barrier:)

<sub>Instance Method</sub>

Encodes a command that samples the GPU’s hardware counters during a blit pass and stores the data in a counter sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)
```

## Parameters

- `sampleBuffer` — A counter sample buffer where the command stores the sample data.

- `sampleIndex` — A location within `sampleBuffer` where the command stores the sample data.

- `barrier` — A Boolean value that indicates whether the command inserts a barrier before taking the sample.

## Discussion

Inserting a barrier ensures that any work you encode with this encoder is complete before the GPU samples the hardware counters. If you don’t insert a barrier, the GPU can sample the counters concurrently with other commands you encode with this encoder. Using a barrier can help the counter results be more predictable and repeatable, but it may adversely affect your app’s runtime performance.

> [!note] Note
> The GPU doesn’t isolate this sampling command from any commands that come from another encoder, with or without a barrier.

## See Also

### Sampling counters

- [resolveCounters(_:range:destinationBuffer:destinationOffset:)](<resolvecounters(__range_destinationbuffer_destinationoffset_).md>) — Encodes a command that resolves the data from the samples in a sample counter buffer and stores the results into a buffer.
