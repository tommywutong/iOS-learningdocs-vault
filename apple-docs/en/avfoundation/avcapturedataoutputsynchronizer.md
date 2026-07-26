---
title: AVCaptureDataOutputSynchronizer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedataoutputsynchronizer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedataoutputsynchronizer.json'
content_hash: 'sha256:7491cf95606469e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureDataOutputSynchronizer

<sub>Class</sub>

An object that coordinates time-matched delivery of data from multiple capture outputs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCaptureDataOutputSynchronizer
```

## Overview

Use this class when you need to capture media from multiple capture outputs and want to receive all data samples from the same timestamp in a single delegate callback.

For example, when you use an [AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md) object to coordinate the output of [AVCaptureVideoDataOutput](avcapturevideodataoutput.md) and [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md) objects, you can easily match each captured video frame to depth information captured at the same moment.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring synchronized capture

- [- initWithDataOutputs:](<avcapturedataoutputsynchronizer/init(dataoutputs_).md>) — Creates a capture output synchronizer for the specified capture outputs.
- [dataOutputs](avcapturedataoutputsynchronizer/dataoutputs.md) — The list of data outputs governed by this data output synchronizer.

### Receiving synchronized capture data

- [- setDelegate:queue:](<avcapturedataoutputsynchronizer/setdelegate(__queue_).md>) — Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.
- [delegate](avcapturedataoutputsynchronizer/delegate.md) — A delegate object that receives synchronized capture data.
- [delegateCallbackQueue](avcapturedataoutputsynchronizer/delegatecallbackqueue.md) — A dispatch queue for delivering synchronized capture data.
- [AVCaptureDataOutputSynchronizerDelegate](avcapturedataoutputsynchronizerdelegate.md) — Methods for receiving captured data from multiple capture outputs synchronized to the same timestamp.

## See Also

### Synchronized capture

- [AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md) — A set of data samples collected simultaneously from multiple capture outputs.
- [AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md) — A container for video or audio samples collected using synchronized capture.
- [AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md) — A container for metadata objects collected using synchronized capture.
- [AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md) — A container for scene depth information collected using synchronized capture.
- [AVCaptureSynchronizedData](avcapturesynchronizeddata.md) — The abstract superclass for media samples collected using synchronized capture.
