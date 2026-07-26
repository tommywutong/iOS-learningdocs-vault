---
title: 'copy(colorSpace:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgimage/copy(colorspace:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimage/copy(colorspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimage/copy%28colorspace%3A%29.json'
content_hash: 'sha256:ac9d7064757777b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGImage](../cgimage.md)

# copy(colorSpace:)

<sub>Instance Method</sub>

Creates a copy of a bitmap image, replacing its colorspace.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy(colorSpace space: CGColorSpace) -> CGImage?
```

## Parameters

- `space` — The destination color space. The number of components in this color space must be the same as the number in the specified image.

## Return Value

A new CGImage that is a copy of the image passed as the `image` parameter but with its color space replaced by that specified by the `colorspace` parameter. Returns `NULL` if `image` is an image mask, or if the number of components of `colorspace` is not the same as the number of components of the colorspace of `image`. In Objective-C, you’re responsible for releasing this object using [CGImageRelease](../cgimagerelease.md).

## See Also

### Copying an image

- [CGImageCreateCopy](<copy().md>) — Creates a copy of a bitmap image.
