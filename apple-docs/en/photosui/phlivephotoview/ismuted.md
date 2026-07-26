---
title: isMuted
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotoview/ismuted
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoview/ismuted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoview/ismuted.json'
content_hash: 'sha256:aa3ecbe94c77dba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoView](../phlivephotoview.md)

# isMuted

<sub>Instance Property</sub>

A Boolean value that determines whether the view plays the audio content of its Live Photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isMuted: Bool { get set }
```

## Discussion

The default value is `false`, indicating that the view plays audio content along with the motion content of its Live Photo. Change this value to `true` to play motion content but not audio content.

## See Also

### Managing Playback

- [playbackGestureRecognizer](playbackgesturerecognizer.md) — A gesture recognizer that controls playback of the Live Photo in the view.
- [audioVolume](audiovolume.md) — The audio gain to apply to the Live Photo’s movie content during playback.
