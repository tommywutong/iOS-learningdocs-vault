---
title: 'init(fromDictionaryRepresentation:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avportraiteffectsmatte/init(fromdictionaryrepresentation:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/init(fromdictionaryrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avportraiteffectsmatte/init%28fromdictionaryrepresentation%3A%29.json'
content_hash: 'sha256:6c2c0795fb038c8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPortraitEffectsMatte](../avportraiteffectsmatte.md)

# init(fromDictionaryRepresentation:)

<sub>Initializer</sub>

Initializes a portrait effects matte instance from auxiliary image information in an image file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(fromDictionaryRepresentation imageSourceAuxDataInfoDictionary: [AnyHashable : Any]) throws
```

## Parameters

- `imageSourceAuxDataInfoDictionary` — A dictionary of information related to primitive portrait effects matte; obtained from [CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>).

## Discussion

When using the [Image I/O](../../imageio.md) API to read from a HEIF or JPEG file containing a portrait effects matte, you can create an [AVPortraitEffectsMatte](../avportraiteffectsmatte.md) object from the result of [CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>). This function returns a [CFDictionary](../../corefoundation/cfdictionary.md) of primitive map information.

## See Also

### Creating a Portrait Effects matte

- [Configuring camera capture to collect a Portrait Effects matte](../configuring-camera-capture-to-collect-a-portrait-effects-matte.md) — Prepare your app to capture a portrait effects matte when taking photos.
- [- portraitEffectsMatteByApplyingExifOrientation:](<applyingexiforientation(__).md>) — Returns a derivative portrait effects matte after applying the specified EXIF orientation.
- [- portraitEffectsMatteByReplacingPortraitEffectsMatteWithPixelBuffer:error:](<replacingportraiteffectsmatte(with_).md>) — Returns a portrait effects matte by wrapping the replacement pixel buffer.
