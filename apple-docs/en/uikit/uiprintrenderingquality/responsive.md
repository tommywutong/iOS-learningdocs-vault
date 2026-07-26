---
title: UIPrintRenderingQuality.responsive
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintrenderingquality/responsive
source_url: 'https://developer.apple.com/documentation/uikit/uiprintrenderingquality/responsive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintrenderingquality/responsive.json'
content_hash: 'sha256:80d301fa8f70b000'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintRenderingQuality](../uiprintrenderingquality.md)

# UIPrintRenderingQuality.responsive

<sub>Case</sub>

A constant that reduces rendering quality by the smallest possible amount to increase speed and maintain a responsive user interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case responsive
```

## Discussion

Use this option if you determine that rendering at the best quality using [UIPrintRenderingQualityBest](best.md) reduces the responsiveness of the user interface.

## See Also

### Constants

- [UIPrintRenderingQualityBest](best.md) — A constant that renders the printing at the best possible quality, regardless of speed.
