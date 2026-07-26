---
title: 'draw(at:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlinefragment/draw(at:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlinefragment/draw(at:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlinefragment/draw%28at%3Ain%3A%29.json'
content_hash: 'sha256:50eba2c810cb9a06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLineFragment](../nstextlinefragment.md)

# draw(at:in:)

<sub>Instance Method</sub>

Renders the line fragment contents at the rendering origin.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func draw(at point: CGPoint, in context: CGContext)
```

## Parameters

- `point` — The origin as a `CGPoint`.

- `context` — The drawing context.

## Discussion

You can specify the origin as (`NSMinX(typographicBounds) + glyphOrigin.x, NSMinY(typographicBounds) + glyphOrigin.y)` relative to the line fragment group coordinate system.
