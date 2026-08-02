---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_CollectionViewContainerCell_swift.html
archived_at: '2026-07-18T03:27:28.406526Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-AppDelegate.swift.md)[Previous](UIKitCatalog-VideoPlayerViewController.swift.md)

# UIKitCatalog/CollectionViewContainerCell.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `UICollectionViewCell` subclass that contains a `UICollectionView`. This class demonstrates how to ensure the focus is passed to the contained collection view.
*/

import UIKit

class CollectionViewContainerCell: UICollectionViewCell, UICollectionViewDataSource, UICollectionViewDelegate {
    // MARK: Properties

    static let reuseIdentifier = "CollectionViewContainerCell"

    @IBOutlet var collectionView: UICollectionView!

    private var dataItems = [DataItem]()

    private let cellComposer = DataItemCellComposer()

    override var preferredFocusedView: UIView? {
        return collectionView
    }

    // MARK: Configuration

    func configure(with dataItems: [DataItem]) {
        self.dataItems = dataItems
        collectionView.reloadData()
    }

    // MARK: UICollectionViewDataSource

    func numberOfSections(in collectionView: UICollectionView) -> Int {
        return 1
    }

    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return dataItems.count
    }

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        return collectionView.dequeueReusableCell(withReuseIdentifier: DataItemCollectionViewCell.reuseIdentifier, for: indexPath)
    }

    // MARK: UICollectionViewDelegate

    func collectionView(_ collectionView: UICollectionView, willDisplay cell: UICollectionViewCell, forItemAt indexPath: IndexPath) {
        guard let cell = cell as? DataItemCollectionViewCell else { fatalError("Expected to display a DataItemCollectionViewCell") }
        let item = dataItems[(indexPath as NSIndexPath).row]

        // Configure the cell.
        cellComposer.compose(cell, withDataItem: item)
    }
}
```

[Next](UIKitCatalog-AppDelegate.swift.md)[Previous](UIKitCatalog-VideoPlayerViewController.swift.md)

