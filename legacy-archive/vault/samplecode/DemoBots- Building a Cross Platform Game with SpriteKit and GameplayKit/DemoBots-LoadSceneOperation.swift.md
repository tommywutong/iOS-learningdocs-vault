---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_LoadSceneOperation_swift.html
archived_at: '2026-07-18T03:06:19.945415Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-SceneOperation.swift.md)[Previous](DemoBots-LevelConfiguration.swift.md)

# DemoBots/LoadSceneOperation.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A subclass of `Operation` that manages the loading of a `BaseScene`.

*/

import Foundation

class LoadSceneOperation: SceneOperation, ProgressReporting {
    // MARK: Properties

    /// The metadata for the scene to load.
    let sceneMetadata: SceneMetadata

    /// The scene this operation is responsible for loading. Set after completion.
    var scene: BaseScene?

    /// Progress used to report on the status of this operation.
    let progress: Progress

    // MARK: Initialization

    init(sceneMetadata: SceneMetadata) {
        self.sceneMetadata = sceneMetadata

        progress = Progress(totalUnitCount: 1)
        super.init()
    }

    // MARK: NSOperation

    override func start() {
        // If the operation is cancelled there's nothing to do.
        guard !isCancelled else { return }

        if progress.isCancelled {
            // Ensure the operation is marked as `cancelled`.
            cancel()
            return
        }

        // Mark the operation as executing.
        state = .executing

        // Load the scene into memory using `SKNode(fileNamed:)`.
        let scene = sceneMetadata.sceneType.init(fileNamed: sceneMetadata.fileName)!
        self.scene = scene

        // Set up the scene's camera and native size.
        scene.createCamera()

        // Update the progress object's completed unit count.
        progress.completedUnitCount = 1

        state = .finished
    }
}
```

[Next](DemoBots-SceneOperation.swift.md)[Previous](DemoBots-LevelConfiguration.swift.md)

