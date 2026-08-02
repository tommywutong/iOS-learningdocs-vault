---
title: 'SimpleTunnel: Customized Networking Using the NetworkExtension Framework'
apple_id: TP40016140
resource_type: Sample Code
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleTunnel/Listings/SimpleTunnel_TextFieldCell_swift.html
archived_at: '2026-07-18T03:24:24.879783Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleTunnel: Customized Networking Using the NetworkExtension Framework](SimpleTunnel-%20Customized%20Networking%20Using%20the%20NetworkExtension%20Framework.md)


[Next](SimpleTunnel-ClientTunnelConnection.swift.md)[Previous](SimpleTunnel-ProxyServerAddEditController.swift.md)

# SimpleTunnel/TextFieldCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This file contains the TextFieldCell class, which is a UITableViewCell sub-class for a cell that contains a UITextField.
*/

import UIKit

/// A custom table view object that contains a text field.
class TextFieldCell : UITableViewCell, UITextFieldDelegate {

    // MARK: Properties

    /// The text input field.
    @IBOutlet weak var textField: UITextField!

    /// The block to call when the value of the text field changes.
    var valueChanged: ((Void) -> Void)?

    // MARK: UITextFieldDelegate

    /// Handle the event of the user finishing changing the value of the text field.
    func textFieldDidEndEditing(_ textField: UITextField) {
        textField.resignFirstResponder()

        valueChanged?()
    }

    /// Dismiss the keyboard
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
}
```

[Next](SimpleTunnel-ClientTunnelConnection.swift.md)[Previous](SimpleTunnel-ProxyServerAddEditController.swift.md)

