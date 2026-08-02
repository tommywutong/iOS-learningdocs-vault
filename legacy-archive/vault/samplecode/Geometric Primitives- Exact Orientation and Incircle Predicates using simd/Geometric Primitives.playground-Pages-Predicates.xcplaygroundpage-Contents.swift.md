---
title: 'Geometric Primitives: Exact Orientation and Incircle Predicates using simd'
apple_id: TP40017307
resource_type: Sample Code
platform: iOS|macOS
topic: Performance
technology: Accelerate
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/GeometricPrimitives/Listings/Geometric_Primitives_playground_Pages_Predicates_xcplaygroundpage_Contents_swift.html
archived_at: '2026-07-18T03:10:43.737513Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Geometric Primitives: Exact Orientation and Incircle Predicates using simd](Geometric%20Primitives-%20Exact%20Orientation%20and%20Incircle%20Predicates%20using%20simd.md)


[Next](Geometric%20Primitives.playground-Sources-Support.swift.md)[Previous](Geometric%20Primitives.playground-Pages-Incircle.xcplaygroundpage-Contents.swift.md)

# Geometric Primitives.playground/Pages/Predicates.xcplaygroundpage/Contents.swift

```
/*:
# simd geometric primitives

## Overview
This file demonstrates the use of the robust orientation and incircle tests
introduced to the `simd` module in OS X 10.12 and iOS 10.

## Table of Contents
 * Vector orientation predicates
 * [Affine orientation predicates](Affine)
 * [Incircle predicates](Incircle)

Everything that we'll be demonstrating in this playground is based on the
simd module, so let's start by importing that.
*/
import simd

/*:
## Vector orientation predicates
An ordered tuple of *n* *n*-dimensional vectors is "positively oriented" if the determinant of the matrix whose columns (or rows) are the vectors in the same order is positive.  Equivalently, the orientation is the sign of the oriented area of the parallelepiped with vertices defined by the vectors and the origin.  Consult [Wikipedia](https://en.wikipedia.org/wiki/Determinant#2_.C3.97_2_matrices) for more details.

### A simple example
Let's consider a simple example to make this more concrete.  Suppose we're working in two dimensions, and have the vectors `u = (1,0)` and `v = (0,1)`.
*/
var u = float2(1, 0)
var v = float2(0, 1)

/*:
We can compute the determinant of the matrix whose columns are `u` and `v`:
~~~
determinant = u.x*v.y - u.y*v.x = 1*1 + 0*0 = 1
~~~
since this number is positive, the ordered pair of vectors `(u,v)` is positively-oriented.
*/
Orientation(float2x2([u,v]).determinant)

/*:
(`Orientation()`, defined in `Support.swift` in this playground, converts a floating-point number into one of `positive`, `negative`, `zero`, or `nan` to make these examples a little bit more readable.)

 In two dimensions, an equivalent definition of orientation is the sign of the z-component of the cross product of the two vectors:
*/
Orientation(cross(u,v).z)

/*:
It's also equivalent to saying that if we move around the triangle with vertices at `u`, `v`, and `0` in that order, we will be turning counter-clockwise (i.e. the interior of the triangle will be on our left).  This makes clear that the orientation depends not only on the vectors but also their ordering; the orientation changes if two vectors are swapped.

Rather than needing to remember an expression involving the cross product or determinant, and potentially getting the order wrong, you can use the `simd_orient(_:,_:)` function to compute the orientation of two vectors more easily.  It returns a positive number if the vectors are positively oriented, and a negative number if they are negatively oriented.
*/
Orientation(simd_orient(u,v))

/*:
### Numerical stability
In the preceeding examples, the vectors `u` and `v` were orthogonal unit vectors; their oriented area is not close to zero, so small rounding errors incurred in computing the determinant or cross product cannot effect the sign of the result.  If, however, we choose `u` and `v` that point very nearly in the same or opposite direction, this is not the case.  Because the oriented area is almost zero, small rounding errors could cause it to become zero or even have the wrong sign
*/
let tiny = Float(0x1.0p-23)
u = float2(1, 1+tiny)
v = float2(1-tiny, 1)

/*:
The exact determinant of the matrix with columns (u,v) is:
~~~
determinant = 1*1 - (1+tiny)*(1-tiny) = 1 - (1 - tiny**2) = tiny**2
~~~
This is a positive number, so the vectors are positively oriented.  However, we will see that both the determinant and the cross product produce the wrong result because of numerical rounding:
*/
// Should be positive, but may be zero due to rounding.
Orientation(float2x2([u,v]).determinant)

// Should be positive, but may be zero due to rounding.
Orientation(cross(u,v).z)

/*:
The `simd_orient` function uses *adaptive precision*; it first tries to use a simple computation of the determinant, and if it is sufficiently far away from zero, it returns that value.  However, if it is too nearly equal to zero, `simd_orient` uses a more careful computation that maintains precise error bounds to ensure that the final result has the right sign, even if the vectors are very nearly collinear, as in this case.
*/
// Correctly computed as positive.
Orientation(simd_orient(u,v))

/*:
This adaptive precision is the crucial feature of all the predicates that you'll see in this Playground.  They are always exact, even when that requires that extreme care be taken, while still delivering results as quickly as possible in the common case.  This is essential to ensure the stability of some algorithms that work with orientation and incircle tests.  Without this guarantee, they may produce incorrect results or simply loop forever.

 [Next](@next)
 */
```

[Next](Geometric%20Primitives.playground-Sources-Support.swift.md)[Previous](Geometric%20Primitives.playground-Pages-Incircle.xcplaygroundpage-Contents.swift.md)

