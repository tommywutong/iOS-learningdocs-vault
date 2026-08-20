---
title: Quartz2D for iOS
apple_id: DTS40007531
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/samplecode/QuartzDemo/Listings/QuartzDemo_QuartzDashViewController_swift.html
archived_at: '2026-07-18T03:21:34.961111Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz2D for iOS](Quartz2D%20for%20iOS.md)


[Next](QuartzDemo-QuartzBlendingViewController.swift.md)[Previous](QuartzDemo-QuartzBezierView.swift.md)

# QuartzDemo/QuartzDashViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A UIViewController subclass that manages a QuartzDashView and a UI to allow for the selection of the line dash pattern and phase.
 */



import UIKit


class QuartzDashViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource
{


    @IBOutlet weak var quartzDashView: QuartzDashView!
    @IBOutlet weak var picker: UIPickerView!
    @IBOutlet weak var phaseSlider: UISlider!



    let patterns: [[CGFloat]] = [
        [10.0, 10.0],
        [10.0, 20.0, 10.0],
        [10.0, 20.0, 30.0],
        [10.0, 20.0, 10.0, 30.0],
        [10.0, 10.0, 20.0, 20.0],
        [10.0, 10.0, 20.0, 30.0, 50.0]
    ]



    override func viewDidLoad() {

        super.viewDidLoad()

        quartzDashView.dashPattern = patterns[0]

        picker.selectRow(0, inComponent:0, animated:false)
    }



    @IBAction func takeDashPhaseFrom(_ sender: UISlider) {
        quartzDashView.dashPhase = CGFloat(sender.value)
    }



    @IBAction func reset(_ sender: AnyObject) {
        phaseSlider.value = 0.0
        quartzDashView.dashPhase = 0.0
    }



    // UIPickerViewDelegate & UIPickerViewDataSource methods


    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }



    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return patterns.count
    }



    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        var p: [CGFloat] = patterns[row]
        var title = String(format:"%.0f", p[0])
        for i in 1..<p.count {
            title += String(format:"-%.0f", p[i])
        }
        return title
    }



    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        quartzDashView.dashPattern = patterns[row]
    }

}
```

[Next](QuartzDemo-QuartzBlendingViewController.swift.md)[Previous](QuartzDemo-QuartzBezierView.swift.md)

