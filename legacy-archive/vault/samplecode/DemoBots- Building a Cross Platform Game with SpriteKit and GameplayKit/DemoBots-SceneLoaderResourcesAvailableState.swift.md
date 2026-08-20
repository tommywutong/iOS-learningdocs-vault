---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_SceneLoaderResourcesAvailableState_swift.html
archived_at: '2026-07-18T03:06:21.227542Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Shaders-Teleport.fsh.md)[Previous](DemoBots-ResourceLoadableType.swift.md)

# DemoBots/SceneLoaderResourcesAvailableState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state used by `SceneLoader` to indicate that all of the resources for the scene are available.
*/

import GameplayKit

class SceneLoaderResourcesAvailableState: GKState {
    // MARK: Properties

    unowned let sceneLoader: SceneLoader

    // MARK: Initialization

    init(sceneLoader: SceneLoader) {
        self.sceneLoader = sceneLoader
    }

    // MARK: GKState Life Cycle

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        switch stateClass {
            case is SceneLoaderInitialState.Type, is SceneLoaderPreparingResourcesState.Type:
                return true

            default:
                return false
        }
    }

}
```

[Next](DemoBots-Shaders-Teleport.fsh.md)[Previous](DemoBots-ResourceLoadableType.swift.md)

