---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_TextFieldsViewController_swift.html
archived_at: '2026-07-18T03:27:29.447595Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-ButtonsViewController.swift.md)[Previous](UIKitCatalog-PageViewController.swift.md)

# UIKitCatalog/TextFieldsViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A view controller that demonstrates how customize the `inputAccessoryView` of `UITextField`s.
*/

import UIKit

class TextFieldsViewController: UIViewController {
    // MARK: Properties

    @IBOutlet var regularKeyboardTextField: UITextField!

    @IBOutlet var emailKeyboardTextField: UITextField!

    @IBOutlet var numberPadTextField: UITextField!

    @IBOutlet var numbersAndPunctuationKeyboardTextField: UITextField!

    // MARK: UIViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        // Specify custom input accessory fields for each text view.
        regularKeyboardTextField.inputAccessoryView = CustomInputAccessoryView(title: NSLocalizedString("Regular Text", comment: ""))
        emailKeyboardTextField.inputAccessoryView = CustomInputAccessoryView(title: NSLocalizedString("Email Address", comment: ""))
        numberPadTextField.inputAccessoryView = CustomInputAccessoryView(title: NSLocalizedString("Number Pad", comment: ""))
        numbersAndPunctuationKeyboardTextField.inputAccessoryView = CustomInputAccessoryView(title: NSLocalizedString("Numbers and Punctation", comment: ""))
    }
}
```

[Next](UIKitCatalog-ButtonsViewController.swift.md)[Previous](UIKitCatalog-PageViewController.swift.md)

