---
title: 'livePhotoView(_:didEndPlaybackWith:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:didendplaybackwith:)'
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:didendplaybackwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoviewdelegate/livephotoview%28_%3Adidendplaybackwith%3A%29.json'
content_hash: 'sha256:c14db7eb4b7fcf71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoViewDelegate](../phlivephotoviewdelegate.md)

# livePhotoView(_:didEndPlaybackWith:)

<sub>Instance Method</sub>

Notifies the delegate when Live Photos playback ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func livePhotoView(_ livePhotoView: PHLivePhotoView, didEndPlaybackWith playbackStyle: PHLivePhotoViewPlaybackStyle)
```

## Parameters

- `livePhotoView` — The view that ended playback of Live Photo content.

- `playbackStyle` — The style of playback, indicating whether the content played in full or as a brief preview.

## See Also

### Responding to Live Photos Playback Events

- [- livePhotoView:canBeginPlaybackWithStyle:](<livephotoview(__canbeginplaybackwith_).md>) — Notifies the delegate to determine whether the Live Photo can begin playback.
- [- livePhotoView:willBeginPlaybackWithStyle:](<livephotoview(__willbeginplaybackwith_).md>) — Notifies the delegate when Live Photos playback is beginning.
- [- livePhotoView:extraMinimumTouchDurationForTouch:withStyle:](<livephotoview(__extraminimumtouchdurationfor_with_).md>) — Notifies the delegate to offset the timing of a touch.
