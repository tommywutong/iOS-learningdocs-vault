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
doc_path: '/documentation/metal/mtlrendercommandencoder/samplecounters(samplebuffer:sampleindex:barrier:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/samplecounters(samplebuffer:sampleindex:barrier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/samplecounters%28samplebuffer%3Asampleindex%3Abarrier%3A%29.json'
content_hash: 'sha256:fc4ffbf38aebbe3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# sampleCounters(sampleBuffer:sampleIndex:barrier:)

<sub>Instance Method</sub>

Encodes a command that samples hardware counters during the render pass and stores the data into a counter sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)
```

## Parameters

- `sampleBuffer` — An [MTLCounterSampleBuffer](../mtlcountersamplebuffer.md) instance that stores the GPU hardware data.

- `sampleIndex` — An index within `sampleBuffer` the command stores the data to.

- `barrier` — A Boolean value that indicates whether the command inserts a barrier before sampling the counter’s data. A barrier ensures that the commands you encode before this one complete before the GPU samples the hardware counters, but can negatively impact runtime performance. Running this command without a barrier means the GPU can sample counters concurrently with other commands from the encoder. Either way, the `barrier` parameter for the command has no impact on sampling commands from other passes.
