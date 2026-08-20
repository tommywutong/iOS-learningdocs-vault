---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_LevelSceneFailState_swift.html
archived_at: '2026-07-18T03:06:19.348497Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-GeometryExtensions.swift.md)[Previous](DemoBots-KeyboardControlInputSource.swift.md)

# DemoBots/LevelSceneFailState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state used by `LevelScene` to indicate that the player failed to complete a level.
*/

import SpriteKit
import GameplayKit

class LevelSceneFailState: LevelSceneOverlayState {
    // MARK: Properties

    override var overlaySceneFileName: String {
        return "FailScene"
    }

    // MARK: GKState Life Cycle

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        if let inputComponent = levelScene.playerBot.component(ofType: InputComponent.self) {
            inputComponent.isEnabled = false
        }
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        return false
    }
}
```

[Next](DemoBots-GeometryExtensions.swift.md)[Previous](DemoBots-KeyboardControlInputSource.swift.md)

