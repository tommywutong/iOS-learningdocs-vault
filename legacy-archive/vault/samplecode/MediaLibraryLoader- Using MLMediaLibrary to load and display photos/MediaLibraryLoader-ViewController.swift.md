---
title: 'MediaLibraryLoader: Using MLMediaLibrary to load and display photos'
apple_id: TP40017375
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2016-11-03'
source_url: https://developer.apple.com/library/archive/samplecode/MediaLibraryLoader/Listings/MediaLibraryLoader_ViewController_swift.html
archived_at: '2026-07-18T03:14:33.563495Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MediaLibraryLoader: Using MLMediaLibrary to load and display photos](MediaLibraryLoader-%20Using%20MLMediaLibrary%20to%20load%20and%20display%20photos.md)


[Next](MediaLibraryLoader-AppDelegate.swift.md)[Previous](LICENSE.txt.md)

# MediaLibraryLoader/ViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The `ViewController` class is a subclass to NSViewController responsible for managing the app's content.
 */

import Cocoa
import MediaLibrary

class IconViewBox : NSBox {
    override func hitTest(_ aPoint: NSPoint) -> NSView? {
        // Don't allow any mouse clicks for subviews in this NSBox.
        return nil
    }
}

// MARK: -

class ViewController: NSViewController, NSCollectionViewDelegate {

    // MARK: - Types

    // Keys describing the dictionary for each photo loaded.
    private struct ItemKeys {
        static let imageKey = "icon"
        static let nameKey = "name"
    }

    // MLMediaLibrary property values for KVO.
    private struct MLMediaLibraryPropertyKeys {
        static let mediaSourcesKey = "mediaSources"
        static let rootMediaGroupKey = "rootMediaGroup"
        static let mediaObjectsKey = "mediaObjects"
        static let contentTypeKey = "contentType"
    }

    // MARK: - Properties

    /**
     The KVO contexts for `MLMediaLibrary`.
     This provides a stable address to use as the `context` parameter for KVO observation methods.
     */
    private var mediaSourcesContext = 1
    private var rootMediaGroupContext = 2
    private var mediaObjectsContext = 3

    private var photoSize = CGSize(width: 168, height: 145)

    // Contains an array of dictionaries describing each photo (refer to ItemKeys for key/values).
    @IBOutlet weak var arrayController: NSArrayController!

    @IBOutlet weak var collectionView: NSCollectionView!
    @IBOutlet private weak var noPhotosLabel: NSTextField!
    @IBOutlet private weak var activityIndicator: NSProgressIndicator!

    // MLMediaLibrary instances for loading the photos.
    private var mediaLibrary: MLMediaLibrary!
    private var mediaSource: MLMediaSource!
    private var rootMediaGroup: MLMediaGroup!

    // MARK: - View Controller Lifecycle

    override func viewDidLoad() {

        super.viewDidLoad()

        // Start progress indicator in case fetching the photos from the photo library takes time.
        self.activityIndicator.isHidden = false
        self.activityIndicator.startAnimation(self)

        self.collectionView.minItemSize = self.photoSize
        self.collectionView.maxItemSize = self.photoSize

        self.arrayController.setSelectionIndex(-1)  // No selection to start out with.

        // Setup the media library to load only photos, don't include other source types.
        let options: [String : AnyObject] =
            [MLMediaLoadSourceTypesKey: MLMediaSourceType.image.rawValue as AnyObject,
             MLMediaLoadIncludeSourcesKey: [MLMediaSourcePhotosIdentifier, MLMediaSourceiPhotoIdentifier] as AnyObject]

        // Create our media library instance to get our photo.
        mediaLibrary = MLMediaLibrary(options: options)

        // We want to be called when media sources come in that's available (via observeValueForKeyPath).
        self.mediaLibrary.addObserver(self,
                                      forKeyPath: MLMediaLibraryPropertyKeys.mediaSourcesKey,
                                      options: NSKeyValueObservingOptions.new,
                                      context: &mediaSourcesContext)

        if (self.mediaLibrary.mediaSources != nil) {} // Reference returns nil but starts the asynchronous loading.
    }

    deinit {

        // Make sure to remove us as an observer before "mediaLibrary" is released.
        self.mediaLibrary.removeObserver(self, forKeyPath: MLMediaLibraryPropertyKeys.mediaSourcesKey, context:&mediaSourcesContext)
    }

    // MARK: - NSCollectionViewDataSource

    func numberOfSectionsInCollectionView(_ collectionView: NSCollectionView) -> Int {

        return 1
    }

    func collectionView(_ collectionView: NSCollectionView, numberOfItemsInSection section: Int) -> Int {

        let photos = self.arrayController.arrangedObjects as! NSArray
        return photos.count
    }

    func collectionView(_ collectionView: NSCollectionView, itemForRepresentedObjectAtIndexPath indexPath: IndexPath) -> NSCollectionViewItem {

        let item = collectionView.makeItem(withIdentifier: "IconItem", for:indexPath)
        let photos = self.arrayController.arrangedObjects as! NSArray
        let iconInfo = photos[(indexPath as NSIndexPath).item]
        item.representedObject = iconInfo
        return item
    }

    // MARK: - NSCollectionViewDelegate

