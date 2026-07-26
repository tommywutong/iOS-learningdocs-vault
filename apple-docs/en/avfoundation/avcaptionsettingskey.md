---
title: AVCaptionSettingsKey
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionsettingskey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionsettingskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionsettingskey.json'
content_hash: 'sha256:b8ab17f031266947'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionSettingsKey

<sub>Structure</sub>

A structure that defines dictionary keys to configure the caption converter and validator.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
struct AVCaptionSettingsKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Keys

- [AVCaptionMediaTypeKey](avcaptionsettingskey/mediatype.md) — A key that identifies the output media type of a caption conversion operation.
- [AVCaptionMediaSubTypeKey](avcaptionsettingskey/mediasubtype.md) — A key that identifies the output media subtype of a caption conversion operation.
- [AVCaptionTimeCodeFrameDurationKey](avcaptionsettingskey/timecodeframeduration.md) — A key that identifies the frame duration that the system uses for the time code.
- [AVCaptionUseDropFrameTimeCodeKey](avcaptionsettingskey/usedropframetimecode.md) — A key that identifies whether the system uses drop frame time code.

### Initializers

- [init(rawValue:)](<avcaptionsettingskey/init(rawvalue_).md>) — Creates a settings key with a string.

## See Also

### Conversion and validation

- [AVCaptionFormatConformer](avcaptionformatconformer.md) — An object that converts a canonical caption to a specific format.
- [AVCaptionConversionValidator](avcaptionconversionvalidator.md) — An object that validates captions for a conversion operation.
