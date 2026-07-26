---
title: PHLivePhotoViewDelegate
framework: PhotosUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotoviewdelegate
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoviewdelegate.json'
content_hash: 'sha256:939b7093c34e7fd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHLivePhotoViewDelegate

<sub>Protocol</sub>

The [PHLivePhotoViewDelegate](phlivephotoviewdelegate.md) protocol describes messages sent by a [PHLivePhotoView](phlivephotoview.md) instance in response to playback events when playing the motion and sound content associated with a Live Photo. To receive these messages, implement the methods in this protocol in one of your controller objects and assign that object to the [delegate](phlivephotoview/delegate.md) property of a Live Photo view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor protocol PHLivePhotoViewDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to Live Photos Playback Events

- [- livePhotoView:canBeginPlaybackWithStyle:](<phlivephotoviewdelegate/livephotoview(__canbeginplaybackwith_).md>) — Notifies the delegate to determine whether the Live Photo can begin playback.
- [- livePhotoView:willBeginPlaybackWithStyle:](<phlivephotoviewdelegate/livephotoview(__willbeginplaybackwith_).md>) — Notifies the delegate when Live Photos playback is beginning.
- [- livePhotoView:didEndPlaybackWithStyle:](<phlivephotoviewdelegate/livephotoview(__didendplaybackwith_).md>) — Notifies the delegate when Live Photos playback ends.
- [- livePhotoView:extraMinimumTouchDurationForTouch:withStyle:](<phlivephotoviewdelegate/livephotoview(__extraminimumtouchdurationfor_with_).md>) — Notifies the delegate to offset the timing of a touch.

## See Also

### Responding to Playback Events

- [delegate](phlivephotoview/delegate.md) — An object to be notified when Live Photo playback begins or ends.
