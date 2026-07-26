---
title: PHImageContentMode
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagecontentmode
source_url: 'https://developer.apple.com/documentation/photos/phimagecontentmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagecontentmode.json'
content_hash: 'sha256:93a17bd2b47afa98'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageContentMode

<sub>Enumeration</sub>

Options for fitting an image’s aspect ratio to a requested size, used by the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHImageContentMode
```

## Overview

With either option, the resulting image may not exactly match the target size, depending on the [deliveryMode](phimagerequestoptions/deliverymode.md) and [resizeMode](phimagerequestoptions/resizemode.md) properties of the image request. To serve your request more quickly, Photos may provide a slightly larger image—one that it can generate more easily or one that is already cached.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHImageContentModeDefault](phimagecontentmode/default.md) — Fits the image to the requested size using the default option, [PHImageContentModeAspectFit](phimagecontentmode/aspectfit.md).
- [PHImageContentModeAspectFit](phimagecontentmode/aspectfit.md) — Scales the image so that its larger dimension fits the target size.
- [PHImageContentModeAspectFill](phimagecontentmode/aspectfill.md) — Scales the image so that it completely fills the target size.

### Initializers

- [init(rawValue:)](<phimagecontentmode/init(rawvalue_).md>)

## See Also

### Constants

- [Image Result Info Keys](../photokit/image-result-info-keys.md) — Keys identifying information about an image loading result, used in the `resultHandler` block with image request methods.
