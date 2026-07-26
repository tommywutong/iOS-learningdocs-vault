---
title: Sampling GPU data into counter sample buffers
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/sampling-gpu-data-into-counter-sample-buffers
source_url: 'https://developer.apple.com/documentation/metal/sampling-gpu-data-into-counter-sample-buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/sampling-gpu-data-into-counter-sample-buffers.json'
content_hash: 'sha256:4521c98cde24ce1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU counters and counter sample buffers](gpu-counters-and-counter-sample-buffers.md)

# Sampling GPU data into counter sample buffers

<sub>Article</sub>

Retrieve a GPU’s counter data at a time the GPU supports.

## Overview

You can sample a GPU device’s performance counter data at different times, including:

- At pipeline stage boundaries
- Between different Metal commands

Typically, a GPU supports one of these boundary types. For example, Apple silicon supports sampling at the stage boundary because it processes fragments after processing every primitive for a render pass. However, a typical immediate-mode GPU supports sampling between commands.

Before you can sample a GPU counter, implement the following prerequisite steps:

1. Identify which counters you can sample from an [MTLDevice](mtldevice.md) instance (see [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)).
2. Make an [MTLCounterSampleBuffer](mtlcountersamplebuffer.md) instance to store the counter’s data (see [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md)).

The sections below explain how to identify when you can sample a GPU’s counters, and how to encode commands to retrieve their data.

Each GPU vendor defines its own private data format for its counter sample buffers, which means your app can’t read the contents of each buffer directly. Instead, your app can transform the data from the vendor’s internal format to the standard Metal formats by _resolving_ each sample buffer. See [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md) for the next steps that resolve the data within a counter sample buffer.

### Check which boundaries a GPU supports

You can inspect a GPU device instance to see whether it supports a specific sample boundary by calling its [- supportsCounterSampling:](<mtldevice/supportscountersampling(__).md>) method with each [MTLCounterSamplingPoint](mtlcountersamplingpoint.md) case.

**Swift**

```swift
func samplingBoundariesFor(_ device: MTLDevice) -> [MTLCounterSamplingPoint] {
    let boundaryNames = ["atStageBoundary",
                         "atDrawBoundary",
                         "atBlitBoundary",
                         "atDispatchBoundary",
                         "atTileDispatchBoundary"]

    let allBoundaries: [MTLCounterSamplingPoint] = [.atStageBoundary,
                                                   .atDrawBoundary,
                                                   .atBlitBoundary,
                                                   .atDispatchBoundary,
                                                   .atTileDispatchBoundary]

    print("The GPU device supports the following sampling boundary/ies: [", terminator: "")
    var boundaries = [MTLCounterSamplingPoint]()

    for index in 0..<boundaryNames.count {
        let boundary = allBoundaries[index]
        if device.supportsCounterSampling(boundary) {
            if boundaries.count >= 1 {
                // Prefix the boundary's name with a comma and a space.
                print(", ", terminator: "")
            }

            // Print the boundary's name.
            print("\(boundaryNames[index])", terminator: "")

            // Add the boundary to the return-value array.
            boundaries.append(boundary)
        }
    }

    // Finish printing the line that lists the boundaries the GPU device supports.
    // Example: "The GPU device supports the following sampling boundaries: [atStageBoundary]"
    print("]")

    return boundaries
}
```

**Objective-C**

```objective-c
+ (NSArray<NSNumber*>*) samplingBoundariesFor:(id<MTLDevice>)device
{
    NSArray<NSString*>* boundaryNames = @[@"atStageBoundary",
                                          @"atDrawBoundary",
                                          @"atBlitBoundary",
                                          @"atDispatchBoundary",
                                          @"atTileDispatchBoundary"];

    NSUInteger allBoundaries[] = {
        MTLCounterSamplingPointAtStageBoundary,
        MTLCounterSamplingPointAtDrawBoundary,
        MTLCounterSamplingPointAtBlitBoundary,
        MTLCounterSamplingPointAtDispatchBoundary,
        MTLCounterSamplingPointAtTileDispatchBoundary};

    printf("The GPU device supports the following sampling boundary/ies: [");

    NSMutableArray<NSNumber*>* boundaries = [[NSMutableArray<NSNumber*> alloc] init];

    for (int index = 0; index < boundaryNames.count; index++) {
        if ([device supportsCounterSampling:allBoundaries[index]]) {
            if (boundaries.count >= 1) {
                // Prefix the boundary's name with a comma and a space.
                printf(", ");
            }

            // Print the boundary's name.
            printf("%s", boundaryNames[index].UTF8String);

            // Add the boundary to the return-value array.
            NSNumber* boundaryNumber = [NSNumber numberWithUnsignedLong:allBoundaries[index]];
            [boundaries addObject: boundaryNumber];
        }
    }

    // Finish printing the line that lists the boundaries the GPU device supports.
    // Example: "The GPU device supports these sampling boundaries: [atStageBoundary]"
    printf("]\n");

    return boundaries;
}
```

