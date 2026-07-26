---
title: UTTypeAppleProtectedMPEG4Video
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeappleprotectedmpeg4video
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeappleprotectedmpeg4video'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeappleprotectedmpeg4video.json'
content_hash: 'sha256:6181cac12de49529'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeAppleProtectedMPEG4Video

<sub>Global Variable</sub>

A type that represents data in Apple-protected MPEG-4 format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeAppleProtectedMPEG4Video;
```

## Discussion

The identifier for this type is `com.apple.protected-mpeg-4-video`.

This type conforms to a base type identified by `com.apple.m4v-video`, which in turn conforms to [UTTypeMPEG4Movie](uttypempeg4movie.md).

## See Also

### Audio and video

- [UTTypeQuickTimeMovie](uttypequicktimemovie.md) — A type that represents a QuickTime movie.
- [UTTypeMPEG](uttypempeg.md) — A type that represents an MPEG-1 or MPEG-2 movie.
- [UTTypeMPEG2Video](uttypempeg2video.md) — A type that represents an MPEG-2 video.
- [UTTypeMPEG2TransportStream](uttypempeg2transportstream.md) — A type that represents data in MPEG-2 transport stream movie format.
- [UTTypeMPEG4Movie](uttypempeg4movie.md) — A type that represents an MPEG-4 movie.
- [UTTypeMPEG4Audio](uttypempeg4audio.md) — A type that represents an MPEG-4 audio layer file.
- [UTTypeAppleProtectedMPEG4Audio](uttypeappleprotectedmpeg4audio.md) — A type that represents data in Apple-protected MPEG-4 format.
- [UTTypeAVI](uttypeavi.md) — A type that represents data in AVI movie format.
