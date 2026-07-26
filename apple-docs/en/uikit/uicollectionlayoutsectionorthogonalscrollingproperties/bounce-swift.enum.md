---
title: UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum.json'
content_hash: 'sha256:5b9fc130c48187c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutSectionOrthogonalScrollingProperties](../uicollectionlayoutsectionorthogonalscrollingproperties.md)

# UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce

<sub>Enumeration</sub>

Constants that specify whether the orthogonal scrolling section bounces past the edge of content and back again.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Bounce
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Selecting bounce options

- [UICollectionLayoutSectionOrthogonalScrollingBounceAlways](bounce-swift.enum/always.md) — The orthogonal scroll view bounces even if the content is smaller than its bounds.
- [UICollectionLayoutSectionOrthogonalScrollingBounceAutomatic](bounce-swift.enum/automatic.md) — The orthogonal scroll view bounces when it encounters a content boundary.
- [UICollectionLayoutSectionOrthogonalScrollingBounceNever](bounce-swift.enum/never.md) — The orthogonal scroll view stops scrolling immediately when it encounters a content boundary without bouncing.

### Initializers

- [init(rawValue:)](<bounce-swift.enum/init(rawvalue_).md>)

## See Also

### Specifying the bounce behavior

- [bounce](bounce-swift.property.md) — A value that specifies whether the orthogonal scrolling section bounces past the edge of content and back again.
