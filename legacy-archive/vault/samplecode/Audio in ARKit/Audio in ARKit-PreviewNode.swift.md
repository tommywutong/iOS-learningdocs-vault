---
title: Audio in ARKit
apple_id: TP40017668
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: ARKit
published: '2018-03-28'
source_url: https://developer.apple.com/library/archive/samplecode/AudioInARKit/Listings/Audio_in_ARKit_PreviewNode_swift.html
archived_at: '2026-07-18T03:01:25.504085Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio in ARKit](Audio%20in%20ARKit.md)


[Next](README.md.md)[Previous](Audio%20in%20ARKit-ARSCNView%2BHitTests.swift.md)

# Audio in ARKit/PreviewNode.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 SceneKit node wrapper that estimates an object's final placement
 */

import Foundation
import ARKit

class PreviewNode: SCNNode {

    // Saved positions that help smooth the movement of the preview
    var lastPositionOnPlane: float3?
    var lastPosition: float3?

    // Use average of recent positions to avoid jitter.
    private var recentPreviewNodePositions: [float3] = []

    // MARK: - Initialization

    override init() {
        super.init()
    }

    convenience init(node: SCNNode) {
        self.init()
        opacity = 0.5
        addChildNode(node)
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    // MARK: - Appearence

    func update(for position: float3, planeAnchor: ARPlaneAnchor?, camera: ARCamera?) {
        lastPosition = position
        if planeAnchor != nil {
            lastPositionOnPlane = position
        }
        updateTransform(for: position, camera: camera)
    }

    // MARK: - Private

    private func updateTransform(for position: float3, camera: ARCamera?) {
        // Add to the list of recent positions.
        recentPreviewNodePositions.append(position)

        // Remove anything older than the last 8 positions.
        recentPreviewNodePositions.keepLast(8)

        // Move to average of recent positions to avoid jitter.
        if let average = recentPreviewNodePositions.average {
            simdPosition = average
        }
    }
}
```

[Next](README.md.md)[Previous](Audio%20in%20ARKit-ARSCNView%2BHitTests.swift.md)

