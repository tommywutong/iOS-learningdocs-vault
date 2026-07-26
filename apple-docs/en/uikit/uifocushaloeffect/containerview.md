---
title: containerView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocushaloeffect/containerview
source_url: 'https://developer.apple.com/documentation/uikit/uifocushaloeffect/containerview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocushaloeffect/containerview.json'
content_hash: 'sha256:aaed014149467853'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusHaloEffect](../uifocushaloeffect.md)

# containerView

<sub>Instance Property</sub>

The container view to place the halo effect into.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var containerView: UIView? { get set }
```

## Discussion

If you don’t set this property, the system automatically determines the container according to the focus item that provides the effect and [referenceView](referenceview.md), if present.

## See Also

### Configuring a halo effect

- [referenceView](referenceview.md) — The view to place the halo effect above.
- [position](position-swift.property.md) — The position of the halo effect relative to its shape.
- [Position](position-swift.enum.md) — Constants that describe positions for drawing the halo focus effect.
