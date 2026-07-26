---
title: MTLCounterSampleBufferDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebufferdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebufferdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebufferdescriptor.json'
content_hash: 'sha256:3de31cfa799465f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterSampleBufferDescriptor

<sub>Class</sub>

A group of properties that configures the counter sample buffers you create with it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLCounterSampleBufferDescriptor
```

## Overview

To create a new counter sample buffer, create and configure an [MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md) instance, and then call an [MTLDevice](mtldevice.md) instance’s [- newCounterSampleBufferWithDescriptor:error:](<mtldevice/makecountersamplebuffer(descriptor_).md>) method. See [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md).

Each new sample counter buffer inherits the values of the descriptor’s properties when you create it. You can modify a descriptor and reuse it to create other counter sample buffers, which has no effect on existing counter sample buffers.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring a descriptor for a counter sample buffer

- [counterSet](mtlcountersamplebufferdescriptor/counterset.md) — A GPU device’s counter set instance that you want to sample.
- [label](mtlcountersamplebufferdescriptor/label.md) — The name for the counter sample buffer you create with the descriptor.
- [sampleCount](mtlcountersamplebufferdescriptor/samplecount.md) — The number of instances of a counter set’s data that a counter sample buffer can store.
- [storageMode](mtlcountersamplebufferdescriptor/storagemode.md) — The memory storage mode for the counter sample buffers you create with the descriptor.

## See Also

### Counter sample buffers

- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) — Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [MTLCounterSampleBuffer](mtlcountersamplebuffer.md) — A specialized memory buffer that stores a GPU’s counter set data.
- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md) — Retrieve a GPU’s counter data at a time the GPU supports.
- [MTLCounterDontSample](mtlcounterdontsample.md) — A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.
