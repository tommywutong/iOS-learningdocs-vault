---
title: preferredRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/preferredrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/preferredrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/preferredrate.json'
content_hash: 'sha256:880d9e9f6a2884f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# preferredRate

<sub>Instance Property</sub>

The asset’s rate preference for playing its media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var preferredRate: Float { get set }
```

## Discussion

This value is typically, but not always, 1.0.

## See Also

### Inspecting preferences

- [preferredVolume](preferredvolume.md) — The asset’s volume preference for playing its audible media.
- [preferredTransform](preferredtransform.md) — The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredMediaSelection](preferredmediaselection.md) — The default media selections for this asset’s media selection groups.
