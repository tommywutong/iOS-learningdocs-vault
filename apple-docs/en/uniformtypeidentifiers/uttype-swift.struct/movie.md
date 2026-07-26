---
title: movie
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/movie
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/movie'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/movie.json'
content_hash: 'sha256:41054671466b9daa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# movie

<sub>Type Property</sub>

A base type representing media formats that may contain both video and audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var movie: UTType { get }
```

## Discussion

This type corresponds to what users would label a “movie”.

The identifier for this type is `public.movie`.

This type conforms to [UTTypeAudiovisualContent](../uttypeaudiovisualcontent.md).

## See Also

### Image, audio, and video base types

- [image](image.md) — A base type that represents image data.
- [audio](audio.md) — A type that represents audio that doesn’t contain video.
- [audiovisualContent](audiovisualcontent.md) — A base type that represents data that contains video content that may or may not also include audio.
- [video](video.md) — A type that represents video that doesn’t contain audio.
