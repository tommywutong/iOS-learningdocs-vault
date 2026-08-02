---
title: 'SimpleTunnel: Customized Networking Using the NetworkExtension Framework'
apple_id: TP40016140
resource_type: Sample Code
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleTunnel/Listings/SimpleTunnel_ProxyAutoConfigScriptController_swift.html
archived_at: '2026-07-18T03:24:24.552647Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleTunnel: Customized Networking Using the NetworkExtension Framework](SimpleTunnel-%20Customized%20Networking%20Using%20the%20NetworkExtension%20Framework.md)


[Next](SimpleTunnel-OnDemandRuleListController.swift.md)[Previous](SimpleTunnel-ConnectionRuleAddEditController.swift.md)

# SimpleTunnel/ProxyAutoConfigScriptController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This file contains the ProxyAutoConfigScriptController class, which controls a view used to input the text of a Proxy Auto-Configuration Script.
*/

import UIKit
import NetworkExtension

/// A view controller object for a view that contains a text box where the user can enter a Proxy Auto-Configuration (PAC) script.
class ProxyAutoConfigScriptController: UIViewController {

    // MARK: Properties

    /// The text view containing the script.
    @IBOutlet weak var scriptText: UITextView!

    /// The block to call when the user taps on the "Done" button.
    var saveScriptCallback: (String?) -> Void = { script in return }

    // MARK: Interface

    /// Call the saveScriptCallback and transition back to the proxy settings view.
    @IBAction func saveScript(_ sender: AnyObject) {
        saveScriptCallback(scriptText.text)
        performSegue(withIdentifier: "save-proxy-script", sender: sender)
    }
}
```

[Next](SimpleTunnel-OnDemandRuleListController.swift.md)[Previous](SimpleTunnel-ConnectionRuleAddEditController.swift.md)

