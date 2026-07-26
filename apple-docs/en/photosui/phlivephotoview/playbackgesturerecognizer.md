---
title: playbackGestureRecognizer
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotoview/playbackgesturerecognizer
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoview/playbackgesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoview/playbackgesturerecognizer.json'
content_hash: 'sha256:5289ccc9bfaed835'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoView](../phlivephotoview.md)

# playbackGestureRecognizer

<sub>Instance Property</sub>

A gesture recognizer that controls playback of the Live Photo in the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var playbackGestureRecognizer: UIGestureRecognizer { get }
```

## Discussion

The Live Photo view automatically creates and installs this gesture recognizer. Use this property to customize the gesture recognizer’s behavior. For example, you might use it in delegate methods that affect how it interacts with other gesture recognizers, or install it on a different view to ensure proper event handling in your app’s view hierarchy.

## See Also

### Managing Playback

- [muted](ismuted.md) — A Boolean value that determines whether the view plays the audio content of its Live Photo.
- [audioVolume](audiovolume.md) — The audio gain to apply to the Live Photo’s movie content during playback.
