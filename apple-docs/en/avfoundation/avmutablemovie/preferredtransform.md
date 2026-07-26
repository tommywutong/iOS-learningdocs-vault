---
title: preferredTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/preferredtransform
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/preferredtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/preferredtransform.json'
content_hash: 'sha256:38d896c780ac5027'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# preferredTransform

<sub>Instance Property</sub>

The asset’s transform preference to apply to its visual content during presentation or processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var preferredTransform: CGAffineTransform { get set }
```

## Discussion

The value is typically, but not always, the identity transform.

## See Also

### Inspecting preferences

- [preferredRate](preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredVolume](preferredvolume.md) — The asset’s volume preference for playing its audible media.
- [preferredMediaSelection](preferredmediaselection.md) — The default media selections for this asset’s media selection groups.
