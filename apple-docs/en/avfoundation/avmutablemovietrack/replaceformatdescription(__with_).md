---
title: 'replaceFormatDescription(_:with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovietrack/replaceformatdescription(_:with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/replaceformatdescription(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/replaceformatdescription%28_%3Awith%3A%29.json'
content_hash: 'sha256:49fec591e4bee111'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# replaceFormatDescription(_:with:)

<sub>Instance Method</sub>

Replaces the track’s format description with a new format description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func replaceFormatDescription(_ formatDescription: CMFormatDescription, with newFormatDescription: CMFormatDescription)
```

## Parameters

- `formatDescription` — The [CMFormatDescription](../../coremedia/cmformatdescription.md) object to be replaced.

- `newFormatDescription` — The [CMFormatDescription](../../coremedia/cmformatdescription.md) object to replacing the specified format description.

## Discussion

Use this method to change a track’s format descriptions, such as adding format description extensions to a format description or changing the audio channel layout of an audio track. Format description can have extensions of type [kCMFormatDescriptionExtension_VerbatimSampleDescription](../../coremedia/kcmformatdescriptionextension_verbatimsampledescription.md) and [kCMFormatDescriptionExtension_VerbatimISOSampleEntry](../../coremedia/kcmformatdescriptionextension_verbatimisosampleentry.md). If you modify a copy of a format description, delete those extensions from the copy or your changes might be ignored.

## See Also

### Changing format descriptions

- [formatDescriptions](formatdescriptions.md) — The format descriptions of the media samples that a track references.
