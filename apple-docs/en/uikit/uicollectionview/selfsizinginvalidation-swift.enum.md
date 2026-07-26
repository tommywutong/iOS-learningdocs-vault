---
title: UICollectionView.SelfSizingInvalidation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum.json'
content_hash: 'sha256:cf1141c860e90fd1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# UICollectionView.SelfSizingInvalidation

<sub>Enumeration</sub>

Constants that describe modes for invalidating the size of self-sizing collection view cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum SelfSizingInvalidation
```

## Discussion

Use these constants with the [selfSizingInvalidation](selfsizinginvalidation-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UICollectionViewSelfSizingInvalidationDisabled](selfsizinginvalidation-swift.enum/disabled.md) — A mode that disables self-sizing invalidation.
- [UICollectionViewSelfSizingInvalidationEnabled](selfsizinginvalidation-swift.enum/enabled.md) — A mode that enables manual self-sizing invalidation.
- [UICollectionViewSelfSizingInvalidationEnabledIncludingConstraints](selfsizinginvalidation-swift.enum/enabledincludingconstraints.md) — A mode that enables automatic self-sizing invalidation after Auto Layout changes.

### Initializers

- [init(rawValue:)](<selfsizinginvalidation-swift.enum/init(rawvalue_).md>)

## See Also

### Resizing self-sizing cells

- [selfSizingInvalidation](selfsizinginvalidation-swift.property.md) — The mode that the collection view uses for invalidating the size of self-sizing cells.
