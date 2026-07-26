---
title: orientation
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoeditingcontext/orientation
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/orientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingcontext/orientation.json'
content_hash: 'sha256:abf1f7d3e465270d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md)

# orientation

<sub>Instance Property</sub>

The image orientation of the Live Photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var orientation: CGImagePropertyOrientation { get }
```

## Discussion

This [fullSizeImage](fullsizeimage.md) object does not reflect the Live Photo’s orientation metadata. Use this property when displaying that image to ensure that it appears to the user in the correct orientation.

## See Also

### Examining an Editing Context’s Live Photo

- [fullSizeImage](fullsizeimage.md) — The unedited still photo content of the Live Photo.
- [duration](duration.md) — The duration, in seconds, of the Live Photo.
- [photoTime](phototime.md) — The offset, in seconds, from the beginning of the Live Photo’s duration to the time corresponding to its still photo.
