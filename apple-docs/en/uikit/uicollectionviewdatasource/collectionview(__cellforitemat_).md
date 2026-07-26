---
title: 'collectionView(_:cellForItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdatasource/collectionview(_:cellforitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:cellforitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdatasource/collectionview%28_%3Acellforitemat%3A%29.json'
content_hash: 'sha256:4567bd7af70138b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDataSource](../uicollectionviewdatasource.md)

# collectionView(_:cellForItemAt:)

<sub>Instance Method</sub>

Asks your data source object for the cell that corresponds to the specified item in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell
```

## Parameters

- `collectionView` — The collection view requesting this information.

- `indexPath` — The index path that specifies the location of the item.

## Return Value

A configured cell object. You must not return `nil` from this method.

## Discussion

Your implementation of this method is responsible for creating, configuring, and returning the appropriate cell for the given item. You do this by calling the [- dequeueReusableCellWithReuseIdentifier:forIndexPath:](<../uicollectionview/dequeuereusablecell(withreuseidentifier_for_).md>) method of the collection view and passing the reuse identifier that corresponds to the cell type you want. That method always returns a valid cell object. Upon receiving the cell, you should set any properties that correspond to the data of the corresponding item, perform any additional needed configuration, and return the cell.

You don’t need to set the location of the cell inside the collection view’s bounds. The collection view sets the location of each cell automatically using the layout attributes provided by its layout object.

If [prefetchingEnabled](../uicollectionview/isprefetchingenabled.md) on the collection view is set to [true](../../swift/true.md) then this method is called in advance of the cell appearing. Use the [- collectionView:willDisplayCell:forItemAtIndexPath:](<../uicollectionviewdelegate/collectionview(__willdisplay_foritemat_).md>) delegate method to make any changes to the appearance of the cell to reflect its visual state such as selection.

This method must always return a valid view object.

## See Also

### Getting views for items

- [- collectionView:viewForSupplementaryElementOfKind:atIndexPath:](<collectionview(__viewforsupplementaryelementofkind_at_).md>) — Asks your data source object to provide a supplementary view to display in the collection view.
