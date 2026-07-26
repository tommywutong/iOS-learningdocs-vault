---
title: UIStackView.Distribution
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistackview/distribution-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/distribution-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/distribution-swift.enum.json'
content_hash: 'sha256:12c29aaa170644bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# UIStackView.Distribution

<sub>Enumeration</sub>

The layout that defines the size and position of the arranged views along the stack view’s axis.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Distribution
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIStackViewDistributionFill](distribution-swift.enum/fill.md) — A layout where the stack view resizes its arranged views so that they fill the available space along the stack view’s axis.
- [UIStackViewDistributionFillEqually](distribution-swift.enum/fillequally.md) — A layout where the stack view resizes all arranged views to the same size, filling the available space along the stack view’s axis.
- [UIStackViewDistributionFillProportionally](distribution-swift.enum/fillproportionally.md) — A layout where the stack view resizes views proportionally based on their intrinsic content size to fill the available space along the stack view’s axis.
- [UIStackViewDistributionEqualSpacing](distribution-swift.enum/equalspacing.md) — A layout where the stack view maintains equal spacing between adjacent views while preserving their intrinsic content size.
- [UIStackViewDistributionEqualCentering](distribution-swift.enum/equalcentering.md) — A layout that attempts to position the arranged views with equal center-to-center spacing along the stack view’s axis, while maintaining the spacing property’s distance between views.

### Initializers

- [init(rawValue:)](<distribution-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [Alignment](alignment-swift.enum.md) — The layout of arranged views perpendicular to the stack view’s axis.