This method checks for multiple sample boundaries and returns those the GPU supports in an array.

### Sample counters at stage boundaries

For a GPU device that can sample counters at stage boundaries ( [MTLCounterSamplingPointAtStageBoundary](mtlcountersamplingpoint/atstageboundary.md)), you can sample its counters between the stages of a pass. When the GPU starts or finishes a stage, it samples the counters and copies the results into a counter sample buffer.

> [!note] Note
> By default, a pass doesn’t sample any GPU counters.

You tell the GPU which counters to sample by configuring a pass descriptor’s [sampleBufferAttachments](mtlcomputepassdescriptor/samplebufferattachments.md) property. For example, you can sample the timestamp counters before and after the vertex and fragment stages by configuring an [MTLRenderPassDescriptor](mtlrenderpassdescriptor.md) instance’s [sampleBufferAttachments](mtlrenderpassdescriptor/samplebufferattachments.md) property.

**Swift**

```swift
func configureRenderPass(_ renderPass: MTLRenderPassDescriptor, attachmentIndex: Int = 0) {
    guard let sampleAttachment = renderPass.sampleBufferAttachments[attachmentIndex] else {
        return
    }

    sampleAttachment.sampleBuffer = self.counterSampleBuffer
    sampleAttachment.startOfVertexSampleIndex = 0
    sampleAttachment.endOfVertexSampleIndex = 1
    sampleAttachment.startOfFragmentSampleIndex = 2
    sampleAttachment.endOfFragmentSampleIndex = 3
}
```

**Objective-C**

```objective-c
- (void) configureRenderPass:(MTLRenderPassDescriptor *)renderPass
             attachmentIndex: (int)index
{
    MTLRenderPassSampleBufferAttachmentDescriptor *sampleAttachment;
    sampleAttachment = renderPass.sampleBufferAttachments[index];

    sampleAttachment.sampleBuffer = self.counterSampleBuffer;
    sampleAttachment.startOfVertexSampleIndex = 0;
    sampleAttachment.endOfVertexSampleIndex = 1;
    sampleAttachment.startOfFragmentSampleIndex = 2;
    sampleAttachment.endOfFragmentSampleIndex = 3;
}
```

Each index value tells the GPU where to put a specific counter value within a counter sample buffer. You can skip specific counters by setting an index to [MTLCounterDontSample](mtlcounterdontsample.md). For example, you can alter the code example above so that the GPU only samples before and after a fragment stage.

```swift
    ...
    sampleAttachment.sampleBuffer = self.counterSampleBuffer;
    sampleAttachment.startOfVertexSampleIndex = MTLCounterDontSample;
    sampleAttachment.endOfVertexSampleIndex = MTLCounterDontSample;
    sampleAttachment.startOfFragmentSampleIndex = 2;
    sampleAttachment.endOfFragmentSampleIndex = 3;
}
```

This example still stores the fragment counter data in the third and fourth positions within the counter sample buffer (at indexes 2 and 3, respectively). However, it doesn’t sample the vertex stage timestamps, which leaves that part of the counter sample buffer unaltered.

Each type of pass has different boundary types and corresponding properties in their descriptor types.

