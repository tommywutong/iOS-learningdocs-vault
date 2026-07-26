---
title: formatDescriptionReplacements
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/formatdescriptionreplacements
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/formatdescriptionreplacements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/formatdescriptionreplacements.json'
content_hash: 'sha256:54e0c6b28f07176e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# formatDescriptionReplacements

<sub>Instance Property</sub>

The replacement format descriptions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var formatDescriptionReplacements: [AVCompositionTrackFormatDescriptionReplacement] { get }
```

## Discussion

The property’s values specify an original and a replacement format description, as set in a previous call to [- replaceFormatDescription:withFormatDescription:](<../avmutablecompositiontrack/replaceformatdescription(__with_).md>).

## See Also

### Managing format descriptions

- [formatDescriptions](formatdescriptions.md) — The format descriptions of the media samples that a track references.
- [AVCompositionTrackFormatDescriptionReplacement](../avcompositiontrackformatdescriptionreplacement.md) — An object that represents a format description and its replacement.
