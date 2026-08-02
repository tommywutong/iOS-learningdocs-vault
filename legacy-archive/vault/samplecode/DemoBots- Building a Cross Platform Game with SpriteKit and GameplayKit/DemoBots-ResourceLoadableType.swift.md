---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_ResourceLoadableType_swift.html
archived_at: '2026-07-18T03:06:20.593874Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-SceneLoaderResourcesAvailableState.swift.md)[Previous](DemoBots-Physics-ColliderType.swift.md)

# DemoBots/ResourceLoadableType.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A protocol representing a type that loads resources into memory and keeps them around for future use. Classes adopt this protocol to indicate that they can preload SpriteKit textures and other resources in advance of when they will be needed, to improve performance when those resources are accessed.
*/

/// A type capable of loading and managing static resources.
protocol ResourceLoadableType: class {
    /// Indicates that static resources need to be loaded.
    static var resourcesNeedLoading: Bool { get }

    /// Loads static resources into memory.
    static func loadResources(withCompletionHandler completionHandler: @escaping () -> ())

    /// Releases any static resources that can be loaded again later.
    static func purgeResources()
}
```

[Next](DemoBots-SceneLoaderResourcesAvailableState.swift.md)[Previous](DemoBots-Physics-ColliderType.swift.md)

