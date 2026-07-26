---
title: AnimationStateKey
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animationstatekey
source_url: 'https://developer.apple.com/documentation/swiftui/animationstatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationstatekey.json'
content_hash: 'sha256:505d54f82e677e8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnimationStateKey

<sub>Protocol</sub>

A key for accessing animation state values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AnimationStateKey
```

## Overview

To access animation state from an [AnimationContext](animationcontext.md) in a custom animation, create an `AnimationStateKey`. For example, the following code creates an animation state key named `PausableState` and sets the value for the required [defaultValue](animationstatekey/defaultvalue.md) property. The code also defines properties for state values that the custom animation needs when calculating animation values. Keeping the state values in the animation state key makes it more convenient to read and write those values in the implementation of a [CustomAnimation](customanimation.md).

```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    var paused = false
    var pauseTime: TimeInterval = 0.0

    static var defaultValue: Self { .init() }
}
```

To make accessing the value of the animation state key more convenient, define a property for it by extending [AnimationContext](animationcontext.md):

```swift
extension AnimationContext {
    fileprivate var pausableState: PausableState<Value> {
        get { state[PausableState<Value>.self] }
        set { state[PausableState<Value>.self] = newValue }
    }
}
```

Then, you can read and write your state in an instance of `CustomAnimation` using the [AnimationContext](animationcontext.md):

```swift
struct PausableAnimation: CustomAnimation {
    let base: Animation

    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        let paused = context.environment.animationPaused

        let pausableState = context.pausableState
        var pauseTime = pausableState.pauseTime
        if pausableState.paused != paused {
            pauseTime = time - pauseTime
            context.pausableState = PausableState(paused: paused, pauseTime: pauseTime)
        }

        let effectiveTime = paused ? pauseTime : time - pauseTime
        let result = base.animate(value: value, time: effectiveTime, context: &context)
        return result
    }
}
```

## Topics

### Setting the default value

- [defaultValue](animationstatekey/defaultvalue.md) — The default value for the animation state key.
- [Value](animationstatekey/value.md) — The associated type representing the type of the animation state key’s value.

## See Also

### Creating custom animations

- [CustomAnimation](customanimation.md) — A type that defines how an animatable value changes over time.
- [AnimationContext](animationcontext.md) — Contextual values that a custom animation can use to manage state and access a view’s environment.
- [AnimationState](animationstate.md) — A container that stores the state for a custom animation.
- [UnitCurve](unitcurve.md) — A  function defined by a two-dimensional curve that maps an input progress in the range [0,1] to an output progress that is also in the range [0,1]. By changing the shape of the curve, the effective speed of an animation or other interpolation can be changed.
- [Spring](spring.md) — A representation of a spring’s motion.