| Pass descriptor type | Attachment type | Attachment descriptor properties |
|---|---|---|
| [MTLRenderPassDescriptor](mtlrenderpassdescriptor.md) | [MTLRenderPassSampleBufferAttachmentDescriptor](mtlrenderpasssamplebufferattachmentdescriptor.md) | [sampleBuffer](mtlrenderpasssamplebufferattachmentdescriptor/samplebuffer.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [startOfVertexSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/startofvertexsampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfVertexSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/endofvertexsampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [startOfFragmentSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/startoffragmentsampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfFragmentSampleIndex](mtlrenderpasssamplebufferattachmentdescriptor/endoffragmentsampleindex.md) |
| [MTLAccelerationStructurePassDescriptor](mtlaccelerationstructurepassdescriptor.md) | [MTLAccelerationStructurePassSampleBufferAttachmentDescriptor](mtlaccelerationstructurepasssamplebufferattachmentdescriptor.md) | [sampleBuffer](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/samplebuffer.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [startOfEncoderSampleIndex](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfEncoderSampleIndex](mtlaccelerationstructurepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [MTLComputePassDescriptor](mtlcomputepassdescriptor.md) | [MTLComputePassSampleBufferAttachmentDescriptor](mtlcomputepasssamplebufferattachmentdescriptor.md) | [sampleBuffer](mtlcomputepasssamplebufferattachmentdescriptor/samplebuffer.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [startOfEncoderSampleIndex](mtlcomputepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfEncoderSampleIndex](mtlcomputepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [MTLBlitPassDescriptor](mtlblitpassdescriptor.md) | [MTLBlitPassSampleBufferAttachmentDescriptor](mtlblitpasssamplebufferattachmentdescriptor.md) | [sampleBuffer](mtlblitpasssamplebufferattachmentdescriptor/samplebuffer.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [startOfEncoderSampleIndex](mtlblitpasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfEncoderSampleIndex](mtlblitpasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |
| [MTLResourceStatePassDescriptor](mtlresourcestatepassdescriptor.md) | [MTLResourceStatePassSampleBufferAttachmentDescriptor](mtlresourcestatepasssamplebufferattachmentdescriptor.md) | [sampleBuffer](mtlresourcestatepasssamplebufferattachmentdescriptor/samplebuffer.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [startOfEncoderSampleIndex](mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [endOfEncoderSampleIndex](mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) |

### Sample counters at command boundaries

You can encode specific commands to sample a counter’s data during a pass for a GPU that supports any of the following boundaries:

- [MTLCounterSamplingPointAtDrawBoundary](mtlcountersamplingpoint/atdrawboundary.md)
- [MTLCounterSamplingPointAtDispatchBoundary](mtlcountersamplingpoint/atdispatchboundary.md)
- [MTLCounterSamplingPointAtBlitBoundary](mtlcountersamplingpoint/atblitboundary.md)
- [MTLCounterSamplingPointAtTileDispatchBoundary](mtlcountersamplingpoint/attiledispatchboundary.md)

You do this by calling an encoder’s [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlrendercommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) method.

**Swift**

```swift
renderEncoder.drawPrimitives(type: .triangle, vertexStart: 0, vertexCount: 6)

...

// Store the GPU counter data in the sample buffer.
renderEncoder.sampleCounters(sampleBuffer: self.counterSampleBuffer,
                             sampleIndex: 0,
                             barrier: false)

...

renderEncoder.drawPrimitives(type: .triangle,
                             vertexStart: entity.offset,
                             vertexCount: entity.count)
```

**Objective-C**

```objective-c
[renderEncoder drawPrimitives:MTLPrimitiveTypeTriangle
                  vertexStart:0
                  vertexCount: 6];

...

// Store the GPU counter data in the sample buffer.
[renderEncoder sampleCountersInBuffer: self.counterSampleBuffer
                        atSampleIndex: 0
                          withBarrier: NO];

...

[renderEncoder drawPrimitives: MTLPrimitiveTypeTriangle
                  vertexStart: entity.start
                  vertexCount: entity.count];
```

The code example above encodes a sample command between two draw commands. When the GPU reaches the sample command, it samples the counters and copies the results into a counter sample buffer.

Each pass encoder type has its own version of the method.

| Pass encoder type | Sample method |
|---|---|
| [MTLRenderCommandEncoder](mtlrendercommandencoder.md) | [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlrendercommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) |
| [MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md) | [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlaccelerationstructurecommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) |
| [MTLComputeCommandEncoder](mtlcomputecommandencoder.md) | [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlcomputecommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) |
| [MTLBlitCommandEncoder](mtlblitcommandencoder.md) | [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<mtlblitcommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) |

The `barrier` parameter for these methods controls whether the pass waits for the GPU to complete all the previous commands in the buffer before sampling the counters (see [Resource synchronization](resource-synchronization.md)). Each barrier typically reduces performance, but can be useful during development to get accurate and consistent data across multiple runs.

## See Also

### Counter sample buffers

- [Creating a counter sample buffer to store a GPU’s counter data during a pass](creating-a-counter-sample-buffer-to-store-a-gpus-counter-data-during-a-pass.md) — Make a buffer that provides a place for a GPU to save its runtime performance metrics as it runs a pass.
- [MTLCounterSampleBufferDescriptor](mtlcountersamplebufferdescriptor.md) — A group of properties that configures the counter sample buffers you create with it.
- [MTLCounterSampleBuffer](mtlcountersamplebuffer.md) — A specialized memory buffer that stores a GPU’s counter set data.
- [MTLCounterDontSample](mtlcounterdontsample.md) — A sentinel value that instructs an encoder to skip sampling a counter as the GPU runs the encoder’s pass.
