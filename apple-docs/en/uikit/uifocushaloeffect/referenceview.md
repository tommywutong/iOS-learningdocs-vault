---
title: referenceView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocushaloeffect/referenceview
source_url: 'https://developer.apple.com/documentation/uikit/uifocushaloeffect/referenceview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocushaloeffect/referenceview.json'
content_hash: 'sha256:072d2e39e69bd464'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusHaloEffect](../uifocushaloeffect.md)

# referenceView

<sub>Instance Property</sub>

The view to place the halo effect above.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var referenceView: UIView? { get set }
```

## Discussion

If you set this property, the halo effect appears above this view. If you also set [containerView](containerview.md), this reference view must be a descendant of the container view. The system ensures that the halo effect is in the container but visually above the reference view.

## See Also

### Configuring a halo effect

- [containerView](containerview.md) — The container view to place the halo effect into.
- [position](position-swift.property.md) — The position of the halo effect relative to its shape.
- [Position](position-swift.enum.md) — Constants that describe positions for drawing the halo focus effect.
