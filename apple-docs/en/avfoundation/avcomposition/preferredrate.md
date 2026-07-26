---
title: preferredRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/preferredrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/preferredrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/preferredrate.json'
content_hash: 'sha256:3ee57bc36678ccd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# preferredRate

<sub>Instance Property</sub>

The asset’s rate preference for playing its media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredRate: Float { get }
```

## Discussion

This value is typically, but not always, 1.0.

## See Also

### Inspecting preferences

- [preferredVolume](preferredvolume.md) — The asset’s volume preference for playing its audible media.
- [preferredTransform](preferredtransform.md) — The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredMediaSelection](preferredmediaselection.md) — The default media selections for this asset’s media selection groups.
- [preferredDisplayCriteria](preferreddisplaycriteria.md) — The asset’s display mode preference for optimal playback of its content.
