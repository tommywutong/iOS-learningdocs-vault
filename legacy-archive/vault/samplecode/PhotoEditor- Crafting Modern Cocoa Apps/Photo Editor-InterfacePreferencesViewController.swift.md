---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_InterfacePreferencesViewController_swift.html
archived_at: '2026-07-18T03:18:49.330759Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-CanvasViewController.swift.md)[Previous](Photo%20Editor-AppDelegate.swift.md)

# Photo Editor/InterfacePreferencesViewController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 InterfacePreferencesViewController is a basic view controller to control the system settings. The "dark mode" check box is bound to the user defaults with the key "UseDarkMode". When the value changes a notification is manually sent out so all windows can switch to a dark mode.
*/

import Cocoa

class InterfacePreferencesViewController: NSViewController {

    @IBAction func didToggleDarkMode(_ sender: NSButton) {
        // The button is bound to the user default value "UseDarkMode". We send a notification when the value changes so the app can update its state based on it.
        NotificationCenter.default.post(name: .appearanceChanged, object: nil)
    }
}
```

[Next](Photo%20Editor-CanvasViewController.swift.md)[Previous](Photo%20Editor-AppDelegate.swift.md)

