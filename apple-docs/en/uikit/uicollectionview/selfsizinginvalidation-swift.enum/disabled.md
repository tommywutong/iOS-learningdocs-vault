---
title: UICollectionView.SelfSizingInvalidation.disabled
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum/disabled
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum/disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum/disabled.json'
content_hash: 'sha256:d5d382791e7739e1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionView](../../uicollectionview.md) · [SelfSizingInvalidation](../selfsizinginvalidation-swift.enum.md)

# UICollectionView.SelfSizingInvalidation.disabled

<sub>Case</sub>

A mode that disables self-sizing invalidation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case disabled
```

## Discussion

If you use this self-sizing invalidation mode, no sizing updates occur after calling [- invalidateIntrinsicContentSize](<../../uiview/invalidateintrinsiccontentsize().md>) on a self-sizing cell or its [contentView](../../uicollectionviewcell/contentview.md).

## See Also

### Constants

- [UICollectionViewSelfSizingInvalidationEnabled](enabled.md) — A mode that enables manual self-sizing invalidation.
- [UICollectionViewSelfSizingInvalidationEnabledIncludingConstraints](enabledincludingconstraints.md) — A mode that enables automatic self-sizing invalidation after Auto Layout changes.
