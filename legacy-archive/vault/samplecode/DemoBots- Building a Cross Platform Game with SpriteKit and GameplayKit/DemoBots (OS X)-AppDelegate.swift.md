---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots__OS_X__AppDelegate_swift.html
archived_at: '2026-07-18T03:06:22.017135Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](README.md.md)[Previous](DemoBots%20%28OS%20X%29-GameWindowController.swift.md)

# DemoBots (OS X)/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Application delegate for the OS X version of DemoBots.
*/

import Cocoa

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool {
        return true
    }
}
```

[Next](README.md.md)[Previous](DemoBots%20%28OS%20X%29-GameWindowController.swift.md)

