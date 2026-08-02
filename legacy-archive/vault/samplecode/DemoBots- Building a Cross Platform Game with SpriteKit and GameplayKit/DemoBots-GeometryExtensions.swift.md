---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_GeometryExtensions_swift.html
archived_at: '2026-07-18T03:06:18.979220Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-SceneOverlay.swift.md)[Previous](DemoBots-LevelSceneFailState.swift.md)

# DemoBots/GeometryExtensions.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A series of extensions to provide convenience interoperation between `CGPoint` representations of geometric points (common in SpriteKit) and `float2` representations of points (common in GameplayKit).
*/

import CoreGraphics
import simd

// Extend `CGPoint` to add an initializer from a `float2` representation of a point.
extension CGPoint {
    // MARK: Initializers

    /// Initialize with a `float2` type.
    init(_ point: float2) {
        x = CGFloat(point.x)
        y = CGFloat(point.y)
    }
}

// Extend `float2` to add an initializer from a `CGPoint`.
extension float2 {
    // MARK: Initialization

    /// Initialize with a `CGPoint` type.
    init(_ point: CGPoint) {
        self.init(x: Float(point.x), y: Float(point.y))
    }
}

/*
    Extend `float2` to declare conformance to the `Equatable` protocol.
    The conformance to the protocol is provided by the `==` operator function below.
*/
extension float2: Equatable {}

/// An equality operator function to determine if two `float2`s are the same.
public func ==(lhs: float2, rhs: float2) -> Bool {
    return lhs.x == rhs.x && lhs.y == rhs.y
}

// Extend `float2` to provide a convenience method for working with pathfinding graphs.
extension float2 {
    /// Calculates the nearest point to this point on a line from `pointA` to `pointB`.
    func nearestPointOnLineSegment(lineSegment: (startPoint: float2, endPoint: float2)) -> float2 {
        // A vector from this point to the line start.
        let vectorFromStartToLine = self - lineSegment.startPoint

        // The vector that represents the line segment.
        let lineSegmentVector = lineSegment.endPoint - lineSegment.startPoint

        // The length of the line squared.
        let lineLengthSquared = distance_squared(lineSegment.startPoint, lineSegment.endPoint)

        // The amount of the vector from this point that lies along the line.
        let projectionAlongSegment = dot(vectorFromStartToLine, lineSegmentVector)

        // Component of the vector from the point that lies along the line.
        let componentInSegment = projectionAlongSegment / lineLengthSquared

        // Clamps the component between [0 - 1].
        let fractionOfComponent = max(0, min(1, componentInSegment))

        return lineSegment.startPoint + lineSegmentVector * fractionOfComponent
    }
}
```

[Next](DemoBots-SceneOverlay.swift.md)[Previous](DemoBots-LevelSceneFailState.swift.md)

