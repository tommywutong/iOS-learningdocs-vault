---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_ButtonsViewController_swift.html
archived_at: '2026-07-18T03:27:28.356992Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-ProgressViewController.swift.md)[Previous](UIKitCatalog-TextFieldsViewController.swift.md)

# UIKitCatalog/ButtonsViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A view controller that demonstrates how to use `UIButton`. The buttons are created using storyboards, but the attributed text button has its text set in code.
*/

import UIKit

class ButtonsViewController: UIViewController {
    // MARK: Properties

    @IBOutlet weak var systemButton: UIButton!

    @IBOutlet weak var attributedTextButton: UIButton!

    override var preferredFocusEnvironments: [UIFocusEnvironment] {
        return [systemButton]
    }

    // MARK: UIViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        configureAttributedTextSystemButton()
    }

    // MARK: IB Actions

    @IBAction func buttonClicked(_ sender: AnyObject) {
        /*
            Clicking a button fires a UIControlEventPrimaryActionTriggered event.
            The buttons in this view controller have been setup in Interface Builder
            to call this action for the UIControlEventPrimaryActionTriggered event.
        */
        print("A button was clicked.")
    }

    // MARK: Convenience

    private func configureAttributedTextSystemButton() {
        let buttonTitle = NSLocalizedString("Button", comment: "")

        // Set the button's title for normal state.
        let normalTitleAttributes: [String : Any] = [
            NSForegroundColorAttributeName: UIColor.blue,
            NSStrikethroughStyleAttributeName: NSUnderlineStyle.styleSingle.rawValue
        ]
        let normalAttributedTitle = NSAttributedString(string: buttonTitle, attributes: normalTitleAttributes)
        attributedTextButton.setAttributedTitle(normalAttributedTitle, for: UIControlState())

        // Set the button's title for highlighted state.
        let highlightedTitleAttributes: [String : Any] = [
            NSForegroundColorAttributeName: UIColor.green,
            NSStrikethroughStyleAttributeName: NSUnderlineStyle.styleThick.rawValue
        ]
        let highlightedAttributedTitle = NSAttributedString(string: buttonTitle, attributes: highlightedTitleAttributes)
        attributedTextButton.setAttributedTitle(highlightedAttributedTitle, for: .highlighted)
    }
}
```

[Next](UIKitCatalog-ProgressViewController.swift.md)[Previous](UIKitCatalog-TextFieldsViewController.swift.md)

