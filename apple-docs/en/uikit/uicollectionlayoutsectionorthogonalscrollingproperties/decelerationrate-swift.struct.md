---
title: UICollectionLayoutSectionOrthogonalScrollingProperties.DecelerationRate
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/decelerationrate-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/decelerationrate-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/decelerationrate-swift.struct.json'
content_hash: 'sha256:3a86bc3e27fb238f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutSectionOrthogonalScrollingProperties](../uicollectionlayoutsectionorthogonalscrollingproperties.md)

# UICollectionLayoutSectionOrthogonalScrollingProperties.DecelerationRate

<sub>Structure</sub>

Constants that specify the rate of deceleration in the orthogonal scrolling section after the scrolling pan gesture ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct DecelerationRate
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Selecting deceleration rates

- [UICollectionLayoutSectionOrthogonalScrollingDecelerationRateAutomatic](decelerationrate-swift.struct/automatic.md) — A deceleration rate that matches the parent scroll view’s deceleration rate for the orthogonal scrolling section.
- [UICollectionLayoutSectionOrthogonalScrollingDecelerationRateFast](decelerationrate-swift.struct/fast.md) — A rapid deceleration rate for the orthogonal scrolling section.
- [UICollectionLayoutSectionOrthogonalScrollingDecelerationRateNormal](decelerationrate-swift.struct/normal.md) — The default deceleration rate for the orthogonal scrolling section.

### Creating a deceleration rate

- [init(rawValue:)](<decelerationrate-swift.struct/init(rawvalue_).md>) — Creates a deceleration rate.

## See Also

### Specifying the rate of deceleration

- [decelerationRate](decelerationrate-swift.property.md) — A value that specifies the rate of deceleration in the orthogonal scrolling section after the scrolling pan gesture ends.
