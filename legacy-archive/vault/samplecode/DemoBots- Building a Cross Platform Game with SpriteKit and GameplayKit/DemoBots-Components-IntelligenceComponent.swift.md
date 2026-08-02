---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_IntelligenceComponent_swift.html
archived_at: '2026-07-18T03:06:16.976673Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-ShadowComponent.swift.md)[Previous](DemoBots-LevelScene%2BPause.swift.md)

# DemoBots/Components/IntelligenceComponent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `GKComponent` that provides a `GKStateMachine` for entities to use in determining their actions.
*/

import SpriteKit
import GameplayKit

class IntelligenceComponent: GKComponent {

    // MARK: Properties

    let stateMachine: GKStateMachine

    let initialStateClass: AnyClass

    // MARK: Initializers

    init(states: [GKState]) {
        stateMachine = GKStateMachine(states: states)
        let firstState = states.first!
        initialStateClass = type(of: firstState)
        super.init()
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    // MARK: GKComponent Life Cycle

    override func update(deltaTime seconds: TimeInterval) {
        super.update(deltaTime: seconds)

        stateMachine.update(deltaTime: seconds)
    }

    // MARK: Actions

    func enterInitialState() {
        stateMachine.enter(initialStateClass)
    }
}
```

[Next](DemoBots-Components-ShadowComponent.swift.md)[Previous](DemoBots-LevelScene%2BPause.swift.md)

