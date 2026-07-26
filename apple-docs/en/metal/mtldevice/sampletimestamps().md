---
title: sampleTimestamps()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/sampletimestamps()
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/sampletimestamps()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/sampletimestamps%28%29.json'
content_hash: 'sha256:8afa72545d4a1d2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# sampleTimestamps()

<sub>Instance Method</sub>

Captures and returns a CPU timestamp and a GPU timestamp from the same moment in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sampleTimestamps() -> (cpu: MTLTimestamp, gpu: MTLTimestamp)
```

## Return Value

A tuple that contains the CPU and GPU timestamps.

- **`cpu`** — A timestamp from the CPU.
- **`gpu`** — A timestamp from the GPU the device instance represents.

## Discussion

For an example of how and when to use corresponding timestamps from the CPU and GPU, see [Converting GPU timestamps into CPU time](../converting-gpu-timestamps-into-cpu-time.md).
