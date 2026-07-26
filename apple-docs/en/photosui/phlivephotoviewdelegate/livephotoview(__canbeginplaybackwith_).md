---
title: 'livePhotoView(_:canBeginPlaybackWith:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:canbeginplaybackwith:)'
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:canbeginplaybackwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoviewdelegate/livephotoview%28_%3Acanbeginplaybackwith%3A%29.json'
content_hash: 'sha256:d8d5cdbe6668d993'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoViewDelegate](../phlivephotoviewdelegate.md)

# livePhotoView(_:canBeginPlaybackWith:)

<sub>Instance Method</sub>

Notifies the delegate to determine whether the Live Photo can begin playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func livePhotoView(_ livePhotoView: PHLivePhotoView, canBeginPlaybackWith playbackStyle: PHLivePhotoViewPlaybackStyle) -> Bool
```

## Parameters

- `livePhotoView` — The view requesting whether it can begin the playback of Live Photo content.

- `playbackStyle` — The style of playback, indicating whether the content can play in full or as a brief preview.

## Return Value

Whether the playback of Live Photo content can begin.

## See Also

### Responding to Live Photos Playback Events

- [- livePhotoView:willBeginPlaybackWithStyle:](<livephotoview(__willbeginplaybackwith_).md>) — Notifies the delegate when Live Photos playback is beginning.
- [- livePhotoView:didEndPlaybackWithStyle:](<livephotoview(__didendplaybackwith_).md>) — Notifies the delegate when Live Photos playback ends.
- [- livePhotoView:extraMinimumTouchDurationForTouch:withStyle:](<livephotoview(__extraminimumtouchdurationfor_with_).md>) — Notifies the delegate to offset the timing of a touch.
