---
title: AVCaptionConversionWarning.WarningType
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionwarning/warningtype-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning/warningtype-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionwarning/warningtype-swift.struct.json'
content_hash: 'sha256:445d8bc0634df76a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionWarning](../avcaptionconversionwarning.md)

# AVCaptionConversionWarning.WarningType

<sub>Structure</sub>

The type of a caption conversion warning.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
struct WarningType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Warning types

- [AVCaptionConversionWarningTypeExcessMediaData](warningtype-swift.struct/excessmediadata.md) — A type that indicates one or more captions exceed the media data capacity for media of the type and subtype that the conversion settings specify.

### Initializers

- [init(rawValue:)](<warningtype-swift.struct/init(rawvalue_).md>) — Creates a warning type with a string.

## See Also

### Inspecting the warning

- [warningType](warningtype-swift.property.md) — A type that indicates the nature of the validation warning.
- [rangeOfCaptions](rangeofcaptions.md) — The range of the captions for which the system issued a warning.
- [adjustment](adjustment.md) — A correction the converter makes when it converts a caption to a specific format.
- [AVCaptionConversionAdjustment](../avcaptionconversionadjustment.md) — An object that describes an adjustment to correct a problem found during validation of a caption conversion.
