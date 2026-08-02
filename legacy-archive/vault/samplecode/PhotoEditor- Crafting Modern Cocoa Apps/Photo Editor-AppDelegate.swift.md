---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_AppDelegate_swift.html
archived_at: '2026-07-18T03:18:48.844801Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-InterfacePreferencesViewController.swift.md)[Previous](Photo%20Editor-ImageSizeViewController.swift.md)

# Photo Editor/AppDelegate.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The skelaton application delegate implementation.
*/

import Cocoa

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {

    func applicationDidFinishLaunching(_ notification: Notification) {
        UserDefaults.standard.register(defaults: [ UserDefaults.useDarkModeKey.rawValue : false ])
    }

}
```

[Next](Photo%20Editor-InterfacePreferencesViewController.swift.md)[Previous](Photo%20Editor-ImageSizeViewController.swift.md)

