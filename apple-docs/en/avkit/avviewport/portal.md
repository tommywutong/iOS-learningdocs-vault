---
title: portal
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 27.0+ beta]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avviewport/portal
source_url: 'https://developer.apple.com/documentation/avkit/avviewport/portal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avviewport/portal.json'
content_hash: 'sha256:7891742d39279437'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVViewport](../avviewport.md)

# portal

<sub>Instance Property</sub>

The viewport configuration to use when immersive content is displayed in a portal.

<sub>visionOS</sub>

```swift
var portal: AVPortalViewport? { get set }
```

## Discussion

Set this property to customize how content appears within a portal frame. When nil, the system uses default portal settings.

> [!note] Note
> Spatial videos do not support portal viewport settings.

## See Also

### Configuring the portal viewport

- [AVPortalViewport](../avportalviewport.md) — A viewport configuration used when displaying content in portals. _(beta)_
