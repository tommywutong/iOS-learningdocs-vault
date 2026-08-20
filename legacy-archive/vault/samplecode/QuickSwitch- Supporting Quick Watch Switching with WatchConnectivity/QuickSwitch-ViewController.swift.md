---
title: 'QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity'
apple_id: TP40016647
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: WatchConnectivity
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/QuickSwitch/Listings/QuickSwitch_ViewController_swift.html
archived_at: '2026-07-18T03:21:46.180330Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity](QuickSwitch-%20Supporting%20Quick%20Watch%20Switching%20with%20WatchConnectivity.md)


[Next](QuickSwitch-AppDelegate.swift.md)[Previous](LICENSE.txt.md)

# QuickSwitch/ViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The `ViewController` class that handles interface updates based on the changing of the `WCSession`.
*/

import UIKit
import WatchConnectivity

class ViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource, WatchConnectivityManagerPhoneDelegate {
    // MARK: Properties

    let colorMapping = [
        "Gray":   UIColor.darkGray,
        "Blue":   UIColor(red: 0.42, green: 0.70, blue: 0.88, alpha: 1),
        "Green":  UIColor(red: 0.71, green: 0.84, blue: 0.31, alpha: 1),
        "Yellow": UIColor(red: 0.95, green: 0.88, blue: 0.15, alpha: 1),
        "Orange": UIColor(red: 0.96, green: 0.63, blue: 0.20, alpha: 1),
        "Red":    UIColor(red: 0.96, green: 0.42, blue: 0.42, alpha: 1)
    ]

    struct MorseCode {
        let text: String
        let code: String
    }

    let morseCodes = [
                         MorseCode(text: "WWDC", code: ".-- .-- -.. -.-."),
                         MorseCode(text: "is", code: ".. ..."),
                         MorseCode(text: "fun", code: "..-. ..- -."),
                         MorseCode(text: "exciting", code: ". -..- -.-. .. - .. -. --."),
                         MorseCode(text: "educational", code: ". -.. ..- -.-. .- - .. --- -. .- .-.."),
                         MorseCode(text: "social", code: "... --- -.-. .. .- .-..")
                         ]

    @IBOutlet weak var deviceDesignator: UILabel!

    override func viewDidLoad() {
        super.viewDidLoad()

        // The `WatchConnectivityManager` will provide tailored callbacks to its delegate.
        WatchConnectivityManager.sharedConnectivityManager.delegate = self
    }

    // MARK: WatchConnectivityManagerDelegate

    func watchConnectivityManager(_ watchConnectivityManager: WatchConnectivityManager, updatedWithDesignator designator: String, designatorColor: String) {
        DispatchQueue.main.async(execute: {
            self.view.backgroundColor = self.colorMapping[designatorColor] ?? UIColor.white
            self.deviceDesignator.text = designator
        })
    }

    // MARK: UIPicker

    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }

    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return morseCodes.count
    }

    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        let morseCode = morseCodes[row]
        return "\(morseCode.text) [\(morseCode.code)]"
    }

    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        WCSession.default().transferUserInfo(["MorseCode": morseCodes[row].code as AnyObject])
    }
}
```

[Next](QuickSwitch-AppDelegate.swift.md)[Previous](LICENSE.txt.md)

