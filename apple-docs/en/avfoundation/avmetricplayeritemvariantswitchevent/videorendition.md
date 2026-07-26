---
title: videoRendition
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricplayeritemvariantswitchevent/videorendition
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricplayeritemvariantswitchevent/videorendition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricplayeritemvariantswitchevent/videorendition.json'
content_hash: 'sha256:ca6f0cd046696d5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetricPlayerItemVariantSwitchEvent](../avmetricplayeritemvariantswitchevent.md)

# videoRendition

<sub>Instance Property</sub>

Represents the currently selected video rendition’s identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var videoRendition: AVMetricMediaRendition { get }
```

## Discussion

Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## See Also

### Inspecting the event

- [didSucceed](didsucceed.md)
- [fromVariant](fromvariant.md)
- [loadedTimeRanges](loadedtimeranges-5lkmg.md)
- [toVariant](tovariant.md)
- [audioRendition](audiorendition.md) — Represents the currently selected video rendition’s identifiers.
- [subtitleRendition](subtitlerendition.md) — Represents the currently selected audio rendition’s identifiers.
