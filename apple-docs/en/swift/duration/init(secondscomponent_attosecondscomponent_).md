---
title: 'init(secondsComponent:attosecondsComponent:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/init(secondscomponent:attosecondscomponent:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/init(secondscomponent:attosecondscomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/init%28secondscomponent%3Aattosecondscomponent%3A%29.json'
content_hash: 'sha256:550ead330eca86d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# init(secondsComponent:attosecondsComponent:)

<sub>Initializer</sub>

Construct a `Duration` by adding attoseconds to a seconds value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(secondsComponent: Int64, attosecondsComponent: Int64)
```

## Parameters

- `secondsComponent` — The seconds component portion of the `Duration` value.

- `attosecondsComponent` — The attosecond component portion of the `Duration` value.

## Discussion

This is useful for when an external decomposed components of a `Duration` has been stored and needs to be reconstituted. Since the values are added no precondition is expressed for the attoseconds being limited to 1e18.

```swift
  let d1 = Duration(
    secondsComponent: 3, 
    attosecondsComponent: 123000000000000000)
  print(d1) // 3.123 seconds

  let d2 = Duration(
    secondsComponent: 3, 
    attosecondsComponent: -123000000000000000)
  print(d2) // 2.877 seconds

  let d3 = Duration(
    secondsComponent: -3, 
    attosecondsComponent: -123000000000000000)
  print(d3) // -3.123 seconds
```

## See Also

### Creating a duration

- [seconds(_:)](<seconds(__)-311cx.md>) — Construct a `Duration` given a number of seconds represented as a `BinaryInteger`.
- [seconds(_:)](<seconds(__)-5ifzr.md>) — Construct a `Duration` given a number of seconds represented as a `Double` by converting the value into the closest attosecond scale value.
- [milliseconds(_:)](<milliseconds(__)-1w328.md>) — Construct a `Duration` given a number of milliseconds represented as a `BinaryInteger`.
- [milliseconds(_:)](<milliseconds(__)-7ledy.md>) — Construct a `Duration` given a number of seconds milliseconds as a `Double` by converting the value into the closest attosecond scale value.
- [microseconds(_:)](<microseconds(__)-1zzcc.md>) — Construct a `Duration` given a number of seconds microseconds as a `Double` by converting the value into the closest attosecond scale value.
- [microseconds(_:)](<microseconds(__)-2majo.md>) — Construct a `Duration` given a number of microseconds represented as a `BinaryInteger`.
