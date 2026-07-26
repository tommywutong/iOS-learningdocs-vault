---
title: 'dequeueReusableCell(withReuseIdentifier:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/dequeuereusablecell(withreuseidentifier:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/dequeuereusablecell(withreuseidentifier:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/dequeuereusablecell%28withreuseidentifier%3Afor%3A%29.json'
content_hash: 'sha256:661fd622f56424ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# dequeueReusableCell(withReuseIdentifier:for:)

<sub>Instance Method</sub>

Dequeues a reusable cell object located by its identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dequeueReusableCell(withReuseIdentifier identifier: String, for indexPath: IndexPath) -> UICollectionViewCell
```

## Parameters

- `identifier` — The reuse identifier for the specified cell. This parameter must not be `nil`.

- `indexPath` — The index path specifying the location of the cell. The data source receives this information when it is asked for the cell and should just pass it along. This method uses the index path to perform additional configuration based on the cell’s position in the collection view.

## Return Value

A valid [UICollectionReusableView](../uicollectionreusableview.md) object.

## Discussion

Call this method from your data source object when asked to provide a new cell for the collection view. This method dequeues an existing cell if one is available or creates a new one based on the class or nib file you previously registered.

> [!important] Important
> You must register a class or nib file using the [- registerClass:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-3vaho.md>) or [- registerNib:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-6z6t4.md>) method before calling this method.

If you registered a class for the specified `identifier` and a new cell must be created, this method initializes the cell by calling its [- initWithFrame:](<../uiview/init(frame_).md>) method. For nib-based cells, this method loads the cell object from the provided nib file. If an existing cell was available for reuse, this method calls the cell’s [- prepareForReuse](<../uicollectionreusableview/prepareforreuse().md>) method instead.

## See Also

### Creating cells

- [CellRegistration](cellregistration.md) — A registration for the collection view’s cells.
- [dequeueConfiguredReusableCell(using:for:item:)](<dequeueconfiguredreusablecell(using_for_item_).md>) — Dequeues a configured reusable cell object.
- [- registerClass:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-3vaho.md>) — Registers a class for use in creating new collection view cells.
- [- registerNib:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-6z6t4.md>) — Registers a nib file for use in creating new collection view cells.
