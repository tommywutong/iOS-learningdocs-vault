---
title: CoreGraphics Geometry Primitives
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/cggeometry/'
original_language: en
published: 2019-04-22
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:06591c48187c7dd9'
translated: false
---

> 原文：[CoreGraphics Geometry Primitives](https://nshipster.com/cggeometry/)　·　NSHipster (Mattt)

# [Core​Graphics Geometry Primitives](https://nshipster.com/cggeometry/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  April 22^nd, 2019 ([revised](https://github.com/nshipster/articles/commits/master/2019-04-22-cggeometry.md))

Unless you were a Math Geek or an Ancient Greek, Geometry probably wasn’t your favorite subject in school. More likely, you were that kid in class who dutifully programmed all of those necessary formulæ into your TI-8X calculator to avoid rote memorization.

So for those of you who spent more time learning TI-BASIC than Euclid, here’s the cheat-sheet for how geometry works in [Quartz 2D](https://developer.apple.com/library/mac/#documentation/graphicsimaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html), the drawing system used by Apple platforms:

![](https://nshipster.com/assets/core-graphics-primitives-669295da8c1112f066e80978b96f3f60de8236d450cc3a73e279357195d66bf7703327f02c4affa8775f6233f8f5274abe01d3dd63076fa28dcc6e2b8507fe03.svg)

<sub>CoreGraphics Primitives (iOS)</sub>

- A `CGFloat` represents a scalar quantity.
- A `CGPoint` represents a location in a two-dimensional coordinate system and is defined by `x` and `y` scalar components.
- A `CGVector` represents a change in position in 2D space and is defined by `dx` and `dy` scalar components.
- A `CGSize` represents the extent of a figure in 2D space and is defined by `width` and `height` scalar components.
- A `CGRect` represents a rectangle and is defined by an origin point (`CGPoint`) and a size (`CGSize`).

```
import CoreGraphics

let float: CGFloat = 1.0
let point = CGPoint(x: 1.0, y: 2.0)
let vector = CGVector(dx: 4.0, dy: 3.0)
let size = CGSize(width: 4.0, height: 3.0)
var rectangle = CGRect(origin: point, size: size)
```

![](https://nshipster.com/assets/core-graphics-coordinate-systems-483faf8b5ad2b37db24ac28089115ddc2c71d3a0bbb3b094e1bb9583fe95fbf5073461daed9379c8528d9d11594d990e0091605dc618a6be52fc0de689960f76.svg)

<sub>CoreGraphics Coordinates Systems (iOS)</sub>

On iOS, the origin is located at the top-left corner of a window, so `x` and `y` values increase as they move down and to the right. macOS, by default, orients `(0, 0)` at the bottom left corner of a window, such that `y` values increase as they move up.

---

Every view in an iOS or macOS app has a `frame` represented by a `CGRect` value, so one would do well to learn the fundamentals of these geometric primitives.

In this week’s article, we’ll do a quick run through the APIs with which every app developer should be familiar.

---

## Introspection

_“First, know thyself.”_ So goes the philosophical aphorism. And it remains practical guidance as we begin our survey of CoreGraphics API.

As structures, you can access the member values of geometric types directly through their stored properties:

```
point.x // 1.0
point.y // 2.0

size.width // 4.0
size.height // 3.0

rectangle.origin // {x 1 y 2}
rectangle.size // {w 4 h 3}
```

You can mutate variables by reassignment or by using mutating operators like `*=` and `+=`:

```
var mutableRectangle = rectangle // {x 1 y 2 w 4 h 3}
mutableRectangle.origin.x = 7.0
mutableRectangle.size.width *= 2.0
mutableRectangle.size.height += 3.0
mutableRectangle // {x 7 y 2 w 8 h 6}
```

For convenience, rectangles also expose `width` and `height` as top-level, computed properties; (`x` and `y` coordinates must be accessed through the intermediary `origin`):

```
rectangle.origin.x
rectangle.origin.y
rectangle.width
rectangle.height
```

### Accessing Minimum, Median, and Maximum Values

Although a rectangle can be fully described by a location (`CGPoint`) and an extent (`CGSize`), that’s just one side of the story.

For the other 3 sides, use the built-in convenience properties to get the minimum (`min`), median (`mid`), and maximum (`max`) values in the `x` and `y` dimensions:

![](https://nshipster.com/assets/core-graphics-cgrect-min-mid-max-b3cb3042dad84d3e0b8881471dfed363933fc5a476453732679885767102db204be1365d3e93ed83677b1d52fb7ab1a48c35399afc076f3da9f1ae187fb3c5e6.svg)

<sub>CoreGraphics CGRect Properties (iOS)</sub>

```
rectangle.minX // 1.0
rectangle.midX // 3.0
rectangle.maxX // 5.0

rectangle.minY // 2.0
rectangle.midY // 3.5
rectangle.maxY // 5.0
```

#### Computing the Center of a Rectangle

It’s often useful to compute the center point of a rectangle. Although this isn’t provided by the framework SDK, you can easily extend `CGRect` to implement it using the `midX` and `midY` properties:

```
extension CGRect {
    var center: CGPoint {
        return CGPoint(x: midX, y: midY)
    }
}
```

## Normalization

Things can get a bit strange when you use non-integral or negative values in geometric calculations. Fortunately, CoreGraphics has just the APIs you need to keep everything in order.

### Standardizing Rectangles

We expect that a rectangle’s origin is situated at its top-left corner. However, if its size has a negative width or height, the origin could become any of the other corners instead.

For example, consider the following _bizarro_ rectangle that extends leftwards and upwards from its origin.

```
let ǝןƃuɐʇɔǝɹ = CGRect(origin: point,
                         size: CGSize(width: -4.0, height: -3.0))
ǝןƃuɐʇɔǝɹ // {x 1 y 2 w -4 h -3}
```

We can use the `standardized` property to get the equivalent rectangle with non-negative width and height. In the case of the previous example, the standardized rectangle has a width of `4` and height of `3` and is situated at the point `(-3, -1)`:

```
ǝןƃuɐʇɔǝɹ.standardized // {x -3 y -1 w 4 h 3}
```

### Integrating Rectangles

It’s generally a good idea for all `CGRect` values to be rounded to the nearest whole point. Fractional values can cause the frame to be drawn on a pixel boundary. Because pixels are atomic units, a fractional value causes drawing to be averaged over the neighboring pixels. The result: blurry lines that don’t look great.

The `integral` property takes the `floor` each origin value and the `ceil` each size value. This ensures that your drawing code aligns on pixel boundaries crisply.

```
let blurry = CGRect(x: 0.1, y: 0.5, width: 3.3, height: 2.7)
blurry // {x 0.1 y 0.5 w 3.3 h 2.7}
blurry.integral // {x 0 y 0 w 4 h 4}
```

## Transformations

While it’s possible to mutate a rectangle by performing member-wise operations on its origin and size, the CoreGraphics framework offers better solutions by way of the APIs discussed below.

### Translating Rectangles

Translation describes the geometric operation of moving a shape from one location to another.

Use the `offsetBy` method (or `CGRectOffset` function in Objective-C) to translate a rectangle’s origin by a specified `x` and `y` distance.

```
rectangle.offsetBy(dx: 2.0, dy: 2.0) // {x 3 y 4 w 4 h 3}
```

Consider using this method whenever you shift a rectangle’s position. Not only does it save a line of code, but it more semantically represents intended operation than manipulating the origin values individually.

### Contracting and Expanding Rectangles

Other common transformations for rectangles include contraction and expansion around a center point. The `insetBy(dx:dy:)` method can accomplish both.

When passed a positive value for either component, this method returns a rectangle that _shrinks_ by the specified amount from each side as computed from the center point. For example, when inset by `1.0` horizontally (`dy = 0.0`), a rectangle originating at `(1, 2)` with a width of `4` and `height` equal to `3`, produces a new rectangle originating at `(2, 2)` with width equal to `2` and height equal to `3`. Which is to say: **the result of insetting a rectangle by `1` point horizontally is a rectangle whose `width` is `2` points _smaller_ than the original.**

```
rectangle // {x 1 y 2 w 4 h 3}
rectangle.insetBy(dx: 1.0, dy: 0.0) // {x 2 y 2 w 2 h 3}
```

When passed a negative value for either component, the rectangle _grows_ by that amount from each side. When passed a non-integral value, this method may produce a rectangle with non-integral components.

```
rectangle.insetBy(dx: -1.0, dy: 0.0) // {x 0 y 2 w 6 h 3}
rectangle.insetBy(dx: 0.5, dy: 0.0) // {x 1.5 y 2 w 3 h 3}
```

## Identities and Special Values

Points, sizes, and rectangles each have a `zero` property, which defines the identity value for each respective type:

```
CGPoint.zero // {x 0 y 0}
CGSize.zero // {w 0 h 0}
CGRect.zero // {x 0 y 0 w 0 h 0}
```

Swift shorthand syntax allows you to pass `.zero` directly as an argument for methods and initializers, such as `CGRect.init(origin:size:)`:

```
let square = CGRect(origin: .zero,
                    size: CGSize(width: 4.0, height: 4.0))
```

---

`CGRect` has two additional special values: `infinite` and `null`:

```
CGRect.infinite // {x -∞ y -∞ w +∞ h +∞}
CGRect.null // {x +∞ y +∞ w 0 h 0}
```

`CGRect.null` is conceptually similar to `NSNotFound`, in that it represents the absence of an expected value, and does so using the largest representable number to exclude all other values.

`CGRect.infinite` has even more interesting properties, as it intersects with all points and rectangles, contains all rectangles, and its union with any rectangle is itself.

```
CGRect.infinite.contains(any point) // true
CGRect.infinite.intersects(any other rectangle) // true
CGRect.infinite.union(any other rectangle) // CGRect.infinite
```

Use `isInfinite` to determine whether a rectangle is, indeed, infinite.

```
CGRect.infinite.isInfinite // true
```

But to fully appreciate why these values exist and how they’re used, let’s talk about geometric relationships:

## Relationships

Up until this point, we’ve been dealing with geometries in isolation. To round out our discussion, let’s consider what’s possible when evaluating two or more rectangles.

### Intersection

Two rectangles intersect if they overlap. Their intersection is the smallest rectangle that encompasses all points contained by both rectangles.

![](https://nshipster.com/assets/core-graphics-intersection-492033ecd614a0c1583524b7445d4a49f8abee2f9e600d24c0444548f6c070e24979ba092c5998b026906f589329b6e460a2e8261629468f1e5e5324c76d10f3.svg)

<sub>CoreGraphics CGRect Intersection (iOS)</sub>

In Swift, you can use the `intersects(_:)` and `intersection(_:)` methods to efficiently compute the intersection of two `CGRect` values:

```
let square = CGRect(origin: .zero,
                    size: CGSize(width: 4.0, height: 4.0))
square // {x 0 y 0 w 4 h 4}

rectangle.intersects(square) // true
rectangle.intersection(square) // {x 1 y 2 w 3 h 2}
```

If two rectangles _don’t_ intersect, the `intersection(_:)` method produces `CGRect.null`:

```
rectangle.intersects(.zero) // false
rectangle.intersection(.zero) // CGRect.null
```

### Union

The union of two rectangles is the smallest rectangle that encompasses all of the points contained by either rectangle.

![](https://nshipster.com/assets/core-graphics-union-3f0bb9a033a863b9fa22e9a4319a3bbe6db46160562300f29d8f3531cf19cae38481e858c2ef71fa05cf1e3db50fd0c8bd02d0d3e8fdaba14ae2dc52a90e9df4.svg)

<sub>CoreGraphics CGRect Union (iOS)</sub>

In Swift, the aptly-named `union(_:)` method does just this for two `CGRect` values:

```
rectangle.union(square) // {x 0 y 0 w 5 h 5}
```

---

So what if you didn’t pay attention in Geometry class — this is the real world. And in the real world, you have `CGGeometry.h` and all of the types and functions it provides.

Know it well, and you’ll be on your way to discovering great new user interfaces in your apps. Do a good enough job with that, and you may encounter the best arithmetic problem of all: adding up all the money you’ve made with your awesome new app. _Mathematical!_
