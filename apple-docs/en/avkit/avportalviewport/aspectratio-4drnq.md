---
title: aspectRatio
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 27.0+ beta]
languages: [swift, swift, swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avportalviewport/aspectratio-4drnq
source_url: 'https://developer.apple.com/documentation/avkit/avportalviewport/aspectratio-4drnq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avportalviewport/aspectratio-4drnq.json'
content_hash: 'sha256:b5324320148e655c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPortalViewport](../avportalviewport.md)

# aspectRatio

<sub>Instance Property</sub>

The aspect ratio of the portal frame.

<sub>visionOS</sub>

```swift
var aspectRatio: Double? { get set }
```

## Discussion

This value determines the width-to-height ratio of the portal frame. Common aspect ratios include:

- 1.78 (16:9) for standard widescreen content
- 2.35 or 2.39 for cinematic widescreen content
- 1.33 (4:3) for traditional content

When nil, the system defaults to a 16:9 (1.78) aspect ratio.

> [!important] Important
> The system may adjust values outside typical ranges to ensure a comfortable viewing experience.
