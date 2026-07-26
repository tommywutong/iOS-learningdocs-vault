---
title: Creating a counter sample buffer to store a GPU’s counter data during a pass
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass
source_url: 'https://developer.apple.com/documentation/metal/creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.json'
content_hash: 'sha256:c04ced2f3293930d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU counters and counter sample buffers](gpu-counters-and-counter-sample-buffers.md)

# Creating a counter sample buffer to store a GPU’s counter data during a pass

<sub>Article</sub>

Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.

## Overview

You can create and use an [MTLCounterSampleBuffer](mtlcountersamplebuffer.md) instance to store information from a GPU counter. To check whether a GPU produces data for a specific counter, see [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md). Each _counter sample buffer_ represents memory that a GPU uses to save data from the counter as it runs a pass. Counter sample buffers provide the GPU a place to temporarily store sample data, which avoids the need to synchronize data with the CPU. However, your app has the option to _resolve_ the sample data with the CPU after the pass completes. See [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md) for more information about resolving sample data.

Create a counter sample buffer for a GPU by:

1. Confirming a GPU device supports the counter set you want to sample
2. Retrieving the GPU’s instance of that counter set
3. Creating an [MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md) instance and configuring its properties for the counter set
4. Passing the descriptor to the GPU device’s [- newCounterSampleBufferWithDescriptor:error:](<mtldevice/makecountersamplebuffer(descriptor_).md>) factory method

**Swift**

```swift
func createTimestampBufferFor(_ device: MTLDevice) -> MTLCounterSampleBuffer? {
    // Confirm the device's counter set contains the timestamp counter.
    guard let timestampCounterSet = getCounterSet(MTLCommonCounterSet.timestamp,
                                                  from: device) else { return nil }

    // Confirm the device's counter set contains the timestamp counter.
    guard counterSet(timestampCounterSet,
                     contains: MTLCommonCounter.timestamp) else { return nil }

    // Create and configure a descriptor for the counter sample buffer.
    let descriptor = MTLCounterSampleBufferDescriptor()

    // This counter set instance belongs to the `device` instance.
    descriptor.counterSet = timestampCounterSet

    // Set the buffer to use shared memory so the CPU and GPU can directly access its contents.
    descriptor.storageMode = .shared

    // Set the sample count to 4, to make room for the:
    // – Vertex stage's start time
    // – Vertex stage's completion time
    // – Fragment stage's start time
    // – Fragment stage's completion time
    descriptor.sampleCount = sampleCount

    // Create the sample buffer by passing the descriptor to the device's factory method.
    guard let buffer = try? device.makeCounterSampleBuffer(descriptor: descriptor) else {
        print("Device failed to create a counter sample buffer.")
        return nil
    }

    return buffer
}
```

**Objective-C**

```objective-c
+ (id<MTLCounterSampleBuffer>)createTimestampBufferForDevice:(id<MTLDevice>)device
{
    // Confirm the device's counter set contains the timestamp counter.
    id<MTLCounterSet> timestampCounterSet = [self.class getCounterSet:MTLCommonCounterSetTimestamp
                                                           fromDevice:device];

    if (timestampCounterSet == nil) { return nil; }

    // Confirm the device's counter set contains the timestamp counter.
    if (![self.class counterSet:timestampCounterSet
                       contains:MTLCommonCounterTimestamp]) { return nil; }

    // Create and configure a descriptor for the counter sample buffer.
    MTLCounterSampleBufferDescriptor *descriptor;
    descriptor = [[MTLCounterSampleBufferDescriptor alloc] init];

    // This counter set instance belongs to the `device` instance.
    descriptor.counterSet = timestampCounterSet;

    // Set the buffer to use shared memory so the CPU and GPU can directly access its contents.
    descriptor.storageMode = MTLStorageModeShared;

    // Set the sample count to 4, to make room for the:
    // – Vertex stage's start time
    // – Vertex stage's completion time
    // – Fragment stage's start time
    // – Fragment stage's completion time
    descriptor.sampleCount = sampleCount;

    // Create the sample buffer by passing the descriptor to the device's factory method.
    id<MTLCounterSampleBuffer> buffer;
    NSError *error = nil;
    buffer = [device newCounterSampleBufferWithDescriptor:descriptor error:&error];

    if (error != nil) {
        NSLog(@"Device failed to create a counter sample buffer.");
        return nil;
    }

    return buffer;
}
```

The code example above gives the CPU access to the counter sample buffer by configuring the descriptor’s [storageMode](mtlcountersamplebufferdescriptor/storagemode.md) property to [MTLStorageModeShared](mtlstoragemode/shared.md). Alternatively, you can set this property to [MTLStorageModePrivate](mtlstoragemode/private.md) if your app only uses the GPU to access its data. The example also sets the descriptor’s [sampleCount](mtlcountersamplebufferdescriptor/samplecount.md) property to `4` to store the starting and completion timestamps for both the vertex and the fragment stages. The value for the descriptor’s sample count in this example is directly related to the following four properties of the [MTLRenderPassSampleBufferAttachmentDescriptor](mtlrenderpasssamplebufferattachmentdescriptor.md) type:

- [startOfVertexSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex.md)
- [endOfVertexSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/endofvertexsampleindex.md)
- [startOfFragmentSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/startoffragmentsampleindex.md)
- [endOfFragmentSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/endoffragmentsampleindex.md)

> [!note] Note
> The value you set for [sampleCount](mtlcountersamplebufferdescriptor/samplecount.md) depends on the type of data you sample and the number of passes you sample that data from.

When your app has a counter sample buffer, it can then instruct the GPU to save its counter sample data to it during a pass. See [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md) for more information.

## See Also

### Counter sample buffers

- [MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md) — A group of properties that configures the counter sample buffers you create with it.
- [MTLCounterSampleBuffer](mtlcountersamplebuffer.md) — A specialized memory buffer that stores a GPU’s counter set data.
- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md) — Retrieve a GPU’s counter data at a time the GPU supports.
- [MTLCounterDontSample](mtlcounterdontsample.md) — A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.
