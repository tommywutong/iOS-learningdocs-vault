---
title: 'validateCaptionConversion(warningHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionconversionvalidator/validatecaptionconversion(warninghandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/validatecaptionconversion(warninghandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionvalidator/validatecaptionconversion%28warninghandler%3A%29.json'
content_hash: 'sha256:73ebe3434af6e903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionValidator](../avcaptionconversionvalidator.md)

# validateCaptionConversion(warningHandler:)

<sub>Instance Method</sub>

Validates the object’s captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func validateCaptionConversion(warningHandler handler: @escaping @Sendable (AVCaptionConversionWarning?) -> Void)
```

## Parameters

- `handler` — The callback the system invokes when it finishes validation.

## Discussion

When the object finishes validating and reports all warnings, it invokes the callback once with a value of `nil` for its warning parameter. When this occurs, the validator’s [status](status-swift.property.md) value changes to [AVCaptionConversionValidatorStatusCompleted](status-swift.enum/completed.md).

Stop an in-progress validation operation by calling [- stopValidating](<stopvalidating().md>).

> [!important] Important
> It’s only valid to call this method when the validator’s state is [AVCaptionConversionValidatorStatusUnknown](status-swift.enum/unknown.md).

## See Also

### Validating captions

- [warnings](warnings.md) — The collection of warnings the validator encountered.
- [AVCaptionConversionWarning](../avcaptionconversionwarning.md) — An object that represents a conversion warning produced by a validator.
- [- stopValidating](<stopvalidating().md>) — Stops the active validation operation.
