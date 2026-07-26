---
title: PHImageRequestOptionsVersion
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsversion
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsversion.json'
content_hash: 'sha256:24aa9ae3ed7db368'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageRequestOptionsVersion

<sub>Enumeration</sub>

Options for requesting an image asset with or without adjustments, used by the [version](phimagerequestoptions/version.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHImageRequestOptionsVersion
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHImageRequestOptionsVersionCurrent](phimagerequestoptionsversion/current.md) — Request the most recent version of the image asset (the one that reflects all edits).
- [PHImageRequestOptionsVersionUnadjusted](phimagerequestoptionsversion/unadjusted.md) — Request a version of the image asset without adjustments.
- [PHImageRequestOptionsVersionOriginal](phimagerequestoptionsversion/original.md) — Request the original, highest-fidelity version of the image asset.

### Initializers

- [init(rawValue:)](<phimagerequestoptionsversion/init(rawvalue_).md>)

## See Also

### Specifying Image Request Options

- [version](phimagerequestoptions/version.md) — The version of the image to be requested.
- [deliveryMode](phimagerequestoptions/deliverymode.md) — The requested image quality and delivery priority.
- [PHImageRequestOptionsDeliveryMode](phimagerequestoptionsdeliverymode.md) — Options for delivering requested image data, used by the [deliveryMode](phimagerequestoptions/deliverymode.md) property.
- [resizeMode](phimagerequestoptions/resizemode.md) — A mode that specifies how to resize the requested image.
- [PHImageRequestOptionsResizeMode](phimagerequestoptionsresizemode.md) — Options for how to resize the requested image to fit a target size, used by the [resizeMode](phimagerequestoptions/resizemode.md) property.
- [normalizedCropRect](phimagerequestoptions/normalizedcroprect.md) — A rectangle for requesting a cropped version of the original image.
