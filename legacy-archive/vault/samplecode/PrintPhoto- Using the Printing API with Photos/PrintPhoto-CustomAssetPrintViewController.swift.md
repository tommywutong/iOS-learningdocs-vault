---
title: 'PrintPhoto: Using the Printing API with Photos'
apple_id: DTS40010366
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: null
published: '2015-10-22'
source_url: https://developer.apple.com/library/archive/samplecode/PrintPhoto/Listings/PrintPhoto_CustomAssetPrintViewController_swift.html
archived_at: '2026-07-18T03:19:32.630558Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PrintPhoto: Using the Printing API with Photos](PrintPhoto.md)


[Next](PrintPhoto-StandardAssetPrintViewController.swift.md)[Previous](PrintPhoto-Assets.xcassets-CustomAssetPrintPageRenderer.swift.md)

# PrintPhoto/CustomAssetPrintViewController.swift

```swift
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `UIViewController` subclass to handle picking, viewing, and printing of a photo.
*/

import MobileCoreServices
import UIKit

class CustomAssetPrintViewController: UIViewController, UINavigationControllerDelegate {
    // MARK: Properties

    @IBOutlet weak var imageView: UIImageView!

    // MARK: Target / Action Methods

    /// Invoked when the user chooses the action icon for printing.
    @IBAction func shareImage() {
        guard let image = imageView.image else {
            fatalError("\(__FUNCTION__) expects image to not be nil.")
        }

        let printPageRenderer = CustomAssetPrintPageRenderer(image: image)

        // Create a print info object for the activity.
        let printInfo = UIPrintInfo.printInfo()

        /*
            This application prints photos. UIKit will pick a paper size and print
            quality appropriate for this content type.
        */
        printInfo.outputType = .Photo

        // Use the name from the image metadata we've set.
        printInfo.jobName = "Horse"

        // Give the print info and page renderer to UIKit.
        let printActivityItems: [AnyObject] = [
            printInfo,
            printPageRenderer
        ]

        /*
            Let the `UIActivityViewController` class handle presenting an action
            sheet that will let the user print the image.
        */
        let activityViewController = UIActivityViewController(activityItems: printActivityItems, applicationActivities: nil)

        presentViewController(activityViewController, animated: true, completion: nil)
    }
}
```

[Next](PrintPhoto-StandardAssetPrintViewController.swift.md)[Previous](PrintPhoto-Assets.xcassets-CustomAssetPrintPageRenderer.swift.md)

