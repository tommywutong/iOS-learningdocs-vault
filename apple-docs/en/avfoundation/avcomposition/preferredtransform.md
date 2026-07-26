---
title: preferredTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcomposition/preferredtransform
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/preferredtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/preferredtransform.json'
content_hash: 'sha256:04516bc7fe65b99a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# preferredTransform

<sub>Instance Property</sub>

The asset’s transform preference to apply to its visual content during presentation or processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredTransform: CGAffineTransform { get }
```

## Discussion

The value is typically, but not always, the identity transform.

## See Also

### Inspecting preferences

- [preferredRate](preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredVolume](preferredvolume.md) — The asset’s volume preference for playing its audible media.
- [preferredMediaSelection](preferredmediaselection.md) — The default media selections for this asset’s media selection groups.
- [preferredDisplayCriteria](preferreddisplaycriteria.md) — The asset’s display mode preference for optimal playback of its content.
