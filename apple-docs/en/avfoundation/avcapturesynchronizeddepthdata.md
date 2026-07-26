---
title: AVCaptureSynchronizedDepthData
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizeddepthdata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddepthdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizeddepthdata.json'
content_hash: 'sha256:ee010e7a49018660'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSynchronizedDepthData

<sub>Class</sub>

A container for scene depth information collected using synchronized capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCaptureSynchronizedDepthData
```

## Relationships

- **Inherits From**: [AVCaptureSynchronizedData](avcapturesynchronizeddata.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing synchronized data

- [depthData](avcapturesynchronizeddepthdata/depthdata.md) — The depth data captured at this synchronization point.

### Handling dropped data

- [depthDataWasDropped](avcapturesynchronizeddepthdata/depthdatawasdropped.md) — A Boolean value indicating whether depth data was discarded between capture and processing.
- [droppedReason](avcapturesynchronizeddepthdata/droppedreason.md) — A value indicating why the capture output failed to deliver depth data, if applicable.

## See Also

### Synchronized capture

- [AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md) — An object that coordinates time-matched delivery of data from multiple capture outputs.
- [AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md) — A set of data samples collected simultaneously from multiple capture outputs.
- [AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md) — A container for video or audio samples collected using synchronized capture.
- [AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md) — A container for metadata objects collected using synchronized capture.
- [AVCaptureSynchronizedData](avcapturesynchronizeddata.md) — The abstract superclass for media samples collected using synchronized capture.
