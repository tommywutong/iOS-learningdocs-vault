---
title: duration
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoeditingcontext/duration
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingcontext/duration.json'
content_hash: 'sha256:722b30c5512df644'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md)

# duration

<sub>Instance Property</sub>

The duration, in seconds, of the Live Photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var duration: CMTime { get }
```

## See Also

### Examining an Editing Context’s Live Photo

- [fullSizeImage](fullsizeimage.md) — The unedited still photo content of the Live Photo.
- [photoTime](phototime.md) — The offset, in seconds, from the beginning of the Live Photo’s duration to the time corresponding to its still photo.
- [orientation](orientation.md) — The image orientation of the Live Photo.
