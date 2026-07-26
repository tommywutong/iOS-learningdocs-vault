---
title: UIImage.RenderingMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/renderingmode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/renderingmode-swift.enum.json'
content_hash: 'sha256:4e7a199a75501f92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# UIImage.RenderingMode

<sub>Enumeration</sub>

Constants that specify the possible rendering modes for an image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum RenderingMode
```

## Overview

The rendering mode controls how UIKit uses color information to display an image. See [Providing images for different appearances](../providing-images-for-different-appearances.md) for creating tintable images with template mode.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Rendering modes

- [UIImageRenderingModeAutomatic](renderingmode-swift.enum/automatic.md) — Draw the image using the context’s default rendering mode.
- [UIImageRenderingModeAlwaysOriginal](renderingmode-swift.enum/alwaysoriginal.md) — Always draw the original image, without treating it as a template.
- [UIImageRenderingModeAlwaysTemplate](renderingmode-swift.enum/alwaystemplate.md) — Always draw the image as a template image, ignoring its color information.

### Initializers

- [init(rawValue:)](<renderingmode-swift.enum/init(rawvalue_).md>)

## See Also

### Getting rendering information

- [renderingMode](renderingmode-swift.property.md) — A setting that determines how the app renders an image.
- [imageRendererFormat](imagerendererformat.md) — The preferred image renderer format for the image.
