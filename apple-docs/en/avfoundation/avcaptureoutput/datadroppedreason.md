---
title: AVCaptureOutput.DataDroppedReason
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureoutput/datadroppedreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureoutput/datadroppedreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureoutput/datadroppedreason.json'
content_hash: 'sha256:562d30006c935ad0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureOutput](../avcaptureoutput.md)

# AVCaptureOutput.DataDroppedReason

<sub>Enumeration</sub>

Constants that define reasons for why the system dropped a frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum DataDroppedReason
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Reasons

- [AVCaptureOutputDataDroppedReasonNone](datadroppedreason/none.md) — The system didn’t drop data.
- [AVCaptureOutputDataDroppedReasonLateData](datadroppedreason/latedata.md) — The system dropped data because you’ve configured capture output to drop data when delegate queue is in a blocked state, and there’s data to deliver.
- [AVCaptureOutputDataDroppedReasonOutOfBuffers](datadroppedreason/outofbuffers.md) — The system dropped data because the capture output exhausted its internal pool of memory buffers.
- [AVCaptureOutputDataDroppedReasonDiscontinuity](datadroppedreason/discontinuity.md) — The system dropped data because the device providing data experienced a discontinuity, and the output lost an unknown number of data objects.

### Initializers

- [init(rawValue:)](<datadroppedreason/init(rawvalue_).md>)

## See Also

### Accessing connections

- [connections](connections.md) — The capture output object’s connections.
- [- connectionWithMediaType:](<connection(with_).md>) — Returns the first connection with an input port of a specified media type.
