---
title: UTTypeAIFF
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeaiff
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeaiff'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeaiff.json'
content_hash: 'sha256:9fd861a1bb2d0585'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeAIFF

<sub>Global Variable</sub>

A type that represents data in AIFF audio format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeAIFF;
```

## Discussion

The identifier for this type is `public.aiff-audio`.

This type conforms to a base type identified by `public.aifc-audio`, which in turn conforms to [UTTypeAudio](uttypeaudio.md).

## See Also

### Audio

- [UTTypeMP3](uttypemp3.md) — A type that represents MP3 audio.
- [UTTypeWAV](uttypewav.md) — A type that represents data in Microsoft Waveform Audio File Format.
- [UTTypeMIDI](uttypemidi.md) — A type that represents data in MIDI audio format.
- [UTTypePlaylist](uttypeplaylist.md) — A base type that represents a playlist.
- [UTTypeM3UPlaylist](uttypem3uplaylist.md) — A type that represents an M3U or M3U8 playlist.
