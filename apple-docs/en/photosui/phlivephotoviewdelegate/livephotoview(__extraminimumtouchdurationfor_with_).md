---
title: 'livePhotoView(_:extraMinimumTouchDurationFor:with:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:extraminimumtouchdurationfor:with:)'
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:extraminimumtouchdurationfor:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoviewdelegate/livephotoview%28_%3Aextraminimumtouchdurationfor%3Awith%3A%29.json'
content_hash: 'sha256:d24b5e69c9d977a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoViewDelegate](../phlivephotoviewdelegate.md)

# livePhotoView(_:extraMinimumTouchDurationFor:with:)

<sub>Instance Method</sub>

Notifies the delegate to offset the timing of a touch.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func livePhotoView(_ livePhotoView: PHLivePhotoView, extraMinimumTouchDurationFor touch: UITouch, with playbackStyle: PHLivePhotoViewPlaybackStyle) -> TimeInterval
```

## Parameters

- `livePhotoView` — The view that ends playback of Live Photos content.

- `touch` — The touch to offset the timing for.

- `playbackStyle` — The style of playback, indicating whether the content plays in full or as a brief preview.

## Return Value

The time interval offset.

## See Also

### Responding to Live Photos Playback Events

- [- livePhotoView:canBeginPlaybackWithStyle:](<livephotoview(__canbeginplaybackwith_).md>) — Notifies the delegate to determine whether the Live Photo can begin playback.
- [- livePhotoView:willBeginPlaybackWithStyle:](<livephotoview(__willbeginplaybackwith_).md>) — Notifies the delegate when Live Photos playback is beginning.
- [- livePhotoView:didEndPlaybackWithStyle:](<livephotoview(__didendplaybackwith_).md>) — Notifies the delegate when Live Photos playback ends.
