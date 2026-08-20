---
title: Unit Testing Apps and Frameworks
apple_id: DTS40011742
resource_type: Sample Code
platform: iOS|macOS
topic: Xcode
technology: null
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/UnitTests/Listings/Calc_Calc_CalcViewController_swift.html
archived_at: '2026-07-18T03:27:33.844768Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Unit Testing Apps and Frameworks](Unit%20Testing%20Apps%20and%20Frameworks.md)


[Next](ReadMe.md.md)[Previous](Calc-Calc-AppDelegate.swift.md)

# Calc/Calc/CalcViewController.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements the UI of a calculator. Calls the Calculator class to implement the
         associated operation when tapping a character in the calculator.
*/

import UIKit
import CalculatorKit

class CalcViewController: UIViewController {
    // MARK: - Properties

    var calculator = Calculator()
    @IBOutlet weak var display: UITextField!

    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    // MARK: - Handle Tapped Character

    @IBAction func tap(_ sender: UIButton) {
        if let label = sender.titleLabel?.text {
            do {
                try calculator.input(label)
                display.text = calculator.displayValue
            } catch let error {
                print("\(error.localizedDescription)")
            }
        }
    }
}
```

[Next](ReadMe.md.md)[Previous](Calc-Calc-AppDelegate.swift.md)

