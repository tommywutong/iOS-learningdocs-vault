---
title: 'Fox: Building a SceneKit Game with the Xcode Scene Editor'
apple_id: TP40016154
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: General
technology: SceneKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Fox/Listings/Swift_OSX_AppDelegate_swift.html
archived_at: '2026-07-18T03:08:54.177908Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox: Building a SceneKit Game with the Xcode Scene Editor](Fox-%20Building%20a%20SceneKit%20Game%20with%20the%20Xcode%20Scene%20Editor.md)


[Next](Swift-Common-GameViewController.swift.md)[Previous](Swift-tvOS-AppDelegate.swift.md)

# Swift/OSX/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The OS X implementation of the application delegate of the game.
*/

import Cocoa

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {

    @IBOutlet weak var window: NSWindow!

    private func applicationShouldTerminate(afterLastWindowClosed sender: NSApplication) -> Bool {
        return true
    }

}
```

[Next](Swift-Common-GameViewController.swift.md)[Previous](Swift-tvOS-AppDelegate.swift.md)

