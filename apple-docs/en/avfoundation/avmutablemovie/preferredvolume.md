---
title: preferredVolume
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/preferredvolume
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/preferredvolume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/preferredvolume.json'
content_hash: 'sha256:caabb69d556133f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# preferredVolume

<sub>Instance Property</sub>

The asset’s volume preference for playing its audible media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var preferredVolume: Float { get set }
```

## Discussion

This value is typically, but not always, 1.0.

## See Also

### Inspecting preferences

- [preferredRate](preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredTransform](preferredtransform.md) — The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredMediaSelection](preferredmediaselection.md) — The default media selections for this asset’s media selection groups.
