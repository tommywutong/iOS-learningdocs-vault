---
title: Putting the Physics Into Measurements and Units
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/07/unitproduct/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e3e6f4bd4fbca345'
translated: false
---

> 原文：[Putting the Physics Into Measurements and Units](https://oleb.net/blog/2016/07/unitproduct/)　·　Ole Begemann

# Putting the Physics Into Measurements and Units

_Thanks to [Chris Eidhof](http://chris.eidhof.nl) and [Florian Kugler](http://floriankugler.com) for helping me figure this out._

I ended [the previous article](https://oleb.net/blog/2016/07/measurements-and-units/) with the plan to find a generic, declarative solution for expressing dependencies between physical quantities, such as _velocity = length / time_. Let’s continue that train of thought.

# A common form for equations

At the moment, the different `Unit…` classes don’t know anything about each other. As far as the type system is concerned, they are independent entities.[1](#fn:1) In reality, though, quantities are connected to each other, and we express these relations in equations. We have already seen one example above, here are some more:

| Dependencies between physical quantities |
|---|
| _velocity = length / time_ |
| _acceleration = velocity / time_ |
| _area = length × length_ |
| _volume = length × length × length = area × length_ |
| _resistance = voltage / current_ |
| _energy = power × time_ |
| _density = mass / volume_ |
| _force = mass × acceleration_ |
| _pressure = force / area_ |
| _torque = force × length_ |

The first thing to note is that we can reduce all these equations to the same form: _a = b × c_. Division can be rewritten as multiplication: _velocity = length / time ⇔ length = velocity × time_. And although some equations have more than two factors, we can always introduce intermediary quantities to reduce them to two (see the volume equation above for an example).

# The `UnitProduct` protocol

So we need a way to express the relation _a = b × c_ in the type system for a specific group of three unit classes, and we want to do this in a manner that can be adopted by any number of types. We can do this by defining a protocol named `UnitProduct` that has two associated types, `Factor1` and `Factor2`. We constrain these types to [`Dimension`](https://developer.apple.com/reference/foundation/nsdimension), the superclass of all dimensional units:

```
/// Describes the relation Self = Factor1 * Factor2.
protocol UnitProduct {
    associatedtype Factor1: Dimension
    associatedtype Factor2: Dimension
}
```

What else do we need? In order to perform calculations, we need to specify the actual _units_ the values should be converted to for the calculation. In other words, we must tell the type system that _meters_ divided by _seconds_ yields a result in _meters per second_ and not, for instance, _kilometers per hour_. Let’s add a static method called `defaultUnitMapping()` to the protocol for that purpose. It returns a three-tuple of matching units, one each for _a_, _b_, and _c_.

Ideally, I’d like the type of this return value to be `(Factor1, Factor2, Self)`, but the `Self` will later cause problems when we implement the protocol for a concrete type, such as [`UnitLength`](https://developer.apple.com/reference/foundation/nsunitlength). The `Unit…` types are non-final classes, meaning they can be subclassed. Now if `UnitLength` adopted the protocol and implemented this method by returning a `UnitLength` instance for `Self`, any subclass would inherit the conformance, [but no longer fulfill the protocol contract](https://twitter.com/slava_pestov/status/755288757427838977) because `Self` now refers to the subclass’s type. The compiler doesn’t allow such an implementation [for that reason](http://stackoverflow.com/a/37555215/116862). This would be different if `UnitLength` were a value type or a final class.

As a workaround, we can introduce a third associated type to represent the product of the multiplication. I don’t like this solution because it forces adopters of the protocol to specify themselves as an associated type, which is really unintuitive. But it works. The complete protocol becomes:

```
protocol UnitProduct {
    associatedtype Factor1: Dimension
    associatedtype Factor2: Dimension
    associatedtype Product: Dimension // is always == Self

    static func defaultUnitMapping() -> (Factor1, Factor2, Product)
}
```

This is enough to express the mathematical relation in the type system and provides sufficient information about the unit relationships to perform calculations.

Next, let’s write a concrete implementation. Remember, we want to model the relation _[`UnitLength`](https://developer.apple.com/reference/foundation/nsunitlength) = [`UnitSpeed`](https://developer.apple.com/reference/foundation/nsunitspeed) × [`UnitDuration`](https://developer.apple.com/reference/foundation/nsunitduration)_, so we want `UnitLength` to adopt the protocol:

```
/// UnitLength = UnitSpeed * UnitDuration
/// ⇔ UnitSpeed = UnitLength / UnitDuration
extension UnitLength: UnitProduct {
    typealias Factor1 = UnitSpeed
    typealias Factor2 = UnitDuration
    typealias Product = UnitLength

    static func defaultUnitMapping() -> (UnitSpeed, UnitDuration, UnitLength) {
        return (.metersPerSecond, .seconds, .meters)
    }
}
```

I have explicitly specified the associated types here with typealiases, but we could leave those out. The compiler can infer the types from the return type of the `defaultUnitMapping()` method. We return the triple `(.metersPerSecond, .seconds, .meters)`, specifying that these units are [coherent](https://en.wikipedia.org/wiki/Coherence_(units_of_measurement)) (multiplying or dividing two yields the third). These units also happen to be their unit type’s respective base units, but that is not necessarily the case. We could have chosen other values, such as `(.kilometersPerHour, .hours, .kilometers)`, as long as they are coherent with each other.

# Overloading the multiplication operator

There is one more step until we can perform a calculation. We need to implement the multiplication operator for our protocol. The function type says, “this is an implementation of the `*` operator for types adopting the `UnitProduct` protocol, where the left argument is a `Measurement<Factor1>`, the right argument is a `Measurement<Factor2>`, and the return value is a `Measurement<Product>`”:

```
/// UnitProduct.Product = Factor1 * Factor2
func * <UnitType: UnitProduct> (lhs: Measurement<UnitType.Factor1>, rhs: Measurement<UnitType.Factor2>)
    -> Measurement<UnitType> where UnitType: Dimension, UnitType == UnitType.Product {    
    let (leftUnit, rightUnit, resultUnit) = UnitType.defaultUnitMapping()
    let quantity = lhs.converted(to: leftUnit).value
        * rhs.converted(to: rightUnit).value
    return Measurement(value: quantity, unit: resultUnit)
}
```

The function body has three steps. First we retrieve the unit mapping from the protocol. Then we convert the two arguments to their respective target units and multiply the amounts. Lastly, we wrap the result in a new `Measurement` value and return it. Let’s try it out:

```
let speed = Measurement(value: 20, unit: UnitSpeed.kilometersPerHour)
// → 20.0 km/h
let time = Measurement(value: 2, unit: UnitDuration.hours)
// → 2.0 hr
let distance: Measurement<UnitLength> = speed * time
// → 40000.032 m
```

It works, awesome! Three observations:

1. The type checker currently cannot infer the return type of the multiplication automatically, we have to specify `Measurement<UnitLength>` explicitly. I’m not quite sure why that is. I experimented with various constraints for the generic parameters of the `*` function, but I couldn’t get it to work.
2. The result is in meters. Not a big deal, but it would be nicer if it were in kilometers, given that the arguments of the multiplication were in kilometers per hour and hours, respectively. More on that in the next article.
3. There is a small rounding error in the result, caused by a rounding error in the conversion from kilometers per hour to meters per second.

## _a × b ⇔ b × a_

We need to write three more functions to complete the task, two for division and another one for multiplication. Multiplication is [commutative](https://en.wikipedia.org/wiki/Commutative_property), so _time * speed_ should work just like _speed * time_. This is not true yet for our solution, but it is easy to add. Simply add another overload for `*`, swapping the two arguments. The function simply forwards to the first one:

```
/// UnitProduct.Product = Factor2 * Factor1
func * <UnitType: UnitProduct>(lhs: Measurement<UnitType.Factor2>, rhs: Measurement<UnitType.Factor1>)
    -> Measurement<UnitType> where UnitType: Dimension, UnitType == UnitType.Product {
    return rhs * lhs
}

let distance2: Measurement<UnitLength> = time * speed
// → 40000.032 m
```

# Division

Similarly, for division we need one overload for _`Product` / `Factor1`_ and one for _`Product` / `Factor2`_:

```
/// UnitProduct / Factor1 = Factor2
func / <UnitType: UnitProduct>(lhs: Measurement<UnitType>, rhs: Measurement<UnitType.Factor1>)
    -> Measurement<UnitType.Factor2> where UnitType: Dimension, UnitType == UnitType.Product {
    let (rightUnit, resultUnit, leftUnit) = UnitType.defaultUnitMapping()
    let quantity = lhs.converted(to: leftUnit).value / rhs.converted(to: rightUnit).value
    return Measurement(value: quantity, unit: resultUnit)
}

/// UnitProduct / Factor2 = Factor1
func / <UnitType: UnitProduct>(lhs: Measurement<UnitType>, rhs: Measurement<UnitType.Factor2>)
    -> Measurement<UnitType.Factor1> where UnitType: Dimension, UnitType == UnitType.Product {
    let (resultUnit, rightUnit, leftUnit) = UnitType.defaultUnitMapping()
    let quantity = lhs.converted(to: leftUnit).value / rhs.converted(to: rightUnit).value
    return Measurement(value: quantity, unit: resultUnit)
}

let timeReversed = distance / speed
// → 7200.0 s
timeReversed.converted(to: .hours)
// → 2.0 hr
let speedReversed = distance / time
// → 5.55556 m/s
speedReversed.converted(to: .kilometersPerHour)
// → 20.0 km/h
```

Interestingly, the type inference works for the division operations. I suspect it has something to do with the fact that in the division functions one of the arguments can be directly traced back to the generic parameter `UnitType`, whereas the arguments of the multiplication functions are only associated types of the generic parameter. I tried to introduce `Factor1` and `Factor2` as full-fledged generic parameters to the multiplication functions, but it didn’t change anything, though. Please let me know if you can explain this.

# Adopt the protocol with five lines of code

That’s it. Now, all we need to do to express the dependencies between three physical quantities is adopt the protocol and implement a single one-line function. Here it is for resistance ([`UnitElectricResistance`](https://developer.apple.com/reference/foundation/nsunitelectricresistance)), voltage ([`UnitElectricPotentialDifference`](https://developer.apple.com/reference/foundation/nsunitelectricpotentialdifference)), and current ([`UnitElectricCurrent`](https://developer.apple.com/reference/foundation/nsunitelectriccurrent)):

```
/// UnitElectricPotentialDifference = UnitElectricResistance * UnitElectricCurrent
extension UnitElectricPotentialDifference: UnitProduct {
    static func defaultUnitMapping() -> (UnitElectricResistance, UnitElectricCurrent, UnitElectricPotentialDifference) {
        return (.ohms, .amperes, .volts)
    }
}
```

And in use:

```
let voltage = Measurement(value: 5, unit: UnitElectricPotentialDifference.volts)
// → 5.0 V
let current = Measurement(value: 500, unit: UnitElectricCurrent.milliamperes)
// → 500.0 mA
let resistance = voltage / current
// → 10.0 Ω
```

# Conclusion

I think this is pretty cool, and it shows how a powerful type system can help us write correct code. Once the relations are defined, the compiler will not allow calculations with types that don’t make sense (e.g. mixing up numerator and denominator). And when type inference works, the compiler can even tell you the result type of an operation (note that in the last example above we have not specified the type of the `resistance` variable).

I also like that this is a [declarative](https://en.wikipedia.org/wiki/Declarative_programming) way of expressing these relationships. We essentially tell the compiler, “hey, this is how these three quantities are related, you figure out the rest”, and all the calculations and type checks just work.

# Outlook

In [part 3](https://oleb.net/blog/2016/07/unitsquare/), I would like to present a possible solution for preserving the units during a calculation (kilometers divided by hours should yield kilometers per hours, not meters per second), and discuss one more limitation that the current solution has. Stay tuned!

1. They have a common superclass, but that is not important at the moment. [↩︎](#fnref:1)
