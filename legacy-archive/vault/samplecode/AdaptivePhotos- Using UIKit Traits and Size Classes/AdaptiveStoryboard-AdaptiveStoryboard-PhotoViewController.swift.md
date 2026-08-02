---
title: 'AdaptivePhotos: Using UIKit Traits and Size Classes'
apple_id: TP40014636
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptivePhotos/Listings/AdaptiveStoryboard_AdaptiveStoryboard_PhotoViewController_swift.html
archived_at: '2026-07-18T03:00:44.903187Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptivePhotos: Using UIKit Traits and Size Classes](AdaptivePhotos-%20Using%20UIKit%20Traits%20and%20Size%20Classes.md)


[Next](AdaptiveStoryboard-AdaptiveStoryboard-RatingControl.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-OverlayView.swift.md)

# AdaptiveStoryboard/AdaptiveStoryboard/PhotoViewController.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A view controller that shows a photo and its metadata.
*/

import UIKit

class PhotoViewController: UIViewController {
    // MARK: Properties

    @IBOutlet fileprivate var imageView: UIImageView?
    @IBOutlet fileprivate var overlayView: OverlayView?
    @IBOutlet fileprivate var ratingControl: RatingControl?

    var photo: Photo?

    // MARK: View Controller

    override func viewDidLoad() {
        super.viewDidLoad()

        updatePhoto()
    }

    // MARK: IBActions

    /*
        Action for a change in value from the `RatingControl` (the user choose a
        different rating for the photo).
    */
    @IBAction func changeRating(_ sender: RatingControl) {
        photo?.rating = sender.rating
    }

    // MARK: Convenience

    // Updates the image view and meta data views with the data from the current photo.
    func updatePhoto() {
        imageView?.image = photo?.image
        overlayView?.text = photo?.comment
        ratingControl?.rating = photo?.rating ?? RatingControl.minimumRating
    }

    // This method is originally declared in the PhotoContents extension on UIViewController.
    override func containedPhoto() -> Photo? {
        return photo
    }
}
```

[Next](AdaptiveStoryboard-AdaptiveStoryboard-RatingControl.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-OverlayView.swift.md)

