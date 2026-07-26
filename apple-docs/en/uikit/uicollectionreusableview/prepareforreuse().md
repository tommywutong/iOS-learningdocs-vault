---
title: prepareForReuse()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionreusableview/prepareforreuse()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionreusableview/prepareforreuse()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionreusableview/prepareforreuse%28%29.json'
content_hash: 'sha256:df7217a34b2a37ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionReusableView](../uicollectionreusableview.md)

# prepareForReuse()

<sub>Instance Method</sub>

Performs any clean up necessary to prepare the view for use again.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepareForReuse()
```

## Discussion

The default implementation of this method does nothing. Subclasses such as [UICollectionViewCell](../uicollectionviewcell.md) override this method and use it to perform relevant actions. So, if your subclass descends from [UICollectionViewCell](../uicollectionviewcell.md) or another intermediate class, call `super` to ensure that your class gets the parent’s behavior.

When the collection view dequeues your view for use, it calls this method before the corresponding dequeue method returns the view to your code. Override this method in your subclass to reset properties to their default values and make the view ready to use again. Don’t use this method to assign any new data to the view; that’s the responsibility of your data source object.

The collection view doesn’t call this method when you use [- reconfigureItemsAtIndexPaths:](<../uicollectionview/reconfigureitems(at_).md>) on `UICollectionView`, or [reconfigureItems(_:)](<../nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(__).md>) (Swift) or [- reconfigureItemsWithIdentifiers:](<../nsdiffabledatasourcesnapshotreference/reconfigureitems(withidentifiers_).md>) (Objective-C) on `NSDiffableDataSourceSnapshot` to update the contents of an existing cell.

## See Also

### Reusing cells

- [reuseIdentifier](reuseidentifier.md) — A string that identifies the purpose of the view.
