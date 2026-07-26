---
title: preferredTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablecompositiontrack/preferredtransform
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/preferredtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecompositiontrack/preferredtransform.json'
content_hash: 'sha256:cca29c738a51a29a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCompositionTrack](../avmutablecompositiontrack.md)

# preferredTransform

<sub>Instance Property</sub>

The preferred transformation of the visual media data for display purposes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredTransform: CGAffineTransform { get set }
```

## Discussion

If not set, the value is [CGAffineTransformIdentity](../../coregraphics/cgaffinetransformidentity.md).

## See Also

### Configuring track properties

- [enabled](isenabled.md) — A Boolean value that indicates whether the tracks is in an enabled state.
- [naturalTimeScale](naturaltimescale.md) — The time scale in which you can perform time-based operations without extra numerical conversion.
- [languageCode](languagecode.md) — The language associated with the track, as an ISO 639-2/T language code.
- [extendedLanguageTag](extendedlanguagetag.md) — The language tag associated with the track, as an RFC 4646 language tag.
- [preferredVolume](preferredvolume.md) — The volume the track prefers for its audible media data.
