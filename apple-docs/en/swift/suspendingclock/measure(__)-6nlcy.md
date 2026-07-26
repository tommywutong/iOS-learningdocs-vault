---
title: 'measure(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/suspendingclock/measure(_:)-6nlcy'
source_url: 'https://developer.apple.com/documentation/swift/suspendingclock/measure(_:)-6nlcy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/suspendingclock/measure%28_%3A%29-6nlcy.json'
content_hash: 'sha256:7d93ba4f6d0de94a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SuspendingClock](../suspendingclock.md)

# measure(_:)

<sub>Instance Method</sub>

Measure the elapsed time to execute a closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func measure(_ work: () throws -> Void) rethrows -> Self.Instant.Duration
```

## Discussion

```swift
  let clock = ContinuousClock()
  let elapsed = clock.measure {
     someWork()
  }
```
