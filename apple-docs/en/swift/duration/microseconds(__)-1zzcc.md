---
title: 'microseconds(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/microseconds(_:)-1zzcc'
source_url: 'https://developer.apple.com/documentation/swift/duration/microseconds(_:)-1zzcc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/microseconds%28_%3A%29-1zzcc.json'
content_hash: 'sha256:dd98670bcfbeb2c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# microseconds(_:)

<sub>Type Method</sub>

Construct a `Duration` given a number of seconds microseconds as a `Double` by converting the value into the closest attosecond scale value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func microseconds(_ microseconds: Double) -> Duration
```

## Return Value

A `Duration` representing a given number of microseconds.

## Discussion

```swift
  let d: Duration = .microseconds(382.9)
```

## See Also

### Creating a duration

- [init(secondsComponent:attosecondsComponent:)](<init(secondscomponent_attosecondscomponent_).md>) — Construct a `Duration` by adding attoseconds to a seconds value.
- [seconds(_:)](<seconds(__)-311cx.md>) — Construct a `Duration` given a number of seconds represented as a `BinaryInteger`.
- [seconds(_:)](<seconds(__)-5ifzr.md>) — Construct a `Duration` given a number of seconds represented as a `Double` by converting the value into the closest attosecond scale value.
- [milliseconds(_:)](<milliseconds(__)-1w328.md>) — Construct a `Duration` given a number of milliseconds represented as a `BinaryInteger`.
- [milliseconds(_:)](<milliseconds(__)-7ledy.md>) — Construct a `Duration` given a number of seconds milliseconds as a `Double` by converting the value into the closest attosecond scale value.
- [microseconds(_:)](<microseconds(__)-2majo.md>) — Construct a `Duration` given a number of microseconds represented as a `BinaryInteger`.
