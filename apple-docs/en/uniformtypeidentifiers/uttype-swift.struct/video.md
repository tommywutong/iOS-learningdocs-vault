---
title: video
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/video
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/video'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/video.json'
content_hash: 'sha256:220d229f0edc6731'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# video

<sub>Type Property</sub>

A type that represents video that doesn’t contain audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var video: UTType { get }
```

## Discussion

The identifier for this type is `public.video`.

This type conforms to [UTTypeMovie](../uttypemovie.md).

## See Also

### Image, audio, and video base types

- [image](image.md) — A base type that represents image data.
- [audio](audio.md) — A type that represents audio that doesn’t contain video.
- [audiovisualContent](audiovisualcontent.md) — A base type that represents data that contains video content that may or may not also include audio.
- [movie](movie.md) — A base type representing media formats that may contain both video and audio.
