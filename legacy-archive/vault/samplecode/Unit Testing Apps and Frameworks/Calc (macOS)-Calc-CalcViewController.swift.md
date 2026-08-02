---
title: Unit Testing Apps and Frameworks
apple_id: DTS40011742
resource_type: Sample Code
platform: iOS|macOS
topic: Xcode
technology: null
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/UnitTests/Listings/Calc__macOS__Calc_CalcViewController_swift.html
archived_at: '2026-07-18T03:27:34.003121Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Unit Testing Apps and Frameworks](Unit%20Testing%20Apps%20and%20Frameworks.md)


[Next](Calc-CalcUITests-CalcUITests.swift.md)[Previous](Calc%20%28macOS%29-Calc-AppDelegate.swift.md)

# Calc (macOS)/Calc/CalcViewController.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements the UI of a calculator. Calls the Calculator class to implement the
         associated operation when pressing a character in the calculator.
*/

import Cocoa
import CalculatorKit

class CalcViewController: NSViewController {
    // MARK: - Properties

    @IBOutlet var display: NSTextField!
    var calculator = Calculator()

    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
    }

     // MARK: - Handle Pressed Character

    @IBAction func press(_ sender: NSButton) {
        do {
            try calculator.input(sender.title)
            display.stringValue = calculator.displayValue
        } catch let error {
            print("\(error.localizedDescription)")
        }
    }
}
```

[Next](Calc-CalcUITests-CalcUITests.swift.md)[Previous](Calc%20%28macOS%29-Calc-AppDelegate.swift.md)

