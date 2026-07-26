---
title: colorBurn
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciblendkernel/colorburn
source_url: 'https://developer.apple.com/documentation/coreimage/ciblendkernel/colorburn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciblendkernel/colorburn.json'
content_hash: 'sha256:1f2e651e868fae03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIBlendKernel](../ciblendkernel.md)

# colorBurn

<sub>Type Property</sub>

A blend kernel that darkens the background image samples to reflect the foreground image samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class var colorBurn: CIBlendKernel { get }
```

## Discussion

![The result of using the color burn blend kernel (background image is top left, foreground image is bottom left)](../../../../attachments/35d3cf3428c2e2280c4a80e5df08c8c5/media-2926850@2x.png)

## See Also

### Builtin Blend Kernels

- [clear](clear.md) — A blend kernel that returns a clear color.
- [color](color.md) — A blend kernel that uses the luminance values of the background with the hue and saturation values of the foreground image.
- [colorDodge](colordodge.md) — A blend kernel that brightens the background image samples to reflect the foreground image samples.
- [componentAdd](componentadd.md) — A blend kernel that adds color components to achieve a brightening effect.
- [componentMax](componentmax.md) — A blend kernel that creates an image using the maximum values of two input images.
- [componentMin](componentmin.md) — A blend kernel that creates an image using the minimum values of two input images.
- [componentMultiply](componentmultiply.md) — A blend kernel that multiplies the color components of its input images.
- [darken](darken.md) — A blend kernel that creates an image using the darker values of two input images.
- [darkerColor](darkercolor.md) — A blend kernel that creates an image using the darker color of two input images.
- [destination](destination.md) — A blend kernel that returns the background input image.
- [destinationAtop](destinationatop.md) — A blend kernel that places the background over the foreground and crops based on the visibility of the foreground.
- [destinationIn](destinationin.md) — A blend kernel that places the background over the foreground and crops based on the visibility of both.
- [destinationOut](destinationout.md) — A blend kernel that uses the background image to define what to take out of the foreground image.
- [destinationOver](destinationover.md) — A blend kernel that places the background image over the input foreground image.
- [difference](difference.md) — A blend kernel that creates an image using the difference between the background and foreground images.
