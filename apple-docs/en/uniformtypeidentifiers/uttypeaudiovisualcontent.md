---
title: UTTypeAudiovisualContent
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeaudiovisualcontent
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeaudiovisualcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeaudiovisualcontent.json'
content_hash: 'sha256:b6cca1fab317b138'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeAudiovisualContent

<sub>Global Variable</sub>

A base type that represents data that contains video content that may or may not also include audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeAudiovisualContent;
```

## Discussion

The identifier for this type is `public.audiovisual-content`.

This type conforms to [UTTypeContent](uttypecontent.md) and [UTTypeData](uttypedata.md).

## See Also

### Image, audio, and video base types

- [UTTypeImage](uttypeimage.md) — A base type that represents image data.
- [UTTypeAudio](uttypeaudio.md) — A type that represents audio that doesn’t contain video.
- [UTTypeMovie](uttypemovie.md) — A base type representing media formats that may contain both video and audio.
- [UTTypeVideo](uttypevideo.md) — A type that represents video that doesn’t contain audio.
