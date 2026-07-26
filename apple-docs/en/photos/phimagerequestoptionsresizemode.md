---
title: PHImageRequestOptionsResizeMode
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsresizemode
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsresizemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsresizemode.json'
content_hash: 'sha256:b2a7782d498236d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageRequestOptionsResizeMode

<sub>Enumeration</sub>

Options for how to resize the requested image to fit a target size, used by the [resizeMode](phimagerequestoptions/resizemode.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHImageRequestOptionsResizeMode
```

## Overview

Specify a `targetSize` parameter when you request an image with the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHImageRequestOptionsResizeModeNone](phimagerequestoptionsresizemode/none.md) — Photos does not resize the image asset.
- [PHImageRequestOptionsResizeModeFast](phimagerequestoptionsresizemode/fast.md) — Photos efficiently resizes the image to a size similar to, or slightly larger than, the target size.
- [PHImageRequestOptionsResizeModeExact](phimagerequestoptionsresizemode/exact.md) — Photos resizes the image to match the target size exactly.

### Initializers

- [init(rawValue:)](<phimagerequestoptionsresizemode/init(rawvalue_).md>)

## See Also

### Specifying Image Request Options

- [version](phimagerequestoptions/version.md) — The version of the image to be requested.
- [PHImageRequestOptionsVersion](phimagerequestoptionsversion.md) — Options for requesting an image asset with or without adjustments, used by the [version](phimagerequestoptions/version.md) property.
- [deliveryMode](phimagerequestoptions/deliverymode.md) — The requested image quality and delivery priority.
- [PHImageRequestOptionsDeliveryMode](phimagerequestoptionsdeliverymode.md) — Options for delivering requested image data, used by the [deliveryMode](phimagerequestoptions/deliverymode.md) property.
- [resizeMode](phimagerequestoptions/resizemode.md) — A mode that specifies how to resize the requested image.
- [normalizedCropRect](phimagerequestoptions/normalizedcroprect.md) — A rectangle for requesting a cropped version of the original image.
