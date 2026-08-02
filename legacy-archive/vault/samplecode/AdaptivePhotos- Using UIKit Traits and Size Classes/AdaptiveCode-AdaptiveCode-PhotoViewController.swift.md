---
title: 'AdaptivePhotos: Using UIKit Traits and Size Classes'
apple_id: TP40014636
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptivePhotos/Listings/AdaptiveCode_AdaptiveCode_PhotoViewController_swift.html
archived_at: '2026-07-18T03:00:44.089115Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptivePhotos: Using UIKit Traits and Size Classes](AdaptivePhotos-%20Using%20UIKit%20Traits%20and%20Size%20Classes.md)


[Next](AdaptiveCode-AdaptiveCode-RatingControl.swift.md)[Previous](AdaptiveCode-AdaptiveCode-OverlayView.swift.md)

# AdaptiveCode/AdaptiveCode/PhotoViewController.swift

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

    fileprivate var imageView: UIImageView?
    fileprivate var overlayView: OverlayView?
    fileprivate var ratingControl: RatingControl?

    var photo: Photo

    // MARK: Initialization

    init(photo: Photo) {
        self.photo = photo

        super.init(nibName: nil, bundle: nil)
    }

    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    // MARK: View Controller

    override func loadView() {
        let view = UIView()
        view.backgroundColor = UIColor.white

        let imageView = UIImageView()
        imageView.contentMode = .scaleAspectFit
        imageView.translatesAutoresizingMaskIntoConstraints = false
        self.imageView = imageView
        view.addSubview(imageView)

        let ratingControl = RatingControl()
        ratingControl.translatesAutoresizingMaskIntoConstraints = false
        ratingControl.addTarget(self, action: #selector(PhotoViewController.changeRating(_:)), for: .valueChanged)
        self.ratingControl = ratingControl
        view.addSubview(ratingControl)

        let overlayView = OverlayView()
        overlayView.translatesAutoresizingMaskIntoConstraints = false
        self.overlayView = overlayView
        view.addSubview(overlayView)

        updatePhoto()

        let views = [
            "imageView":        imageView,
            "ratingControl":    ratingControl,
            "overlayView":      overlayView
        ]

        var newConstraints = [NSLayoutConstraint]()

        newConstraints += NSLayoutConstraint.constraints(withVisualFormat: "|[imageView]|", options: [], metrics: nil, views: views)

        newConstraints += NSLayoutConstraint.constraints(withVisualFormat: "V:|[imageView]|", options: [], metrics: nil, views: views)

        newConstraints += NSLayoutConstraint.constraints(withVisualFormat: "[ratingControl]-20-|", options: [], metrics: nil, views: views)

        newConstraints += NSLayoutConstraint.constraints(withVisualFormat: "[overlayView]-20-|", options: [], metrics: nil, views: views)

        newConstraints += NSLayoutConstraint.constraints(withVisualFormat: "V:[overlayView]-[ratingControl]-20-|", options: [], metrics: nil, views: views)

        NSLayoutConstraint.activate(newConstraints)

        // Now add optional constraints.
        var optionalConstraints = [NSLayoutConstraint]()

        optionalConstraints += NSLayoutConstraint.constraints(withVisualFormat: "|-(>=20)-[ratingControl]", options: [], metrics: nil, views: views)

        optionalConstraints += NSLayoutConstraint.constraints(withVisualFormat: "|-(>=20)-[overlayView]", options: [], metrics: nil, views: views)

        // We want these constraints to be able to be broken if our interface is resized to be small enough that these margins don't fit.
        for constraint in optionalConstraints {
            constraint.priority = UILayoutPriorityRequired - 1
        }

        NSLayoutConstraint.activate(optionalConstraints)

        self.view = view
    }

    /*
        Action for a change in value from the `RatingControl` (the user choose a
        different rating for the photo).
    */
    func changeRating(_ sender: RatingControl) {
        photo.rating = sender.rating
    }

    // MARK: Convenience

    // Updates the image view and meta data views with the data from the current photo.
    func updatePhoto() {
        imageView?.image = photo.image
        overlayView?.text = photo.comment
        ratingControl?.rating = photo.rating
    }

    // This method is originally declared in the PhotoContents extension on UIViewController.
    override func containedPhoto() -> Photo? {
        return photo
    }
}
```

[Next](AdaptiveCode-AdaptiveCode-RatingControl.swift.md)[Previous](AdaptiveCode-AdaptiveCode-OverlayView.swift.md)

