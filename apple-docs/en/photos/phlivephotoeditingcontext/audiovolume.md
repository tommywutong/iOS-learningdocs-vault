---
title: audioVolume
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoeditingcontext/audiovolume
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/audiovolume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingcontext/audiovolume.json'
content_hash: 'sha256:fbfd3c638bf0ba72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md)

# audioVolume

<sub>Instance Property</sub>

The audio gain to apply to the processed Live Photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var audioVolume: Float { get set }
```

## Discussion

Values must be between `0.0` and `1.0`, inclusive. A value of `1.0` (the default) leaves the audio content of the Live Photo unchanged. A value of `0.0` mutes all audio in the output Live Photo.

Setting this property does not process the Live Photo content; instead, it sets the audio gain to be applied when you later process the Live Photo using one of the methods listed in Processing an Editing Context’s Live Photo.

## See Also

### Preparing an Editing Context for Processing

- [frameProcessor](frameprocessor.md) — A block to be called by Photos for processing each frame of the Live Photo’s visual content.
- [PHLivePhotoFrameProcessingBlock](../phlivephotoframeprocessingblock.md) — The signature for a block Photos calls to process Live Photo frames.
