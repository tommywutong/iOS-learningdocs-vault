---
title: 'Geometric Primitives: Exact Orientation and Incircle Predicates using simd'
apple_id: TP40017307
resource_type: Sample Code
platform: iOS|macOS
topic: Performance
technology: Accelerate
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/GeometricPrimitives/Listings/Geometric_Primitives_playground_Pages_Affine_xcplaygroundpage_Contents_swift.html
archived_at: '2026-07-18T03:10:43.645226Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Geometric Primitives: Exact Orientation and Incircle Predicates using simd](Geometric%20Primitives-%20Exact%20Orientation%20and%20Incircle%20Predicates%20using%20simd.md)


[Next](Geometric%20Primitives.playground-Pages-Incircle.xcplaygroundpage-Contents.swift.md)[Previous](README.md.md)

# Geometric Primitives.playground/Pages/Affine.xcplaygroundpage/Contents.swift

```
/*:
[Previous](@previous)
## Affine orientation predicates

The vector orientation predicates discussed on the previous page allow one to orient a simplex (triangle or tetrahedron) with one vertex at the origin in 2- or 3-dimensional space.  Most of the time, however, a simplex that you want to orient does not have a vertex at the origin.
 */
import simd

let huge = Float(0x1.0p24)
var a = float3(1,     0,     0)
var b = float3(0,     1,     0)
var c = float3(0,     0,     1)
var d = float3(-huge, -huge, -huge)

/*:
A simplex like the tetrahedron with vertices (a, b, c, d) has *n+1* vertices, each of which is a point in *n* dimensional space.  The usual way to compute the orientation is to build the affine matrix whose columns are the vectors augmented with `1`:
~~~
 matrix = 1     0     0   -huge
          0     1     0   -huge
          0     0     1   -huge
          1     1     1     1
~~~
Simply computing this determinant happens to give the correct result for this case; these vectors are positively oriented:
*/
let matrix = float4x4([a, b, c, d].map{ return float4($0.x, $0.y, $0.z, 1) })
Orientation(matrix.determinant)

//: As we saw on the previous page, the determinant cannot be depended on to give the correct orientation in general.  To get a robust solution, we might try subtracting off one of the vertices and using `simd_orient(a-d, b-d, c-d)`:
Orientation(simd_orient(a-d, b-d, c-d))

/*:
Unfortuantely, this gives the wrong answer.  But `simd_orient` is exact!  What went wrong?  Subtracting `a-d` is not exact, so rounding error has been introduced before the arguments even reach the function.  `simd_orient` is exact, but it is exactly solving the wrong problem.

Fortunately there's an easy solution; `simd` also provides *affine* variants orientation functions, which solve exactly the problem we're trying to solve (orienting *n+1* vectors in *n*-dimensional space).
*/
Orientation(simd_orient(a, b, c, d))

//: [Next](@next)
```

[Next](Geometric%20Primitives.playground-Pages-Incircle.xcplaygroundpage-Contents.swift.md)[Previous](README.md.md)

