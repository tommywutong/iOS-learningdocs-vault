---
title: 'UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uivideoatpathiscompatiblewithsavedphotosalbum(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uivideoatpathiscompatiblewithsavedphotosalbum(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoatpathiscompatiblewithsavedphotosalbum%28_%3A%29.json'
content_hash: 'sha256:8d4b51955acf4733'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether the specified video is compatible to save to the user’s Camera Roll album.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_ videoPath: String) -> Bool
```

## Parameters

- `videoPath` — The filesystem path to the movie file you want to save.

## Return Value

[true](../swift/true.md) if the video can be saved to the Camera Roll album or [false](../swift/false.md) if it cannot.

## Discussion

Not all devices are able to play video files placed in the user’s Camera Roll album. Before attempting to save a video, call this function and check its return value to ensure that saving the video is supported for the current device. For a code example, refer to [Camera Programming Topics for iOS](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/CameraAndPhotoLib_TopicsForIOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010400).

When used on an iOS device without a camera, this method indicates whether the specified movie can be saved to the Saved Photos album rather than to the Camera Roll album.

## See Also

### Photo album

- [UIImageWriteToSavedPhotosAlbum](<uiimagewritetosavedphotosalbum(________).md>) — Adds the specified image to the user’s Camera Roll album.
- [UISaveVideoAtPathToSavedPhotosAlbum](<uisavevideoatpathtosavedphotosalbum(________).md>) — Adds the movie from the specified path to the user’s Camera Roll album.
