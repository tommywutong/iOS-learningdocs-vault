---
title: 'startPlayback(with:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phlivephotoview/startplayback(with:)'
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoview/startplayback(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoview/startplayback%28with%3A%29.json'
content_hash: 'sha256:e47664e2f903286e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoView](../phlivephotoview.md)

# startPlayback(with:)

<sub>Instance Method</sub>

Begins playback of Live Photo content in the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startPlayback(with playbackStyle: PHLivePhotoViewPlaybackStyle)
```

## Parameters

- `playbackStyle` — An option for how much of the Live Photo’s motion and sound content to play. See [PHLivePhotoViewPlaybackStyle](../phlivephotoviewplaybackstyle.md).

## Discussion

Use the `playbackStyle` parameter to choose whether to play the full motion and sound content of the Live Photo or only a brief section.

Typically, an app does not need to directly control playback, because a Live Photo view provides interactive playback control. Use this method only when non-interactive playback is appropriate—for example, to briefly animate the content to indicate that a view contains a Live Photo rather than a still image.

## See Also

### Manually Playing Live Photo Content

- [- stopPlayback](<stopplayback().md>) — Stops playback of a Live Photo.
- [- stopPlaybackAnimated:](<stopplayback(animated_).md>) — Stops playback of a Live Photo in an animated manner.
