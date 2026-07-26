---
title: 'applyingExifOrientation(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avportraiteffectsmatte/applyingexiforientation(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/applyingexiforientation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avportraiteffectsmatte/applyingexiforientation%28_%3A%29.json'
content_hash: 'sha256:d9733067db87455b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPortraitEffectsMatte](../avportraiteffectsmatte.md)

# applyingExifOrientation(_:)

<sub>Instance Method</sub>

Returns a derivative portrait effects matte after applying the specified EXIF orientation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applyingExifOrientation(_ exifOrientation: CGImagePropertyOrientation) -> Self
```

## Parameters

- `exifOrientation` — One of the standard EXIF orientation tags expressing how the portrait effects matte should be rotated or mirrored.

## See Also

### Creating a Portrait Effects matte

- [Configuring camera capture to collect a Portrait Effects matte](../configuring-camera-capture-to-collect-a-portrait-effects-matte.md) — Prepare your app to capture a portrait effects matte when taking photos.
- [+ portraitEffectsMatteFromDictionaryRepresentation:error:](<init(fromdictionaryrepresentation_).md>) — Initializes a portrait effects matte instance from auxiliary image information in an image file.
- [- portraitEffectsMatteByReplacingPortraitEffectsMatteWithPixelBuffer:error:](<replacingportraiteffectsmatte(with_).md>) — Returns a portrait effects matte by wrapping the replacement pixel buffer.
