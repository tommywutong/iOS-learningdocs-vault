---
title: Quartz2D for iOS
apple_id: DTS40007531
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/samplecode/QuartzDemo/Listings/QuartzDemo_QuartzGradientViewController_swift.html
archived_at: '2026-07-18T03:21:35.133524Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz2D for iOS](Quartz2D%20for%20iOS.md)


[Next](QuartzDemo-QuartzMaskingView.swift.md)[Previous](QuartzDemo-QuartzImageView.swift.md)

# QuartzDemo/QuartzGradientViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A UIViewController subclass that manages a QuartzGradientView and a UI to allow for the selection of gradient type and if the gradient extends past its start or end point.
 */

import UIKit

class QuartzGradientViewController: UIViewController {

    @IBOutlet weak var quartzGradientView: QuartzGradientView!

    @IBOutlet weak var gradientTypeSegmentedControl: UISegmentedControl!

    @IBOutlet weak var extendsPastStartSwitch: UISwitch!

    @IBOutlet weak var extendsPastEndSwitch: UISwitch!


    override func viewDidLoad() {
        super.viewDidLoad()

        self.quartzGradientView.gradientTypeToDisplay = QuartzGradientView.GradientType(rawValue: self.gradientTypeSegmentedControl.selectedSegmentIndex)!
        self.quartzGradientView.extendsPastStart = self.extendsPastStartSwitch.isOn
        self.quartzGradientView.extendsPastEnd = self.extendsPastEndSwitch.isOn
    }



    @IBAction func takeGradientTypeFrom(_ sender: UISegmentedControl) {
        self.quartzGradientView.gradientTypeToDisplay = QuartzGradientView.GradientType(rawValue: self.gradientTypeSegmentedControl.selectedSegmentIndex)!
    }



    @IBAction func takeExtendsPastStartFrom(_ sender: UISegmentedControl) {
        self.quartzGradientView.extendsPastStart = self.extendsPastStartSwitch.isOn
    }



    @IBAction func takeExtendsPastEndFrom(_ sender: UISlider) {
        self.quartzGradientView.extendsPastEnd = self.extendsPastEndSwitch.isOn
    }

}
```

[Next](QuartzDemo-QuartzMaskingView.swift.md)[Previous](QuartzDemo-QuartzImageView.swift.md)

