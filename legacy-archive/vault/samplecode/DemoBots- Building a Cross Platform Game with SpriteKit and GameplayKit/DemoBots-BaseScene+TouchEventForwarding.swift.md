---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_BaseScene_TouchEventForwarding_swift.html
archived_at: '2026-07-18T03:06:15.780100Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-LevelScene%2BDebug.swift.md)[Previous](DemoBots-Utilities.swift.md)

# DemoBots/BaseScene+TouchEventForwarding.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An extension of `BaseScene` to provide iOS platform specific functionality. This file is only included in the iOS target.
*/

import UIKit

/*
    Extend `BaseScene` to forward events from the scene to a platform-specific
    control input source. On iOS, this is a `TouchControlInputNode`, which is
    overlaid on the scene to receive touch events.
*/
extension BaseScene {
    // MARK: Properties

    var touchControlInputNode: TouchControlInputNode {
        return sceneManager.gameInput.nativeControlInputSource as! TouchControlInputNode
    }

    // MARK: Setup Touch Handling

    func addTouchInputToScene() {
        guard let camera = camera else { fatalError("Touch input controls can only be added to a scene that has an associated camera.") }

        // Ensure the touch input source is not associated any other parent.
        touchControlInputNode.removeFromParent()

        if self is LevelScene {
            // Ensure the control node fills the scene's size.
            touchControlInputNode.size = size

            // Center the control node on the camera.
            touchControlInputNode.position = CGPoint.zero

            /*
                Assign a `zPosition` that is above in-game elements, but below the top
                layer where buttons are added.
            */
            touchControlInputNode.zPosition = WorldLayer.top.rawValue - CGFloat(1.0)

            // Add the control node to the camera node so the controls remain stationary as the camera moves.
            camera.addChild(touchControlInputNode)

            // Make sure the controls are visible.
            touchControlInputNode.hideThumbStickNodes = false
        }
    }
}
```

[Next](DemoBots-LevelScene%2BDebug.swift.md)[Previous](DemoBots-Utilities.swift.md)

