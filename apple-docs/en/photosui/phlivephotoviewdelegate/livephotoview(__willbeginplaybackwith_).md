---
title: 'livePhotoView(_:willBeginPlaybackWith:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:willbeginplaybackwith:)'
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:willbeginplaybackwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoviewdelegate/livephotoview%28_%3Awillbeginplaybackwith%3A%29.json'
content_hash: 'sha256:ad528e661840db54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoViewDelegate](../phlivephotoviewdelegate.md)

# livePhotoView(_:willBeginPlaybackWith:)

<sub>Instance Method</sub>

Notifies the delegate when Live Photos playback is beginning.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func livePhotoView(_ livePhotoView: PHLivePhotoView, willBeginPlaybackWith playbackStyle: PHLivePhotoViewPlaybackStyle)
```

## Parameters

- `livePhotoView` — The view beginning playback of Live Photo content.

- `playbackStyle` — The style of playback, indicating whether the content is to play in full or as a brief preview.

## See Also

### Responding to Live Photos Playback Events

- [- livePhotoView:canBeginPlaybackWithStyle:](<livephotoview(__canbeginplaybackwith_).md>) — Notifies the delegate to determine whether the Live Photo can begin playback.
- [- livePhotoView:didEndPlaybackWithStyle:](<livephotoview(__didendplaybackwith_).md>) — Notifies the delegate when Live Photos playback ends.
- [- livePhotoView:extraMinimumTouchDurationForTouch:withStyle:](<livephotoview(__extraminimumtouchdurationfor_with_).md>) — Notifies the delegate to offset the timing of a touch.
