---
title: 'stopPlayback(animated:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.12+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phlivephotoview/stopplayback(animated:)'
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoview/stopplayback(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoview/stopplayback%28animated%3A%29.json'
content_hash: 'sha256:03388b9b880325c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoView](../phlivephotoview.md)

# stopPlayback(animated:)

<sub>Instance Method</sub>

Stops playback of a Live Photo in an animated manner.

<sub>macOS</sub>

```swift
func stopPlayback(animated: Bool)
```

## Parameters

- `animated` — A Boolean value that indicates whether playback stops immediately or with animation.

## Discussion

Calling this method with a value of `false` is the same as calling [- stopPlayback](<stopplayback().md>).

## See Also

### Manually Playing Live Photo Content

- [- startPlaybackWithStyle:](<startplayback(with_).md>) — Begins playback of Live Photo content in the view.
- [- stopPlayback](<stopplayback().md>) — Stops playback of a Live Photo.
