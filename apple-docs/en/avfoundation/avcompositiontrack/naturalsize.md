---
title: naturalSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/naturalsize
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/naturalsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/naturalsize.json'
content_hash: 'sha256:137eb29b3bdb4fd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# naturalSize

<sub>Instance Property</sub>

The natural dimensions of the media data that the track references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var naturalSize: CGSize { get }
```

## Discussion

For visual tracks, like video or subtitle tracks, this property value is the natural size of the media. For nonvisual tracks, like audio or chapter tracks, the value is [zero](../../corefoundation/cgsize/zero.md).

## See Also

### Accessing visual characteristics

- [preferredTransform](preferredtransform.md) — The track’s transform preference to apply to its visual content during presentation or processing.
