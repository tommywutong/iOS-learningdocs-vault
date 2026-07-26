---
title: UICollectionView.SelfSizingInvalidation.enabled
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum/enabled
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum/enabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum/enabled.json'
content_hash: 'sha256:5414ab6eea7492f9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionView](../../uicollectionview.md) · [SelfSizingInvalidation](../selfsizinginvalidation-swift.enum.md)

# UICollectionView.SelfSizingInvalidation.enabled

<sub>Case</sub>

A mode that enables manual self-sizing invalidation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case enabled
```

## Discussion

If you use this self-sizing invalidation mode, calling [- invalidateIntrinsicContentSize](<../../uiview/invalidateintrinsiccontentsize().md>) on a self-sizing cell or its [contentView](../../uicollectionviewcell/contentview.md) causes the cell to resize if necessary.

## See Also

### Constants

- [UICollectionViewSelfSizingInvalidationDisabled](disabled.md) — A mode that disables self-sizing invalidation.
- [UICollectionViewSelfSizingInvalidationEnabledIncludingConstraints](enabledincludingconstraints.md) — A mode that enables automatic self-sizing invalidation after Auto Layout changes.
