---
title: 'AppChat: Using Peek and Pop APIs'
apple_id: TP40017298
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppChat/Listings/AppChat_MathUtilities_swift.html
archived_at: '2026-07-18T03:01:06.395977Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppChat: Using Peek and Pop APIs](AppChat-%20Using%20Peek%20and%20Pop%20APIs.md)


[Next](AppChat-Friend.swift.md)[Previous](AppChat-ChatReplyDismissAnimator.swift.md)

# AppChat/MathUtilities.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Various math utilities used throughout the app.
 */

import CoreGraphics

func clamp<T: Comparable>(value: T, minimum: T, maximum: T) -> T {
    return min(max(value, minimum), maximum)
}

func rotate(vector: CGVector, by radians: Double) -> CGVector {
    let dx = (vector.dx * CGFloat(cos(radians))) - (vector.dy * CGFloat(sin(radians)))
    let dy = (vector.dy * CGFloat(cos(radians))) + (vector.dx * CGFloat(sin(radians)))
    return CGVector(dx: dx, dy: dy)
}
```

[Next](AppChat-Friend.swift.md)[Previous](AppChat-ChatReplyDismissAnimator.swift.md)

