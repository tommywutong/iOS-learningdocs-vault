---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_SceneLoaderDownloadingResourcesState_swift.html
archived_at: '2026-07-18T03:06:20.942721Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-GameControllerInputSource.swift.md)[Previous](DemoBots-BaseScene%2BScreenRecording.swift.md)

# DemoBots/SceneLoaderDownloadingResourcesState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state used by `SceneLoader` to indicate that the loader is currently downloading on demand resources.
*/

import GameplayKit

class SceneLoaderDownloadingResourcesState: GKState {
    // MARK: Properties

    unowned let sceneLoader: SceneLoader

    /// Optionally progress directly to preparing state when download completes.
    var enterPreparingStateWhenFinished = false

    // MARK: Initialization

    init(sceneLoader: SceneLoader) {
        self.sceneLoader = sceneLoader
    }

    // MARK: GKState Life Cycle

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        // Clear any previous errors, and begin downloading the scene's resources. 
        sceneLoader.error = nil
        beginDownloadingScene()
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        switch stateClass {
            case is SceneLoaderDownloadFailedState.Type, is SceneLoaderResourcesAvailableState.Type, is SceneLoaderPreparingResourcesState.Type:
                return true

            default:
                return false
        }
    }

    // MARK: Downloading Actions

    /// Downloads the scene into local storage.
    private func beginDownloadingScene() {
        /*
            Create a new bundle request every time downloading needs to begin 
            because `NSBundleResourceRequest`s are single use objects.
        */
        let bundleResourceRequest = NSBundleResourceRequest(tags: sceneLoader.sceneMetadata.onDemandResourcesTags)

        // Hold onto the new resource request. 
        sceneLoader.bundleResourceRequest = bundleResourceRequest

        // Begin downloading the on demand resources.
        bundleResourceRequest.beginAccessingResources { error in

            // Progress to the next appropriate state from the main queue.
            DispatchQueue.main.async {
                if let error = error {
                    // Release the resources because we'll need to start a new request.
                    bundleResourceRequest.endAccessingResources()

                    // Set the error on the sceneLoader. 
                    self.sceneLoader.error = error

                    self.stateMachine!.enter(SceneLoaderDownloadFailedState.self)
                }
                else if self.enterPreparingStateWhenFinished {
                    // If requested, proceed to the preparing state immediately.
                    self.stateMachine!.enter(SceneLoaderPreparingResourcesState.self)
                }
                else {
                    self.stateMachine!.enter(SceneLoaderResourcesAvailableState.self)
                }
            }
        }
    }
}
```

[Next](DemoBots-GameControllerInputSource.swift.md)[Previous](DemoBots-BaseScene%2BScreenRecording.swift.md)

