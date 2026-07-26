---
title: AVCaptionConversionValidator.Status
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionvalidator/status-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionvalidator/status-swift.enum.json'
content_hash: 'sha256:5037bbed62a35331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionValidator](../avcaptionconversionvalidator.md)

# AVCaptionConversionValidator.Status

<sub>Enumeration</sub>

Constants that indicate the status of a validator.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Validation statuses

- [AVCaptionConversionValidatorStatusUnknown](status-swift.enum/unknown.md) — A status that indicates the system didn’t initialize the validation operation.
- [AVCaptionConversionValidatorStatusValidating](status-swift.enum/validating.md) — A status that indicates the system validation is in progress.
- [AVCaptionConversionValidatorStatusCompleted](status-swift.enum/completed.md) — A status that indicates the system validation is complete.
- [AVCaptionConversionValidatorStatusStopped](status-swift.enum/stopped.md) — A status that indicates the system validation stopped prior to completion.

### Initializers

- [init(rawValue:)](<status-swift.enum/init(rawvalue_).md>)

## See Also

### Checking the status

- [status](status-swift.property.md) — A value that indicates the status of validation.
