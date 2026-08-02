---
title: 'Badger: Advanced Rendering in SceneKit'
apple_id: TP40017309
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: SceneKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Badger/Listings/Common_CAAnimation_SceneName_swift.html
archived_at: '2026-07-18T03:01:42.750058Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Badger: Advanced Rendering in SceneKit](Badger-%20Advanced%20Rendering%20in%20SceneKit.md)


[Next](README.md.md)[Previous](Common-ViewController%2BControls.swift.md)

# Common/CAAnimation+SceneName.swift

```swift
/*
     Copyright (C) 2016 Apple Inc. All Rights Reserved.
     See LICENSE.txt for this sample’s licensing information

     Abstract:
     An extension on CAAnimation used to load animations from an SCNScene.
 */

import SceneKit

// MARK: Core Animation

extension CAAnimation {
    class func animation(withSceneName name: String) -> CAAnimation {
        guard let scene = SCNScene(named: name) else {
            fatalError("Failed to find scene with name \(name).")
        }

        var animation: CAAnimation?
        scene.rootNode.enumerateChildNodes { (child, stop) in
            guard let firstKey = child.animationKeys.first else { return }
            animation = child.animation(forKey: firstKey)
            stop.initialize(to: true)
        }

        guard let foundAnimation = animation else {
            fatalError("Failed to find animation named \(name).")
        }

        foundAnimation.fadeInDuration = 0.3
        foundAnimation.fadeOutDuration = 0.3
        foundAnimation.repeatCount = 1

        return foundAnimation
    }
}
```

[Next](README.md.md)[Previous](Common-ViewController%2BControls.swift.md)

