---
title: stopValidating()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionvalidator/stopvalidating()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/stopvalidating()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionvalidator/stopvalidating%28%29.json'
content_hash: 'sha256:c3bfd20772cd5bc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionValidator](../avcaptionconversionvalidator.md)

# stopValidating()

<sub>Instance Method</sub>

Stops the active validation operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func stopValidating()
```

## Discussion

You can call this method at any time, even within the validator’s callback to its handler.

Calling this method stops validation and changes the [status](status-swift.property.md) value to [AVCaptionConversionValidatorStatusStopped](status-swift.enum/stopped.md).

## See Also

### Validating captions

- [- validateCaptionConversionWithWarningHandler:](<validatecaptionconversion(warninghandler_).md>) — Validates the object’s captions.
- [warnings](warnings.md) — The collection of warnings the validator encountered.
- [AVCaptionConversionWarning](../avcaptionconversionwarning.md) — An object that represents a conversion warning produced by a validator.
