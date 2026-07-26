---
title: image
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/image
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/image.json'
content_hash: 'sha256:496975fc04ffb0c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# image

<sub>Type Property</sub>

A base type that represents image data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var image: UTType { get }
```

## Discussion

The identifier for this type is `public.image`.

This type conforms to [UTTypeData](../uttypedata.md) and [UTTypeContent](../uttypecontent.md).

## See Also

### Image, audio, and video base types

- [audio](audio.md) — A type that represents audio that doesn’t contain video.
- [audiovisualContent](audiovisualcontent.md) — A base type that represents data that contains video content that may or may not also include audio.
- [movie](movie.md) — A base type representing media formats that may contain both video and audio.
- [video](video.md) — A type that represents video that doesn’t contain audio.
