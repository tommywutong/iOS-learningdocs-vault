---
title: 'sampleCounters(sampleBuffer:sampleIndex:barrier:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/samplecounters%28samplebuffer%3Asampleindex%3Abarrier%3A%29.json'
content_hash: 'sha256:d2c25fb531fdf158'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# sampleCounters(sampleBuffer:sampleIndex:barrier:)

<sub>Instance Method</sub>

Encodes a command to sample hardware counters at this point in the acceleration structure pass and store the samples into a counter sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)
```

## Parameters

- `sampleBuffer` — The sample buffer to sample into.

- `sampleIndex` — The index in the counter buffer to write the sample.

- `barrier` — A Boolean value that states whether to insert a barrier before taking the sample.

## Discussion

Inserting a barrier ensures that any work you encoded with this encoder is complete before the GPU samples the hardware counters. If you don’t insert a barrier, the GPU can sample the counters concurrently with other commands encoded by this encoder. Using a barrier leads to more repeatable counter results but can negatively impact performance.

Regardless of whether you set a barrier, the GPU doesn’t isolate the sampling from work encoded by other encoders.
