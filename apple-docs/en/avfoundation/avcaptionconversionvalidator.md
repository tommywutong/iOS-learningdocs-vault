---
title: AVCaptionConversionValidator
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionvalidator
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionvalidator.json'
content_hash: 'sha256:4a8354a6e9afea62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionConversionValidator

<sub>Class</sub>

An object that validates captions for a conversion operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaptionConversionValidator
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a validator

- [- initWithCaptions:timeRange:conversionSettings:](<avcaptionconversionvalidator/init(captions_timerange_conversionsettings_).md>) — Creates an object that validates captions for a conversion operation.

### Inspecting the validator

- [captions](avcaptionconversionvalidator/captions.md) — The array of captions that the system validates.
- [timeRange](avcaptionconversionvalidator/timerange.md) — The time range of the media timeline in which the captions must exist.

### Validating captions

- [- validateCaptionConversionWithWarningHandler:](<avcaptionconversionvalidator/validatecaptionconversion(warninghandler_).md>) — Validates the object’s captions.
- [warnings](avcaptionconversionvalidator/warnings.md) — The collection of warnings the validator encountered.
- [AVCaptionConversionWarning](avcaptionconversionwarning.md) — An object that represents a conversion warning produced by a validator.
- [- stopValidating](<avcaptionconversionvalidator/stopvalidating().md>) — Stops the active validation operation.

### Checking the status

- [status](avcaptionconversionvalidator/status-swift.property.md) — A value that indicates the status of validation.
- [Status](avcaptionconversionvalidator/status-swift.enum.md) — Constants that indicate the status of a validator.

## See Also

### Conversion and validation

- [AVCaptionSettingsKey](avcaptionsettingskey.md) — A structure that defines dictionary keys to configure the caption converter and validator.
- [AVCaptionFormatConformer](avcaptionformatconformer.md) — An object that converts a canonical caption to a specific format.
