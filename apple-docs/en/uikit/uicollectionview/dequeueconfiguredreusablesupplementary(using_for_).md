---
title: 'dequeueConfiguredReusableSupplementary(using:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/dequeueconfiguredreusablesupplementary(using:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/dequeueconfiguredreusablesupplementary(using:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/dequeueconfiguredreusablesupplementary%28using%3Afor%3A%29.json'
content_hash: 'sha256:74a7887f92445cbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# dequeueConfiguredReusableSupplementary(using:for:)

<sub>Instance Method</sub>

Dequeues a configured reusable supplementary view object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func dequeueConfiguredReusableSupplementary<Supplementary>(using registration: UICollectionView.SupplementaryRegistration<Supplementary>, for indexPath: IndexPath) -> Supplementary where Supplementary : UICollectionReusableView
```

## Parameters

- `registration` — The supplementary registration for configuring the supplementary view object. See [SupplementaryRegistration](supplementaryregistration.md).

- `indexPath` — The index path that specifies the location of the supplementary view in the collection view.

## Return Value

A configured reusable supplementary view object.

## See Also

### Creating headers and footers

- [SupplementaryRegistration](supplementaryregistration.md) — A registration for the collection view’s supplementary views.
- [- registerClass:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-661io.md>) — Registers a class for use in creating supplementary views for the collection view.
- [- registerNib:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-9hn73.md>) — Registers a nib file for use in creating supplementary views for the collection view.
- [- dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:](<dequeuereusablesupplementaryview(ofkind_withreuseidentifier_for_).md>) — Dequeues a reusable supplementary view located by its identifier and kind.
