---
title: UICollectionView.CellRegistration
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/cellregistration
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/cellregistration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/cellregistration.json'
content_hash: 'sha256:e1fe1e1b43a9f8d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# UICollectionView.CellRegistration

<sub>Structure</sub>

A registration for the collection view’s cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct CellRegistration<Cell, Item> where Cell : UICollectionViewCell
```

## Overview

Use a cell registration to register cells with your collection view and configure each cell for display. You create a cell registration with your cell type and data item type as the registration’s generic parameters, passing in a registration handler to configure the cell. In the registration handler, you specify how to configure the content and appearance of that type of cell.

The following example creates a cell registration for cells of type [UICollectionViewListCell](../uicollectionviewlistcell.md). It creates a content configuration with a system default style, customizes the content and appearance of the configuration, and then assigns the configuration to the cell.

```swift
let cellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, Int> { cell, indexPath, item in
    
    var contentConfiguration = cell.defaultContentConfiguration()
    
    contentConfiguration.text = "\(item)"
    contentConfiguration.textProperties.color = .lightGray
    
    cell.contentConfiguration = contentConfiguration
}
```

After you create a cell registration, you pass it in to [dequeueConfiguredReusableCell(using:for:item:)](<dequeueconfiguredreusablecell(using_for_item_).md>), which you call from your data source’s cell provider.

```swift
dataSource = UICollectionViewDiffableDataSource<Section, Int>(collectionView: collectionView) {
    (collectionView: UICollectionView, indexPath: IndexPath, itemIdentifier: Int) -> UICollectionViewCell? in
    
    return collectionView.dequeueConfiguredReusableCell(using: cellRegistration,
                                                        for: indexPath,
                                                        item: itemIdentifier)
}
```

You don’t need to call [- registerNib:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-6z6t4.md>) or [- registerClass:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-3vaho.md>). The collection view registers your cell automatically when you pass the cell registration to [dequeueConfiguredReusableCell(using:for:item:)](<dequeueconfiguredreusablecell(using_for_item_).md>).

> [!important] Important
> Don’t create your cell registration inside a [CellProvider](../uicollectionviewdiffabledatasource-9tqpa/cellprovider.md) closure; doing so prevents cell reuse, and generates an exception in iOS 15 and higher.

## Topics

### Creating a cell registration

- [init(handler:)](<cellregistration/init(handler_).md>) — Creates a cell registration with the specified registration handler.
- [init(cellNib:handler:)](<cellregistration/init(cellnib_handler_).md>) — Creates a cell registration with the specified registration handler and nib file.
- [Handler](cellregistration/handler.md) — A closure that handles the cell registration and configuration.

## See Also

### Creating cells

- [dequeueConfiguredReusableCell(using:for:item:)](<dequeueconfiguredreusablecell(using_for_item_).md>) — Dequeues a configured reusable cell object.
- [- registerClass:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-3vaho.md>) — Registers a class for use in creating new collection view cells.
- [- registerNib:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-6z6t4.md>) — Registers a nib file for use in creating new collection view cells.
- [- dequeueReusableCellWithReuseIdentifier:forIndexPath:](<dequeuereusablecell(withreuseidentifier_for_).md>) — Dequeues a reusable cell object located by its identifier.
