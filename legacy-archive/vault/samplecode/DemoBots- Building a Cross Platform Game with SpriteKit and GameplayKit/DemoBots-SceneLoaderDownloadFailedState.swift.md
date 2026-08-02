---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_SceneLoaderDownloadFailedState_swift.html
archived_at: '2026-07-18T03:06:20.904274Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-SceneManager.swift.md)[Previous](DemoBots-SceneLoaderInitialState.swift.md)

# DemoBots/SceneLoaderDownloadFailedState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state used by `SceneLoader` to indicate that the downloading of on demand resources failed.
*/

import GameplayKit

class SceneLoaderDownloadFailedState: GKState {
    // MARK: Properties

    unowned let sceneLoader: SceneLoader

    // MARK: Initialization

    init(sceneLoader: SceneLoader) {
        self.sceneLoader = sceneLoader
    }

    // MARK: GKState Life Cycle

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        // Clear the `sceneLoader`'s progress.
        sceneLoader.progress = nil

        // Notify any interested objects that the download has failed.
        NotificationCenter.default.post(name: NSNotification.Name.SceneLoaderDidFailNotification, object: sceneLoader)
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        return stateClass is SceneLoaderDownloadingResourcesState.Type
    }
}
```

[Next](DemoBots-SceneManager.swift.md)[Previous](DemoBots-SceneLoaderInitialState.swift.md)

