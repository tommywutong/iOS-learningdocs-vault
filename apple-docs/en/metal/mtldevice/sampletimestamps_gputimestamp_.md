---
title: 'sampleTimestamps:gpuTimestamp:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/sampletimestamps:gputimestamp:'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/sampletimestamps:gputimestamp:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/sampletimestamps%3Agputimestamp%3A.json'
content_hash: 'sha256:af007c169756664a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# sampleTimestamps:gpuTimestamp:

<sub>Instance Method</sub>

Captures and returns a CPU timestamp and a GPU timestamp from the same moment in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) sampleTimestamps:(MTLTimestamp *) cpuTimestamp gpuTimestamp:(MTLTimestamp *) gpuTimestamp;
```

## Parameters

- `cpuTimestamp` — A pointer the method uses to save a timestamp from the CPU.

- `gpuTimestamp` — A pointer the method uses to save a timestamp from the GPU the device instance represents.

## Discussion

For an example of how and when to use corresponding timestamps from the CPU and GPU, see [Converting GPU timestamps into CPU time](../converting-gpu-timestamps-into-cpu-time.md).
