---
title: 'PhotoProgress: Using NSProgress'
apple_id: TP40016186
resource_type: Sample Code
platform: iOS
topic: null
technology: Foundation
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoProgress/Listings/PhotoProgress_PhotosCollectionViewController_swift.html
archived_at: '2026-07-18T03:18:53.718045Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoProgress: Using NSProgress](PhotoProgress-%20Using%20NSProgress.md)


[Next](PhotoProgress-AppDelegate.swift.md)[Previous](PhotoProgress-%20Using%20NSProgress.md)

# PhotoProgress/PhotosCollectionViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
                PhotosCollectionViewController is a UICollectionViewController subclass that has a reference to the Album.

*/

import UIKit

class PhotosCollectionViewController: UICollectionViewController {
    // MARK: Properties

    var album: Album? {
        didSet {
            collectionView?.reloadData()
        }
    }

    // MARK: UICollectionViewController

    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return album?.photos.count ?? 0
    }

    /**
        The cell that is returned must be retrieved from a call to 
        `dequeueReusableCellWithReuseIdentifier(_:forIndexPath:)`.
    */
    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Photo", for: indexPath) as! PhotoCollectionViewCell

        cell.photo = album?.photos[(indexPath as NSIndexPath).row]

        return cell
    }
}
```

[Next](PhotoProgress-AppDelegate.swift.md)[Previous](PhotoProgress-%20Using%20NSProgress.md)

