---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_LoadResourcesOperation_swift.html
archived_at: '2026-07-18T03:06:19.888308Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-SceneLoader.swift.md)[Previous](DemoBots-Nodes-ThumbStickNode.swift.md)

# DemoBots/LoadResourcesOperation.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A subclass of `Operation` that manages the loading of a `ResourceLoadableType`'s resources.

*/

import Foundation

class LoadResourcesOperation: SceneOperation, ProgressReporting {
    // MARK: Properties

    /// A class that conforms to the `ResourceLoadableType` protocol.
    let loadableType: ResourceLoadableType.Type

    let progress: Progress

    // MARK: Initialization

    init(loadableType: ResourceLoadableType.Type) {
        self.loadableType = loadableType

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

        // Avoid reloading the resources if they are already available.
        guard loadableType.resourcesNeedLoading else {
            finish()
            return
        }

        // Mark the operation as executing.
        state = .executing

        // Begin loading the resources.
        loadableType.loadResources() { [unowned self] in
            // Mark the operation as complete once the resources are loaded.
            self.finish()
        }
    }

    func finish() {
        progress.completedUnitCount = 1
        state = .finished
    }
}
```

[Next](DemoBots-SceneLoader.swift.md)[Previous](DemoBots-Nodes-ThumbStickNode.swift.md)

