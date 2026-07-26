---
title: containerView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihovereffectlayer/containerview
source_url: 'https://developer.apple.com/documentation/uikit/uihovereffectlayer/containerview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovereffectlayer/containerview.json'
content_hash: 'sha256:ff8449d22de8b130'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIHoverEffectLayer](../uihovereffectlayer.md)

# containerView

<sub>Instance Property</sub>

The [UIView](../uiview.md) in which this layer is contained. This view is used to derive traits and other properties for applying the correct hover effect to the layer. It may also be used to assist with applying some kinds of hover effects to the layer.

<sub>visionOS</sub>

```swift
weak var containerView: UIView? { get set }
```

## Discussion

The [containerView](containerview.md) should be an ancestor of this layer (once it has been added to a layer hierarchy) to behave correctly, but does not need to be the immediate parent of this layer. If the [containerView](containerview.md) is set to nil or is deallocated, some aspects of this layer’s hover effect may no longer work correctly.
