---
title: 'Flags: A demonstration of automatic RTL support in Asset Catalogs and UIStackViews'
apple_id: TP40017471
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/Flags/Listings/Flags_DataViewController_swift.html
archived_at: '2026-07-18T03:08:46.457489Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Flags: A demonstration of automatic RTL support in Asset Catalogs and UIStackViews](Flags-%20A%20demonstration%20of%20automatic%20RTL%20support%20in%20Asset%20Catalogs%20and%20UIStackVie.md)


[Next](Flags-AppDelegate.swift.md)[Previous](Flags-RootViewController.swift.md)

# Flags/DataViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The Data View Controller displays a flag, and controls the 'Reveal' button for showing the answer.
*/

import UIKit

class DataViewController: UIViewController {
    // MARK: Properties

    @IBOutlet weak var answerLabel: UILabel!

    @IBOutlet weak var flagLabel: UILabel!

    @IBOutlet weak var revealButton: UIButton!

    var regionCode: String? {
        didSet {
            if let regionCode = regionCode {
                // Offset for flags range in Unicode.
                flag = ""
                let base: UInt32 = 127397

                for character in regionCode.unicodeScalars {
                    guard let unicodeScalar = UnicodeScalar(base + character.value) else {
                        // `base` + `character.value` is an invalid unicode scalar value.
                        continue
                    }
                    flag?.append(String(unicodeScalar))
                }
            }
            else {
                flag = nil
            }
        }
    }

    private var flag: String?

    // MARK: UIViewController

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        guard let regionCode = regionCode else { fatalError("No region code has been set") }

        answerLabel.text = Locale.current.localizedString(forRegionCode: regionCode)
        flagLabel.text = flag

        answerLabel.isHidden = true
        revealButton.isHidden = false
    }

    @IBAction func revealAnswer(sender: UIButton) {
        answerLabel.isHidden = false
        revealButton.isHidden = true
    }
}
```

[Next](Flags-AppDelegate.swift.md)[Previous](Flags-RootViewController.swift.md)

