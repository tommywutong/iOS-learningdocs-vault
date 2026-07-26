---
title: delegate
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotoview/delegate
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoview/delegate.json'
content_hash: 'sha256:0b909021ada78bed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoView](../phlivephotoview.md)

# delegate

<sub>Instance Property</sub>

An object to be notified when Live Photo playback begins or ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var delegate: (any PHLivePhotoViewDelegate)? { get set }
```

## See Also

### Responding to Playback Events

- [PHLivePhotoViewDelegate](../phlivephotoviewdelegate.md) — The [PHLivePhotoViewDelegate](../phlivephotoviewdelegate.md) protocol describes messages sent by a [PHLivePhotoView](../phlivephotoview.md) instance in response to playback events when playing the motion and sound content associated with a Live Photo. To receive these messages, implement the methods in this protocol in one of your controller objects and assign that object to the [delegate](delegate.md) property of a Live Photo view.
