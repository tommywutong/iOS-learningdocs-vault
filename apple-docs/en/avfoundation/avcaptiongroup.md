---
title: AVCaptionGroup
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptiongroup
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptiongroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptiongroup.json'
content_hash: 'sha256:a50ec41c1b1b63c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionGroup

<sub>Class</sub>

An object that represents zero or more captions that intersect in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaptionGroup
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [SupportedPayload](avassetreaderoutput/supportedpayload.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a caption group

- [- initWithTimeRange:](<avcaptiongroup/init(timerange_).md>) — Creates a caption group with a time range.
- [- initWithCaptions:timeRange:](<avcaptiongroup/init(captions_timerange_).md>) — Creates a caption group with captions and a time range.

### Inspecting the caption group

- [captions](avcaptiongroup/captions.md) — The captions associated with the caption group.
- [timeRange](avcaptiongroup/timerange.md) — The time range of the caption group.

## See Also

### Groups

- [AVCaptionGrouper](avcaptiongrouper.md) — An object that analyzes the temporal overlaps of caption objects to create caption groups for each span of concurrent captions.
