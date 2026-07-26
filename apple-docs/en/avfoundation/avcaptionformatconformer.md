---
title: AVCaptionFormatConformer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionformatconformer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionformatconformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionformatconformer.json'
content_hash: 'sha256:ded9a96d4c39a416'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionFormatConformer

<sub>Class</sub>

An object that converts a canonical caption to a specific format.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaptionFormatConformer
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a format conformer

- [- initWithConversionSettings:](<avcaptionformatconformer/init(conversionsettings_).md>) — Creates a new object with format conversion settings.

### Conforming captions

- [conformsCaptionsToTimeRange](avcaptionformatconformer/conformscaptionstotimerange.md) — A Boolean value that indicates whether to conform the time range of a canonical caption.
- [- conformedCaptionForCaption:error:](<avcaptionformatconformer/conformedcaption(for_).md>) — Creates a caption that conforms to a specific format.

## See Also

### Conversion and validation

- [AVCaptionSettingsKey](avcaptionsettingskey.md) — A structure that defines dictionary keys to configure the caption converter and validator.
- [AVCaptionConversionValidator](avcaptionconversionvalidator.md) — An object that validates captions for a conversion operation.
