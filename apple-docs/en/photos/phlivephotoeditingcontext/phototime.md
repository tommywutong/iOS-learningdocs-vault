---
title: photoTime
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoeditingcontext/phototime
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/phototime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingcontext/phototime.json'
content_hash: 'sha256:125f579add2e69d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md)

# photoTime

<sub>Instance Property</sub>

The offset, in seconds, from the beginning of the Live Photo’s duration to the time corresponding to its still photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var photoTime: CMTime { get }
```

## Discussion

To create time-based effects in your [frameProcessor](frameprocessor.md) block, use this property together with the [duration](duration.md) property.

## See Also

### Examining an Editing Context’s Live Photo

- [fullSizeImage](fullsizeimage.md) — The unedited still photo content of the Live Photo.
- [duration](duration.md) — The duration, in seconds, of the Live Photo.
- [orientation](orientation.md) — The image orientation of the Live Photo.
