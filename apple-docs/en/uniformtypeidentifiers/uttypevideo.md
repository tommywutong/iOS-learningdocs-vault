---
title: UTTypeVideo
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypevideo
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypevideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypevideo.json'
content_hash: 'sha256:1f5ab6ed701a22b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeVideo

<sub>Global Variable</sub>

A type that represents video that doesn’t contain audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeVideo;
```

## Discussion

The identifier for this type is `public.video`.

This type conforms to [UTTypeMovie](uttypemovie.md).

## See Also

### Image, audio, and video base types

- [UTTypeImage](uttypeimage.md) — A base type that represents image data.
- [UTTypeAudio](uttypeaudio.md) — A type that represents audio that doesn’t contain video.
- [UTTypeAudiovisualContent](uttypeaudiovisualcontent.md) — A base type that represents data that contains video content that may or may not also include audio.
- [UTTypeMovie](uttypemovie.md) — A base type representing media formats that may contain both video and audio.
