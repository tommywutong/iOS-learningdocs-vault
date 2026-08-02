---
title: 'PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative
  and interruptible custom view controller transition'
apple_id: TP40017554
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoTransitioning/Listings/Photo_Transitioning_AssetTransitioningMath_swift.html
archived_at: '2026-07-18T03:18:55.622277Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative and interruptible custom view controller transition](PhotoTransitioning-%20Using%20UIViewPropertyAnimator%20to%20create%20a%20fully%20interative%20an.md)


[Next](Photo%20Transitioning-AssetViewController%2BAssetTransitioning.swift.md)[Previous](Photo%20Transitioning-AssetTransitioning.swift.md)

# Photo Transitioning/AssetTransitioningMath.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Convenience math operators
*/

import QuartzCore

func clip<T : Comparable>(_ x0: T, _ x1: T, _ v: T) -> T {
    return max(x0, min(x1, v))
}

func lerp<T : FloatingPoint>(_ v0: T, _ v1: T, _ t: T) -> T {
    return v0 + (v1 - v0) * t
}


func -(lhs: CGPoint, rhs: CGPoint) -> CGVector {
    return CGVector(dx: lhs.x - rhs.x, dy: lhs.y - rhs.y)
}

func -(lhs: CGPoint, rhs: CGVector) -> CGPoint {
    return CGPoint(x: lhs.x - rhs.dx, y: lhs.y - rhs.dy)
}

func -(lhs: CGVector, rhs: CGVector) -> CGVector {
    return CGVector(dx: lhs.dx - rhs.dx, dy: lhs.dy - rhs.dy)
}

func +(lhs: CGPoint, rhs: CGPoint) -> CGVector {
    return CGVector(dx: lhs.x + rhs.x, dy: lhs.y + rhs.y)
}

func +(lhs: CGPoint, rhs: CGVector) -> CGPoint {
    return CGPoint(x: lhs.x + rhs.dx, y: lhs.y + rhs.dy)
}

func +(lhs: CGVector, rhs: CGVector) -> CGVector {
    return CGVector(dx: lhs.dx + rhs.dx, dy: lhs.dy + rhs.dy)
}

func *(left: CGVector, right:CGFloat) -> CGVector {
    return CGVector(dx: left.dx * right, dy: left.dy * right)
}

extension CGPoint {
    var vector: CGVector {
        return CGVector(dx: x, dy: y)
    }
}

extension CGVector {
    var magnitude: CGFloat {
        return sqrt(dx*dx + dy*dy)
    }

    var point: CGPoint {
        return CGPoint(x: dx, y: dy)
    }

    func apply(transform t: CGAffineTransform) -> CGVector {
        return point.applying(t).vector
    }
}
```

[Next](Photo%20Transitioning-AssetViewController%2BAssetTransitioning.swift.md)[Previous](Photo%20Transitioning-AssetTransitioning.swift.md)

