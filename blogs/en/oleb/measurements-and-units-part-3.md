---
title: Measurements and Units, Part 3
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/07/unitsquare/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e14b5dd012a15909'
translated: false
---

> 原文：[Measurements and Units, Part 3](https://oleb.net/blog/2016/07/unitsquare/)　·　Ole Begemann

# Measurements and Units, Part 3

I still have [a few loose ends to tie up](https://movie-sounds.org/sci-fi-movie-samples/sound-clips-from-star-trek-insurrection-1998/you-re-not-finished-here-just-a-few-loose-ends-to-tie-up-dougherty-out) to complete my little series on working with units of measurements in Swift. If you haven’t yet seen the previous articles, check out [part 1](https://oleb.net/blog/2016/07/measurements-and-units/) for an overview of the Measurements and Units API in Foundation, and [part 2](https://oleb.net/blog/2016/07/unitproduct/) for my extension of the system for type-safe multiplication and division.

# Preserving units in computations

The multiplication and division code we developed in the [previous article](https://oleb.net/blog/2016/07/unitproduct/) always converts quantities to their _default units_ before performing the computation, as specified by the implementation of the `defaultUnitMapping()` method in the `UnitProduct` protocol. This is necessary for the calculations to be correct in all cases, regardless of the units the arguments are in.

Until now, we have also used the _default unit mapping_ as the unit for the return value of a computation. For example, the default unit mapping for [`UnitSpeed`](https://developer.apple.com/reference/foundation/nsunitspeed), [`UnitDuration`](https://developer.apple.com/reference/foundation/nsunitduration), and [`UnitLength`](https://developer.apple.com/reference/foundation/nsunitlength) is `(.metersPerSecond, .seconds, .meters)`. That means a division of _72 km / 2 hr_ is first converted to _72000 m / 7200 s_ before the calculation is performed. We then wrap the result in a `Measurement<UnitVelocity>` and return it in meters per second.

This is the simplest solution from an implementation point of view, but it is conceivable that callers would like units to be preserved if possible. _If I give you meters and seconds, then by all means give me back meters per second, but if I give you kilometers and hours, then I want you to return kilometers per hour to me._

## Preferred unit mappings

We can achieve this by adding another method to our protocol that returns a collection of preferred unit mappings, ordered by priority. The computation code would then iterate over this list and look for a match with the units used in the current calculation. If it does not find a match, it can always fall back to the default unit mapping. I call this method `preferredUnitMappings()`. The complete protocol now looks like this:

```
protocol UnitProduct {
    associatedtype Factor1: Dimension
    associatedtype Factor2: Dimension
    associatedtype Product: Dimension

    static func defaultUnitMapping() -> (Factor1, Factor2, Product)
    static func preferredUnitMappings() -> [(Factor1, Factor2, Product)]
}
```

We should provide a default implementation that just returns an empty array. This gives adopters of the protocol the choice to ignore it if they don’t require this functionality.

```
extension UnitProduct {
    // Default implementation.
    static func preferredUnitMappings() -> [(Factor1, Factor2, Product)] {
        return []
    }
}
```

Next, we will write some convenience methods whose job it is to find the matching unit mapping for a given pair of arguments that were passed to one of the multiplication or division functions. We need three variants of this method, depending on which pair of the three argument types `Factor1`, `Factor2`, and `Product` we have. They all work the same way: return the first element in the `preferredUnitMappings` array that matches both arguments. If there is no match, return the default unit mapping. The implementation uses the new [`first(where:)`](http://swiftdoc.org/v3.0/protocol/Sequence/#comment-func--first-where_) method that was added to `Sequence` in Swift 3:

```
extension UnitProduct {
    static func unitMapping(factor1: Factor1, factor2: Factor2) -> (Factor1, Factor2, Product) {
        let match = preferredUnitMappings().first { (f1, f2, _) in
            f1 == factor1 && f2 == factor2
        }
        return match ?? defaultUnitMapping()
    }

    static func unitMapping(product: Product, factor2: Factor2) -> (Factor1, Factor2, Product) {
        let match = preferredUnitMappings().first { (_, f2, p) in
            p == product && f2 == factor2
        }
        return match ?? defaultUnitMapping()
    }

    static func unitMapping(product: Product, factor1: Factor1) -> (Factor1, Factor2, Product) {
        let match = preferredUnitMappings().first { (f1, _, p) in
            p == product && f1 == factor1
        }
        return match ?? defaultUnitMapping()
    }
}
```

## Use preferred unit mappings in computations

Finally, we can adjust the multiplication and division functions to use the new functionality. The computation itself does not change. We still perform it in terms of the default unit mapping. But before returning the result, we convert it to the preferred unit now. Here is the code for one of the division functions (the changes to the other two functions are analogous):

```
/// UnitProduct / Factor2 = Factor1
public func / <UnitType: Dimension> (lhs: Measurement<UnitType>, rhs: Measurement<UnitType.Factor2>)
    -> Measurement<UnitType.Factor1> where UnitType: UnitProduct, UnitType == UnitType.Product {

    // Perform the calculation in the default unit mapping
    let (resultUnit, rightUnit, leftUnit) = UnitType.defaultUnitMapping()
    let value = lhs.converted(to: leftUnit).value / rhs.converted(to: rightUnit).value
    let result = Measurement(value: value, unit: resultUnit)

    // Convert to preferred unit mapping
    let (desiredUnit, _, _) = UnitType.unitMapping(product: lhs.unit, factor2: rhs.unit)
    return result.converted(to: desiredUnit)
}
```

With everything in place, we provide an implementation of `preferredUnitMappings()` for `UnitLength`, the type that adopted the `UnitProduct` protocol:

```
extension UnitLength {
    static func preferredUnitMappings() -> [(UnitSpeed, UnitDuration, UnitLength)] {
        return [
            (.kilometersPerHour, .hours, .kilometers),
            (.milesPerHour, .hours, .miles),
            (.knots, .hours, .nauticalMiles)
        ]
    }
}
```

Now, computations that match the preferred unit mappings will have their units preserved (again, with small rounding errors):

```
Measurement(value: 72, unit: UnitLength.kilometers) / Measurement(value: 2, unit: UnitDuration.hours)
// → 35.999971200023 km/h
Measurement(value: 10, unit: UnitLength.miles) / Measurement(value: 1, unit: UnitDuration.hours)
// → 9.99997514515231 mph
Measurement(value: 25, unit: UnitLength.nauticalMiles) / Measurement(value: 2, unit: UnitDuration.hours)
// → 12.5000107991454 kn
```

## Is this a good idea?

I’m not sure if this is actually a good idea. It makes the code considerably more complex and the benefit is arguably small. Iterating over the array of preferred unit mappings in every single computation also makes the code slower[1](#fn:1), which could be a problem in loops. Simple calculations such as the ones we do here should arguably be as fast as possible.

# Problems with squares

If you’ve played around with the `UnitProduct` protocol, you may have noticed that it does not work for quantities that are _squares_ of other quantities, that is, `Factor1` and `Factor2` are the same type. An example would be _area = length × length_:

```
extension UnitArea: UnitProduct {
    typealias Factor1 = UnitLength
    typealias Factor2 = UnitLength
    typealias Product = UnitArea

    static func defaultUnitMapping() -> (UnitLength, UnitLength, UnitArea) {
        return (.meters, .meters, .squareMeters)
    }
}
```

If we try to perform a multiplication of two lengths, the compiler complains about an ambiguous use of the `*` operator:

```
let width = Measurement(value: 4, unit: UnitLength.meters)
let height = Measurement(value: 6, unit: UnitLength.meters)
let area: Measurement<UnitArea> = width * height
// error: Ambiguous use of operator '*'
```

The reason is that our two overloads for the multiplication operator, one for `(Factor1, Factor2) -> Product`, the other one for `(Factor2, Factor1) -> Product`, all of a sudden have the same type when `Factor1` is the same as `Factor2`. The compiler cannot decide which implementation to use, so it raises an error. (In our case, either implementation would be fine as they both yield the same result, but the compiler doesn’t know that.)

The best way to solve this would be if it were possible to add an additional generic constraint like `Factor1 != Factor2` to one of the overloads in order to exclude that function from the type checker when both factors have the same type. Like this:

```
func * <UnitType: Dimension> (...) -> ...
    where UnitType: UnitProduct, UnitType == UnitType.Product, UnitType.Factor1 != UnitType.Factor2
// error: Expected ':' or '==' to indicate a conformance or same-type requirement
```

Unfortunately, this syntax is not valid in Swift. A `where` clause can only contain `:` or `==` requirements.

## A separate protocol for squares

The workaround is to introduce a separate protocol, `UnitSquare`, for square relations. This protocol only needs two associated types, `Factor` and `Product`:

```
protocol UnitSquare {
    associatedtype Factor: Dimension
    associatedtype Product: Dimension

    static func defaultUnitMapping() -> (Factor, Factor, Product)
    static func preferredUnitMappings() -> [(Factor, Factor, Product)]
}
```

I won’t go over the implementation here as it is largely identical to the one for `UnitProduct`. (There will only be one overload each for multiplication and division, as opposed to two each for `UnitProduct`.)

If we now conform [`UnitArea`](https://developer.apple.com/reference/foundation/nsunitarea) to `UnitSquare`, the computations work as expected:

```
extension UnitArea: UnitSquare {
    typealias Factor = UnitLength
    typealias Product = UnitArea

    static func defaultUnitMapping() -> (UnitLength, UnitLength, UnitArea) {
        return (.meters, .meters, .squareMeters)
    }
}

let width = Measurement(value: 4, unit: UnitLength.meters)
let height = Measurement(value: 6, unit: UnitLength.meters)
let area: Measurement<UnitArea> = width * height
// → 24.0 m²
area / width
// → 6.0 m
area / height
// → 4.0 m
```

# Division by itself

The final piece of the puzzle that I can think of is the division of two measurements of the same unit class, such as _6 meters / 4 meters = 1.5_. This operation yields a [dimensionless quantity](https://en.wikipedia.org/wiki/Dimensionless_quantity) (in other words, a `Double`) and is valid for all [`Dimension`](https://developer.apple.com/reference/foundation/nsdimension) types.

Supporting this is very easy. All we need is one more overload of the division operator. The function type says, for two measurements of the same `Dimension`, the return type is a `Double`. For the implementation, we simply convert both measurements to the base unit and perform the division:

```
func / <UnitType: Dimension> (lhs: Measurement<UnitType>, rhs: Measurement<UnitType>) -> Double {
    return lhs.converted(to: UnitType.baseUnit()).value / rhs.converted(to: UnitType.baseUnit()).value
}

let ratio = height / width
// → 1.5
```

# The code

I bundled all the code I discussed in this series in a library named [Ampere](https://github.com/ole/Ampere) that you can check out on GitHub. It’s a work in progress and I haven’t set up any infrastructure yet to turn it into a “real” library like versioning and CocoaPods support because I don’t know if this is something the community would be interested in. So let me know what you think!

1. In the current implementation, the array of preferred unit mappings is not even cached but recreated every single time. So this could definitely be optimized for performance, but it will always be slower than without the additional lookup. [↩︎](#fnref:1)
