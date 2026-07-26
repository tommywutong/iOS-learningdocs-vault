---
title: AVCaptureSynchronizedData
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizeddata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizeddata.json'
content_hash: 'sha256:379da36e17140160'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSynchronizedData

<sub>Class</sub>

The abstract superclass for media samples collected using synchronized capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCaptureSynchronizedData
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md), [AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md), [AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Correlating synchronized data

- [timestamp](avcapturesynchronizeddata/timestamp.md) — The time at which this synchronized data was captured.

## See Also

### Synchronized capture

- [AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md) — An object that coordinates time-matched delivery of data from multiple capture outputs.
- [AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md) — A set of data samples collected simultaneously from multiple capture outputs.
- [AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md) — A container for video or audio samples collected using synchronized capture.
- [AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md) — A container for metadata objects collected using synchronized capture.
- [AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md) — A container for scene depth information collected using synchronized capture.
