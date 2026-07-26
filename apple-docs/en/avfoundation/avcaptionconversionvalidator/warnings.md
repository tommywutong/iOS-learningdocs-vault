---
title: warnings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionvalidator/warnings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/warnings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionvalidator/warnings.json'
content_hash: 'sha256:c54ff4f94b334784'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionValidator](../avcaptionconversionvalidator.md)

# warnings

<sub>Instance Property</sub>

The collection of warnings the validator encountered.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var warnings: [AVCaptionConversionWarning] { get }
```

## Discussion

This property value may change while the validator’s status is [AVCaptionConversionValidatorStatusValidating](status-swift.enum/validating.md).

## See Also

### Validating captions

- [- validateCaptionConversionWithWarningHandler:](<validatecaptionconversion(warninghandler_).md>) — Validates the object’s captions.
- [AVCaptionConversionWarning](../avcaptionconversionwarning.md) — An object that represents a conversion warning produced by a validator.
- [- stopValidating](<stopvalidating().md>) — Stops the active validation operation.
