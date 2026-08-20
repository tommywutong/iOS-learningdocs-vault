---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_SceneLoaderResourcesReadyState_swift.html
archived_at: '2026-07-18T03:06:21.282089Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Protocols-ContactNotifiableType.swift.md)[Previous](DemoBots-SceneOverlay.swift.md)

# DemoBots/SceneLoaderResourcesReadyState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state used by `SceneLoader` to indicate that all of the resources for the scene are loaded into memory and ready for use. This is the final state in the `SceneLoader`'s state machine.
*/

import GameplayKit

class SceneLoaderResourcesReadyState: GKState {
    // MARK: Properties

    unowned let sceneLoader: SceneLoader

    // MARK: Initialization

    init(sceneLoader: SceneLoader) {
        self.sceneLoader = sceneLoader
    }

    // MARK: GKState Life Cycle

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        // Clear the `sceneLoader`'s progress as loading is complete. 
        sceneLoader.progress = nil

        // Notify to any interested objects that the download has completed.
        NotificationCenter.default.post(name: NSNotification.Name.SceneLoaderDidCompleteNotification, object: sceneLoader)
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        switch stateClass {
            case is SceneLoaderResourcesAvailableState.Type, is SceneLoaderInitialState.Type:
                return true

            default:
                return false
        }
    }

    override func willExit(to nextState: GKState) {
        super.willExit(to: nextState)

        /*
            Presenting the scene is a one shot operation. Clear the scene when 
            exiting the ready state.
        */
        sceneLoader.scene = nil
    }
}
```

[Next](DemoBots-Protocols-ContactNotifiableType.swift.md)[Previous](DemoBots-SceneOverlay.swift.md)

