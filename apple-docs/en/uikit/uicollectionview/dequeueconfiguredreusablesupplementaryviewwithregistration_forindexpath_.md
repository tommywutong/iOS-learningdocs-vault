---
title: 'dequeueConfiguredReusableSupplementaryViewWithRegistration:forIndexPath:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/dequeueconfiguredreusablesupplementaryviewwithregistration:forindexpath:'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/dequeueconfiguredreusablesupplementaryviewwithregistration:forindexpath:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/dequeueconfiguredreusablesupplementaryviewwithregistration%3Aforindexpath%3A.json'
content_hash: 'sha256:7e645eee0ef95b68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# dequeueConfiguredReusableSupplementaryViewWithRegistration:forIndexPath:

<sub>Instance Method</sub>

Dequeues a configured reusable supplementary view object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UICollectionReusableView *) dequeueConfiguredReusableSupplementaryViewWithRegistration:(UICollectionViewSupplementaryRegistration *) registration forIndexPath:(NSIndexPath *) indexPath;
```

## Parameters

- `registration` — The supplementary registration for configuring the supplementary view object. See [UICollectionViewSupplementaryRegistration](../uicollectionviewsupplementaryregistration.md).

- `indexPath` — The index path that specifies the location of the supplementary view in the collection view.

## Return Value

A configured reusable supplementary view object.

## See Also

### Creating headers and footers

- [UICollectionViewSupplementaryRegistration](../uicollectionviewsupplementaryregistration.md) — A registration for the collection view’s supplementary views.
- [- registerClass:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-661io.md>) — Registers a class for use in creating supplementary views for the collection view.
- [- registerNib:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-9hn73.md>) — Registers a nib file for use in creating supplementary views for the collection view.
- [- dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:](<dequeuereusablesupplementaryview(ofkind_withreuseidentifier_for_).md>) — Dequeues a reusable supplementary view located by its identifier and kind.
