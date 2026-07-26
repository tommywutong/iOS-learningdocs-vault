---
title: 'nanoseconds(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/nanoseconds(_:)-1cg32'
source_url: 'https://developer.apple.com/documentation/swift/duration/nanoseconds(_:)-1cg32'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/nanoseconds%28_%3A%29-1cg32.json'
content_hash: 'sha256:62f6cf8764e19083'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# nanoseconds(_:)

<sub>Type Method</sub>

Construct a `Duration` given a number of nanoseconds as a `Double` by converting the value into the closest attosecond scale value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func nanoseconds(_ nanoseconds: Double) -> Duration
```

## Return Value

A `Duration` representing a given number of nanoseconds.

## Discussion

```swift
  let d: Duration = .nanoseconds(382.9)
```
