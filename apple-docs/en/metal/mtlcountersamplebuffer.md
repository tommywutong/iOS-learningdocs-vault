---
title: MTLCounterSampleBuffer
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffer.json'
content_hash: 'sha256:e4bc1956b253bc1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterSampleBuffer

<sub>Protocol</sub>

A specialized memory buffer that stores a GPU’s counter set data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLCounterSampleBuffer : NSObjectProtocol
```

## Overview

Create a counter sample buffer by calling an [MTLDevice](mtldevice.md) instance’s [- newCounterSampleBufferWithDescriptor:error:](<mtldevice/makecountersamplebuffer(descriptor_).md>) method. See [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md).

You can store a GPU device’s counter set data only with an [MTLCounterSampleBuffer](mtlcountersamplebuffer.md) instance that you create from the same device. See [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md) for information about storing counter sample data in a counter sample buffer.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Resolving the counter sample buffer’s data

- [resolveCounterRange(_:)](<mtlcountersamplebuffer/resolvecounterrange(__).md>) — Transforms samples of a GPU’s counter set from the driver’s internal format to a standard Metal data structure.

### Inspecting the counter sample buffer’s configuration

- [label](mtlcountersamplebuffer/label.md) — A string that identifies the counter sample buffer.
- [device](mtlcountersamplebuffer/device.md) — The GPU device instance that owns the counter sample buffer.
- [sampleCount](mtlcountersamplebuffer/samplecount.md) — The number of samples in the buffer.

## See Also

### Counter sample buffers

- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) — Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md) — A group of properties that configures the counter sample buffers you create with it.
- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md) — Retrieve a GPU’s counter data at a time the GPU supports.
- [MTLCounterDontSample](mtlcounterdontsample.md) — A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.
