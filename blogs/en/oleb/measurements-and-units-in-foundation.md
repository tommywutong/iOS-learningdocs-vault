---
title: Measurements and Units in Foundation
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/07/measurements-and-units/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:1cb036fe6ef1aca2'
translated: false
---

> 原文：[Measurements and Units in Foundation](https://oleb.net/blog/2016/07/measurements-and-units/)　·　Ole Begemann

# Measurements and Units in Foundation

New in Foundation in iOS 10 and macOS 10.12 is a family of types for modeling [units of measurement](https://en.wikipedia.org/wiki/Units_of_measurement) as well as actual measurements in those units, such as _1 kilometer_ or _21 degrees Celsius_. If you haven’t looked at it yet, [WWDC session 238](https://developer.apple.com/videos/play/wwdc2016/238/) gives a good overview.

# Introduction

Here is an example of what you can do with this. Let’s start by creating a value for the distance I covered on [my latest bike tour](http://www.gpsies.com/map.do?fileId=jlrraxtktaxippup):

```
let distance = Measurement(value: 106.4, unit: UnitLength.kilometers)
// → 106.4 km
```

A [`Measurement`](https://developer.apple.com/reference/foundation/nsmeasurement) (which is a [value type](https://developer.apple.com/swift/blog/?id=10) in Swift) combines a quantity (106.4) with a unit of measure (kilometers). We could define our own units, but Foundation already includes a bunch of the most common physical quantities. There are currently [21 predefined unit types](https://developer.apple.com/reference/foundation/nsdimension). These are all subclasses of the abstract [`Dimension`](https://developer.apple.com/reference/foundation/nsdimension) class, and their names all begin with `Unit…`, such as [`UnitAcceleration`](https://developer.apple.com/reference/foundation/nsunitacceleration), [`UnitMass`](https://developer.apple.com/reference/foundation/nsunitmass), or [`UnitTemperature`](https://developer.apple.com/reference/foundation/nsunittemperature). Here, we use [`UnitLength`](https://developer.apple.com/reference/foundation/nsunitlength).

Each unit class provides class properties for the various specific units that can represent measurements of that type, such as `.meters`, `.kilometers`, `.miles`, or `.lightyears`. To convert our original measurement in kilometers to other units, we can write:

```
let distanceInMeters = distance.converted(to: .meters)
// → 106400 m
let distanceInMiles = distance.converted(to: .miles)
// → 66.1140591795394 mi
let distanceInFurlongs = distance.converted(to: .furlongs)
// → 528.911158832419 fur
```

`UnitLength` comes with [22 predefined units](https://developer.apple.com/reference/foundation/nsunitlength) from picometers to lightyears, but if your [preferred unit](https://www.youtube.com/watch?v=r7x-RGfd0Yk) is not among them, it is easy to add your own. Simply extend the type with another static property that describes the new unit’s symbol and its conversion factor to the type’s _base unit_. This last part is done through a [`UnitConverter`](https://developer.apple.com/reference/foundation/unitconverter). The _base unit_ is the unit in terms of which all other units of the same type are defined. It must be documented and is usually (but not necessarily) identical to the corresponding base unit in the [SI system](https://en.wikipedia.org/wiki/International_System_of_Units). For `UnitLength`, the base unit is `.meters`.

```
extension UnitLength {
    static var leagues: UnitLength {
        // 1 league = 5556 meters
        return UnitLength(symbol: "leagues", 
            converter: UnitConverterLinear(coefficient: 5556))
    }
}

let distanceInLeagues = distance.converted(to: .leagues)
// → 19.150467962563 leagues
```

(I’d like `leagues` to be a static stored constant rather than a computed property, but stored type properties don’t seem to be supported in extensions of `NSObject` subclasses. See [SR-993](https://bugs.swift.org/browse/SR-993) for more information.)

We can also multiply measurements by scalar values, as well as add and subtract measurements. Unit conversions are handled automatically if necessary:

```
let doubleDistance = distance * 2
// → 212.8 km
let distance2 = distance + Measurement(value: 5, unit: UnitLength.kilometers)
// → 111.4 km
let distance3 = distance + Measurement(value: 10, unit: UnitLength.miles)
// → 122493.4 m
```

Note what happens in the last example. When we add one measurement in kilometers and one in miles, the framework converts both to meters (the base unit of `UnitLength`) before adding them together. The original unit information gets lost. This does not happen in the previous example, where we add two measurements that have the same unit (kilometers).

# Benefits

## Safety

This works great so far, and is vastly better than what most of us usually do, which is to use plain floating-point numbers for all measurements and encode the units in variable names, such as `distanceInKilometers` or `temperatureInCelsius`. Not only does it prevent [conversion errors](http://www.wired.com/2010/11/1110mars-climate-observer-report/), the stricter typing also enables the compiler to check our logic: it is impossible to accidentally add a `Measurement<UnitLength>` to a `Measurement<UnitTemperature>` because that code wouldn’t compile.

## More expressive APIs

APIs (from Apple or third parties) that adopt the new types in the future will become more expressive and self-documenting, too.

Imagine a method to rotate an image. Right now it probably takes a `Double` for the _angle_ parameter. The author of the method must document whether the angle should be passed in degrees or radians, and the developer using the API must take care not to violate this assumption. In the new world of units, the _angle_ parameter’s type would be [`Measurement<UnitAngle>`](https://developer.apple.com/reference/foundation/nsunitangle), giving both the API client and the author the freedom to work in the unit that is most convenient for them, and eliminating bugs due to conversion errors.

Similarly, an animation API would no longer need to document that the _duration_ parameter must be passed in seconds. It would simply be a [`Measurement<UnitDuration>`](https://developer.apple.com/reference/foundation/nsunitduration).

## MeasurementFormatter

Finally, the new [`MeasurementFormatter`](https://developer.apple.com/reference/foundation/nsmeasurementformatter) is another plus. It formats measurements in a locale-specific way, taking regional unit preferences (miles over kilometers), number formats, and symbols into account.

```
let formatter = MeasurementFormatter()
let 🇩🇪 = Locale(identifier: "de_DE")
formatter.locale = 🇩🇪
formatter.string(from: distance) // "106,4 km"

let 🇺🇸 = Locale(identifier: "en_US")
formatter.locale = 🇺🇸
formatter.string(from: distance) // "66.114 mi"

let 🇨🇳 = Locale(identifier: "zh_Hans_CN")
formatter.locale = 🇨🇳
formatter.string(from: distance) // "106.4公里"
```

# What I don’t like

One thing I do not like about the new API is its verbosity. `Measurement(value: 5, unit: UnitLength.kilometers)` is tedious to write and hard to read. It’s always hard to find the right balance between conciseness and clarity, but I think this initializer errs on the side of verbosity.

An extreme alternative would be something like `let d = 5.kilometers`, which reads extremely well, but has the drawback of polluting the common integer and floating-point namespaces. Maybe something like `5.measure.kilometers`?

I think it would already be a big improvement to lose the argument labels for the initializer. `let d = Measurement(5, UnitLength.kilometers)` reads much nicer. Now add one typealias per unit class to get rid of the `UnitLength` prefix and I really start to like it:

```
typealias Length = Measurement<UnitLength>
let d = Length(5, .kilometers)

typealias Duration = Measurement<UnitDuration>
let t = Duration(10, .seconds)
```

These things are easy to add in your own projects, but only Apple can introduce a better standard syntax.

# Relationships between unit classes

We have seen that we can add measurements of the same class, but what if I wanted to calculate my average speed during the bike tour? Velocity is distance divided by time, so let’s create a measurement for the tour’s duration and then do the calculation:

```
// 8h 6m 17s
let time = Measurement(value: 8, unit: UnitDuration.hours)
    + Measurement(value: 6, unit: UnitDuration.minutes)
    + Measurement(value: 17, unit: UnitDuration.seconds)
let speed = distance / time
// error: binary operator '/' cannot be applied to operands of type 'Measurement<UnitLength>' and 'Measurement<UnitDuration>'
```

The division operation causes a compiler error. It turns out Apple (probably wisely for a first version) stopped short of creating a fully coherent system of interrelated units. So we cannot express a division of `UnitLength` by `UnitDuration` in terms of [`UnitSpeed`](https://developer.apple.com/reference/foundation/nsunitspeed). However, we can easily add this manually. All we need to do is provide a matching overload for the division operator `/`:

```
func / (lhs: Measurement<UnitLength>, rhs: Measurement<UnitDuration>) -> Measurement<UnitSpeed> {
    let quantity = lhs.converted(to: .meters).value / rhs.converted(to: .seconds).value
    let resultUnit = UnitSpeed.metersPerSecond
    return Measurement(value: quantity, unit: resultUnit)
}
```

We convert the length value to meters and the duration value to seconds, perform the division, and return the result as a measurement in meters per second. Now the compiler is happy:

```
let speed = distance / time
// → 3.64670802344312 m/s
speed.converted(to: .kilometersPerHour)
// → 13.1281383818845 km/h
```

## Can we do better?

This is nice, but also a bit limited. We would need to provide additional overloads for the reverse operations (_length = speed × time_, or _time = length / speed_), and if we wanted to express other relations (e.g. resistance = voltage / current), we would have to do the same thing all over again. Wouldn’t it be cool if we could somehow _declaratively_ express these relations once and then it would all work automatically? And that’s what I’m going to show you [in the next article](https://oleb.net/blog/2016/07/unitproduct/).
