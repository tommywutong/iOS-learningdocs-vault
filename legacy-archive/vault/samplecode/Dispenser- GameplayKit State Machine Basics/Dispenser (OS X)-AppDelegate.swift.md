---
title: 'Dispenser: GameplayKit State Machine Basics'
apple_id: TP40016460
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Listings/Dispenser__OS_X__AppDelegate_swift.html
archived_at: '2026-07-18T03:07:04.064443Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Dispenser: GameplayKit State Machine Basics](Dispenser-%20GameplayKit%20State%20Machine%20Basics.md)


[Next](Dispenser%20%28iOS%29-GameViewController.swift.md)[Previous](Dispenser%20%28OS%20X%29-GameViewController.swift.md)

# Dispenser (OS X)/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Application delegate for the OS X version of Dispenser.
*/

import Cocoa
import SpriteKit

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {    
    func applicationShouldTerminateAfterLastWindowClosed(_: NSApplication) -> Bool {
        return true
    }
}
```

[Next](Dispenser%20%28iOS%29-GameViewController.swift.md)[Previous](Dispenser%20%28OS%20X%29-GameViewController.swift.md)

