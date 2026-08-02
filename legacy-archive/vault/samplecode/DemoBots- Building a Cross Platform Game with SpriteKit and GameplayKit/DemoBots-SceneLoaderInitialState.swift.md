---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_SceneLoaderInitialState_swift.html
archived_at: '2026-07-18T03:06:21.017158Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-SceneLoaderDownloadFailedState.swift.md)[Previous](DemoBots-LevelSceneOverlayState.swift.md)

# DemoBots/SceneLoaderInitialState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The initial state of a `SceneLoader`. Determines which state should be entered at the beginning of the scene loading process.
*/

import GameplayKit

class SceneLoaderInitialState: GKState {
    // MARK: Properties

    unowned let sceneLoader: SceneLoader

    // MARK: Initialization

    init(sceneLoader: SceneLoader) {
        self.sceneLoader = sceneLoader
    }

    // MARK: GKState Life Cycle

    override func didEnter(from previousState: GKState?) {
        #if os(iOS) || os(tvOS)
        // Move the `stateMachine` to the available state if no on-demand resources are required.
        if !sceneLoader.sceneMetadata.requiresOnDemandResources {
            stateMachine!.enter(SceneLoaderResourcesAvailableState.self)
        }
        #elseif os(OSX)
        // On OS X the resources will always be in local storage available for download.
        _ = stateMachine!.enter(SceneLoaderResourcesAvailableState.self)
        #endif
    }

    override func isValidNextState(_  stateClass: AnyClass) -> Bool {
        #if os(iOS) || os(tvOS)
        if stateClass is SceneLoaderDownloadingResourcesState.Type {
            return true
        }
        #endif

        return stateClass is SceneLoaderResourcesAvailableState.Type
    }
}
```

[Next](DemoBots-SceneLoaderDownloadFailedState.swift.md)[Previous](DemoBots-LevelSceneOverlayState.swift.md)

