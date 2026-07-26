---
title: AVCaptureSynchronizedDataCollection
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizeddatacollection
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddatacollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizeddatacollection.json'
content_hash: 'sha256:1d06cc2dbdab66e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSynchronizedDataCollection

<sub>Class</sub>

A set of data samples collected simultaneously from multiple capture outputs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCaptureSynchronizedDataCollection
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSFastEnumeration](../foundation/nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sequence](../swift/sequence.md)

## Topics

### Accessing synchronized data

- [count](avcapturesynchronizeddatacollection/count.md) — The number of synchronized data objects in the collection.
- [- synchronizedDataForCaptureOutput:](<avcapturesynchronizeddatacollection/synchronizeddata(for_).md>) — Returns synchronized data captured by the specified capture output.
- [- objectForKeyedSubscript:](<avcapturesynchronizeddatacollection/subscript(__).md>) — Returns data captured by the specified capture output, using subscript syntax.

## See Also

### Synchronized capture

- [AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md) — An object that coordinates time-matched delivery of data from multiple capture outputs.
- [AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md) — A container for video or audio samples collected using synchronized capture.
- [AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md) — A container for metadata objects collected using synchronized capture.
- [AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md) — A container for scene depth information collected using synchronized capture.
- [AVCaptureSynchronizedData](avcapturesynchronizeddata.md) — The abstract superclass for media samples collected using synchronized capture.
