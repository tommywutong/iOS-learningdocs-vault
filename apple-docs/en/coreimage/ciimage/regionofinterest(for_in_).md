---
title: 'regionOfInterest(for:in:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/regionofinterest(for:in:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/regionofinterest(for:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/regionofinterest%28for%3Ain%3A%29.json'
content_hash: 'sha256:e1bc2dc9d39137a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# regionOfInterest(for:in:)

<sub>Instance Method</sub>

Returns the region of interest for the filter chain that generates the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func regionOfInterest(for image: CIImage, in rect: CGRect) -> CGRect
```

## Parameters

- `image` — Another image that is part of the filter chain that generates the image.

- `rect` — A rectangle in the image’s coordinate space.

## Return Value

A rectangle in the coordinate space of the input image (the `im` parameter).

## Discussion

The region of interest is the rectangle containing pixel data in a source image (the `im` parameter) necessary to produce a corresponding rectangle in the output image. If the image is not the output of a filter (or of a chain or graph of several [CIFilter](../cifilter-swift.class.md) objects), or the image in the `im` parameter is not an input to that filter, the rectangle returned is the same as that in the `r` parameter.

For example,

- If the image is the output of a filter that doubles the size of its input image, the rectangle returned will be half the size of that in the `r` parameter. (Upscaling causes every pixel in the input image to correspond to multiple pixels in the output image.)
- If the image is the output of a blur filter, the rectangle returned will be slightly larger than that in the `r` parameter. (In a blur filter, each pixel in the output image is produced using information from the corresponding pixel and those immediately surrounding it in the input image.)
