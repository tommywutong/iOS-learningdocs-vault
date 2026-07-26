---
title: AVCaptionConversionWarning
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionwarning
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionwarning.json'
content_hash: 'sha256:80a762ae4192114f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionConversionWarning

<sub>Class</sub>

An object that represents a conversion warning produced by a validator.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaptionConversionWarning
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the warning

- [warningType](avcaptionconversionwarning/warningtype-swift.property.md) — A type that indicates the nature of the validation warning.
- [rangeOfCaptions](avcaptionconversionwarning/rangeofcaptions.md) — The range of the captions for which the system issued a warning.
- [adjustment](avcaptionconversionwarning/adjustment.md) — A correction the converter makes when it converts a caption to a specific format.
- [AVCaptionConversionAdjustment](avcaptionconversionadjustment.md) — An object that describes an adjustment to correct a problem found during validation of a caption conversion.
- [WarningType](avcaptionconversionwarning/warningtype-swift.struct.md) — The type of a caption conversion warning.

## See Also

### Validating captions

- [- validateCaptionConversionWithWarningHandler:](<avcaptionconversionvalidator/validatecaptionconversion(warninghandler_).md>) — Validates the object’s captions.
- [warnings](avcaptionconversionvalidator/warnings.md) — The collection of warnings the validator encountered.
- [- stopValidating](<avcaptionconversionvalidator/stopvalidating().md>) — Stops the active validation operation.
