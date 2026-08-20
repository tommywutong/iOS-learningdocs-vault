---
title: 'Geometric Primitives: Exact Orientation and Incircle Predicates using simd'
apple_id: TP40017307
resource_type: Sample Code
platform: iOS|macOS
topic: Performance
technology: Accelerate
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/GeometricPrimitives/Listings/Geometric_Primitives_playground_Contents_swift.html
archived_at: '2026-07-18T03:10:43.573351Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Geometric Primitives: Exact Orientation and Incircle Predicates using simd](Geometric%20Primitives-%20Exact%20Orientation%20and%20Incircle%20Predicates%20using%20simd.md)


[Next](LICENSE.txt.md)[Previous](Geometric%20Primitives.playground-Sources-Support.swift.md)

# Geometric Primitives.playground/Contents.swift

```
/*:
# simd geometric predicates

## Overview

This file demonstrates the use of the robust orientation and incircle tests
introduced to the `simd` module in OS X 10.12 and iOS 10.0.

## Table of Contents

 * [Introduction to orientation predicates](Orientation)
 * [Affine orientation predicates](Affine)
 * [Incircle predicates](Incircle)
*/

import simd

/*: 
//  Orientation tests for vectors
//
//  An ordered tuple of N N-dimensional vectors is "positively oriented" if
//  the determinant of the matrix whose columns (or rows) are the vectors in
//  the same order is positive.  Equivalently, the orientation is the sign
//  of the oriented area of the parallelepiped with vertices defined by the
//  vectors and the origin.  Wikipedia has more details:
//
//    https://en.wikipedia.org/wiki/Determinant#2_.C3.97_2_matrices
//
//  Let's consider a simple example to make this more concrete.  Suppose we're
//  working in two dimensions, and have the vectors u = (1,0) and v = (0,1).

print("An easy example; u and v are orthogonal:")
var u = float2(1, 0)
var v = float2(0, 1)

//  The ordered pair (u,v) is positively oriented because the determinant of
//  the matrix with u and v as columns is positive:

print("Orientation computed by determinant is \(float2x2([u,v]).determinant.direction).")

//  Equivalently, if we extend u and v to three dimensions, the z-component
//  of their cross-product is positive:

print("Orientation computed by cross product is \(cross(u,v).z.direction).")

//  Positive orientation is also equivalent to saying that if we move around
//  the triangle with vertices at u, v, and the origin, in that order, we
//  will be turning counter-clockwise (so the interior of the triangle is
//  on our left).  The simd_orient function lets us check the orientation
//  directly:

print("Orientation computed by simd_orient is \(simd_orient(u,v).direction).\n")

//  Why do we need functions just to compute the orientation?  What's wrong
//  with simply using `cross(u,v).z`?
//
//  When working with orientation, we are only interested in the *sign* of
//  the oriented area; this is a discontinuous function of the vectors; it
//  jumps suddenly from "negative" to "zero" to "positive".  Because of this,
//  if the two vectors are very nearly colinear, small numerical error may
//  cause us to compute an entirely wrong result.  For a simple example of
//  this, consider what happens if we try to orient the vectors:

print("A difficult example; u and v are nearly colinear:")
let tiny = Float(0x1.0p-23)
u = float2(1, 1+tiny)
v = float2(1-tiny, 1)

//  The exact determinant of the matrix with columns (u,v) is:
//
//    determinant = 1*1 - (1+tiny)*(1-tiny)
//                = 1 - (1 - tiny**2)
//                = tiny**2
//
//  since this is a positive number, the vectors are positively oriented.
//  However, numerical rounding and cancellation can result in "zero"
//  being returned instead of "positive":

print("Orientation computed by determinant is \(float2x2([u,v]).determinant.direction).")
print("Orientation computed by cross product is \(cross(u,v).z.direction).")

//  The simd_orient function, however, uses "adaptive precision"; it
//  first tries a simple computation of the determinant, but if it 
//  determines that the result is sufficiently close to zero that it might
//  have been computed incorrectly, it will use a more sophisticated
//  computation, so that it delivers the right answer even if the vectors
//  are very nearly colinear:

print("Orientation computed by simd_orient is \(simd_orient(u,v).direction).\n")

//  This is the crucial feature of the new predicates defined in geometry.h.
//  They are always exact, even when that requires a signficiant amount of
//  extra computation, while still delivering results as quickly as possible.
//  This is essential for ensuring the stability of some algorithms that work
//  with triangle orientations; without this feature many of these algorithms
//  will loop forever.

print("Orienting 4 points in 3-dimensions:")
//  Sometimes you need to determine the orientation of a set of N+1 N-dimensional
//  points, instead of N vectors.  This corresponds to orienting a triangle or
//  parallelepiped that doesn't have the origin as a vertex.

let huge = Float(0x1.0p24)
var a = float3(1,     0,     0)
var b = float3(0,     1,     0)
var c = float3(0,     0,     1)
var d = float3(-huge, -huge, -huge)

//  Though it may not be obvious, the orientation of the points (a,b,c,d)
//  is positive.  The usual simple approach would be to compute the
//  determinant of the matrix whose columns are (a,b,c,d) augmented with a
//  row of ones.  This happens to give the correct result for this matrix,
//  but cannot be depended on to do so in general.
let matrix = float4x4([a,b,c,d].map{ float4($0.x, $0.y, $0.z, 1) })
print("Orientation computed by determinant of augmented matrix is \(matrix.determinant.direction)")

//  To get a more robust solution, we might try using simd_orient as described
//  above, but subtracting off d so that one of our points becomes the origin;
//  since this is just a translation in three-dimensional space, it does not
//  change the orientation of the tetrahedron in which we're interested.
//
//  Unfortunately, this doesn't work; even though simd_orient can compute
//  exact results, the subtraction causes rounding so the data is inexact
//  even before it is passed to simd_orient; the result is zero even though
//  it should be positive.
print("Orientation comptued by simd_orient(a-d, b-d, c-d) is \(simd_orient(a-d,b-d,c-d).direction)")

//  Fortunately, simd provides a solution to this problem.  The functions can
//  take N+1 points, and perform the entire comptuation (including the
//  subtraction) with additional precision if needed to deliver an exact
//  result.
print("Orientation comptuted by simd_orient(a, b, c, d) is \(simd_orient(a,b,c,d).direction)")
```

[Next](LICENSE.txt.md)[Previous](Geometric%20Primitives.playground-Sources-Support.swift.md)

