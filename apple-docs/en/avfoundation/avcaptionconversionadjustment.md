---
title: AVCaptionConversionAdjustment
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionadjustment
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionadjustment.json'
content_hash: 'sha256:150fd819f1092fe2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionConversionAdjustment

<sub>Class</sub>

An object that describes an adjustment to correct a problem found during validation of a caption conversion.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaptionConversionAdjustment
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVCaptionConversionTimeRangeAdjustment](avcaptionconversiontimerangeadjustment.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the adjustment type

- [adjustmentType](avcaptionconversionadjustment/adjustmenttype-swift.property.md) — The type of caption conversion adjustment.
- [AdjustmentType](avcaptionconversionadjustment/adjustmenttype-swift.struct.md) — Constants that indicate an adjustment type.
- [AVCaptionConversionTimeRangeAdjustment](avcaptionconversiontimerangeadjustment.md) — An object that describes an adjustment to the time range of one or more captions.

## See Also

### Inspecting the warning

- [warningType](avcaptionconversionwarning/warningtype-swift.property.md) — A type that indicates the nature of the validation warning.
- [rangeOfCaptions](avcaptionconversionwarning/rangeofcaptions.md) — The range of the captions for which the system issued a warning.
- [adjustment](avcaptionconversionwarning/adjustment.md) — A correction the converter makes when it converts a caption to a specific format.
- [WarningType](avcaptionconversionwarning/warningtype-swift.struct.md) — The type of a caption conversion warning.
