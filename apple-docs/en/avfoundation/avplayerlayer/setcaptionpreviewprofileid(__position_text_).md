---
title: 'setCaptionPreviewProfileID(_:position:text:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerlayer/setcaptionpreviewprofileid(_:position:text:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlayer/setcaptionpreviewprofileid(_:position:text:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlayer/setcaptionpreviewprofileid%28_%3Aposition%3Atext%3A%29.json'
content_hash: 'sha256:3169cbfeb0ad86bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLayer](../avplayerlayer.md)

# setCaptionPreviewProfileID(_:position:text:)

<sub>Instance Method</sub>

Starts displaying a caption preview with the specified accessibility profile.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setCaptionPreviewProfileID(_ profileID: String, position: CGPoint, text: String?)
```

## Parameters

- `profileID` — The identifier of the accessibility profile to use for caption appearance. Profile IDs can be obtained from `MACaptionAppearanceCopyProfileIDs()`. This determines font, color, background, and other visual characteristics.

- `position` — A CGPoint that defines the position (in points) of the caption preview relative to the default positioning of content captions (centered near the bottom of the video). Position values can be negative. (0, 0) represents the default positioning.

- `text` — Optional custom text to display in the preview. If `nil`, a standard localized preview message will be shown.

## Discussion

This method enables a preview mode that displays sample caption text using the visual appearance settings from the specified accessibility profile. The preview replaces any currently active subtitles and/or closed captions while active. The sample caption text position can be specified to avoid UI controls.

> [!note] Note
> You must call [- stopShowingCaptionPreview](<stopshowingcaptionpreview().md>) to exit the preview.
