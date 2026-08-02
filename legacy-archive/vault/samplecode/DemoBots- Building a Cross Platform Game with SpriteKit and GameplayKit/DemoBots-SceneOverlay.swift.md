---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_SceneOverlay_swift.html
archived_at: '2026-07-18T03:06:21.697660Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-SceneLoaderResourcesReadyState.swift.md)[Previous](DemoBots-GeometryExtensions.swift.md)

# DemoBots/SceneOverlay.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A class to manage the display of an overlay set of nodes on top of an existing scene.
*/

import SpriteKit

class SceneOverlay {
    // MARK: Properties

    let backgroundNode: SKSpriteNode

    let contentNode: SKSpriteNode

    let nativeContentSize: CGSize

    // MARK: Intialization

    init(overlaySceneFileName fileName: String, zPosition: CGFloat) {
        // Load the scene and get the overlay node from it.
        let overlayScene = SKScene(fileNamed: fileName)!
        let contentTemplateNode = overlayScene.childNode(withName: "Overlay") as! SKSpriteNode

        // Create a background node with the same color as the template.
        backgroundNode = SKSpriteNode(color: contentTemplateNode.color, size: contentTemplateNode.size)
        backgroundNode.zPosition = zPosition

        // Copy the template node into the background node.
        contentNode = contentTemplateNode.copy() as! SKSpriteNode
        contentNode.position = .zero
        backgroundNode.addChild(contentNode)

        // Set the content node to a clear color to allow the background node to be seen through it.
        contentNode.color = .clear

        // Store the current size of the content to allow it to be scaled correctly.
        nativeContentSize = contentNode.size
    }

    func updateScale() {
        guard let viewSize = backgroundNode.scene?.view?.frame.size else {
            return
        }

        // Resize the background node.
        backgroundNode.size = viewSize

        // Scale the content so that the height always fits.
        let scale = viewSize.height / nativeContentSize.height
        contentNode.setScale(scale)
    }
}
```

[Next](DemoBots-SceneLoaderResourcesReadyState.swift.md)[Previous](DemoBots-GeometryExtensions.swift.md)