    func collectionView(_ collectionView: NSCollectionView, didSelectItemsAt indexPaths: Set<IndexPath>) {

        if let itemIndexPath = indexPaths.first {
            let photos = self.arrayController.arrangedObjects as! NSArray
            let itemDict = photos[((itemIndexPath as NSIndexPath).item)] as! NSDictionary
            if let itemTitle = itemDict[ItemKeys.nameKey] as? String {
                if (itemTitle.characters.count > 0) {
                    print("selected photo: '\(itemTitle)'")
                }
                else {
                    print("selected photo: <no title>")
                }
            }
        }
    }

    // MARK: - Utilities

    /// Helps to make sure the media object is the photo format we want.
    private func isValidImage(_ mediaObject: MLMediaObject) -> Bool {

        var isValidImage = false

        let attrs = mediaObject.attributes
        let contentTypeStr = attrs[MLMediaLibraryPropertyKeys.contentTypeKey] as! String

        // We only want photos, not movies or older PICT formats (PICT image files are not supported in a sandboxed environment).
        if ((contentTypeStr != kUTTypePICT as String) && (contentTypeStr != kUTTypeQuickTimeMovie as String))
        {
            isValidImage = true
        }

        return isValidImage
    }

    /// Obtains the title of the MLMediaObject (either the meta name or the last component of the URL).
    func imageTitle(_ fromMediaObject: MLMediaObject) -> String {

        guard let title = fromMediaObject.attributes["name"] else {
            return fromMediaObject.url!.lastPathComponent
        }
        return title as! String
    }


    // MARK: - Photo Loading

    /// Observer for all key paths returned from the MLMediaLibrary.
    override func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {

        if (keyPath == MLMediaLibraryPropertyKeys.mediaSourcesKey && context == &mediaSourcesContext && object! is MLMediaLibrary) {

            // The media sources have loaded, we can access the its root media.

            if let mediaSource = self.mediaLibrary.mediaSources?[MLMediaSourcePhotosIdentifier] {
                self.mediaSource = mediaSource
            }
            else if let mediaSource = self.mediaLibrary.mediaSources?[MLMediaSourceiPhotoIdentifier] {
                self.mediaSource = mediaSource
            }
            else {
                // Can't find any media sources.
                self.noPhotosLabel.isHidden = false

                // Stop progress indicator.
                self.activityIndicator.isHidden = true
                self.activityIndicator.stopAnimation(self)

                return  // No photos found.
            }

            // Media Library is loaded now, we can access mediaSource for photos
            self.mediaSource.addObserver(self,
                                         forKeyPath: MLMediaLibraryPropertyKeys.rootMediaGroupKey,
                                         options: NSKeyValueObservingOptions.new,
                                         context: &rootMediaGroupContext)

            // Obtain the media grouping (reference returns nil but starts asynchronous loading).
            if (self.mediaSource.rootMediaGroup != nil) {}
        }
        else if (keyPath == MLMediaLibraryPropertyKeys.rootMediaGroupKey && context == &rootMediaGroupContext && object! is MLMediaSource) {

            // The root media group is loaded, we can access the media objects.

            // Done observing for media groups.
            self.mediaSource.removeObserver(self, forKeyPath: MLMediaLibraryPropertyKeys.rootMediaGroupKey, context:&rootMediaGroupContext)

            self.rootMediaGroup = self.mediaSource.rootMediaGroup
            self.rootMediaGroup.addObserver(self,
                                            forKeyPath: MLMediaLibraryPropertyKeys.mediaObjectsKey,
                                            options: NSKeyValueObservingOptions.new,
                                            context: &mediaObjectsContext)

            // Obtain the all the photos, (reference returns nil but starts asynchronous loading).
            if (self.rootMediaGroup.mediaObjects != nil) {}
        }
        else if (keyPath == MLMediaLibraryPropertyKeys.mediaObjectsKey && context == &mediaObjectsContext && object! is MLMediaGroup) {

            // The media objects are loaded, we can now finally access each photo.

            // Done observing for media objects that group.
            self.rootMediaGroup.removeObserver(self, forKeyPath: MLMediaLibraryPropertyKeys.mediaObjectsKey, context:&mediaObjectsContext)

            // Stop progress indicator since we know if we have photos (or not).
            self.activityIndicator.isHidden = true
            self.activityIndicator.stopAnimation(self)

            let mediaObjects = self.rootMediaGroup.mediaObjects
            if (mediaObjects != nil && mediaObjects!.count > 0) {
                // Add photos to the array, to be used in our NSCollectionView.
                for mediaObject in mediaObjects! {
                    if (self.isValidImage(mediaObject)) {    // Make sure the media object is a photo.

                        let title = self.imageTitle(mediaObject)

                        if let image = NSImage.init(contentsOf: mediaObject.thumbnailURL!) {
                            let iconItem : Dictionary = [ItemKeys.imageKey: image, ItemKeys.nameKey: title] as [String : Any]
                            self.arrayController.addObject(iconItem)
                        }
                    }
                }

                self.collectionView.reloadData()

            }
            else {
                // No photos available.
                self.noPhotosLabel.isHidden = false
            }

            self.rootMediaGroup = nil // We are done with this.
        }
        else {
            super.observeValue(forKeyPath: keyPath, of: object, change: change, context: context)
        }
    }

}
```

[Next](MediaLibraryLoader-AppDelegate.swift.md)[Previous](LICENSE.txt.md)

