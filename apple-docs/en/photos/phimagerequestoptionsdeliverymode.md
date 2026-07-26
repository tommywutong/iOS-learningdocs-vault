---
title: PHImageRequestOptionsDeliveryMode
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsdeliverymode
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsdeliverymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsdeliverymode.json'
content_hash: 'sha256:337e78588ec8e084'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageRequestOptionsDeliveryMode

<sub>Enumeration</sub>

Options for delivering requested image data, used by the [deliveryMode](phimagerequestoptions/deliverymode.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHImageRequestOptionsDeliveryMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHImageRequestOptionsDeliveryModeOpportunistic](phimagerequestoptionsdeliverymode/opportunistic.md) — Photos automatically provides one or more results in order to balance image quality and responsiveness.
- [PHImageRequestOptionsDeliveryModeHighQualityFormat](phimagerequestoptionsdeliverymode/highqualityformat.md) — Photos provides only the highest-quality image available, regardless of how much time it takes to load.
- [PHImageRequestOptionsDeliveryModeFastFormat](phimagerequestoptionsdeliverymode/fastformat.md) — Photos provides only a fast-loading image, possibly sacrificing image quality.

### Initializers

- [init(rawValue:)](<phimagerequestoptionsdeliverymode/init(rawvalue_).md>)

## See Also

### Specifying Image Request Options

- [version](phimagerequestoptions/version.md) — The version of the image to be requested.
- [PHImageRequestOptionsVersion](phimagerequestoptionsversion.md) — Options for requesting an image asset with or without adjustments, used by the [version](phimagerequestoptions/version.md) property.
- [deliveryMode](phimagerequestoptions/deliverymode.md) — The requested image quality and delivery priority.
- [resizeMode](phimagerequestoptions/resizemode.md) — A mode that specifies how to resize the requested image.
- [PHImageRequestOptionsResizeMode](phimagerequestoptionsresizemode.md) — Options for how to resize the requested image to fit a target size, used by the [resizeMode](phimagerequestoptions/resizemode.md) property.
- [normalizedCropRect](phimagerequestoptions/normalizedcroprect.md) — A rectangle for requesting a cropped version of the original image.
