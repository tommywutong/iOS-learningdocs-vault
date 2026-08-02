---
title: 'Pathfinder: GameplayKit Pathfinding Basics'
apple_id: TP40016461
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/Pathfinder_GameplayKit/Listings/Pathfinder__OS_X__AppDelegate_swift.html
archived_at: '2026-07-18T03:18:48.175967Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Pathfinder: GameplayKit Pathfinding Basics](Pathfinder-%20GameplayKit%20Pathfinding%20Basics.md)


[Next](PathFinder-MazeBuilder.swift.md)[Previous](Pathfinder%20%28OS%20X%29-GameViewController.swift.md)

# Pathfinder (OS X)/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Application delegate for the OS X version of Pathfinder.
*/

import Cocoa
import SpriteKit

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {
    // MARK: Methods

    func applicationShouldTerminateAfterLastWindowClosed(_: NSApplication) -> Bool {
        return true
    }
}
```

[Next](PathFinder-MazeBuilder.swift.md)[Previous](Pathfinder%20%28OS%20X%29-GameViewController.swift.md)

