---
title: 'nanoseconds(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/nanoseconds(_:)-8nsaz'
source_url: 'https://developer.apple.com/documentation/swift/duration/nanoseconds(_:)-8nsaz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/nanoseconds%28_%3A%29-8nsaz.json'
content_hash: 'sha256:3712075f52e04ab5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# nanoseconds(_:)

<sub>Type Method</sub>

Construct a `Duration` given a number of nanoseconds represented as a `BinaryInteger`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func nanoseconds<T>(_ nanoseconds: T) -> Duration where T : BinaryInteger
```

## Return Value

A `Duration` representing a given number of nanoseconds.

## Discussion

```swift
  let d: Duration = .nanoseconds(1929)
```
