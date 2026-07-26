---
title: audioVolume
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.12+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotoview/audiovolume
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoview/audiovolume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoview/audiovolume.json'
content_hash: 'sha256:4ca994df0dd89d8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoView](../phlivephotoview.md)

# audioVolume

<sub>Instance Property</sub>

The audio gain to apply to the Live Photo’s movie content during playback.

<sub>macOS</sub>

```swift
var audioVolume: Float { get set }
```

## Discussion

Values for this property must be between `0.0` and `1.0`, inclusive. A value of `1.0` (the default) plays audio content from the Live Photo at full volume (relative to the system volume). A value of `0.0` is equivalent to setting the [muted](ismuted.md) property to `true`.

## See Also

### Managing Playback

- [playbackGestureRecognizer](playbackgesturerecognizer.md) — A gesture recognizer that controls playback of the Live Photo in the view.
- [muted](ismuted.md) — A Boolean value that determines whether the view plays the audio content of its Live Photo.
