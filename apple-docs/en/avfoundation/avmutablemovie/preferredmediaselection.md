---
title: preferredMediaSelection
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/preferredmediaselection
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/preferredmediaselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/preferredmediaselection.json'
content_hash: 'sha256:6f46755f61d83c66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# preferredMediaSelection

<sub>Instance Property</sub>

The default media selections for this asset’s media selection groups.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var preferredMediaSelection: AVMediaSelection { get }
```

## Discussion

Provides an instance of [AVMediaSelection](../avmediaselection.md) with the default selections for each of the assets media selection groups.

## See Also

### Inspecting preferences

- [preferredRate](preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredVolume](preferredvolume.md) — The asset’s volume preference for playing its audible media.
- [preferredTransform](preferredtransform.md) — The asset’s transform preference to apply to its visual content during presentation or processing.
