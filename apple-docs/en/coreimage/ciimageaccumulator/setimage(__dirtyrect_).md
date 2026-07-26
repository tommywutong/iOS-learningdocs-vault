---
title: 'setImage(_:dirtyRect:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimageaccumulator/setimage(_:dirtyrect:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageaccumulator/setimage(_:dirtyrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageaccumulator/setimage%28_%3Adirtyrect%3A%29.json'
content_hash: 'sha256:4dcd9596c67aa2c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAccumulator](../ciimageaccumulator.md)

# setImage(_:dirtyRect:)

<sub>Instance Method</sub>

Updates an image accumulator with a subregion of an image object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setImage(_ image: CIImage, dirtyRect: CGRect)
```

## Parameters

- `image` — The image object whose contents you want to assign to the image accumulator.

- `dirtyRect` — A rectangle that defines the subregion of the image object that’s changed since the last time you updated the image accumulator. You must guarantee that the new contents differ from the old only within the region specified by the this argument.

## Discussion

For additional details on using this method, see “Imaging Dynamical Systems” in [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## See Also

### Setting an Image

- [- setImage:](<setimage(__).md>) — Sets the contents of the image accumulator to the contents of the specified image object.
