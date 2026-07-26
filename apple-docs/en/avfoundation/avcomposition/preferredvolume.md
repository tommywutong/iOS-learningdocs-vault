---
title: preferredVolume
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/preferredvolume
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/preferredvolume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/preferredvolume.json'
content_hash: 'sha256:c9c6de06248647d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# preferredVolume

<sub>Instance Property</sub>

The asset’s volume preference for playing its audible media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredVolume: Float { get }
```

## Discussion

This value is typically, but not always, 1.0.

## See Also

### Inspecting preferences

- [preferredRate](preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredTransform](preferredtransform.md) — The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredMediaSelection](preferredmediaselection.md) — The default media selections for this asset’s media selection groups.
- [preferredDisplayCriteria](preferreddisplaycriteria.md) — The asset’s display mode preference for optimal playback of its content.
