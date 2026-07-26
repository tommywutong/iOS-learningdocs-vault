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
doc_path: '/documentation/metal/mtlcomputecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/samplecounters%28samplebuffer%3Asampleindex%3Abarrier%3A%29.json'
content_hash: 'sha256:af0d991e541763bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# sampleCounters(sampleBuffer:sampleIndex:barrier:)

<sub>Instance Method</sub>

Encodes a command to sample hardware counters, providing performance information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)
```

## Parameters

- `sampleBuffer` — An [MTLCounterSampleBuffer](../mtlcountersamplebuffer.md) instance that stores the GPU hardware data.

- `sampleIndex` — An index within `sampleBuffer` the command stores the data to.

- `barrier` — Whether or not the command inserts a barrier before sampling the counter’s data. A barrier ensures that the commands you encode before this one complete before the GPU samples the hardware counters, but can negatively impact runtime performance. Running this command without a barrier means the GPU can sample counters concurrently with other commands from the encoder. The `barrier` parameter for the command has no impact on sampling commands from other passes.

## Discussion

> [!important] Important
> To use a sample buffer, it needs to be part of the [sampleBufferAttachments](../mtlcomputepassdescriptor/samplebufferattachments.md) on the compute pass descriptor.

See [GPU counters and counter sample buffers](../gpu-counters-and-counter-sample-buffers.md), [Sampling GPU data into counter sample buffers](../sampling-gpu-data-into-counter-sample-buffers.md), and [MTLCounter](../mtlcounter.md) for more information.
