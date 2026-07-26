---
title: UIStackView.Distribution.equalSpacing
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistackview/distribution-swift.enum/equalspacing
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/distribution-swift.enum/equalspacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/distribution-swift.enum/equalspacing.json'
content_hash: 'sha256:6b7b87117bd3f9f6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIStackView](../../uistackview.md) · [Distribution](../distribution-swift.enum.md)

# UIStackView.Distribution.equalSpacing

<sub>Case</sub>

A layout where the stack view maintains equal spacing between adjacent views while preserving their intrinsic content size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case equalSpacing
```

## Discussion

When the arranged views don’t fill the stack view, it pads the spacing between the views evenly. If the arranged views don’t fit within the stack view, it shrinks the views according to their compression resistance priority. If there’s any ambiguity, the stack view shrinks the views based on their index in the [arrangedSubviews](../arrangedsubviews.md) array.

The following image shows an example of a horizontal stack view that uses the [UIStackViewDistributionEqualSpacing](equalspacing.md) distribution.

![](../../../../../attachments/04510fb208768aac2e839ee8c17db595/media-2557450@2x.png)

<sub>A horizontal stack view with four arranged subviews. The stack view spaces the arranged views equally so that they fill the available space along the stack view’s axis.</sub>

## See Also

### Constants

- [UIStackViewDistributionFill](fill.md) — A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackViewDistributionFillEqually](fillequally.md) — A layout where the stack view resizes all arranged views to the same size, filling the available space along the stack view’s axis.
- [UIStackViewDistributionFillProportionally](fillproportionally.md) — A layout where the stack view resizes views proportionally based on their intrinsic content size to fill the available space along the stack view’s axis.
- [UIStackViewDistributionEqualCentering](equalcentering.md) — A layout that attempts to position the arranged views with equal center-to-center spacing along the stack view’s axis, while maintaining the spacing property’s distance between views.
