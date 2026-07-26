---
title: playbackStyle
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput/playbackstyle
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/playbackstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/playbackstyle.json'
content_hash: 'sha256:84740cd81c109636'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# playbackStyle

<sub>Instance Property</sub>

The style in which to present this content to the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var playbackStyle: PHAsset.PlaybackStyle { get }
```

## Discussion

Use this value to specify the type of view and the appropriate APIs on the content editing input to display this content.

## See Also

### Working with Live Photo Assets

- [livePhoto](livephoto.md) — The unedited Live Photo content of the editing input.
- [PlaybackStyle](../phasset/playbackstyle-swift.enum.md) — An enumeration of asset playback styles that dictate how to present an asset to the user.
