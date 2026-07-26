---
title: Measurements and Units with Phantom Types
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/08/measurements-and-units-with-phantom-types/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:a7986c01b46448c3'
translated: false
---

> 原文：[Measurements and Units with Phantom Types](https://oleb.net/blog/2016/08/measurements-and-units-with-phantom-types/)　·　Ole Begemann

# Measurements and Units with Phantom Types

This is a bonus post in my little series on the new units of measurement types in Foundation. While I like Apple’s API, I thought it could be interesting to explore a slightly different approach to the same problem. Particularly, I was interested in the question if a pure Swift design could be significantly better than Apple’s interface, for which Objective-C compatibility [inevitably is a prime consideration](https://forums.swift.org/t/swiftier-implementation-of-measurement-and-unit-in-foundation/3748/2).

## Apple’s design

The primary data type for users of Apple’s API is [`Measurement`](https://developer.apple.com/reference/foundation/nsmeasurement). It contains a floating-point `value` and the `unit` the value is measured in. It is generic over the unit type:

```
struct Measurement<UnitType: Unit> {
    let unit: UnitType
    var value: Double
}

let length = Measurement(value: 5, unit: UnitLength.meters)
// length is a Measurement<UnitLength>
```

`Measurement` got [the value-type treatment](https://github.com/apple/swift-evolution/blob/master/proposals/0069-swift-mutability-for-foundation.md) — it is a class in Objective-C and a struct in Swift.

Families of units, such as _length_ or _duration_, are modeled as types in a class hierarchy: [`Unit`](https://developer.apple.com/reference/foundation/nsunit) \> [`Dimension`](https://developer.apple.com/reference/foundation/nsdimension) \> [`UnitLength`](https://developer.apple.com/reference/foundation/nsunitlength), [`UnitDuration`](https://developer.apple.com/reference/foundation/nsunitduration), etc. Specific units, such as _meters_ or _kilograms_, are instances of their unit family class. Each unit is composed of the unit’s `symbol` (`"kg"`) and a [unit converter](https://developer.apple.com/reference/foundation/unitconverter) object that encodes the instructions how to convert the unit to the family’s _base unit_.

## Phantom types

What if we modeled specific units also as _types_ instead of _instances_? If we had types named `Meters`, `Kilometers`, or `Miles`, we could design a generic measurement type that had just a single stored property for the quantity. The quantity’s unit would be entirely encoded in the type itself:

```
struct MyMeasurement<UnitType: MyUnit> {
    var value: Double

    init(_ value: Double) {
        self.value = value
    }
}

let length = MyMeasurement<Meters>(5)
// length is a MyMeasurement<Meters>
```

Again, note the difference between the two approaches: in Apple’s API, `Measurement` is parameterized with the unit family _length_; the specific unit _meters_ is part of the value. In my design, the generic parameter is the specific unit _meters_.

`MyMeasurement` is also called a [_phantom type_](https://wiki.haskell.org/Phantom_type) because the generic parameter `UnitType` does not appear anywhere in the type’s definition. Its only purpose is to differentiate two types like `MyMeasurement<Meters>` and `MyMeasurement<Kilometers>` from each other so that they cannot be substituted.

We’ll see later whether this is actually useful in our situation because you could argue that a measurement in meters _should_ be totally interchangeable with a measurement in kilometers. For other examples of phantom types in Swift, see [this objc.io article](https://www.objc.io/blog/2014/12/29/functional-snippet-13-phantom-types/) or [this talk by Johannes Weiß](https://realm.io/news/swift-summit-johannes-weiss-the-type-system-is-your-friend/). The Swift standard library also makes use of phantom types, for example with [`UnsafePointer<Memory>`](https://developer.apple.com/library/ios/documentation/Swift/Reference/Swift_UnsafePointer_Structure/index.html).

### Benefits

One obvious benefit of my approach is the 50% smaller size of the measurement data type because the reference to the `unit` instance is not needed. (Unit instances themselves are shared between all measurements in that unit: two measurements of _5 meters_ and _10 meters_ reference the same unit instance.) The size savings are offset by a potentially much larger code size because the compiler has to generate more specializations of the generic type and functions using the type.

Since `Unit` is a reference type in Apple’s API, passing `Measurement` values to functions also incurs some retain/release overhead. Both of these factors are unlikely to be significant in a typical app, and I haven’t investigated them further. They have certainly not been important for me while exploring these ideas.

## Concrete design

We still need to specify how to define units in this system. Units are grouped into _unit families_, such as length, temperature, or duration. Let’s start by defining a protocol for a unit family:

```
/// Represents a physical quantity or “family of units”.
/// Examples: length, temperature, velocity.
protocol UnitFamily {
    associatedtype BaseUnit
}
```

Just as in Apple’s API, each unit family must define a _base unit_, which is used to convert between units of the same family. For example, the base unit for the family _length_ should be _meters_. We model this as an associated type of the `UnitFamily` protocol. This has the advantage that the base unit is encoded in the type system. In Foundation, base units must be documented separately to allow others to extend the system with custom units.

The next piece is the `MyUnit` protocol for modeling specific units, which in Apple’s design would be instances of a unit family type. (I’m using the `My` prefix to avoid naming conflicts with Apple’s types.)

```
/// Represents a unit of measurement.
/// Examples: meters, kilometers, miles, seconds, hours, degrees Celsius.
protocol MyUnit {
    associatedtype Family: UnitFamily

    static var symbol: String { get }
    static var converter: UnitConverter { get }
}
```

A unit declares the family it belongs to through an associated type. It also defines static properties for its symbol (such as `"m"` for meters or “lbs” for pounds) and a unit converter that describes how to convert the unit to the family’s base unit. For example, if the base unit for the family `Length` is `Meters`, the converter for `Kilometers` should be `UnitConverterLinear(coefficient: 1000)`. The unit converter for the base unit itself should always have the coefficient `1`. I’m borrowing the [`UnitConverter`](https://developer.apple.com/reference/foundation/unitconverter) class from Foundation.

Foundation makes a distinction between `Unit` for dimensionless units and `Dimension` for dimensional units. We don’t do this here for simplicity; all our units are dimensional.

A base unit must be a unit, of course, so ideally the associated type `BaseUnit` in `UnitFamily` should have a corresponding constraint `BaseUnit: MyUnit`. Unfortunately, that creates a circular reference between the two protocols, and that is currently not permitted in Swift. Everything works fine without the constraint, though.

### Conforming to the protocols

It’s time to add some concrete implementations for these protocols. I’m showing length, duration, and speed here, with a few units each. It would be trivial to add more units (such as _miles_ or _centimeters_) or entirely different unit families (such as _temperature_).

I chose to use enums over structs for the types because caseless enums have the nice property that they cannot be instantiated. This is perfect for us because we are only interested in the types, not in instances of the types.

```
// MARK: - Length
enum Length: UnitFamily {
    typealias BaseUnit = Meters
}

enum Meters: MyUnit {
    typealias Family = Length
    static let symbol = "m"
    static let converter: UnitConverter = UnitConverterLinear(coefficient: 1)
}

enum Kilometers: MyUnit {
    typealias Family = Length
    static let symbol = "km"
    static let converter: UnitConverter = UnitConverterLinear(coefficient: 1000)
}

// MARK: - Duration
enum Duration: UnitFamily {
    typealias BaseUnit = Seconds
}

enum Seconds: MyUnit {
    typealias Family = Duration
    static let symbol = "s"
    static let converter: UnitConverter = UnitConverterLinear(coefficient: 1)
}

enum Minutes: MyUnit {
    typealias Family = Duration
    static let symbol = "min"
    static let converter: UnitConverter = UnitConverterLinear(coefficient: 60)
}

enum Hours: MyUnit {
    typealias Family = Duration
    static let symbol = "hr"
    static let converter: UnitConverter = UnitConverterLinear(coefficient: 3600)
}

// MARK: - Speed
enum Speed: UnitFamily {
    typealias BaseUnit = MetersPerSecond
}

enum MetersPerSecond: MyUnit {
    typealias Family = Speed
    static let symbol = "m/s"
    static let converter: UnitConverter = UnitConverterLinear(coefficient: 1)
}

enum KilometersPerHour: MyUnit {
    typealias Family = Speed
    static let symbol = "km/h"
    static let converter: UnitConverter = UnitConverterLinear(coefficient: 1.0/3.6)
}
```

### Converting measurements

Now that we can represent measurements in different units, we need a way to convert between them. The `converted(to:)` method takes the type of a target unit and returns a new measurement in that unit, using the unit converters. Note the constraint `TargetUnit.Family == UnitType.Family`, which limits conversions to the same unit family. The compiler will not let you convert `Meters` to `Seconds`.

```
extension MyMeasurement {
    /// Converts `self` to a measurement that has another unit of the same family.
    func converted<TargetUnit>(to target: TargetUnit.Type) -> MyMeasurement<TargetUnit>
        where TargetUnit: MyUnit, TargetUnit.Family == UnitType.Family
    {
        let valueInBaseUnit = UnitType.converter.baseUnitValue(fromValue: value)
        let valueInTargetUnit = TargetUnit.converter.value(fromBaseUnitValue: valueInBaseUnit)
        return MyMeasurement<TargetUnit>(valueInTargetUnit)
    }
```

Let’s also add some convenience functionality to `MyMeasurement`. Adding conformance to `CustomStringConvertible` provides us with a nice debugging output, and conforming to `ExpressibleByIntegerLiteral` and `ExpressibleByFloatLiteral` makes creating new measurements from literals much more pleasant:

```
extension MyMeasurement: CustomStringConvertible {
    var description: String {
        return "\(value) \(UnitType.symbol)"
    }
}

extension MyMeasurement: ExpressibleByIntegerLiteral {
    init(integerLiteral value: IntegerLiteralType) {
        self.value = Double(value)
    }
}

extension MyMeasurement: ExpressibleByFloatLiteral {
    init(floatLiteral value: FloatLiteralType) {
        self.value = value
    }
}
```

## In use

Now we can create measurements and convert them to other units. The expressible-by-literal syntax is quite nice:

```
let fiveMeters: MyMeasurement<Meters> = 5
// → 5.0 m
let threeKilometers: MyMeasurement<Kilometers> = 3
// → 3.0 km
threeKilometers.converted(to: Meters.self)
// → 3000.0 m
threeKilometers.converted(to: Seconds.self)
// error: 'Family' (aka 'Length') is not convertible to 'Family' (aka 'Duration') (as expected)
```

What about the use of measurements as function arguments? Take this hypothetical `delay` function that takes a duration and a closure and executes the closure after the specified duration:

```
func delay(after duration: MyMeasurement<Seconds>, block: () -> ()) {
    // ...
}
```

In this form, the function requires a measurement in seconds. If you want to call it with an argument in milliseconds, it is your responsibility to convert the value. It has the advantage of ensuring type safety over a simple `TimeInterval` argument — the compiler will not allow you to pass a `MyMeasurement<Milliseconds>` —, but it is significantly less flexible than the equivalent `Measurement<UnitDuration>`, which would accept any duration unit.

We can achieve this, too, by making the function generic over the unit type (with the constraint that it must have a `Duration` family):

```
func delay<Time>(after duration: MyMeasurement<Time>, block: () -> ())
    where Time: MyUnit, Time.Family == Duration
{
    // ...
}
```

It works, but it makes the function signature significantly less readable, even with [the `where` clause out of the way](https://github.com/apple/swift-evolution/blob/master/proposals/0081-move-where-expression.md).

For this reason alone, Apple’s design where units are instances not types is probably more practical. And arguably it also makes more sense. After all, _meters_ and _kilometers_ are just different notations for essentially the same thing. But this is an exploration that doesn’t have to make sense, so let’s continue.

## Addition and scalar multiplication

It should be possible to add two measurements of the same family together, even if they have different units. This is quite easy to implement with a generic overload of the `+` operator. As a convention, we convert the right-hand side value to the left-hand side’s unit and return the result in terms of the that unit:

```
func + <Unit1, Unit2> (lhs: MyMeasurement<Unit1>, rhs: MyMeasurement<Unit2>) -> MyMeasurement<Unit1>
    where Unit1: MyUnit, Unit2: MyUnit, Unit1.Family == Unit2.Family
{
    let rhsConverted = rhs.converted(to: Unit1.self)
    return MyMeasurement(lhs.value + rhsConverted.value)
}

fiveMeters + threeKilometers
// → 3005.0 m
threeKilometers + fiveMeters
// → 3.005 km
```

Again, note the constraint `Unit1.Family == Unit2.Family` to prevent adding _seconds_ to _meters_.

Multiplication with a scalar value is even easier because no unit conversions are involved. We simply multiply the value and create a new measurement. Two overloads are needed for `a * b` and `b * a`:

```
func * <UnitType> (measurement: MyMeasurement<UnitType>, scalar: Double) -> MyMeasurement<UnitType> {
    var result = measurement
    result.value *= scalar
    return result
}

func * <UnitType> (scalar: Double, measurement: MyMeasurement<UnitType>) -> MyMeasurement<UnitType> {
    return measurement * scalar
}

threeKilometers * 2
// → 6.0 km
let twoSeconds: MyMeasurement<Seconds> = 2
60 * twoSeconds
// → 120.0 s
```

## Multiplication and division (i.e. physics)

If you remember [part 2](https://oleb.net/blog/2016/07/unitproduct/) of this series, my original goal was to model how unit families are related to each other, e.g. _speed = length / duration_ or _energy = power × time_. To do this, I introduced a protocol named `UnitProduct`, and unit families could express the factors they are composed of by conforming to the protocol and naming their factors as associated types.

Let’s do the same here, but now we are going to express relationships directly between _units_, not _unit families_. The `Product` protocol looks very similar:

```
/// Describes this relation between units:
/// Product = Factor1 * Factor2
protocol Product: MyUnit {
    associatedtype Factor1: MyUnit
    associatedtype Factor2: MyUnit
}
```

Note that a single protocol is sufficient to describe both multiplicative and fractional relations because _a = b × c_ is equivalent to _b = a / c_. The choice is arbitrary, and whatever you choose makes expressing some relations feel less natural. For example, if we want to express _speed = length / duration_, we have to rewrite it first as _length = speed × duration_.

The next step is to implement the actual computations, i.e. overloads for the multiplication and division operators that work on types conforming to our protocol. We need four variants:

### _a = b × c_

The generic constraints make this quite complicated. For any type `Result` that conforms to `Product`, this overload defines the multiplication of any two measurements whose units `Unit1` and `Unit2` have the same families as the units specified in `Result.Factor1` and `Result.Factor2`. The result is computed by converting the measurements to `Result.Factor1` and `Result.Factor2`, respectively, and multiplying those.

```
func * <Unit1, Unit2, Result> (lhs: MyMeasurement<Unit1>, rhs: MyMeasurement<Unit2>) -> MyMeasurement<Result>
    where Result: Product, Result.Factor1.Family == Unit1.Family, Result.Factor2.Family == Unit2.Family
{
    let left = lhs.converted(to: Result.Factor1.self)
    let right = rhs.converted(to: Result.Factor2.self)
    return MyMeasurement(left.value * right.value)
}
```

### _a = c × b_

```
func * <Unit1, Unit2, Result> (lhs: MyMeasurement<Unit2>, rhs: MyMeasurement<Unit1>) -> MyMeasurement<Result>
    where Result: Product, Result.Factor1.Family == Unit1.Family, Result.Factor2.Family == Unit2.Family
{
    return rhs * lhs
}
```

This is exactly the same as the previous function, with `lhs` and `rhs` reversed. The implementation simply forwards to the other overload.

### _b = a / c_ and _c = a / b_

```
func / <Unit1, Unit2, Result> (lhs: MyMeasurement<Result>, rhs: MyMeasurement<Unit2>) -> MyMeasurement<Unit1>
    where Result: Product, Result.Factor1.Family == Unit1.Family, Result.Factor2.Family == Unit2.Family
{
    let right = rhs.converted(to: Result.Factor2.self)
    return MyMeasurement(lhs.value / right.value)
}

func / <Unit1, Unit2, Result> (lhs: MyMeasurement<Result>, rhs: MyMeasurement<Unit1>) -> MyMeasurement<Unit2>
    where Result: Product, Result.Factor1.Family == Unit1.Family, Result.Factor2.Family == Unit2.Family
{
    let right = rhs.converted(to: Result.Factor1.self)
    return MyMeasurement(lhs.value / right.value)
}
```

Again, these follow the same ideas, only the placement of the generic parameters varies.

### Concrete implementation

Now it is finally possible to express the relation _length = speed × duration_ (i.e. _speed = length / duration_):

```
extension Meters: Product {
    typealias Factor1 = MetersPerSecond
    typealias Factor2 = Seconds
}
```

And it can be used like this:

```
let tenMeters: MyMeasurement<Meters> = 10
let fourSeconds: MyMeasurement<Seconds> = 4
let speed: MyMeasurement<MetersPerSecond> = tenMeters / fourSeconds
// → 2.5 m/s

let thirtyKilometersPerHour: MyMeasurement<KilometersPerHour> = 30
let twoHours: MyMeasurement<Hours> = 2
let tripLength: MyMeasurement<Meters> = thirtyKilometersPerHour * twoHours
// → 60000.0 m
tripLength.converted(to: Kilometers.self)
// → 60.0 km
```

It works quite well, but two drawbacks are apparent. First, the compiler cannot infer the return types of the computations automatically at the moment. I don’t know if improvements to the compiler can solve this in the future or if I could provide more help by specifying better generic constraints to the functions. I experimented with this a little bit, but could not make it work.

Second, while the arguments’ units need only have the correct family, the unit of the return type is currently limited to the specific unit used in the `Product` protocol. So something like `let tripLength: MyMeasurement<Kilometers> = ...` would not work, you have to take the result in `Meters` first and then convert it. I consider this a pretty big limitation.

## Conclusion

Regardless of the (very real) flaws of this design, note that not a single line of executable code is needed to add this mathematical relation to the type system! Simply by adding the protocol conformance (which only involves defining two associated types), we literally added the proposition _1 meter = 1 m/s × 1 s_ to the compiler’s pool of “truth”. And if you wanted to add another relation (such as _1 J = 1 W × 1 s_), adding another protocol conformance is all that’s required.

I find this fascinating.

Nonetheless, I do not think this API based on phantom types is superior to the one in Foundation. It simply makes more sense to parameterize measurements based on unit families rather than units.
