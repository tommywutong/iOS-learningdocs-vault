---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Nodes_ChargeBar_swift.html
archived_at: '2026-07-18T03:06:20.264006Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Nodes-ThumbStickNode.swift.md)[Previous](DemoBots-Nodes-ButtonNode.swift.md)

# DemoBots/Nodes/ChargeBar.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An `SKSpriteNode` subclass that displays a `PlayerBot`'s remaining charge.
*/

import SpriteKit

class ChargeBar: SKSpriteNode {
    // MARK: Static Properties

    struct Configuration {
        /// The size of the complete bar (back and level indicator).
        static let size = CGSize(width: 74.0, height: 10.0)

        /// The size of the colored level bar.
        static let chargeLevelNodeSize = CGSize(width: 70.0, height: 6.0)

        /// The duration used for actions to update the level indicator.
        static let levelUpdateDuration: TimeInterval = 0.1

        /// The background color.
        static let backgroundColor = SKColor.black

        /// The charge level node color.
        static let chargeLevelColor = SKColor.green
    }

    // MARK: Properties

    var level: Double = 1.0 {
        didSet {
            // Scale the level bar node based on the current health level.
            let action = SKAction.scaleX(to: CGFloat(level), duration: Configuration.levelUpdateDuration)
            action.timingMode = .easeInEaseOut

            chargeLevelNode.run(action)
        }
    }

    /// A node representing the charge level.
    let chargeLevelNode = SKSpriteNode(color: Configuration.chargeLevelColor, size: Configuration.chargeLevelNodeSize)

    // MARK: Initializers

    init() {
        super.init(texture: nil, color: Configuration.backgroundColor, size: Configuration.size)

        addChild(chargeLevelNode)

        // Constrain the position of the `chargeLevelNode`.
        let xRange = SKRange(constantValue: chargeLevelNode.size.width / -2.0)
        let yRange = SKRange(constantValue: 0.0)

        let constraint = SKConstraint.positionX(xRange, y: yRange)
        constraint.referenceNode = self

        chargeLevelNode.anchorPoint = CGPoint(x: 0.0, y: 0.5)
        chargeLevelNode.constraints = [constraint]
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

[Next](DemoBots-Nodes-ThumbStickNode.swift.md)[Previous](DemoBots-Nodes-ButtonNode.swift.md)

