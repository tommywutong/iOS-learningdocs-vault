---
title: 'replacingPortraitEffectsMatte(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avportraiteffectsmatte/replacingportraiteffectsmatte(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/replacingportraiteffectsmatte(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avportraiteffectsmatte/replacingportraiteffectsmatte%28with%3A%29.json'
content_hash: 'sha256:5b62199224eb891e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPortraitEffectsMatte](../avportraiteffectsmatte.md)

# replacingPortraitEffectsMatte(with:)

<sub>Instance Method</sub>

Returns a portrait effects matte by wrapping the replacement pixel buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacingPortraitEffectsMatte(with pixelBuffer: CVPixelBuffer) throws -> Self
```

## Parameters

- `pixelBuffer` — A pixel buffer containing a portrait effects matte image, represented as [kCVPixelFormatType_OneComponent8](../../corevideo/kcvpixelformattype_onecomponent8.md) with [kCVImageBufferColorPrimaries_ITU_R_709_2](../../corevideo/kcvimagebuffercolorprimaries_itu_r_709_2.md) color primaries and a [kCVImageBufferTransferFunction_Linear](../../corevideo/kcvimagebuffertransferfunction_linear.md) transfer function.

## See Also

### Creating a Portrait Effects matte

- [Configuring camera capture to collect a Portrait Effects matte](../configuring-camera-capture-to-collect-a-portrait-effects-matte.md) — Prepare your app to capture a portrait effects matte when taking photos.
- [+ portraitEffectsMatteFromDictionaryRepresentation:error:](<init(fromdictionaryrepresentation_).md>) — Initializes a portrait effects matte instance from auxiliary image information in an image file.
- [- portraitEffectsMatteByApplyingExifOrientation:](<applyingexiforientation(__).md>) — Returns a derivative portrait effects matte after applying the specified EXIF orientation.
