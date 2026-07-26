---
title: aiff
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/aiff
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/aiff'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/aiff.json'
content_hash: 'sha256:66c0529f9a0a6597'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# aiff

<sub>Type Property</sub>

A type that represents data in AIFF audio format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var aiff: UTType { get }
```

## Discussion

The identifier for this type is `public.aiff-audio`.

This type conforms to a base type identified by `public.aifc-audio`, which in turn conforms to [UTTypeAudio](../uttypeaudio.md).

## See Also

### Audio

- [mp3](mp3.md) — A type that represents MP3 audio.
- [wav](wav.md) — A type that represents data in Microsoft Waveform Audio File Format.
- [midi](midi.md) — A type that represents data in MIDI audio format.
- [playlist](playlist.md) — A base type that represents a playlist.
- [m3uPlaylist](m3uplaylist.md) — A type that represents an M3U or M3U8 playlist.
