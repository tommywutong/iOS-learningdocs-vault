---
title: 'Geometric Primitives: Exact Orientation and Incircle Predicates using simd'
apple_id: TP40017307
resource_type: Sample Code
platform: iOS|macOS
topic: Performance
technology: Accelerate
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/GeometricPrimitives/Listings/Geometric_Primitives_playground_Sources_Support_swift.html
archived_at: '2026-07-18T03:10:43.795186Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Geometric Primitives: Exact Orientation and Incircle Predicates using simd](Geometric%20Primitives-%20Exact%20Orientation%20and%20Incircle%20Predicates%20using%20simd.md)


[Next](Geometric%20Primitives.playground-Contents.swift.md)[Previous](Geometric%20Primitives.playground-Pages-Predicates.xcplaygroundpage-Contents.swift.md)

# Geometric Primitives.playground/Sources/Support.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Support code for the `simd` geometric primitive playground.
*/

import simd

/// Enum for possible results of an incircle test.
public enum IncircleResult {
    case insideCircle
    case onCircle
    case outsideCircle
    case nan

    /// Initialize incircle result from a floating-point value.
    public init<T: FloatingPoint>(_ value: T) {
        if value < T(0) { self = .outsideCircle }
        else if value > T(0) { self = .insideCircle }
        else if value == T(0) { self = .onCircle }
        else { self = .nan }
    }
}

/// Enum for possible results of an orientation test.
public enum Orientation {
    case positivelyOriented
    case degenerate
    case negativelyOriented
    case nan
    /// Initialize orientation result from a floating-point value.
    public init<T: FloatingPoint>(_ value: T) {
        if value < T(0) { self = .negativelyOriented }
        else if value > T(0) { self = .positivelyOriented }
        else if value == T(0) { self = .degenerate }
        else { self = .nan }
    }
}

public extension float2x2 {
    /// Determinant of `self`.
    var determinant: Float { return matrix_determinant(self.cmatrix) }
}
public extension float3x3 {
    /// Determinant of `self`.
    var determinant: Float { return matrix_determinant(self.cmatrix) }
}
public extension float4x4 {
    /// Determinant of `self`.
    var determinant: Float { return matrix_determinant(self.cmatrix) }
}
```

[Next](Geometric%20Primitives.playground-Contents.swift.md)[Previous](Geometric%20Primitives.playground-Pages-Predicates.xcplaygroundpage-Contents.swift.md)

