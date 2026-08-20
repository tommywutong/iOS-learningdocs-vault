---
title: 'RawExpose: Using CIRAWFilter to Decode RAW Images'
apple_id: TP40017310
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreImage
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/RawExpose/Listings/RawExposeEmbedded_AlbumCollectionViewController_swift.html
archived_at: '2026-07-18T03:21:56.766345Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RawExpose: Using CIRAWFilter to Decode RAW Images](RawExpose-%20Using%20CIRAWFilter%20to%20Decode%20RAW%20Images.md)


[Next](README.md.md)[Previous](RawExposeEmbedded-ImageViewController.swift.md)

# RawExposeEmbedded/AlbumCollectionViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Application Album View.
*/

import UIKit
import Photos

/**
        This UICollectionViewController displayes all albums from
        the Photos library.
 */
class AlbumCollectionViewController: UICollectionViewController {
    // MARK: Properties

    let lightboxSegueName = "LightboxSegue"

    /// Array of albums displayed in this UICollectionView
    var albums = [PHAssetCollection]()


    /// Requests all album and smart albums collections to be fetched.
    override func viewDidLoad() {
        super.viewDidLoad()

        PHPhotoLibrary.requestAuthorization { status in
            guard status == .authorized else { return }

            // Fetch all albums
            PHAssetCollection.fetchAssetCollections(with: PHAssetCollectionType.album, subtype: PHAssetCollectionSubtype.any, options: nil).enumerateObjects( {
                (item, idx, flag) in self.albums.append(item)
            })

            // Fetch all smart albums
            PHAssetCollection.fetchAssetCollections(with: PHAssetCollectionType.smartAlbum, subtype: PHAssetCollectionSubtype.any, options: nil).enumerateObjects({
                (item, idx, flag) in self.albums.append(item)
            })

            OperationQueue.main.addOperation {
                // Ask the collection view to reload data, so the fetched albums is displayed.
                self.collectionView?.reloadData()
            }
        }
    }

    // MARK: UICollectionViewController delegate methods

    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return albums.count
    }

    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: AlbumCollectionViewCell.reuseIdentifier, for: indexPath) as? AlbumCollectionViewCell else { fatalError("Unable to dequeue an AlbumCollectionViewCell") }

        let collection = albums[indexPath.row]

        cell.imageView.image = nil
        cell.label.text = collection.localizedTitle

        if let firstAsset = PHAsset.fetchAssets(in: collection, options: PHFetchOptions()).firstObject {
            let options = PHImageRequestOptions()
            options.isSynchronous = true

            PHCachingImageManager.default().requestImage(for: firstAsset, targetSize: cell.bounds.size, contentMode: PHImageContentMode.aspectFit, options: options) {
                requestedImage, _ in cell.imageView.image = requestedImage
            }
        }

        return cell
    }

    // MARK: Storyboard seque

    override func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        performSegue(withIdentifier: lightboxSegueName, sender: albums[indexPath[1]])
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        guard let lightboxController = segue.destination as? LightboxCollectionViewController else { return }
        guard let collection = sender as? PHAssetCollection else { return }

        // Tell the Lightbox what collection do display 
        lightboxController.assetCollection = collection
    }
}
```

[Next](README.md.md)[Previous](RawExposeEmbedded-ImageViewController.swift.md)

