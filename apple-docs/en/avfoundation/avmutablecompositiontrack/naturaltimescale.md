---
title: naturalTimeScale
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablecompositiontrack/naturaltimescale
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/naturaltimescale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecompositiontrack/naturaltimescale.json'
content_hash: 'sha256:5bc917270e0ca53b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCompositionTrack](../avmutablecompositiontrack.md)

# naturalTimeScale

<sub>Instance Property</sub>

The time scale in which you can perform time-based operations without extra numerical conversion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var naturalTimeScale: CMTimeScale { get set }
```

## Discussion

If not set, the value is the natural time scale of the first non-empty edit, or 600 if there are no non-empty edits.

Set the value to `0` to revert to the default behavior.

## See Also

### Configuring track properties

- [enabled](isenabled.md) — A Boolean value that indicates whether the tracks is in an enabled state.
- [languageCode](languagecode.md) — The language associated with the track, as an ISO 639-2/T language code.
- [extendedLanguageTag](extendedlanguagetag.md) — The language tag associated with the track, as an RFC 4646 language tag.
- [preferredTransform](preferredtransform.md) — The preferred transformation of the visual media data for display purposes.
- [preferredVolume](preferredvolume.md) — The volume the track prefers for its audible media data.
