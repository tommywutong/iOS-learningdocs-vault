---
title: AVCaptionConversionTimeRangeAdjustment
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversiontimerangeadjustment
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversiontimerangeadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversiontimerangeadjustment.json'
content_hash: 'sha256:beb8f5bd55589b11'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionConversionTimeRangeAdjustment

<sub>Class</sub>

An object that describes an adjustment to the time range of one or more captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaptionConversionTimeRangeAdjustment
```

## Relationships

- **Inherits From**: [AVCaptionConversionAdjustment](avcaptionconversionadjustment.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing time offsets

- [startTimeOffset](avcaptionconversiontimerangeadjustment/starttimeoffset.md) — The time value by which the system offsets the start times of captions to correct a problem.
- [durationOffset](avcaptionconversiontimerangeadjustment/durationoffset.md) — The time value by which the system offsets the durations of captions to correct a problem.

## See Also

### Accessing the adjustment type

- [adjustmentType](avcaptionconversionadjustment/adjustmenttype-swift.property.md) — The type of caption conversion adjustment.
- [AdjustmentType](avcaptionconversionadjustment/adjustmenttype-swift.struct.md) — Constants that indicate an adjustment type.
