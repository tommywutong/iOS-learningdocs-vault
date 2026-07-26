---
title: 'finish(with:context:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasynchronousciimagefilteringrequest/finish(with:context:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/finish(with:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousciimagefilteringrequest/finish%28with%3Acontext%3A%29.json'
content_hash: 'sha256:b85687a6d50b56e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md)

# finish(with:context:)

<sub>Instance Method</sub>

Provides the filtered video frame image to AVFoundation for further processing or display.

> [!warning] Deprecated
> Use AVCIImageFilteringParameters instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finish(with filteredImage: CIImage, context: CIContext?)
```

## Parameters

- `filteredImage` — A Core Image image representing the output of whatever filters you’ve applied to the source image.

- `context` — A Core Image context to be used for rendering the output image, or `nil` to use a default context provided by AVFoundation.

## Discussion

Call this method when your handler block has finished applying filters, passing the [outputImage](../../coreimage/cifilter-swift.class/outputimage.md) object from the final filter in your filter chain for the `filteredImage` parameter. The pixel format for this image must be the [BGRA8](../../coreimage/ciformat/bgra8.md) format (of the [kCVPixelFormatType_32BGRA](../../corevideo/kcvpixelformattype_32bgra.md) type).

You can pass the [sourceImage](sourceimage.md) object to the `filteredImage` parameter to disable filtering for the current frame.

By default, you can pass `nil` for the `context` parameter to use a default rendering context provided by Core Image. In iOS and tvOS, the default context uses the Device RGB color space. In macOS, the default context uses the sRGB color space. AVFoundation automatically uses a GPU-accelerated context if possible. To use a different color space or control other rendering options, pass your own [CIContext](../../coreimage/cicontext.md) object instead.

> [!important] Important
> A [CIContext](../../coreimage/cicontext.md) instance is a heavyweight object that maintains expensive rendering state. Don’t create a new context object in the block where you call this method (which runs once per video frame); instead, create a [CIContext](../../coreimage/cicontext.md) instance before create a composition with the [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<../avvideocomposition/init(asset_applyingcifilterswithhandler_).md>) method, and use that instance in your handler block.

## See Also

### Returning the filtered image

- [- finishWithError:](<finish(with_).md>) — Notifies AVFoundation that you cannot fulfill the image filtering request. _(deprecated)_
