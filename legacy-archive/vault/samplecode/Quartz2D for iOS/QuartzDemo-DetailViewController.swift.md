---
title: Quartz2D for iOS
apple_id: DTS40007531
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/samplecode/QuartzDemo/Listings/QuartzDemo_DetailViewController_swift.html
archived_at: '2026-07-18T03:21:34.544352Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz2D for iOS](Quartz2D%20for%20iOS.md)


[Next](QuartzDemo-QuartzGradientView.swift.md)[Previous](QuartzDemo-QuartzPDFView.swift.md)

# QuartzDemo/DetailViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A DetailViewController from the 'Master-Detail Application' template in Xcode 8.3.2.
 */


import UIKit

class DetailViewController: UIViewController {

    @IBOutlet weak var detailDescriptionLabel: UILabel!

    func configureView() {
        // Update the user interface for the detail item.
        if let detail = detailItem {
            if let label = detailDescriptionLabel {
                label.text = detail.description
            }
        }
    }



    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        configureView()
    }



    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }



    var detailItem: NSDate? {
        didSet {
            // Update the view.
            configureView()
        }
    }

}
```

[Next](QuartzDemo-QuartzGradientView.swift.md)[Previous](QuartzDemo-QuartzPDFView.swift.md)

