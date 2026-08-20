---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_SceneOperation_swift.html
archived_at: '2026-07-18T03:06:21.627468Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-BaseScene%2BFocus.swift.md)[Previous](DemoBots-LoadSceneOperation.swift.md)

# DemoBots/SceneOperation.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A subclass of `NSOperation` that maps the different states of an `NSOperation`
        to an explicit `state` enum.
*/

import Foundation

class SceneOperation: Operation {
    // MARK: Types

    /**
        Using the `@objc` prefix exposes this enum to the ObjC runtime,
        allowing the use of `dynamic` on the `state` property.
    */
    @objc enum State: Int {
        /// The `Operation` is ready to begin execution.
        case ready

        /// The `Operation` is executing.
        case executing

        /// The `Operation` has finished executing.
        case finished

        /// The `Operation` has been cancelled.
        case cancelled
    }

    // MARK: Properties

    /// Marking `state` as dynamic allows this property to be key-value observed.
    dynamic var state = State.ready

    // MARK: NSOperation

    override var isExecuting: Bool {
        return state == .executing
    }

    override var isFinished: Bool {
        return state == .finished
    }

    override var isCancelled: Bool {
        return state == .cancelled
    }

    /**
        Add the "state" key to the key value observable properties of `NSOperation`.
    */
    class func keyPathsForValuesAffectingIsReady() -> Set<String> {
        return ["state"]
    }

    class func keyPathsForValuesAffectingIsExecuting() -> Set<String> {
        return ["state"]
    }

    class func keyPathsForValuesAffectingIsFinished() -> Set<String> {
        return ["state"]
    }

    class func keyPathsForValuesAffectingIsCancelled() -> Set<String> {
        return ["state"]
    }
}
```

[Next](DemoBots-BaseScene%2BFocus.swift.md)[Previous](DemoBots-LoadSceneOperation.swift.md)

