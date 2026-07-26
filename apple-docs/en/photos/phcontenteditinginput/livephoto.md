---
title: livePhoto
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput/livephoto
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/livephoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/livephoto.json'
content_hash: 'sha256:f7ecfa9f1240f1c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# livePhoto

<sub>Instance Property</sub>

The unedited Live Photo content of the editing input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var livePhoto: PHLivePhoto? { get }
```

## Discussion

To edit the video and photo content of the Live Photo, create a [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md) object using this [PHContentEditingInput](../phcontenteditinginput.md) object.

If the editing input does not represent a Live Photo, this property’s value is `nil`, indicating that you cannot use this [PHContentEditingInput](../phcontenteditinginput.md) object to create a Live Photo editing context.

## See Also

### Working with Live Photo Assets

- [playbackStyle](playbackstyle.md) — The style in which to present this content to the user.
- [PlaybackStyle](../phasset/playbackstyle-swift.enum.md) — An enumeration of asset playback styles that dictate how to present an asset to the user.
