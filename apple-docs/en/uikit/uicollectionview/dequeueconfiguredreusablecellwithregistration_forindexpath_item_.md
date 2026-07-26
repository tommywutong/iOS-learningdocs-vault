---
title: 'dequeueConfiguredReusableCellWithRegistration:forIndexPath:item:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/dequeueconfiguredreusablecellwithregistration:forindexpath:item:'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/dequeueconfiguredreusablecellwithregistration:forindexpath:item:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/dequeueconfiguredreusablecellwithregistration%3Aforindexpath%3Aitem%3A.json'
content_hash: 'sha256:d7a6ce53d7fe68ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# dequeueConfiguredReusableCellWithRegistration:forIndexPath:item:

<sub>Instance Method</sub>

Dequeues a configured reusable cell object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UICollectionViewCell *) dequeueConfiguredReusableCellWithRegistration:(UICollectionViewCellRegistration *) registration forIndexPath:(NSIndexPath *) indexPath item:(id) item;
```

## Parameters

- `registration` — The cell registration for configuring the cell object. See [UICollectionViewCellRegistration](../uicollectionviewcellregistration.md).

- `indexPath` — The index path that specifies the location of the cell in the collection view.

- `item` — The item that provides data for the cell.

## Return Value

A configured reusable cell object.

## See Also

### Creating cells

- [UICollectionViewCellRegistration](../uicollectionviewcellregistration.md) — A registration for the collection view’s cells.
- [- registerClass:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-3vaho.md>) — Registers a class for use in creating new collection view cells.
- [- registerNib:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-6z6t4.md>) — Registers a nib file for use in creating new collection view cells.
- [- dequeueReusableCellWithReuseIdentifier:forIndexPath:](<dequeuereusablecell(withreuseidentifier_for_).md>) — Dequeues a reusable cell object located by its identifier.
