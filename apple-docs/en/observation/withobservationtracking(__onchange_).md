---
title: 'withObservationTracking(_:onChange:)'
framework: Observation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/observation/withobservationtracking(_:onchange:)'
source_url: 'https://developer.apple.com/documentation/observation/withobservationtracking(_:onchange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/withobservationtracking%28_%3Aonchange%3A%29.json'
content_hash: 'sha256:6153b6a57727549e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Observation](../observation.md)

# withObservationTracking(_:onChange:)

<sub>Function</sub>

Tracks access to properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withObservationTracking<T>(_ apply: () -> T, onChange: @autoclosure () -> @Sendable () -> Void) -> T
```

## Parameters

- `apply` — A closure that contains properties to track.

- `onChange` — The closure invoked when the value of a property changes.

## Return Value

The value that the `apply` closure returns if it has a return value; otherwise, there is no return value.

## Discussion

This method tracks access to any property within the `apply` closure, and informs the caller of value changes made to participating properties by way of the `onChange` closure. For example, the following code tracks changes to the name of cars, but it doesn’t track changes to any other property of `Car`:

```swift
func render() {
    withObservationTracking {
        for car in cars {
            print(car.name)
        }
    } onChange: {
        print("Schedule renderer.")
    }
}
```

## See Also

### Change tracking

- [ObservationRegistrar](observationregistrar.md) — Provides storage for tracking and access to data changes.
