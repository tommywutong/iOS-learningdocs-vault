---
title: 'Geometric Primitives: Exact Orientation and Incircle Predicates using simd'
apple_id: TP40017307
resource_type: Sample Code
platform: iOS|macOS
topic: Performance
technology: Accelerate
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/GeometricPrimitives/Listings/Geometric_Primitives_playground_Pages_Incircle_xcplaygroundpage_Contents_swift.html
archived_at: '2026-07-18T03:10:43.699825Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Geometric Primitives: Exact Orientation and Incircle Predicates using simd](Geometric%20Primitives-%20Exact%20Orientation%20and%20Incircle%20Predicates%20using%20simd.md)


[Next](Geometric%20Primitives.playground-Pages-Predicates.xcplaygroundpage-Contents.swift.md)[Previous](Geometric%20Primitives.playground-Pages-Affine.xcplaygroundpage-Contents.swift.md)

# Geometric Primitives.playground/Pages/Incircle.xcplaygroundpage/Contents.swift

```
//: [Previous](@previous)
/*:
## Incircle / insphere predicates

`simd` also provides the `simd_incircle` and `simd_insphere` predicates, which determine if a point is inside, on, or outside the circle or sphere determined by three or four points in 2- or 3-dimensional space, respectively.
*/
import simd

//: As a simple example, consider the unit circle in two dimensions.  A circle is determined by three points, so let's choose three points on the circle in order:
let a = double2(-1,  0)
let b = double2( 0, -1)
let c = double2( 1,  0)

//: Now test to see if the origin lies inside the circle; the result is positive indicating that it is:
let x = double2(0, 0)
IncircleResult(simd_incircle(x, a, b, c))

//: For points *on* the circle, the result is zero ...:
let y = double2(0, 1)
IncircleResult(simd_incircle(y, a, b, c))

//: ... and if a point is outside the circle, the result is negative:
let z = double2(2, 0)
IncircleResult(simd_incircle(z, a, b, c))

//: If we change the order of the points `a`, `b`, and `c` so that they become negatively oriented, that changes the sense of "inside" and "outside" of the circle:
IncircleResult(simd_incircle(x, a, c, b))
IncircleResult(simd_incircle(z, a, c, b))
```

[Next](Geometric%20Primitives.playground-Pages-Predicates.xcplaygroundpage-Contents.swift.md)[Previous](Geometric%20Primitives.playground-Pages-Affine.xcplaygroundpage-Contents.swift.md)

